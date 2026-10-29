import re

with open('DINKES_PINRANG_MOCKUP_V4/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

hero_idx = text.find('hero')
if hero_idx != -1:
    print(text[hero_idx-50:hero_idx+2000])
else:
    print("Kata 'hero' tidak ditemukan di index.html mockup V4")
