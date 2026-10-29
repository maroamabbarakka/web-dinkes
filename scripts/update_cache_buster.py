import glob, re

version_str = "20261029_1040"

files = glob.glob('public/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as fl:
        content = fl.read()
    
    # Update app.v4.js
    new_content = re.sub(r'assets/app\.v4\.js(?:\?v=[^"\']*)?', f'assets/app.v4.js?v={version_str}', content)
    # Update style.css
    new_content = re.sub(r'assets/style\.css(?:\?v=[^"\']*)?', f'assets/style.css?v={version_str}', new_content)
    # Update v4.css
    new_content = re.sub(r'assets/v4\.css(?:\?v=[^"\']*)?', f'assets/v4.css?v={version_str}', new_content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as fl:
            fl.write(new_content)
        print(f"Updated cache buster in: {f}")

print("Selesai memperbarui 28 file HTML dengan cache buster baru.")
