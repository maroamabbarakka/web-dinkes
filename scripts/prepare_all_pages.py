# -*- coding: utf-8 -*-
"""
Script utama untuk merakit public/assets/app.js secara menyeluruh.
"""

import json
import os

with open('public/data/puskesmas.json', 'r', encoding='utf-8') as f:
    puskesmas_list = json.load(f)

with open('public/data/articles.json', 'r', encoding='utf-8') as f:
    articles_list = json.load(f)

print(f"Data otentik siap: {len(puskesmas_list)} Puskesmas, {len(articles_list)} Artikel")

# Siapkan data ringkas artikel
compact_articles = []
for a in articles_list:
    exc = a.get('excerpt', '')
    if len(exc) > 170:
        exc = exc[:170] + '...'
    compact_articles.append({
        'id': str(a.get('id')),
        'title': a.get('title'),
        'slug': a.get('slug'),
        'published_at': a.get('published_at'),
        'author': a.get('author'),
        'category': a.get('category') or 'Berita',
        'featured_image': a.get('featured_image'),
        'excerpt': exc
    })

pkm_json = json.dumps(puskesmas_list, ensure_ascii=False)
art_json = json.dumps(compact_articles, ensure_ascii=False)

# Baca helper functions dari build_full_script.py
with open('scripts/build_full_script.py', 'r', encoding='utf-8') as f:
    gen_text = f.read()

# Ekstrak bagian code awal
m_code = gen_text.split('code = """')[1]
header_and_home = m_code.split('// 1. BERANDA (homePage)')[0]
home_code = m_code.split('// 1. BERANDA (homePage)')[1].split('"""')[0]

with open('scripts/assemble_app.py', 'w', encoding='utf-8') as out:
    out.write(f'''# -*- coding: utf-8 -*-
import json

pkm_json = {json.dumps(pkm_json)}
art_json = {json.dumps(art_json)}

part1 = r"""{header_and_home}"""

part_home = r"""// 1. BERANDA (homePage)
{home_code}"""

print("Part 1 & Home ready")
''')

print("Generator assemblying app.js...")

