with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('side=')
if pos != -1:
    print(text[pos-50:pos+350])
