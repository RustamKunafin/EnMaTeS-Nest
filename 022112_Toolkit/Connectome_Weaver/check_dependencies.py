# 022112_Toolkit/Connectome_Weaver/check_dependencies.py

def check_module(module_name):
    """Attempts to import a module and reports the result."""
    try:
        __import__(module_name)
        print(f"Module '{module_name}': Available")
        return True
    except ModuleNotFoundError:
        print(f"Module '{module_name}': NOT available (ModuleNotFoundError)")
        return False
    except Exception as e:
        print(f"Module '{module_name}': Error during import - {e}")
        return False

def main():
    """Checks all required modules for Connectome Weaver."""
    required_modules = [
        'yaml', 'json', 're', 'argparse', 'os',
        'shutil', 'datetime', 'uuid', 'collections'
    ]
    
    print("--- Checking Connectome Weaver Dependencies ---")
    
    all_available = True
    for module_name in required_modules:
        if not check_module(module_name):
            all_available = False

    print("\n--- Summary ---")
    if all_available:
        print("All necessary modules are available.")
    else:
        print("Some necessary modules are NOT available. Please install them.")

if __name__ == "__main__":
    main()