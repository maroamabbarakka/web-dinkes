with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function path(')
if pos == -1:
    pos = text.find('const path=')
if pos == -1:
    pos = text.find('const path =')

if pos != -1:
    print(text[pos:pos+300])
