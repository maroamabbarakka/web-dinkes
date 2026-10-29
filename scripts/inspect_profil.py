with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'function profilPage\(\)\s*\{([\s\S]*?)(?=function\s+[a-zA-Z0-9_]+Page|\Z)', text)
if m:
    print('profilPage():')
    print(m.group(0)[:1500])
else:
    print('profilPage tidak ditemukan')
