with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("50 baris terakhir app.js:")
for i in range(max(0, len(lines)-50), len(lines)):
    print(f"L{i+1}: {lines[i]}", end='')
