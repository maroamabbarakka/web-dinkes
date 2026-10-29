with open('scripts/parse_backup.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(80, min(170, len(lines))):
    print(f'{i+1}: {lines[i].rstrip()}')

