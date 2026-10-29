with open('public/assets/v4.js', 'r', encoding='utf-8') as f:
    text = f.read()

print("Panjang assets/v4.js:", len(text))
print("Snippet 1000 karakter pertama:")
print(text[:1000])

