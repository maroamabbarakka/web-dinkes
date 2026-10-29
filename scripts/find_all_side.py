import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
while True:
    pos = text.find('side(', idx)
    if pos == -1:
        break
    start = max(0, pos - 100)
    end = min(len(text), pos + 250)
    print(f"=== Match at {pos} ===")
    print(text[start:end])
    idx = pos + 5

