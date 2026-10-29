with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'Berita Terkini Lainnya' in l or ('beritaDetailPage' in l):
        print(f"L{i+1}: {l.strip()[:100]}")
        for j in range(i, min(i+40, len(lines))):
            if 'href=' in lines[j]:
                print(f"  L{j+1}: {lines[j].strip()[:100]}")
