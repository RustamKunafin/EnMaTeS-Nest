# -*- coding: utf-8 -*-
"""
cleaner.py

This module implements the 'cleanup-backups' command for weaverSG.
Its purpose is to find and safely delete timestamped backup files (*_backup_*.md)
that are created by the LSGManager during save operations. It supports both
interactive and automated (non-interactive) modes.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""

import os
from pathlib import Path
from typing import List

def find_backup_files(directory: Path) -> List[Path]:
    """
    Finds all weaverSG backup files in a given directory.

    Backup files are identified by the pattern '*_backup_*.md'.

    Args:
        directory (Path): The directory to search in.

    Returns:
        A list of Path objects for all found backup files.
    """
    # The pattern matches any file ending with _backup_ followed by any characters
    # and ending with .md. This is the standard backup format.
    pattern = "*_backup_*.md"
    return list(directory.glob(pattern))

def handle_cleanup(file_path: Path, auto_confirm: bool = False):
    """
    Handles the backup cleanup process for the directory of the given file.

    It finds all backup files, asks for user confirmation (unless auto_confirm
    is True), and then deletes them.

    Args:
        file_path (Path): The path to the main SG file. The cleanup will be
                          performed in the same directory.
        auto_confirm (bool): If True, skips the interactive confirmation prompt.
                             This is useful for automated scripts.
    """
    target_directory = file_path.parent
    print(f"Searching for backup files in: {target_directory}")

    backup_files = find_backup_files(target_directory)

    if not backup_files:
        print("No backup files found. Nothing to do.")
        return

    print("\nThe following backup files will be deleted:")
    for bf in backup_files:
        print(f"  - {bf.name}")

    # If not in auto-confirm mode, ask the user for confirmation.
    if not auto_confirm:
        try:
            confirm = input("\nAre you sure you want to permanently delete these files? (y/n): ").lower()
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return
            
        if confirm != 'y':
            print("Cleanup cancelled by user.")
            return
    else:
        print("\n'--yes' flag detected. Proceeding with automatic deletion.")

    # Proceed with deletion
    deleted_count = 0
    error_count = 0
    print("\nDeleting files...")
    for bf in backup_files:
        try:
            bf.unlink()
            print(f"  - Deleted: {bf.name}")
            deleted_count += 1
        except OSError as e:
            print(f"  - Error deleting {bf.name}: {e}")
            error_count += 1
    
    print(f"\nCleanup complete. {deleted_count} file(s) deleted, {error_count} error(s).")
