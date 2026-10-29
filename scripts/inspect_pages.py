with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re

def show_func(name):
    m = re.search(r'function ' + name + r'\(\)\s*\{([\s\S]*?)(?=function\s+[a-zA-Z0-9_]+Page|\Z)', text)
    if m:
        print(f'=== {name} (panjang: {len(m.group(0))}) ===')
        print(m.group(0)[:800])
        print('...\n')

for fn in ['homePage', 'profilPage', 'organisasiPage', 'layananPage', 'puskesmasPage', 'edukasiPage', 'beritaPage', 'dataPage']:
    show_func(fn)
