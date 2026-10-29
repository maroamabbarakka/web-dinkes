# -*- coding: utf-8 -*-
import os, glob

html_files = glob.glob('public/*.html')
print(f'Memperbarui {len(html_files)} berkas HTML...')

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
        
    orig = content
    # Update gambar hero
    content = content.replace('assets/hero_illustration_dinkes.png', 'assets/kolase_emblem_dinkes_pinrang_opt.png')
    
    # Update penyebutan angka 19 pada Puskesmas
    content = content.replace('>19 Puskesmas<', '>Puskesmas<')
    content = content.replace('>19 UPTD Puskesmas<', '>Puskesmas<')
    content = content.replace('Direktori 19 UPTD Puskesmas', 'Direktori Puskesmas')
    content = content.replace('19 UPTD Puskesmas', 'UPTD Puskesmas')
    
    # Update cache-busting version
    content = content.replace('dinsos_theme.css?v=20261029_1400', 'dinsos_theme.css?v=20261029_1500')
    content = content.replace('app.v4.js?v=20261029_1300', 'app.v4.js?v=20261029_1500')
    content = content.replace('app.js?v=20261029_1300', 'app.js?v=20261029_1500')
    
    if content != orig:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {hf}')

print('Seluruh berkas HTML telah diselaraskan!')
