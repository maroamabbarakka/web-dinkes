import glob
import os

files = glob.glob('DINKES_PINRANG_MOCKUP_V4/*.html')
print(f'Menemukan {len(files)} berkas HTML...')

for f in files:
    fname = os.path.basename(f)
    with open(f, 'r', encoding='utf-8') as src:
        text = src.read()
    
    # Update script tag dan metadata
    text = text.replace('src="assets/app.js"', 'type="module" src="assets/app.js"')
    text = text.replace('Mockup V4 Dinkes Pinrang', 'Dinas Kesehatan Kabupaten Pinrang')
    text = text.replace('Mockup UI/UX Dinas Kesehatan Kabupaten Pinrang. Bukan situs resmi.', 'Portal Resmi Dinas Kesehatan Kabupaten Pinrang, Sulawesi Selatan')
    
    dst_path = os.path.join('public', fname)
    with open(dst_path, 'w', encoding='utf-8') as dst:
        dst.write(text)

print(f'Berhasil menyalin {len(files)} berkas HTML ke public/!')
