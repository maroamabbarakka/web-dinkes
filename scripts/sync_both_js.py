import json, re

with open('public/data/articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

with open('public/data/gallery_albums.json', 'r', encoding='utf-8') as f:
    albums = json.load(f)

cache_items = []
for a in articles:
    cache_items.append({
        "id": str(a.get("id")),
        "title": a.get("title", ""),
        "slug": a.get("slug", ""),
        "published_at": a.get("published_at") or a.get("date", ""),
        "author": a.get("author") or "Dinkes Pinrang",
        "category": a.get("category") or "Berita",
        "content_type": a.get("content_type", "berita"),
        "type_label": a.get("type_label", "Berita & Kegiatan"),
        "featured_image": a.get("featured_image", ""),
        "excerpt": (a.get("excerpt", "") or "")[:200]
    })

cache_json = json.dumps(cache_items, ensure_ascii=False)
albums_json = json.dumps(albums, ensure_ascii=False)

for target_file in ['public/assets/app.v4.js', 'public/assets/app.js']:
    with open(target_file, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Ganti window.GALLERY_ALBUMS
    code = re.sub(r'window\.GALLERY_ALBUMS\s*=\s*\[.*?\];\n', f'window.GALLERY_ALBUMS = {albums_json};\n', code, flags=re.DOTALL)
    # Ganti window.ARTICLES_CACHE
    code = re.sub(r'window\.ARTICLES_CACHE\s*=\s*\[.*?\];\n', f'window.ARTICLES_CACHE = {cache_json};\n', code, flags=re.DOTALL)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Updated {target_file}")

