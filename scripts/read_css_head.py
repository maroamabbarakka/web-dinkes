with open('public/assets/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

print('Panjang style.css:', len(text))
print('20 baris pertama:')
for l in text.split('\n')[:20]:
    print(' ', l)

