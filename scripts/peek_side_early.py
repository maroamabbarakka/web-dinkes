import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[:120]):
    if 'side' in l.lower():
        print(f"L{i+1}: {l.strip()[:120]}")
