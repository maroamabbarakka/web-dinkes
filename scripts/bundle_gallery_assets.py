import os, shutil, json

os.makedirs('public/assets/galeri', exist_ok=True)

# Baca gallery_albums.json
with open('public/data/gallery_albums.json', 'r', encoding='utf-8') as f:
    albums = json.load(f)

for a in albums:
    cover_src = os.path.join('public', a['cover'])
    cover_name = os.path.basename(a['cover'])
    cover_dst = os.path.join('public/assets/galeri', cover_name)
    if os.path.exists(cover_src):
        shutil.copyfile(cover_src, cover_dst)
    a['cover'] = f"assets/galeri/{cover_name}"

    for p in a['photos']:
        p_src = os.path.join('public', p['url'])
        p_name = os.path.basename(p['url'])
        p_dst = os.path.join('public/assets/galeri', p_name)
        if os.path.exists(p_src):
            shutil.copyfile(p_src, p_dst)
        p['url'] = f"assets/galeri/{p_name}"

with open('public/data/gallery_albums.json', 'w', encoding='utf-8') as f:
    json.dump(albums, f, ensure_ascii=False, indent=2)
print("Berhasil menyalin semua foto album ke public/assets/galeri/")

# Periksa poster promkes di articles.json
with open('public/data/articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

for art in articles:
    if art.get('content_type') == 'promkes' or art.get('id') in ['350', '352', '354', '2278', '3033']:
        feat = art.get('featured_image', '')
        if 'uploads/' in feat:
            rel_path = feat[feat.find('uploads/'):]
            full_src = os.path.join('public', rel_path)
            if os.path.exists(full_src):
                fname = os.path.basename(rel_path)
                dst = os.path.join('public/assets/galeri', fname)
                shutil.copyfile(full_src, dst)
                art['featured_image'] = f"assets/galeri/{fname}"
                print(f"Salin poster {art['id']} ke assets/galeri/{fname}")

with open('public/data/articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)
print("Berhasil memperbarui articles.json.")

