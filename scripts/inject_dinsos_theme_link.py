import glob, re

files = glob.glob('public/*.html')
version_str = "20261029_1400"

for f in files:
    with open(f, 'r', encoding='utf-8') as fl:
        content = fl.read()

    # Pastikan link dinsos_theme.css ada
    if 'assets/dinsos_theme.css' not in content:
        # Sisipkan setelah style.css
        content = re.sub(
            r'(<link\s+rel="stylesheet"\s+href="assets/style\.css[^"]*">)',
            r'\1<link rel="stylesheet" href="assets/dinsos_theme.css?v=' + version_str + '">',
            content
        )
    else:
        # Perbarui versi cache buster
        content = re.sub(
            r'assets/dinsos_theme\.css(?:\?v=[^"\']*)?',
            f'assets/dinsos_theme.css?v={version_str}',
            content
        )

    # Perbarui versi cache buster app.v4.js & style.css
    content = re.sub(r'assets/app\.v4\.js(?:\?v=[^"\']*)?', f'assets/app.v4.js?v={version_str}', content)
    content = re.sub(r'assets/style\.css(?:\?v=[^"\']*)?', f'assets/style.css?v={version_str}', content)

    with open(f, 'w', encoding='utf-8') as fl:
        fl.write(content)
    print(f"Updated {f}")

print("Selesai memperbarui 28 file HTML dengan tautan dinsos_theme.css.")

