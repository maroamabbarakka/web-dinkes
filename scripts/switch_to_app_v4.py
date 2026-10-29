import glob, re

files = glob.glob('public/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as fl:
        content = fl.read()
    
    # Ganti assets/app.js atau assets/app.js?v=... menjadi assets/app.v4.js
    new_content = re.sub(r'assets/app(?:\.v4)?\.js(?:\?[^"\']*)?', 'assets/app.v4.js', content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as fl:
            fl.write(new_content)
        print(f"Updated script in: {f}")

print("Selesai memperbarui 28 HTML ke app.v4.js")
