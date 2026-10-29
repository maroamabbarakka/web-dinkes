import json
from bs4 import BeautifulSoup

with open('02_HALAMAN/00014_page-id-3392.html', 'r', encoding='utf-8', errors='ignore') as fp:
    soup = BeautifulSoup(fp.read(), 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')
puskesmas_list = []

# Peta kecamatan berdasarkan nama puskesmas di Pinrang
districts = {
    'SUPPA': 'Suppa',
    'MATTIRO DECENG': 'Tiroang',
    'LANRISANG': 'Lanrisang',
    'MATTIRO BULU': 'Mattiro Bulu',
    'TEPPO': 'Patampanua',
    'SALO': 'Watang Sawitto',
    'TADANG PALIE': 'Cempa',
    'CEMPA': 'Cempa',
    'MATTIRO SOMPE': 'Mattiro Sompe',
    'BATULAPPA': 'Batulappa',
    'LEMO': 'Lembang',
    'BIRA': 'Lembang',
    'TADOKKONG': 'Lembang',
    'DUAMPANUA': 'Duampanua',
    'LALINGANGA': 'Duampanua',
    'PARIA': 'Duampanua',
    'KABALLANGAN': 'Duampanua',
    'SULILI': 'Paleteang',
    'TIROANG': 'Tiroang'
}

for r in rows:
    tds = [td.get_text(' ', strip=True) for td in r.find_all(['td', 'th'])]
    if len(tds) >= 6 and tds[0].isdigit():
        nama = tds[1].replace('PUSKESMAS', '').strip()
        raw_name = tds[1].strip()
        if not raw_name.startswith('PUSKESMAS'):
            raw_name = 'PUSKESMAS ' + raw_name
        
        # Cari kecamatan
        kec = 'Pinrang'
        for k, v in districts.items():
            if k in raw_name.upper():
                kec = v
                break
        
        puskesmas_list.append({
            'no': int(tds[0]),
            'slug': raw_name.lower().replace(' ', '-').replace('.', ''),
            'name': raw_name,
            'district': kec,
            'address': tds[2].replace('\xa0', ' '),
            'head': tds[3].replace('\xa0', ' '),
            'head_title': 'Kepala UPTD Puskesmas',
            'innovations': [inv.strip() for inv in tds[4].replace('\xa0', ' ').split('\n') if inv.strip()],
            'innovations_text': tds[4].replace('\xa0', ' '),
            'awards': [aw.strip() for aw in tds[5].replace('\xa0', ' ').split('\n') if aw.strip()],
            'awards_text': tds[5].replace('\xa0', ' '),
            'website': tds[6].replace('_', '').strip() if len(tds) > 6 else '',
            'phone': '+62 853-4217-2724',
            'emergency': '119 / +62 853-4217-2724',
            'accreditation': 'Paripurna (Kemenkes RI)',
            'hours': 'Senin - Sabtu: 08:00 - 14:00 WITA (UGD & Bersalin 24 Jam)'
        })

print(f'Total puskesmas parsed: {len(puskesmas_list)}')
with open('public/data/puskesmas.json', 'w', encoding='utf-8') as fp:
    json.dump(puskesmas_list, fp, ensure_ascii=False, indent=2)

print('Sukses update public/data/puskesmas.json!')

