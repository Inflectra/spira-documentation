#!/usr/bin/env python3
"""
Script to add frontmatter to all markdown files in specified folders.
Usage: python add_frontmatter.py folder1 folder2 ...
"""

import os
import sys
from pathlib import Path

def add_frontmatter_to_file(file_path):
    """Add frontmatter to a single markdown file if it doesn't already have it."""
    frontmatter = "---\npdf: true\n---\n\n"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file already has frontmatter
        if content.startswith('---'):
            print(f"Skipping {file_path} - already has frontmatter")
            return False
        
        # Add frontmatter to the beginning
        new_content = frontmatter + content
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Added frontmatter to {file_path}")
        return True
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def process_folder(folder_path):
    """Process all markdown files in a folder."""
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Folder {folder_path} does not exist")
        return 0
    
    if not folder.is_dir():
        print(f"{folder_path} is not a directory")
        return 0
    
    count = 0
    for md_file in folder.glob('*.md'):
        if add_frontmatter_to_file(md_file):
            count += 1
    
    return count

def main():
    if len(sys.argv) < 2:
        print("Usage: python add_frontmatter.py folder1 folder2 ...")
        print("Example: python add_frontmatter.py ../docs/Spira-User-Manual ../docs/HowTo-Guides")
        sys.exit(1)
    
    total_files = 0
    
    for folder_arg in sys.argv[1:]:
        print(f"\nProcessing folder: {folder_arg}")
        count = process_folder(folder_arg)
        total_files += count
        print(f"Modified {count} files in {folder_arg}")
    
    print(f"\nTotal files modified: {total_files}")

if __name__ == "__main__":
    main()