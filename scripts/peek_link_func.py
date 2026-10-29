with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function link(')
if pos == -1:
    pos = text.find('const link=')
if pos == -1:
    pos = text.find('const link =')

if pos != -1:
    print(text[pos:pos+300])
else:
    print("Tidak ditemukan, cari 'link('")
    matches = [m.start() for m in re.finditer(r'\blink\(', text)]
    print(matches[:5])
