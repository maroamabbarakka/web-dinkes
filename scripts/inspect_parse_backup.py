with open('scripts/parse_backup.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[:60]):
    print(f'{i+1}: {line.rstrip()}')
