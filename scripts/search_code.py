import os

search_term = "Mengabdi untuk masyarakat"
found = False

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for f in files:
        if f.endswith(('.js', '.html', '.json', '.md')):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                    if search_term in content:
                        print(f'Ditemukan di: {p}')
                        found = True
            except:
                pass

if not found:
    print('Tidak ditemukan!')

