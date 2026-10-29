with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'const routes =' in line or 'function router(' in line or 'window.addEventListener' in line:
        print(f'Line {i+1}: {line.strip()}')
        for j in range(max(0, i-5), min(len(lines), i+35)):
            print(f'  {j+1}: {lines[j].rstrip()}')
        break

