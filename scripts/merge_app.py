# -*- coding: utf-8 -*-
import subprocess

print("Menjalankan script pembuatan header...")
subprocess.run(['python', 'scripts/build_definitive_app.py'], check=True)

with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    header_content = f.read()

with open('scripts/build_pages_part1.py', 'r', encoding='utf-8', errors='ignore') as f:
    part1_content = f.read()

with open('scripts/build_pages_part2.py', 'r', encoding='utf-8', errors='ignore') as f:
    part2_content = f.read()

# Gabungkan secara murni
full_app_content = header_content + '\n' + part1_content + '\n' + part2_content

with open('public/assets/app.js', 'w', encoding='utf-8') as f:
    f.write(full_app_content)

print(f"Sukses merakit public/assets/app.js! Total panjang karakter: {len(full_app_content)}")
