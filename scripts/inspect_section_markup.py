import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from bs4 import BeautifulSoup

with open('scripts/dinsos_home.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

def print_section(selector, title):
    print(f"\n==================== {title} ({selector}) ====================")
    el = soup.select_one(selector)
    if el:
        html = el.prettify()
        lines = html.splitlines()
        print(f"Total lines: {len(lines)}")
        print("\n".join(lines[:60]))
        if len(lines) > 60:
            print("... [truncated] ...")
    else:
        print("NOT FOUND")

print_section('.service-strip', 'TOP BAR SERVICE STRIP')
print_section('.site-header', 'SITE HEADER')
print_section('.hero--mockup', 'HERO SECTION')
print_section('.quick-access-mockup', 'QUICK ACCESS')
print_section('.section-services-mockup', 'LAYANAN UTAMA')
print_section('.alert-mockup-section', 'ALERT BANNER')
print_section('.home-info-mockup-section', 'INFORMASI TERBARU & DOKUMEN')
print_section('.psks-section', 'PSKS SECTION')
print_section('.site-footer', 'SITE FOOTER')
print_section('.mobile-dock', 'MOBILE DOCK')
