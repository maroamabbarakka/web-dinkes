import json
import os

with open('public/data/articles.json', 'r', encoding='utf-8') as fp:
    articles = json.load(fp)

print(f'Total artikel di articles.json: {len(articles)}')

# Cek artikel dengan gambar
with_img = [a for a in articles if a.get('image')]
print(f'Artikel yang memiliki atribut image: {len(with_img)}')

# Periksa 10 artikel teratas
for a in articles[:8]:
    img = a.get('image', 'TIDAK ADA')
    # Cek apakah file lokal ada di uploads
    local_img = img.replace('https://dinkes.pinrangkab.go.id/wp-content/uploads/', '03_FOTO/wp-content/uploads/').replace('/', os.sep)
    exists = os.path.exists(local_img)
    print(f"ID {a['id']}: {a['title'][:55]}... | Img: {os.path.basename(img)} (Exists: {exists})")
