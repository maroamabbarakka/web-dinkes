with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'function ' in line and any(k in line.lower() for k in ['nav', 'page', 'render', 'route', 'view', 'hash']):
        print(f"L{i+1}: {line.strip()[:100]}")

