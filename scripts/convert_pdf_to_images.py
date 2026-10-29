import fitz, os

pdf_path = r'd:\# DOWNLOAD\screencapture-dinkes-pinrang-web-app-2026-10-29-10_10_12.pdf'
doc = fitz.open(pdf_path)
print(f"Total Halaman PDF: {len(doc)}")

out_dir = r'C:\Users\ASUS\.gemini\antigravity\brain\ffe98454-07d7-4f5c-86aa-8c238e2e2bde'

for i, page in enumerate(doc):
    rect = page.rect
    print(f"Halaman {i+1}: Lebar {rect.width} x Tinggi {rect.height}")
    pix = page.get_pixmap(dpi=150)
    out_path = os.path.join(out_dir, f"screencapture_page_{i+1}.png")
    pix.save(out_path)
    print(f"Tersimpan ke: {out_path} ({os.path.getsize(out_path)} bytes)")

doc.close()

