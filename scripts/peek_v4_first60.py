with open('DINKES_PINRANG_MOCKUP_V4/assets/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[:60]):
    print(f'{i+1}: {l.rstrip()}')

