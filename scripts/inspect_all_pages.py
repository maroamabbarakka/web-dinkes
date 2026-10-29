import csv

with open('DAFTAR_ARTIKEL_DAN_HALAMAN.csv', encoding='utf-8-sig', errors='ignore') as f:
    r = csv.DictReader(f)
    rows = list(r)
    print("Contoh jenis:", set(row['jenis'] for row in rows))
    pages = [row for row in rows if 'halaman' in row['jenis'].lower() or 'page' in row['jenis'].lower() or '02_HALAMAN' in row['file_html']]
    print(f"Total baris: {len(rows)}, Total halaman: {len(pages)}")
    for p in pages:
        print(f"Jenis: {p['jenis']} | Judul: {p['judul']} | URL: {p['url']} | File: {p['file_html']}")
