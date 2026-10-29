import json, re

with open('public/data/articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Format ringkas untuk ARTICLES_CACHE
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

with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Ganti window.ARTICLES_CACHE
pattern = r'window\.ARTICLES_CACHE\s*=\s*\[.*?\];\n'
match = re.search(pattern, code, flags=re.DOTALL)
if match:
    code = code[:match.start()] + f"window.ARTICLES_CACHE = {cache_json};\n" + code[match.end():]
    print("Berhasil mengganti window.ARTICLES_CACHE dengan data terklasifikasi!")
else:
    print("window.ARTICLES_CACHE tidak ditemukan dengan regex!")

with open('public/assets/app.js', 'w', encoding='utf-8') as f:
    f.write(code)
