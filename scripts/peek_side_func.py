with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Line 930-935:")
for l in lines[928:936]:
    print(l, end='')

for i, l in enumerate(lines[:120]):
    if 'function side(' in l:
        print(f"\nImplementasi side di L{i+1}:")
        for j in range(i, i+15):
            print(lines[j], end='')

