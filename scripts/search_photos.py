import csv, os

with open('DAFTAR_FOTO.csv', encoding='utf-8-sig', errors='ignore') as f:
    rows = list(csv.DictReader(f))

keywords = ['gedung', 'kantor', 'dinkes', 'bangunan', 'kadis', 'ramli', 'germas', 'ckg', 'puskesmas', 'posyandu', 'mobil', 'psc', 'ambulans', 'apel', 'pelayanan', 'banner']

found = []
for r in rows:
    url = r['url_file'].lower()
    fl = r['file_lokal'].lower()
    for kw in keywords:
        if kw in url or kw in fl:
            found.append((kw, r['url_file'], r['file_lokal']))
            break

print(f"Total baris foto: {len(rows)}, Ditemukan cocok: {len(found)}")
for kw, u, fpath in found[:35]:
    print(f"[{kw}] URL: {u} | File: {fpath}")
