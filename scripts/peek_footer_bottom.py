with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function footer()')
if pos != -1:
    print(text[pos+1000:pos+2500])
