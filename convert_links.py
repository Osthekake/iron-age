#!/usr/bin/env python3
import os
import re
from pathlib import Path

def find_target_file(link_text, current_file, all_files):
    """Find the target file for a given link text."""
    # Normalize the link text
    normalized = link_text.strip()
    
    # For image files, try exact filename matches with extensions
    if any(link_text.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg']):
        for file_path in all_files:
            if Path(file_path).name.lower() == normalized.lower():
                return file_path
    
    # Try exact stem matches (filename without extension)
    for file_path in all_files:
        filename = Path(file_path).stem
        if filename == normalized:
            return file_path
    
    # Try case-insensitive stem matches
    for file_path in all_files:
        filename = Path(file_path).stem
        if filename.lower() == normalized.lower():
            return file_path
    
    # Try partial matches (for cases like "summary" matching "summary.png")
    for file_path in all_files:
        filename = Path(file_path).stem
        if normalized.lower() in filename.lower():
            return file_path
    
    return None

def calculate_relative_path(from_file, to_file):
    """Calculate relative path from from_file to to_file."""
    from_path = Path(from_file).parent
    to_path = Path(to_file)
    
    # Calculate relative path
    relative = os.path.relpath(to_path, from_path)
    
    # If we're in the same directory, just return the filename
    if relative == to_path.name:
        return relative
    
    return relative

def convert_obsidian_links(content, current_file, all_files):
    """Convert Obsidian-style links to standard markdown links."""
    
    # Convert image links ![[filename.ext]] to ![alt text](relative/path)
    def replace_image_link(match):
        filename = match.group(1)
        target_file = find_target_file(filename, current_file, all_files)
        
        if target_file:
            relative_path = calculate_relative_path(current_file, target_file)
            # Use filename as alt text
            alt_text = Path(target_file).stem
            return f"![{alt_text}]({relative_path})"
        else:
            # If file not found, keep original but add warning
            return f"![{filename}](FILE_NOT_FOUND: {filename})"
    
    # Convert document links [[Document Name]] to [Document Name](relative/path)
    def replace_doc_link(match):
        doc_name = match.group(1)
        target_file = find_target_file(doc_name, current_file, all_files)
        
        if target_file:
            relative_path = calculate_relative_path(current_file, target_file)
            return f"[{doc_name}]({relative_path})"
        else:
            # If file not found, keep original but add warning
            return f"[{doc_name}](FILE_NOT_FOUND: {doc_name})"
    
    # Apply conversions
    content = re.sub(r'!\[\[([^\]]+)\]\]', replace_image_link, content)
    content = re.sub(r'\[\[([^\]]+)\]\]', replace_doc_link, content)
    
    return content

def main():
    # Find all markdown and image files
    all_files = []
    
    # Get all relevant files
    for root, dirs, files in os.walk('.'):
        # Skip .obsidian directory
        if '.obsidian' in dirs:
            dirs.remove('.obsidian')
        
        for file in files:
            if file.endswith(('.md', '.png', '.jpg', '.jpeg', '.gif', '.svg')):
                all_files.append(os.path.join(root, file))
    
    # Process each markdown file
    for md_file in [f for f in all_files if f.endswith('.md')]:
        print(f"Processing {md_file}...")
        
        # Read the file
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
            continue
        
        # Convert links
        new_content = convert_obsidian_links(content, md_file, all_files)
        
        # Write back if content changed
        if new_content != content:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  Updated {md_file}")
            except Exception as e:
                print(f"Error writing {md_file}: {e}")
        else:
            print(f"  No changes needed for {md_file}")

if __name__ == '__main__':
    main()