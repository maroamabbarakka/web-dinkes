with open('DINKES_PINRANG_MOCKUP_V4/assets/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i in range(min(90, len(lines))):
    print(f'{i+1}: {lines[i]}')
