import os, csv
from bs4 import BeautifulSoup

def clean_html(html_path):
    if not os.path.exists(html_path):
        return ""
    with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    # Cari konten artikel/page utama
    content_div = soup.find('div', class_='entry-content') or soup.find('article') or soup.find('main')
    if content_div:
        # Bersihkan script, style
        for s in content_div(['script', 'style', 'noscript']):
            s.decompose()
        return str(content_div)
    return ""

with open('DAFTAR_ARTIKEL_DAN_HALAMAN.csv', encoding='utf-8-sig', errors='ignore') as f:
    rows = list(csv.DictReader(f))
    pages = [r for r in rows if '02_HALAMAN' in r['file_html']]
    for p in pages:
        txt_path = p['file_teks']
        txt_len = os.path.getsize(txt_path) if os.path.exists(txt_path) else 0
        print(f"=== {p['judul']} ({p['file_html']}) - Teks: {txt_len} bytes ===")
        if os.path.exists(txt_path):
            with open(txt_path, 'r', encoding='utf-8', errors='ignore') as tf:
                lines = [line.strip() for line in tf.readlines() if line.strip()]
                print("Cuplikan:", lines[:4])

