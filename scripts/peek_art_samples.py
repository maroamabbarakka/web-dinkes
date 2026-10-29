import json

with open('public/data/articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

for a in articles:
    if a['id'] in ['4164', '4252', '4505', '4498', '4053', '4492']:
        print(f"ID: {a['id']} | Judul: {a['title']} | Image: {a.get('featured_image')}")

