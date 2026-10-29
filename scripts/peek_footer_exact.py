with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Dinas Kesehatan Pemerintah Ka')
if pos != -1:
    print(text[pos-20:pos+500])
