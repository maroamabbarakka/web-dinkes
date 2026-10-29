with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function footer()')
if pos != -1:
    print(text[pos:pos+1500])
else:
    print("function footer() tidak ditemukan")

