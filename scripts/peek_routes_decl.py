with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[:30]):
    if 'ROUTES' in l:
        print(f"L{i+1}: {l.strip()[:150]}")

