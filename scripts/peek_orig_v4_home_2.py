with open('DINKES_PINRANG_MOCKUP_V4/assets/app.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = text.find('function homePage')
if pos != -1:
    print(text[pos+2000:pos+4500])

