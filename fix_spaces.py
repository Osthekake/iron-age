#!/usr/bin/env python3
import os
import re
from pathlib import Path

def fix_links_in_file(file_path):
    """Fix links with spaces by URL-encoding them in the markdown."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Find all markdown links and fix spaces in URLs
    def fix_link(match):
        link_text = match.group(1)
        url = match.group(2)
        
        # URL-encode spaces as %20 for .md files
        if url.endswith('.md') and ' ' in url:
            fixed_url = url.replace(' ', '%20')
            return f"[{link_text}]({fixed_url})"
        
        return match.group(0)
    
    # Apply the fix
    content = re.sub(r'\[([^\]]+)\]\(([^)]+\.md)\)', fix_link, content)
    
    # Write back if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed links in {file_path}")
        return True
    
    return False

def main():
    """Fix all markdown links with spaces."""
    fixed_files = 0
    
    for root, dirs, files in os.walk('.'):
        # Skip .obsidian directory
        if '.obsidian' in dirs:
            dirs.remove('.obsidian')
        
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if fix_links_in_file(file_path):
                    fixed_files += 1
    
    print(f"Fixed links in {fixed_files} files")

if __name__ == '__main__':
    main()