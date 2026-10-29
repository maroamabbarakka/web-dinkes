import fitz

pdf_path = r'd:\# DOWNLOAD\screencapture-dinkes-pinrang-web-app-2026-10-29-10_10_12.pdf'
doc = fitz.open(pdf_path)

for i, page in enumerate(doc):
    text = page.get_text().strip()
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    print(f"=== HALAMAN {i+1} ({len(lines)} baris) ===")
    print("Top 5 lines:", lines[:5])
    if i == 0 or i == 1:
        print("Snippet:", lines[:15])

doc.close()
