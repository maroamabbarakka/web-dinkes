import glob, re

version_str = "20261029_0945"

files = glob.glob('public/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as fl:
        content = fl.read()
    
    # Ganti assets/app.js atau assets/app.js?v=...
    new_content = re.sub(r'assets/app\.js(?:\?v=[^"\']*)?', f'assets/app.js?v={version_str}', content)
    # Ganti assets/v4.css
    new_content = re.sub(r'assets/v4\.css(?:\?v=[^"\']*)?', f'assets/v4.css?v={version_str}', new_content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as fl:
            fl.write(new_content)
        print(f"Updated cache buster in: {f}")

print("Selesai memperbarui 28 file HTML.")
