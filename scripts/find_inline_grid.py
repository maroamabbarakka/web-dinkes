import re

with open('public/assets/app.v4.js', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'style="([^"]*grid-template[^"]*)"', text)
found = set()
for m in matches:
    found.add(m.group(0))

print(f"Total inline grid styles found: {len(found)}")
for item in sorted(found):
    print("-", item)

