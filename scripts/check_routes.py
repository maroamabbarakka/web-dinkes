import re

with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Cari fungsi route atau renderContent
idx = content.find('function renderContent')
if idx != -1:
    print("Snippet renderContent:")
    print(content[idx:idx+2500])
else:
    print("renderContent tidak ditemukan, mencari router...")
    idx2 = content.find('function router')
    if idx2 != -1:
        print(content[idx2:idx2+2500])

