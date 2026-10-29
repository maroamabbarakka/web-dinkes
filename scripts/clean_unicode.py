# -*- coding: utf-8 -*-
with open('scripts/build_pages_part1.py', 'r', encoding='utf-8', errors='ignore') as f:
    t1 = f.read()

# Ganti karakter khusus dengan teks aman
t1 = t1.replace('·', '-').replace('—', '-').replace('“', '"').replace('”', '"').replace('’', "'")

with open('scripts/build_pages_part1.py', 'w', encoding='utf-8') as f:
    f.write(t1)

with open('scripts/build_pages_part2.py', 'r', encoding='utf-8', errors='ignore') as f:
    t2 = f.read()

t2 = t2.replace('·', '-').replace('—', '-').replace('“', '"').replace('”', '"').replace('’', "'")

with open('scripts/build_pages_part2.py', 'w', encoding='utf-8') as f:
    f.write(t2)

print("Sukses membersihkan karakter unicode di part1 & part2!")

