import glob, os
from bs4 import BeautifulSoup

html_files = sorted(glob.glob('public/*.html'))
print(f'Total html files in public/: {len(html_files)}')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        soup = BeautifulSoup(fp.read(), 'html.parser')
        body = soup.find('body')
        data_page = body.get('data-page') if body else 'NO BODY'
        title = soup.find('title').get_text(strip=True) if soup.find('title') else 'NO TITLE'
        print(f'{os.path.basename(f):25} -> data-page="{data_page}" | {title}')
