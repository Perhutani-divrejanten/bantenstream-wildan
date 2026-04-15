#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Verification Script untuk BantenStream Rebranding
Memverifikasi bahwa semua file sudah di-update dengan benar
"""

import os
import re
from pathlib import Path

# Keywords yang harus ada atau tidak boleh ada
must_have = [
    'BantenStream',
    'bantenstream-theme.css'
]

must_not_have = [
    'Warta Jabar',
    'Warta Janten',
    'warta jabar.png',
    'wartajanten',
    'wartajabar'
]

base_dir = os.getcwd()
errors = []
warnings = []
success_count = 0

def check_file(file_path):
    """Check single file for branding correctness"""
    global success_count, errors, warnings
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        rel_path = os.path.relpath(file_path, base_dir)
        file_ok = True
        
        # Check for old branding
        for bad_term in must_not_have:
            if bad_term.lower() in content.lower():
                errors.append(f"❌ {rel_path}: Masih mengandung '{bad_term}'")
                file_ok = False
        
        # Check for new branding (minimum)
        has_bantenstream = 'BantenStream' in content
        if not has_bantenstream:
            warnings.append(f"⚠️  {rel_path}: Mungkin belum memiliki BantenStream branding")
            file_ok = False
        
        if file_ok:
            success_count += 1
            return True
        return False
        
    except Exception as e:
        errors.append(f"❌ Error membaca {rel_path}: {str(e)}")
        return False

def scan_directory(directory):
    """Scan semua file HTML"""
    html_files = []
    
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d != '.git']
        
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                html_files.append(file_path)
    
    return html_files

if __name__ == '__main__':
    print("=" * 60)
    print("🔍 BANTENSTREAM REBRANDING VERIFICATION")
    print("=" * 60)
    print()
    
    html_files = scan_directory(base_dir)
    total_files = len(html_files)
    
    print(f"📊 Total file HTML ditemukan: {total_files}")
    print(f"🔄 Memverifikasi...")
    print()
    
    for file_path in html_files:
        check_file(file_path)
    
    # Summary
    print("=" * 60)
    print("📋 HASIL VERIFIKASI")
    print("=" * 60)
    print()
    
    print(f"✅ File OK: {success_count}/{total_files}")
    
    if errors:
        print(f"\n❌ ERRORS ({len(errors)}):")
        for error in errors[:10]:  # Show first 10 errors
            print(f"   {error}")
        if len(errors) > 10:
            print(f"   ... dan {len(errors)-10} errors lainnya")
    
    if warnings:
        print(f"\n⚠️  WARNINGS ({len(warnings)}):")
        for warning in warnings[:5]:
            print(f"   {warning}")
        if len(warnings) > 5:
            print(f"   ... dan {len(warnings)-5} warnings lainnya")
    
    print()
    print("=" * 60)
    
    if not errors:
        print("🎉 SEMUANYA SUDAH BENAR! BantenStream siap diluncurkan!")
    else:
        print(f"⚠️  Masih ada {len(errors)} file yang perlu di-check")
    
    print("=" * 60)
