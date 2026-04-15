#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mass Rebranding Script
Mengubah semua referensi "Warta Jabar" / "Warta Janten" menjadi "BantenStream"
di semua file HTML di direktori ini dan subdirektori
"""

import os
import re
from pathlib import Path

# Pattern yang akan diganti
replacements = [
    # Dalam title tags
    ('- Warta Janten</title>', '- BantenStream</title>'),
    ('- Warta Jabar</title>', '- BantenStream</title>'),
    (' Warta Janten</title>', ' BantenStream</title>'),
    (' Warta Jabar</title>', ' BantenStream</title>'),
    # Dalam logo HTML (dari image ke text) - yang belum diubah
    ('<img src="img/warta jabar.png" alt="Warta Jabar">', 'BantenStream'),
    # Dalam copyright
    ('Copyright © 2026 <strong>Warta Janten</strong>', 'Copyright © 2026 <strong>BantenStream</strong>'),
    ('Copyright © 2026 <strong>Warta Jabar</strong>', 'Copyright © 2026 <strong>BantenStream</strong>'),
    # Email
    ('redaksi@wartajanten.id', 'redaksi@bantenstream.id'),
    ('redaksi@wartajabar.com', 'redaksi@bantenstream.id'),
    ('privacy@wartajabar.com', 'privacy@bantenstream.id'),
    # Dalam teks deskripsi atau referensi lain
    ('<strong>Warta Jabar</strong>', '<strong>BantenStream</strong>'),
    ('<strong>Warta Janten</strong>', '<strong>BantenStream</strong>'),
]

# File yang akan diexclude
exclude_files = {'mass_rebrand.php', 'mass_rebrand.py', '.git'}

# Direktori base
base_dir = os.getcwd()

def process_directory(directory):
    """Rekursi ke semua file HTML dan lakukan replacement"""
    processed_count = 0
    unchanged_count = 0
    
    for root, dirs, files in os.walk(directory):
        # Skip .git dan folder lainnya
        dirs[:] = [d for d in dirs if d != '.git']
        
        for file in files:
            if file.endswith('.html') and file not in exclude_files:
                file_path = os.path.join(root, file)
                
                try:
                    # Baca file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        original_content = f.read()
                    
                    new_content = original_content
                    changed = False
                    
                    # Lakukan replacement
                    for find_str, replace_str in replacements:
                        if find_str in new_content:
                            new_content = new_content.replace(find_str, replace_str)
                            changed = True
                    
                    # Tulis kembali jika ada perubahan
                    if changed:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        rel_path = os.path.relpath(file_path, directory)
                        print(f"✓ UPDATED: {rel_path}")
                        processed_count += 1
                    else:
                        rel_path = os.path.relpath(file_path, directory)
                        print(f"- UNCHANGED: {rel_path}")
                        unchanged_count += 1
                        
                except Exception as e:
                    print(f"✗ ERROR in {file_path}: {str(e)}")
    
    return processed_count, unchanged_count

if __name__ == '__main__':
    print("=" * 50)
    print("MASS REBRANDING SCRIPT")
    print("Warta Jabar/Janten → BantenStream")
    print("=" * 50)
    print()
    
    processed, unchanged = process_directory(base_dir)
    
    print()
    print("=" * 50)
    print(f"Rebranding Selesai!")
    print(f"Total file yang diperbarui: {processed}")
    print(f"Total file tanpa perubahan: {unchanged}")
    print("=" * 50)
