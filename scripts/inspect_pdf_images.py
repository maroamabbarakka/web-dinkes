import fitz

doc = fitz.open(r'd:\# DOWNLOAD\screencapture-dinkes-pinrang-web-app-2026-10-29-10_10_12.pdf')
for i in range(len(doc)):
    page = doc[i]
    images = page.get_images()
    print(f"Halaman {i+1}: {len(images)} gambar tertanam")
    for img_info in images:
        xref = img_info[0]
        base_img = doc.extract_image(xref)
        print(f"  xref: {xref}, ext: {base_img['ext']}, w: {base_img['width']}, h: {base_img['height']}")
doc.close()

