import fitz, os
from PIL import Image

doc = fitz.open(r'd:\# DOWNLOAD\screencapture-dinkes-pinrang-web-app-2026-10-29-10_10_12.pdf')

# Ekstrak 12 slice unik
slices = []
total_height = 0
width = 0

for xref in range(41, 53):
    img_data = doc.extract_image(xref)
    import io
    im = Image.open(io.BytesIO(img_data['image']))
    slices.append(im)
    width = max(width, im.width)
    total_height += im.height

print(f"Total slices: {len(slices)}, Dimensi penuh: {width} x {total_height}")

full_img = Image.new('RGB', (width, total_height))
y_offset = 0
for im in slices:
    full_img.paste(im, (0, y_offset))
    y_offset += im.height

out_full = r'C:\Users\ASUS\.gemini\antigravity\brain\ffe98454-07d7-4f5c-86aa-8c238e2e2bde\full_screencapture_stitched.png'
full_img.save(out_full, quality=90)
print(f"Berhasil menyimpan gambar penuh ke: {out_full} ({os.path.getsize(out_full)} bytes)")

doc.close()
