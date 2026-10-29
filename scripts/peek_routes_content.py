with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(45, 80):
    print(f"L{i+1}: {lines[i]}", end='')

