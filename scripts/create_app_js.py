# -*- coding: utf-8 -*-
import json
import os

with open('public/data/puskesmas.json', 'r', encoding='utf-8') as f:
    puskesmas_list = json.load(f)

with open('public/data/articles.json', 'r', encoding='utf-8') as f:
    articles_list = json.load(f)

# Compact articles
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

# Siapkan file create_app_js_step2.py
with open('scripts/create_app_js_step2.py', 'w', encoding='utf-8') as f:
    f.write(f'''# -*- coding: utf-8 -*-
pkm_json = {json.dumps(pkm_json)}
art_json = {json.dumps(art_json)}

out_file = 'public/assets/app.js'
print("Menulis public/assets/app.js...")
''')

print("create_app_js_step2.py ready")
