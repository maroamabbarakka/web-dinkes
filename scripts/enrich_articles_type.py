import json, re

with open('public/data/articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

for a in articles:
    title = a['title'].lower()
    content = a.get('content', '').lower()
    
    # 1. Promkes & Poster
    if any(k in title for k in ['poster', 'leaflet', 'infografis', 'brosur', 'spanduk', 'banner']):
        a['content_type'] = 'promkes'
        a['type_label'] = 'Materi Promkes & Poster'
    # 2. Artikel Kesehatan & Edukasi
    elif any(k in title for k in ['kenali', 'gejala', 'tips', 'faktor risiko', 'panduan', 'cara mencegah', 'manfaat', 'pentingnya', 'edukasi']) or 'Artikel' in a.get('category', ''):
        a['content_type'] = 'artikel'
        a['type_label'] = 'Artikel Kesehatan'
    # 3. Dokumentasi Lapangan
    elif any(k in title for k in ['dokumentasi', 'pemeriksaan gratis', 'fogging', 'posyandu keliling', 'posbindu', 'skrining massal', 'kegiatan lapangan', 'kunjungan rumah']):
        a['content_type'] = 'dokumentasi'
        a['type_label'] = 'Dokumentasi Lapangan'
    # 4. Berita & Kegiatan Dinas
    else:
        a['content_type'] = 'berita'
        a['type_label'] = 'Berita & Kegiatan Dinas'

counts = {}
for a in articles:
    t = a['content_type']
    counts[t] = counts.get(t, 0) + 1

print("Hasil klasifikasi:", counts)

# Simpan kembali articles.json
with open('public/data/articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)
print("Berhasil memperbarui public/data/articles.json")
