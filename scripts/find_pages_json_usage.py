with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'pages.json' in line or 'initPage' in line or 'loadPage' in line or 'renderPage' in line:
        print(f"L{i+1}: {line.strip()[:100]}")

