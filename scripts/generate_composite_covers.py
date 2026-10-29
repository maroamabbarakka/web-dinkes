# -*- coding: utf-8 -*-
"""
Script penyempurnaan pembuatan Visual Cover Profesional Berbasis Foto Riil & Desain Grafis Modern
Warna Berbeda untuk Setiap Kartu Layanan dan Pilar Transformasi
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = 'public/assets/covers'
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_BOLD = r'C:\Windows\Fonts\segoeuib.ttf'
FONT_REG = r'C:\Windows\Fonts\segoeui.ttf'
FONT_SEMI = r'C:\Windows\Fonts\seguisb.ttf'

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def create_rich_card(cfg):
    w, h = 800, 480
    bg_start = cfg['bg_start']
    bg_end = cfg['bg_end']
    accent = cfg['accent']
    
    # 1. Base Gradient
    base = Image.new('RGB', (w, h), bg_start)
    top = Image.new('RGB', (w, h), bg_end)
    mask = Image.new('L', (w, h))
    mask_data = []
    for y in range(h):
        for x in range(w):
            val = int(255 * (x * 0.7 + y * 0.3) / (w * 0.7 + h * 0.3))
            mask_data.append(val)
    mask.putdata(mask_data)
    img = Image.composite(top, base, mask).convert('RGBA')
    
    # 2. Ornamen Geometri Modern (Glow & Subtle Grid)
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    
    # Glow sudut
    odraw.ellipse((w - 240, -100, w + 100, 240), fill=accent + (55,))
    odraw.ellipse((-100, h - 200, 150, h + 80), fill=(255, 255, 255, 20))
    
    # Grid lines halus
    for i in range(0, w, 40):
        odraw.line([(i, 0), (i, h)], fill=(255, 255, 255, 14), width=1)
    for j in range(0, h, 40):
        odraw.line([(0, j), (w, j)], fill=(255, 255, 255, 14), width=1)
        
    img = Image.alpha_composite(img, overlay)
    
    # 3. Masukkan & Olah Foto Dokumentasi Riil di Sisi Kanan
    photo_w, photo_h = 360, 360
    photo_x, photo_y = w - photo_w - 40, (h - photo_h) // 2
    
    photo_src_path = cfg.get('photo_src')
    if photo_src_path and os.path.exists(photo_src_path):
        with Image.open(photo_src_path) as pimg:
            pimg = pimg.convert('RGB')
            pw, ph = pimg.size
            ratio = max(photo_w / pw, photo_h / ph)
            p_resized = pimg.resize((int(pw * ratio), int(ph * ratio)), Image.Resampling.LANCZOS)
            cx, cy = (p_resized.width - photo_w) // 2, (p_resized.height - photo_h) // 2
            p_cropped = p_resized.crop((cx, cy, cx + photo_w, cy + photo_h))
            
            p_mask = Image.new('L', (photo_w, photo_h), 0)
            p_draw = ImageDraw.Draw(p_mask)
            p_draw.rounded_rectangle((0, 0, photo_w, photo_h), radius=28, fill=255)
            
            shadow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
            sdraw = ImageDraw.Draw(shadow)
            sdraw.rounded_rectangle((photo_x + 6, photo_y + 12, photo_x + photo_w + 6, photo_y + photo_h + 12), radius=30, fill=(0, 0, 0, 85))
            shadow = shadow.filter(ImageFilter.GaussianBlur(16))
            img = Image.alpha_composite(img, shadow)
            
            img.paste(p_cropped, (photo_x, photo_y), p_mask)
            
            p_overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
            podraw = ImageDraw.Draw(p_overlay)
            podraw.rounded_rectangle((photo_x, photo_y, photo_x + photo_w, photo_y + photo_h), radius=28, outline=(255, 255, 255, 190), width=3)
            
            badge_font = get_font(FONT_SEMI, 13)
            pill_text = cfg.get('photo_tag', 'DOKUMENTASI RESMI')
            pbbox = badge_font.getbbox(pill_text)
            ptw = pbbox[2] - pbbox[0]
            pth = pbbox[3] - pbbox[1]
            bx = photo_x + 20
            by = photo_y + photo_h - 48
            podraw.rounded_rectangle((bx, by, bx + ptw + 24, by + pth + 14), radius=10, fill=bg_start + (235,), outline=(255, 255, 255, 140), width=1)
            podraw.text((bx + 12, by + 7 - pbbox[1]), pill_text, font=badge_font, fill=(255, 255, 255, 255))
            
            img = Image.alpha_composite(img, p_overlay)
            
    # 4. Gambar Teks dan Informasi Layanan Menggunakan Alpha Composite
    text_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(text_layer)
    
    f_kicker = get_font(FONT_BOLD, 13)
    f_title = get_font(FONT_BOLD, 31)
    f_desc = get_font(FONT_REG, 15)
    f_tag = get_font(FONT_SEMI, 13)
    
    # Kicker Badge Kategori (Gambar di layer RGBA dengan alpha blend sejati)
    kicker_text = cfg['kicker'].upper()
    k_bbox = f_kicker.getbbox(kicker_text)
    kw = k_bbox[2] - k_bbox[0]
    kh = k_bbox[3] - k_bbox[1]
    
    kx, ky = 48, 52
    draw.rounded_rectangle((kx, ky, kx + kw + 28, ky + kh + 16), radius=12, fill=(0, 0, 0, 75), outline=(255, 255, 255, 140), width=1)
    # Titik kecil emas di depan teks kicker
    draw.ellipse((kx + 12, ky + 11, kx + 18, ky + 17), fill=(253, 224, 71, 255))
    draw.text((kx + 24, ky + 8 - k_bbox[1]), kicker_text, font=f_kicker, fill=(255, 255, 255, 255))
    
    # Judul Layanan
    ty = 115
    for tline in cfg['title_lines']:
        draw.text((48, ty), tline, font=f_title, fill=(255, 255, 255, 255))
        ty += 38
        
    # Deskripsi Ringkas
    ty += 14
    for dline in cfg['desc_lines']:
        draw.text((48, ty), dline, font=f_desc, fill=(255, 255, 255, 225))
        ty += 24
        
    # Garis Pembatas Halus & Status Unggulan
    line_y = h - 94
    draw.line([(48, line_y), (photo_x - 30, line_y)], fill=(255, 255, 255, 60), width=1)
    
    # Badge Status Transparansi
    stat_x, stat_y = 48, line_y + 18
    draw.ellipse((stat_x, stat_y + 3, stat_x + 12, stat_y + 15), fill=(74, 222, 128, 255))
    draw.text((stat_x + 20, stat_y), cfg['status_text'], font=f_tag, fill=(255, 255, 255, 250))
    
    img = Image.alpha_composite(img, text_layer)
    
    # Simpan hasil
    out_file = os.path.join(OUTPUT_DIR, cfg['filename'])
    img = img.convert('RGB')
    img.save(out_file, quality=94, optimize=True)
    print(f'Saved: {out_file}')

SERVICE_CARDS = [
    {
        'filename': 'service_puskesmas.jpg',
        'bg_start': (6, 78, 59),       # Emerald Hijau (#064e3b)
        'bg_end': (5, 150, 105),        # Emerald Cerah (#059669)
        'accent': (16, 185, 129),
        'photo_src': 'public/assets/puskesmas.png',
        'photo_tag': 'FASKES PRIMER KEMENKES',
        'kicker': 'Fasilitas Pelayanan Primer',
        'title_lines': ['Pelayanan Rawat', 'Jalan & Inap Puskesmas'],
        'desc_lines': [
            'Pemeriksaan umum, poli gigi, KIA, KB,',
            'laboratorium penunjang, persalinan, dan',
            'fasilitas Unit Gawat Darurat (UGD) 24 jam.'
        ],
        'status_text': 'Gratis Bagi Peserta BPJS / KIS Resmi'
    },
    {
        'filename': 'service_sip_nakes.jpg',
        'bg_start': (23, 37, 84),       # Sapphire Navy (#172554)
        'bg_end': (29, 78, 216),        # Royal Blue (#1d4ed8)
        'accent': (59, 130, 246),
        'photo_src': 'public/uploads/2020/11/piagam-rabies.jpg',
        'photo_tag': 'VERIFIKASI RESMI DINAS',
        'kicker': 'Sumber Daya Kesehatan (SDK)',
        'title_lines': ['Rekomendasi SIP', '& SIK Tenaga Medis'],
        'desc_lines': [
            'Penerbitan surat rekomendasi izin praktik',
            'dokter, bidan, perawat, apoteker, dan tenaga',
            'kesehatan secara transparan dan terstandar.'
        ],
        'status_text': 'Bebas Pungutan Liar (0 Rupiah)'
    },
    {
        'filename': 'service_pangan_sppirt.jpg',
        'bg_start': (120, 53, 15),      # Amber Cokelat (#78350f)
        'bg_end': (217, 119, 6),        # Golden Amber (#d97706)
        'accent': (245, 158, 11),
        'photo_src': 'public/uploads/2021/08/KIE-Keamanan-pangan.jpg',
        'photo_tag': 'MUTU PANGAN & HIGIENITAS',
        'kicker': 'Kefarmasian & Keamanan Pangan',
        'title_lines': ['Sertifikasi Pangan', 'Industri Rumah Tangga (SPP-IRT)'],
        'desc_lines': [
            'Penyuluhan keamanan pangan (PKP) serta',
            'inspeksi higienis sarana produksi industri',
            'rumah tangga untuk produk UMKM Pinrang.'
        ],
        'status_text': 'Fasilitasi Pembinaan Pemkab Pinrang'
    },
    {
        'filename': 'service_ckg.jpg',
        'bg_start': (14, 116, 144),     # Ocean Cyan (#0e7490)
        'bg_end': (8, 145, 178),        # Teal Cerah (#0891b2)
        'accent': (14, 165, 233),
        'photo_src': 'public/uploads/2021/02/posyandu-lansia.jpg',
        'photo_tag': 'SKRINING KESEHATAN GRATIS',
        'kicker': 'Deteksi Dini & Pencegahan Penyakit',
        'title_lines': ['Cek Kesehatan Gratis', '(Program CKG Pinrang)'],
        'desc_lines': [
            'Skrining tekanan darah, gula darah sewaktu,',
            'kolesterol, asam urat, serta faktor risiko',
            'penyakit tidak menular berkala di Puskesmas.'
        ],
        'status_text': '100% Bebas Biaya di Seluruh Puskesmas'
    },
    {
        'filename': 'service_stunting_gizi.jpg',
        'bg_start': (136, 19, 55),      # Deep Rose (#881337)
        'bg_end': (225, 29, 72),        # Coral Rose (#e11d48)
        'accent': (244, 63, 94),
        'photo_src': 'public/uploads/2021/04/rembuk-stunting.jpg',
        'photo_tag': 'AKSI KONVERGENSI STUNTING',
        'kicker': 'Kesehatan Masyarakat & Gizi',
        'title_lines': ['Pencegahan Stunting', '& Imunisasi Terpadu'],
        'desc_lines': [
            'Pemantauan tumbuh kembang balita, pemberian',
            'makanan tambahan (PMT), tablet tambah darah,',
            'dan imunisasi lengkap berkelanjutan di Posyandu.'
        ],
        'status_text': 'Prioritas Transformasi Kesehatan Nasional'
    },
    {
        'filename': 'service_psc119.jpg',
        'bg_start': (127, 29, 29),      # Crimson Red (#7f1d1d)
        'bg_end': (220, 38, 38),        # Red Warning (#dc2626)
        'accent': (239, 68, 68),
        'photo_src': 'public/assets/kolase_emblem_dinkes_pinrang_opt.png',
        'photo_tag': 'SIAGA 24 JAM NONSTOP',
        'kicker': 'Kedaruratan Medis Terpadu',
        'title_lines': ['Layanan Darurat Medis', 'Public Safety Center (PSC 119)'],
        'desc_lines': [
            'Respon cepat kegawatdaruratan medis, evakuasi',
            'korban kecelakaan, armada ambulans siaga,',
            'serta rujukan berkesinambungan antar fasilitas.'
        ],
        'status_text': 'Call Center Bebas Pulsa & Reaksi Cepat'
    }
]

PILAR_CARDS = [
    {
        'filename': 'pilar_puskesmas.jpg',
        'bg_start': (15, 118, 110),     # Teal (#0f766e)
        'bg_end': (20, 184, 166),       # Light Teal (#14b8a6)
        'accent': (45, 212, 191),
        'photo_src': 'public/assets/puskesmas.png',
        'photo_tag': 'UPTD PUSKESMAS DAERAH',
        'kicker': 'Pilar 1: Layanan Primer',
        'title_lines': ['Puskesmas Pelayanan', 'Kesehatan Masyarakat'],
        'desc_lines': [
            'Jaringan faskes tingkat pertama yang menyelenggarakan',
            'pelayanan rawat jalan, rawat inap, poli KIA,',
            'laboratorium, dan IGD 24 Jam di 12 kecamatan.'
        ],
        'status_text': 'Terintegrasi di Seluruh Wilayah Pinrang'
    },
    {
        'filename': 'pilar_germas.jpg',
        'bg_start': (21, 128, 61),      # Green (#15803d)
        'bg_end': (34, 197, 94),        # Bright Green (#22c55e)
        'accent': (74, 222, 128),
        'photo_src': 'public/uploads/2021/02/posyandu-lansia.jpg',
        'photo_tag': 'GERAKAN MASYARAKAT HIDUP SEHAT',
        'kicker': 'Pilar 2: Promotif & Preventif',
        'title_lines': ['GERMAS Pinrang', 'Gerakan Hidup Sehat'],
        'desc_lines': [
            'Pemberdayaan masyarakat melalui aktivitas fisik teratur,',
            'konsumsi buah dan sayur, skrining kesehatan berkala,',
            'serta komitmen 100% Bebas Buang Air Besar (ODF).'
        ],
        'status_text': 'Membudayakan Gaya Hidup Sehat Mandiri'
    },
    {
        'filename': 'pilar_psc119.jpg',
        'bg_start': (194, 65, 12),      # Orange (#c2410c)
        'bg_end': (249, 115, 22),       # Amber Orange (#f97316)
        'accent': (251, 146, 60),
        'photo_src': 'public/assets/kolase_emblem_dinkes_pinrang_opt.png',
        'photo_tag': 'PUBLIC SAFETY CENTER 119',
        'kicker': 'Pilar 3: Ketahanan Medis',
        'title_lines': ['PSC 119 Pinrang', 'Respon Medis Cepat'],
        'desc_lines': [
            'Pusat tanggap darurat pra-faskes dan rujukan cepat',
            'kegawatdaruratan medis, kecelakaan lalu lintas,',
            'dan kesiapsiagaan ambulans terpadu 24 jam.'
        ],
        'status_text': 'Panggilan Darurat Medis Siaga 24 Jam'
    }
]

if __name__ == '__main__':
    print('Memperbarui visual cover...')
    for c in SERVICE_CARDS:
        create_rich_card(c)
    for p in PILAR_CARDS:
        create_rich_card(p)
    print('Semua visual cover terbarukan dengan kontras sempurna!')
