with open('public/data/pages.json', 'r', encoding='utf-8') as f:
    c = f.read()
    print("Panjang pages.json:", len(c))
    print("Snippet:", c[:1500])

