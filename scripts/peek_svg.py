with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('const SVG={')
if pos != -1:
    print(text[pos:pos+1200])

