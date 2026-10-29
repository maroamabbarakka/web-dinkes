from bs4 import BeautifulSoup

with open('scripts/dinsos_home.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("=== DAFTAR SEMUA SECTION & ELEMEN UTAMA ===")
for i, el in enumerate(soup.find_all(['header', 'section', 'footer', 'nav'])):
    cls = " ".join(el.get('class', []))
    id_attr = el.get('id', '')
    h = el.find(['h1', 'h2', 'h3'])
    h_text = h.get_text(strip=True) if h else "(no heading)"
    print(f"{i+1}. <{el.name}> class='{cls}' id='{id_attr}' -> Heading: {h_text[:60]}")
