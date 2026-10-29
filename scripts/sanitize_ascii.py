# -*- coding: utf-8 -*-

def sanitize_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    
    # Ganti bullet dan tanda petik khusus
    replacements = {
        '•': '*',
        '·': '-',
        '—': '-',
        '–': '-',
        '“': '"',
        '”': '"',
        '’': "'",
        '‘': "'",
        '…': '...',
        'é': 'e'
    }
    for k, v in replacements.items():
        txt = txt.replace(k, v)
    
    # Hapus sembarang karakter di atas 127 jika ada yang tersisa
    cleaned = []
    for c in txt:
        if ord(c) < 128:
            cleaned.append(c)
        else:
            cleaned.append(' ')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(''.join(cleaned))

sanitize_file('scripts/build_pages_part1.py')
sanitize_file('scripts/build_pages_part2.py')
print("Sanitasi ASCII selesai!")
