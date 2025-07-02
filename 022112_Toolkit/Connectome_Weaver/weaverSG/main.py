# -*- coding: utf-8 -*-
"""
main.py

The main entry point for the Connectome Weaver (weaverSG) command-line interface.
This script uses argparse to parse user commands and arguments, and then dispatches
the request to the appropriate handler module within the 'commands' package.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""

import argparse
import sys
from pathlib import Path

# To make this script runnable from the project root, we ensure the parent directory
# is in the Python path. This allows for clean package-like imports.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from weaverSG.commands import (
    validator,
    batch_modifier,
    promote_handler,
    log_archiver,
    log_bundler,
    cleaner
)

def create_parser() -> argparse.ArgumentParser:
    """Creates and configures the main argument parser and all subparsers."""
    parser = argparse.ArgumentParser(
        description="Connectome Weaver (weaverSG): A tool for transactional management of Semantic Graphs.",
        epilog="Use 'weaverSG <command> --help' for more information on a specific command."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)

    # --- Validator Command ---
    parser_validate = subparsers.add_parser("validate", help="Validates the integrity of an SG file.")
    parser_validate.add_argument("--file", type=Path, required=True, help="Path to the SG file to validate.")
    # For machine-readable output
    parser_validate.add_argument("--output-format", choices=['human', 'json'], default='human', help="Format for the output. 'json' is for machine processing.")
    parser_validate.set_defaults(func=validator.handle_validation)

    # --- Batch Modifier Command ---
    parser_batch = subparsers.add_parser("batch-modify", help="Modifies an SG file based on a YAML recipe.")
    parser_batch.add_argument("--file", type=Path, required=True, help="Path to the target SG file.")
    parser_batch.add_argument("--recipe", type=Path, required=True, help="Path to the YAML recipe file.")
    parser_batch.set_defaults(func=batch_modifier.handle_batch_modify)

    # --- Promote Relation Command ---
    parser_promote = subparsers.add_parser("promote-relation", help="Promotes a 'link' relation to a 'bind' relation.")
    parser_promote.add_argument("--file", type=Path, required=True, help="Path to the target SG file.")
    parser_promote.add_argument("--lid", type=str, required=True, help="The LID of the link to promote.")
    parser_promote.set_defaults(func=promote_handler.handle_promote_relation)

    # --- Log Archiver Command ---
    parser_archive = subparsers.add_parser("archive-log", help="Archives the current LSG file.")
    parser_archive.add_argument("--file", type=Path, required=True, help="Path to the main SG file.")
    parser_archive.set_defaults(func=log_archiver.handle_archive_log)

    # --- Log Bundler Command ---
    parser_bundle = subparsers.add_parser("bundle-log", help="Bundles the external LSG into the main SG file.")
    parser_bundle.add_argument("--file", type=Path, required=True, help="Path to the main SG file.")
    parser_bundle.set_defaults(func=log_bundler.handle_bundle_log)

    # --- Log Detacher Command ---
    parser_detach = subparsers.add_parser("detach-log", help="Detaches the bundled log to an external LSG file.")
    parser_detach.add_argument("--file", type=Path, required=True, help="Path to the main SG file.")
    parser_detach.set_defaults(func=log_bundler.handle_detach_log)

    # --- Cleaner Command ---
    parser_cleanup = subparsers.add_parser("cleanup-backups", help="Deletes all backup files in the SG directory.")
    parser_cleanup.add_argument("--file", type=Path, required=True, help="Path to the SG file (to identify the directory).")
    parser_cleanup.add_argument("--yes", action="store_true", help="Skip interactive confirmation.")
    parser_cleanup.set_defaults(func=cleaner.handle_cleanup)
    
    return parser

def main():
    """The main execution function."""
    parser = create_parser()
    args = parser.parse_args()

    # Dispatch the call to the appropriate handler function
    if args.command == 'validate':
        args.func(file_path=args.file, output_format=args.output_format)
    elif args.command == 'batch-modify':
        args.func(file_path=args.file, recipe_path=args.recipe)
    elif args.command == 'promote-relation':
        args.func(file_path=args.file, lid=args.lid)
    elif args.command == 'archive-log':
        args.func(file_path=args.file)
    elif args.command == 'bundle-log':
        args.func(file_path=args.file)
    elif args.command == 'detach-log':
        args.func(file_path=args.file)
    elif args.command == 'cleanup-backups':
        args.func(file_path=args.file, auto_confirm=args.yes)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
