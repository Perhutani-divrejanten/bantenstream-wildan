#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script untuk menambahkan link ke bantenstream-theme.css
ke semua file HTML
"""

import os

# File yang akan diexclude
exclude_files = {'mass_rebrand.php', 'mass_rebrand.py', 'add_css_link.py', '.git'}

# Direktori base
base_dir = os.getcwd()

def add_css_link(directory):
    """Tambahkan link CSS ke semua file HTML"""
    processed_count = 0
    
    for root, dirs, files in os.walk(directory):
        # Skip .git dan folder lainnya
        dirs[:] = [d for d in dirs if d != '.git']
        
        for file in files:
            if file.endswith('.html') and file not in exclude_files:
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Cek apakah sudah ada link ke bantenstream-theme.css
                    if 'bantenstream-theme.css' in content:
                        rel_path = os.path.relpath(file_path, directory)
                        print(f"- ALREADY LINKED: {rel_path}")
                        continue
                    
                    # Cari template stylesheet dan tambahkan CSS baru setelahnya
                    old_link = '        <link href="css/style.css" rel="stylesheet">'
                    new_link = '        <link href="css/style.css" rel="stylesheet">\n        <link href="css/bantenstream-theme.css" rel="stylesheet">'
                    
                    if old_link in content:
                        new_content = content.replace(old_link, new_link)
                        
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        rel_path = os.path.relpath(file_path, directory)
                        print(f"✓ LINKED CSS: {rel_path}")
                        processed_count += 1
                    else:
                        # Coba variasi spacing
                        old_link2 = '<link href="css/style.css" rel="stylesheet">'
                        if old_link2 in content:
                            new_link2 = '<link href="css/style.css" rel="stylesheet">\n        <link href="css/bantenstream-theme.css" rel="stylesheet">'
                            new_content = content.replace(old_link2, new_link2)
                            
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            
                            rel_path = os.path.relpath(file_path, directory)
                            print(f"✓ LINKED CSS: {rel_path}")
                            processed_count += 1
                        else:
                            rel_path = os.path.relpath(file_path, directory)
                            print(f"✗ NO MATCHING LINK: {rel_path}")
                            
                except Exception as e:
                    print(f"✗ ERROR in {file_path}: {str(e)}")
    
    return processed_count

if __name__ == '__main__':
    print("=" * 50)
    print("Adding BantenStream Theme CSS Link")
    print("=" * 50)
    print()
    
    processed = add_css_link(base_dir)
    
    print()
    print("=" * 50)
    print(f"Link CSS Ditambahkan: {processed} file")
    print("=" * 50)
