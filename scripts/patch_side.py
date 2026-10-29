with open('scripts/build_definitive_app.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Perbaiki fungsi side
old_side = "url.endsWith('.html') ? url : url + '.html'"
new_side = "url.includes('.html') ? url : url + '.html'"

text = text.replace(old_side, new_side)

with open('scripts/build_definitive_app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Sukses perbaiki fungsi side di build_definitive_app.py!")

