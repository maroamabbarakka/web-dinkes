# -*- coding: utf-8 -*-
"""
Script untuk menginjeksi path gambar riil untuk artikel teratas dan poster di app.v4.js dan app.js
serta menambahkan fallback onerror yang anggun.
"""

for fname in ['public/assets/app.v4.js', 'public/assets/app.js']:
    with open(fname, 'r', encoding='utf-8') as f:
        code = f.read()

    # Perbaiki pemanggilan di home-news-list-mockup
    code = code.replace(
        '<img alt="${a.title}" src="${getSafeImageUrl(a.image)}" />',
        '<img alt="${a.title}" src="${getSafeImageUrl(a.featured_image || a.image)}" onerror="this.onerror=null;this.src=\'assets/kantor_dinkes_pinrang.jpg\';" />'
    )

    # Perbaiki pemanggilan di promkes-poster-grid
    code = code.replace(
        '<img src="${getSafeImageUrl(p.image)}" alt="${p.title}" style="width:100%;height:100%;object-fit:cover;object-position:top;display:block;" />',
        '<img src="${getSafeImageUrl(p.featured_image || p.image)}" alt="${p.title}" onerror="this.onerror=null;this.src=\'uploads/2024/06/poster-stunting-64742fd008a8b563763892c2.jpeg\';" style="width:100%;height:100%;object-fit:cover;object-position:top;display:block;" />'
    )

    # Perbarui gambar hardcoded Poster2, Poster3, Poster4
    code = code.replace(
        '"featured_image": "assets/galeri/poster-stunting-64742fd008a8b563763892c2.jpeg"',
        '"featured_image": "uploads/2024/06/poster-stunting-64742fd008a8b563763892c2.jpeg"'
    )
    code = code.replace(
        '"featured_image": "assets/galeri/VAksin-booster.jpg"',
        '"featured_image": "uploads/2024/06/DZLefUaVMAAkUdX.jpg"'
    )
    code = code.replace(
        '"featured_image": "assets/galeri/files86460Poster-Vaksin-Anak_001.jpg"',
        '"featured_image": "uploads/2024/06/assets_upload_dir_519d41d8cd98f00_files_LEAFLET-STUNTING_985_0000.jpg"'
    )
    
    # Perbarui judul poster agar sangat profesional
    code = code.replace('"title": "Poster2"', '"title": "Poster Edukasi Cegah Stunting"')
    code = code.replace('"title": "Poster3"', '"title": "Poster Vaksinasi & Imunisasi"')
    code = code.replace('"title": "Poster4"', '"title": "Leaflet Gizi Seimbang & PHBS"')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(code)

print('app.v4.js dan app.js gambar artikel & poster berhasil diselaraskan!')
