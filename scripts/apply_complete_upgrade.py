# -*- coding: utf-8 -*-
import json
import re

# Load dataset
with open('public/data/puskesmas.json', 'r', encoding='utf-8') as f:
    puskesmas_data = json.load(f)

with open('public/data/articles.json', 'r', encoding='utf-8') as f:
    articles_data = json.load(f)

print(f"Data siap: {len(puskesmas_data)} puskesmas, {len(articles_data)} artikel")

# Siapkan data json inline yang aman di app.js agar app.js bisa berjalan mandiri tanpa fetch gagal
pkm_json_str = json.dumps(puskesmas_data, ensure_ascii=False)
# Ambil 50 artikel teratas untuk pre-cache instan di browser
articles_preview = articles_data[:60]
articles_preview_str = json.dumps(articles_preview, ensure_ascii=False)

print("Menyusun kode upgrade...")

