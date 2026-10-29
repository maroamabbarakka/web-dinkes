import os
import re

with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    txt = f.read()

print('Panjang public/assets/app.js:', len(txt))

# Cari fungsi Page
pages = re.findall(r'function\s+([a-zA-Z0-9_]+Page)\s*\(', txt)
print('Fungsi Page yang ditemukan:', len(pages))
for p in pages:
    print(' -', p)

# Cari routes
routes = re.findall(r'["\']([a-z0-9\-_]+)["\']:\s*([a-zA-Z0-9_]+Page)', txt)
print('Routes yang terdaftar:', len(routes))
for r, fn in routes:
    print(f'   /{r} -> {fn}')
