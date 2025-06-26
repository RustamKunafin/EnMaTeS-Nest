import json
import yaml
import re
from datetime import datetime
import argparse
import os
import shutil
from collections import Counter
import copy

def normalize_sg_json(file_path):
    """
    Reads an SG Markdown file, validates and normalizes its JSON content,
    and writes the content back to the same file.
    """
    try:
        # 1. Check for file existence
        if not os.path.exists(file_path):
            print(f"Error: File not found at {file_path}")
            return

        # 2. Create a backup
        backup_path = file_path + '.bak'
        shutil.copy2(file_path, backup_path)
        print(f"Created backup: {backup_path}")

        # 3. Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 4. Extract YAML and JSON parts
        yaml_match = re.search(r'^(---.*?)(?:\n---|\.\.\.)\s*\n', content, re.DOTALL)
        if yaml_match:
            yaml_data_str = yaml_match.group(1).strip().lstrip('---').strip()
            yaml_data = yaml.safe_load(yaml_data_str)
            
            yaml_data['last_update_timestamp'] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            current_version = yaml_data.get('graph_version', '0.5')
            major, minor = map(int, current_version.split('.'))
            yaml_data['graph_version'] = f"{major}.{minor + 1}"

            updated_yaml_str = yaml.dump(yaml_data, sort_keys=False, allow_unicode=True, default_flow_style=False)
            yaml_content_block = f'---\n{updated_yaml_str}---'
        else:
            yaml_content_block = ''
        
        json_match = re.search(r'```json\s*(.*?)\s*```', content, re.DOTALL)
        if not json_match:
            raise ValueError("No JSON code block found. Check for correct ```json ... ``` formatting.")
        
        json_string = json_match.group(1)
        json_data = json.loads(json_string)
        print("Successfully parsed YAML front matter and JSON block.")

        # --- 5. Perform Validations ---
        nodes = json_data.get('nodes', [])
        relations = json_data.get('relations', [])
        validation_issues = {}

        print("Clearing previous validation annotations...")
        for item in nodes + relations:
            item.pop('validation_error', None)
        
        # 5a. Check for duplicate MUIDs in nodes
        print("Validating: Checking for duplicate nodes (by MUID)...")
        muid_counts = Counter(node['MUID'] for node in nodes if 'MUID' in node)
        duplicate_muids_set = {muid for muid, count in muid_counts.items() if count > 1}
        if duplicate_muids_set:
            duplicate_nodes_report = []
            reported_muids = set() # Track MUIDs already added to the report

            for node in nodes:
                muid = node.get('MUID')
                if muid in duplicate_muids_set:
                    # **UNIFIED**: Clearer error message about the NODE
                    error_msg = f"Duplicate Node (by MUID): This MUID is used by {muid_counts[muid]} nodes in the graph."
                    node.setdefault('validation_error', []).append(error_msg)
                    
                    if muid not in reported_muids:
                        duplicate_nodes_report.append(copy.deepcopy(node))
                        reported_muids.add(muid)
            
            # **UNIFIED**: Changed key from 'duplicate_muids' to 'duplicate_nodes'
            validation_issues['duplicate_nodes'] = duplicate_nodes_report
            # **UNIFIED**: Clearer print statement about NODES
            print(f"Warning: Found nodes with {len(duplicate_muids_set)} duplicate MUIDs: {list(duplicate_muids_set)}")
        else:
            print("Validation passed: No duplicate nodes found.")

        # 5b. Check for dangling relations
        print("Validating: Checking for dangling relations...")
        node_muids_set = {node['MUID'] for node in nodes}
        dangling_relations_report = []
        for relation in relations:
            from_muid = relation.get('from_MUID')
            to_muid = relation.get('to_MUID')
            
            error_msgs = []
            if from_muid not in node_muids_set:
                error_msgs.append(f"Dangling relation: from_MUID '{from_muid}' not found in nodes.")
            if to_muid not in node_muids_set:
                error_msgs.append(f"Dangling relation: to_MUID '{to_muid}' not found in nodes.")
            
            if error_msgs:
                relation.setdefault('validation_error', []).extend(error_msgs)
                dangling_relations_report.append(copy.deepcopy(relation))
        
        if dangling_relations_report:
            validation_issues['dangling_relations'] = dangling_relations_report
            print(f"Warning: Found {len(dangling_relations_report)} dangling relation(s).")
        else:
            print("Validation passed: No dangling relations found.")

        # 5c. Check for duplicate relations
        print("Validating: Checking for duplicate relations...")
        rel_fingerprints = [(r.get('from_MUID'), r.get('to_MUID'), r.get('type')) for r in relations]
        rel_counts = Counter(rel_fingerprints)
        duplicate_rels_set = {fp for fp, count in rel_counts.items() if count > 1}

        if duplicate_rels_set:
            duplicate_relations_report = []
            reported_fingerprints = set() # Track fingerprints already added to the report

            for rel in relations:
                fingerprint = (rel.get('from_MUID'), rel.get('to_MUID'), rel.get('type'))
                if fingerprint in duplicate_rels_set:
                    error_msg = f"Duplicate relation: This exact relation appears {rel_counts[fingerprint]} times."
                    rel.setdefault('validation_error', []).append(error_msg)
                    
                    if fingerprint not in reported_fingerprints:
                        duplicate_relations_report.append(copy.deepcopy(rel))
                        reported_fingerprints.add(fingerprint)
            
            validation_issues['duplicate_relations'] = duplicate_relations_report
            print(f"Warning: Found {len(duplicate_rels_set)} type(s) of duplicate relations.")
        else:
            print("Validation passed: No duplicate relations found.")

        # Update or remove the validation_issues section
        if validation_issues:
            json_data['validation_issues'] = validation_issues
        else:
            json_data.pop('validation_issues', None)
            print("All validations passed successfully. No issues reported.")

        # 6. Normalize and reassemble the file
        normalized_json = json.dumps(json_data, sort_keys=True, indent=2, ensure_ascii=False)
        new_content = f'{yaml_content_block}\n\n```json\n{normalized_json}\n```'

        # 7. Save the result
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"File successfully normalized and saved: {file_path}")

    except json.JSONDecodeError as e:
        print(f"An error occurred while parsing JSON: {e}")
        print("Please check the JSON syntax in your file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        if 'backup_path' in locals() and os.path.exists(backup_path):
            shutil.copy2(backup_path, file_path)
            print(f"Restored original file from {backup_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Normalize and validate the JSON block within a Semantic Graph (SG) Markdown file.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("file_path", help="Path to the Markdown file to normalize")
    args = parser.parse_args()
    
    normalize_sg_json(args.file_path)