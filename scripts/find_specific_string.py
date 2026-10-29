import os

for root, dirs, files in os.walk('public'):
    for file in files:
        if file.endswith(('.js', '.json', '.html', '.css')):
            fp = os.path.join(root, file)
            try:
                with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
                    c = f.read()
                    if 'unsur pelaksana urusan pemerintahan' in c:
                        print('Ditemukan di:', fp)
            except Exception as e:
                pass

