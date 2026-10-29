import json

with open('public/data/articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

print(f"Total artikel: {len(articles)}")
categories = {}
for a in articles:
    cat = a.get('category') or 'Umum'
    categories[cat] = categories.get(cat, 0) + 1

print("Distribusi Kategori:", categories)

# Cek artikel yang mengandung kata poster/leaflet/stunting/covid/vaksin
posters = [a for a in articles if any(k in a['title'].lower() for k in ['poster', 'leaflet', 'infografis', 'brosur'])]
print(f"Total poster/leaflet ditemukan di judul: {len(posters)}")
for p in posters[:10]:
    print(f"ID: {p['id']} | Judul: {p['title']} | Gambar: {p.get('featured_image')}")

