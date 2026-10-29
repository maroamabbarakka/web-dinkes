with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'route|router|render|location|pathname|hash', text, re.IGNORECASE)]
print('Ditemukan occurrences:', len(matches))

# Cari bagian akhir dari app.js
lines = text.split('\n')
print('Total baris:', len(lines))
print('50 baris terakhir:')
for i in range(max(0, len(lines)-60), len(lines)):
    print(f'{i+1}: {lines[i]}')
