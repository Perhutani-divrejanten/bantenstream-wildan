#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Final Aggressive Rebranding Script
Menghilangkan SEMUA referensi Warta Jabar/Janten dengan aggressive mode
"""

import os
import re

replacements = [
    # Case-sensitive replacements
    ('Warta Janten', 'BantenStream'),
    ('Warta Jabar', 'BantenStream'),
    ('warta janten', 'bantenstream'),
    ('warta jabar', 'bantenstream'),
    ('WARTA JANTEN', 'BANTENSTREAM'),
    ('WARTA JABAR', 'BANTENSTREAM'),
    
    # Email replacements
    ('redaksi@wartajanten.id', 'redaksi@bantenstream.id'),
    ('redaksi@wartajanten.com', 'redaksi@bantenstream.id'),
    ('redaksi@wartajabar.com', 'redaksi@bantenstream.id'),
    ('privacy@wartajanten.com', 'privacy@bantenstream.id'),
    ('privacy@wartajabar.com', 'privacy@bantenstream.id'),
    
    # Domain
    ('WartaJanten.ID', 'BantenStream.ID'),
    ('WartaJanten.id', 'BantenStream.id'),
    ('WartaJabar.ID', 'BantenStream.ID'),
    ('wartajanten.id', 'bantenstream.id'),
    ('wartajabar.com', 'bantenstream.id'),
]

base_dir = os.getcwd()
processed_count = 0

def process_directory(directory):
    """Process semua file HTML di direktori"""
    global processed_count
    
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d != '.git']
        
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        original_content = f.read()
                    
                    new_content = original_content
                    was_modified = False
                    
                    # Lakukan semua replacement
                    for old_str, new_str in replacements:
                        if old_str in new_content:
                            new_content = new_content.replace(old_str, new_str)
                            was_modified = True
                    
                    # Tulis ulang jika ada perubahan
                    if was_modified:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        rel_path = os.path.relpath(file_path, directory)
                        print(f"✅ CLEANED: {rel_path}")
                        processed_count += 1
                    
                except Exception as e:
                    print(f"❌ ERROR in {file_path}: {str(e)}")
    
    return processed_count

if __name__ == '__main__':
    print("=" * 60)
    print("🧹 FINAL CLEANUP - AGGRESSIVE REBRANDING")
    print("=" * 60)
    print()
    
    processed = process_directory(base_dir)
    
    print()
    print("=" * 60)
    print(f"✅ Cleanup Complete! {processed} files cleaned")
    print("=" * 60)
