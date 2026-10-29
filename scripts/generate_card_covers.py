# -*- coding: utf-8 -*-
"""
Script untuk menghasilkan Visual Cover Profesional dengan warna berbeda untuk:
1. Enam (6) Layanan Utama
2. Tiga (3) Pilar Transformasi Layanan Kesehatan
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = 'public/assets/covers'
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_PATH_BOLD = r'C:\Windows\Fonts\segoeuib.ttf'
FONT_PATH_REG = r'C:\Windows\Fonts\segoeui.ttf'
FONT_PATH_SEMIBOLD = r'C:\Windows\Fonts\seguisb.ttf'

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def create_gradient(width, height, color_start, color_end, angle=45):
    """Membuat latar belakang gradien halus dengan sudut tertentu"""
    base = Image.new('RGB', (width, height), color_start)
    top = Image.new('RGB', (width, height), color_end)
    mask = Image.new('L', (width, height))
    mask_data = []
    
    rad = math.radians(angle)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)
    
    for y in range(height):
        for x in range(width):
            # Proyeksi jarak normalisasi 0..1
            p = (x * cos_a + y * sin_a) / (width * cos_a + height * sin_a + 1e-5)
            val = int(max(0, min(255, p * 255)))
            mask_data.append(val)
            
    mask.putdata(mask_data)
    return Image.composite(top, base, mask)

def draw_decorations(img, accent_color, light_color):
    """Menambahkan ornamen geometris dan glow modern"""
    w, h = img.size
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Lingkaran glow di sudut kanan atas
    draw.ellipse((w - 260, -80, w + 120, 260), fill=light_color + (35,))
    draw.ellipse((w - 200, -20, w + 60, 200), fill=light_color + (50,))
    
    # Lingkaran lembut di kiri bawah
    draw.ellipse((-100, h - 180, 140, h + 80), fill=light_color + (25,))
    
    # Garis-garis halus grid futuristik
    for i in range(0, w, 40):
        draw.line([(i, 0), (i, h)], fill=(255, 255, 255, 10), width=1)
    for j in range(0, h, 40):
        draw.line([(0, j), (w, j)], fill=(255, 255, 255, 10), width=1)
        
    # Gabungkan dengan gambar asli
    img = img.convert('RGBA')
    return Image.alpha_composite(img, overlay)

def draw_badge(draw, x, y, text, font, bg_color, text_color):
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    px, py = 14, 7
    draw.rounded_rectangle((x, y, x + tw + px * 2, y + th + py * 2), radius=12, fill=bg_color)
    draw.text((x + px, y + py - bbox[1]), text, font=font, fill=text_color)
    return tw + px * 2

def draw_cross_symbol(draw, cx, cy, size, color):
    """Menggambar palang medis dengan sudut melengkung halus"""
    w = size // 3
    r = 8
    # Vertikal
    draw.rounded_rectangle((cx - w//2, cy - size//2, cx + w//2, cy + size//2), radius=r, fill=color)
    # Horizontal
    draw.rounded_rectangle((cx - size//2, cy - w//2, cx + size//2, cy + w//2), radius=r, fill=color)

def generate_cover(filename, config):
    width, height = 800, 480
    bg = create_gradient(width, height, config['grad_start'], config['grad_end'], angle=config.get('angle', 35))
    img = draw_decorations(bg, config['accent_rgb'], config['light_rgb'])
    draw = ImageDraw.Draw(img)
    
    # 1. Glassmorphism Card di sisi kanan untuk fokus visual
    card_w, card_h = 320, 360
    card_x, card_y = width - card_w - 40, (height - card_h) // 2
    
    # Shadow card
    shadow = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.rounded_rectangle((card_x + 5, card_y + 12, card_x + card_w + 5, card_y + card_h + 12), radius=28, fill=(0, 0, 0, 60))
    shadow = shadow.filter(ImageFilter.GaussianBlur(15))
    img = Image.alpha_composite(img, shadow)
    draw = ImageDraw.Draw(img)
    
    # Card surface dengan border halus
    draw.rounded_rectangle((card_x, card_y, card_x + card_w, card_y + card_h), radius=28, fill=(255, 255, 255, 38), outline=(255, 255, 255, 90), width=2)
    
    # Ikon besar di dalam kartu
    icon_bg_size = 130
    icon_cx = card_x + card_w // 2
    icon_cy = card_y + 110
    draw.ellipse((icon_cx - icon_bg_size//2, icon_cy - icon_bg_size//2, icon_cx + icon_bg_size//2, icon_cy + icon_bg_size//2), fill=config['accent_rgb'] + (230,), outline=(255, 255, 255, 180), width=3)
    
    # Panggil handler simbol spesifik
    sym_type = config.get('symbol', 'cross')
    if sym_type == 'cross':
        draw_cross_symbol(draw, icon_cx, icon_cy, 68, (255, 255, 255, 255))
    elif sym_type == 'doc':
        # Simbol dokumen sertifikat
        dw, dh = 46, 56
        draw.rounded_rectangle((icon_cx - dw//2, icon_cy - dh//2, icon_cx + dw//2, icon_cy + dh//2), radius=6, fill=(255, 255, 255, 255))
        # Garis tulisan
        for line_y in range(icon_cy - 12, icon_cy + 18, 8):
            draw.line([(icon_cx - 14, line_y), (icon_cx + 14, line_y)], fill=config['accent_rgb'] + (220,), width=3)
        # Cap segel bawah
        draw.ellipse((icon_cx + 8, icon_cy + 12, icon_cx + 20, icon_cy + 24), fill=(245, 158, 11, 255))
    elif sym_type == 'heart':
        # Simbol detak jantung / cinta kesehatan
        hw = 36
        draw.ellipse((icon_cx - hw + 8, icon_cy - 20, icon_cx + 2, icon_cy + 10), fill=(255, 255, 255, 255))
        draw.ellipse((icon_cx - 2, icon_cy - 20, icon_cx + hw - 8, icon_cy + 10), fill=(255, 255, 255, 255))
        draw.polygon([(icon_cx - hw + 10, icon_cy - 5), (icon_cx + hw - 10, icon_cy - 5), (icon_cx, icon_cy + 26)], fill=(255, 255, 255, 255))
        # Garis ECG dalam hati
        ecg_points = [(icon_cx - 22, icon_cy), (icon_cx - 10, icon_cy), (icon_cx - 4, icon_cy - 12), (icon_cx + 4, icon_cy + 12), (icon_cx + 10, icon_cy), (icon_cx + 22, icon_cy)]
        draw.line(ecg_points, fill=config['accent_rgb'] + (255,), width=3)
    elif sym_type == 'food':
        # Simbol mangkuk gizi / keamanan pangan
        draw.chord((icon_cx - 32, icon_cy - 12, icon_cx + 32, icon_cy + 30), start=0, end=180, fill=(255, 255, 255, 255))
        # Daun hijau di atas
        draw.ellipse((icon_cx - 18, icon_cy - 26, icon_cx + 6, icon_cy - 6), fill=(255, 255, 255, 255))
        draw.ellipse((icon_cx - 2, icon_cy - 24, icon_cx + 20, icon_cy - 8), fill=(255, 255, 255, 255))
    elif sym_type == 'child':
        # Simbol ibu dan anak / tumbuh kembang
        # Kepala dewasa
        draw.ellipse((icon_cx - 20, icon_cy - 30, icon_cx - 4, icon_cy - 14), fill=(255, 255, 255, 255))
        # Kepala anak
        draw.ellipse((icon_cx + 6, icon_cy - 22, icon_cx + 18, icon_cy - 10), fill=(255, 255, 255, 255))
        # Badan menyatu
        draw.rounded_rectangle((icon_cx - 28, icon_cy - 10, icon_cx + 24, icon_cy + 26), radius=16, fill=(255, 255, 255, 255))
    elif sym_type == 'siren':
        # Simbol ambulans / sirine 119
        # Bodi ambulans
        draw.rounded_rectangle((icon_cx - 32, icon_cy - 10, icon_cx + 32, icon_cy + 20), radius=6, fill=(255, 255, 255, 255))
        # Roda
        draw.ellipse((icon_cx - 24, icon_cy + 14, icon_cx - 12, icon_cy + 26), fill=(30, 41, 59, 255))
        draw.ellipse((icon_cx + 12, icon_cy + 14, icon_cx + 24, icon_cy + 26), fill=(30, 41, 59, 255))
        # Sirine atas
        draw.rounded_rectangle((icon_cx - 6, icon_cy - 22, icon_cx + 6, icon_cy - 10), radius=4, fill=(245, 158, 11, 255))
        draw.line([(icon_cx - 14, icon_cy - 18), (icon_cx - 8, icon_cy - 14)], fill=(255, 255, 255, 255), width=2)
        draw.line([(icon_cx + 8, icon_cy - 14), (icon_cx + 14, icon_cy - 18)], fill=(255, 255, 255, 255), width=2)
    
    # Teks mini di dalam kartu
    f_mini_tag = get_font(FONT_PATH_SEMIBOLD, 14)
    f_mini_sub = get_font(FONT_PATH_BOLD, 17)
    
    draw_badge(draw, card_x + 30, card_y + 200, config['mini_badge'], f_mini_tag, config['accent_rgb'] + (230,), (255, 255, 255, 255))
    
    # 2 baris highlight
    draw.text((card_x + 30, card_y + 246), config['mini_text1'], font=f_mini_sub, fill=(255, 255, 255, 250))
    draw.text((card_x + 30, card_y + 276), config['mini_text2'], font=f_mini_tag, fill=(255, 255, 255, 200))
    
    # Indikator status aman/gratis
    draw.rounded_rectangle((card_x + 30, card_y + 310, card_x + card_w - 30, card_y + 338), radius=8, fill=(255, 255, 255, 30))
    draw.ellipse((card_x + 42, card_y + 320, card_x + 50, card_y + 328), fill=(74, 222, 128, 255))
    f_stat = get_font(FONT_PATH_SEMIBOLD, 12)
    draw.text((card_x + 58, card_y + 317), config.get('status_label', 'Layanan Resmi Terakreditasi'), font=f_stat, fill=(255, 255, 255, 240))
    
    # 2. Sisi Kiri: Judul, Kategori & Deskripsi Layanan
    f_cat = get_font(FONT_PATH_BOLD, 14)
    f_title = get_font(FONT_PATH_BOLD, 30)
    f_desc = get_font(FONT_PATH_REG, 15)
    
    # Kicker Pill
    draw_badge(draw, 50, 60, config['category'].upper(), f_cat, (255, 255, 255, 45), (255, 255, 255, 255))
    
    # Judul Layanan (Bisa 2 baris jika panjang)
    title_lines = config['title']
    ty = 115
    for line in title_lines:
        draw.text((50, ty), line, font=f_title, fill=(255, 255, 255, 255))
        ty += 38
        
    # Deskripsi 3 baris
    ty += 12
    for desc_line in config['desc']:
        draw.text((50, ty), desc_line, font=f_desc, fill=(255, 255, 255, 225))
        ty += 24
        
    # Badge Keunggulan di kiri bawah
    f_feat = get_font(FONT_PATH_SEMIBOLD, 13)
    feat_y = height - 90
    draw.line([(50, feat_y), (card_x - 30, feat_y)], fill=(255, 255, 255, 50), width=1)
    
    draw.ellipse((52, feat_y + 22, 60, feat_y + 30), fill=(253, 224, 71, 255))
    draw.text((68, feat_y + 18), config['feature'], font=f_feat, fill=(255, 255, 255, 240))
    
    out_path = os.path.join(OUTPUT_DIR, filename)
    img = img.convert('RGB')
    img.save(out_path, quality=95, optimize=True)
    print(f'Generated: {out_path}')

# DAFTAR 6 LAYANAN UTAMA DENGAN WARNA BERBEDA:
SERVICES = [
    {
        'file': 'cover_service_puskesmas.jpg',
        'grad_start': (6, 78, 59),      # Emerald Gelap (#064e3b)
        'grad_end': (5, 150, 105),       # Emerald Cerah (#059669)
        'accent_rgb': (16, 185, 129),
        'light_rgb': (167, 243, 208),
        'symbol': 'cross',
        'category': 'Fasilitas Pelayanan Primer',
        'title': ['Pelayanan Rawat', 'Jalan & Inap Puskesmas'],
        'desc': [
            'Pemeriksaan medis umum, gigi, KIA, KB,',
            'laboratorium penunjang, persalinan, serta',
            'fasilitas Unit Gawat Darurat (UGD) siaga 24 jam.'
        ],
        'mini_badge': 'UPTD PUSKESMAS',
        'mini_text1': 'Terakreditasi Kemenkes',
        'mini_text2': 'Kecamatan se-Kabupaten Pinrang',
        'status_label': 'Gratis Bagi Peserta BPJS / KIS',
        'feature': 'Pelayanan Terintegrasi di Seluruh Wilayah Pinrang'
    },
    {
        'file': 'cover_service_sip_nakes.jpg',
        'grad_start': (23, 37, 84),      # Navy Blue Gelap (#172554)
        'grad_end': (29, 78, 216),       # Sapphire Blue (#1d4ed8)
        'accent_rgb': (59, 130, 246),
        'light_rgb': (191, 219, 254),
        'symbol': 'doc',
        'category': 'Sumber Daya Kesehatan (SDK)',
        'title': ['Rekomendasi SIP', '& SIK Tenaga Medis'],
        'desc': [
            'Layanan rekomendasi izin praktik dokter,',
            'bidan, perawat, apoteker, dan nakes lainnya',
            'secara transparan, akuntabel, dan bebas pungli.'
        ],
        'mini_badge': 'PERIZINAN NAKES',
        'mini_text1': 'Verifikasi Berkas Digital',
        'mini_text2': 'Standar SOP Dinas Kesehatan',
        'status_label': 'Tanpa Biaya Ilegal (0 Rupiah)',
        'feature': 'Penerbitan Cepat Melalui Sistem Terpadu'
    },
    {
        'file': 'cover_service_pangan_sppirt.jpg',
        'grad_start': (120, 53, 15),     # Amber Gelap (#78350f)
        'grad_end': (217, 119, 6),       # Golden Amber (#d97706)
        'accent_rgb': (245, 158, 11),
        'light_rgb': (254, 243, 199),
        'symbol': 'food',
        'category': 'Kefarmasian & Keamanan Pangan',
        'title': ['Sertifikasi Pangan', 'Industri Rumah Tangga (SPP-IRT)'],
        'desc': [
            'Penyuluhan keamanan pangan (PKP) dan',
            'pemeriksaan sarana produksi pangan olahan',
            'bagi pelaku UMKM pangan Kabupaten Pinrang.'
        ],
        'mini_badge': 'HIGIENIS & AMAN',
        'mini_text1': 'Sertifikat Standar Mutu',
        'mini_text2': 'Pendampingan Sanitasi UMKM',
        'status_label': 'Fasilitasi Pembinaan Pemkab',
        'feature': 'Mendukung Produk Pangan Sehat & Berdaya Saing'
    },
    {
        'file': 'cover_service_ckg.jpg',
        'grad_start': (14, 116, 144),    # Ocean Cyan Gelap (#0e7490)
        'grad_end': (8, 145, 178),       # Teal Toska (#0891b2)
        'accent_rgb': (14, 165, 233),
        'light_rgb': (186, 230, 253),
        'symbol': 'heart',
        'category': 'Deteksi Dini & Pencegahan Penyakit',
        'title': ['Cek Kesehatan Gratis', '(Program CKG Pinrang)'],
        'desc': [
            'Skrining tekanan darah, gula darah sewaktu,',
            'kolesterol, asam urat, dan faktor risiko',
            'penyakit tidak menular secara berkala.'
        ],
        'mini_badge': 'PROGRAM UNGGULAN',
        'mini_text1': 'Skrining Dini PTM',
        'mini_text2': 'Deteksi Kesehatan Keluarga',
        'status_label': '100% Gratis di Seluruh Puskesmas',
        'feature': 'Pencegahan Risiko Kardiovaskular Sejak Dini'
    },
    {
        'file': 'cover_service_stunting_gizi.jpg',
        'grad_start': (136, 19, 55),     # Deep Rose Gelap (#881337)
        'grad_end': (225, 29, 72),       # Coral Rose (#e11d48)
        'accent_rgb': (244, 63, 94),
        'light_rgb': (254, 205, 211),
        'symbol': 'child',
        'category': 'Kesehatan Masyarakat & Gizi',
        'title': ['Pencegahan Stunting', '& Imunisasi Terpadu'],
        'desc': [
            'Pemantauan status gizi balita, pemberian',
            'makanan tambahan (PMT), tablet tambah darah,',
            'dan imunisasi rutin lengkap di Posyandu.'
        ],
        'mini_badge': 'GENERASI SEHAT',
        'mini_text1': 'Posyandu Aktif 12 Kecamatan',
        'mini_text2': 'Kader Terlatih & Responsif',
        'status_label': 'Prioritas Transformasi Nasional',
        'feature': 'Menuju Nol Stunting Baru di Bumi Lasinrang'
    },
    {
        'file': 'cover_service_psc119.jpg',
        'grad_start': (127, 29, 29),     # Dark Crimson Red (#7f1d1d)
        'grad_end': (220, 38, 38),       # Crimson Red (#dc2626)
        'accent_rgb': (239, 68, 68),
        'light_rgb': (254, 202, 202),
        'symbol': 'siren',
        'category': 'Kedaruratan Medis Terpadu',
        'title': ['Layanan Darurat Medis', 'Public Safety Center (PSC 119)'],
        'desc': [
            'Respon cepat kegawatdaruratan medis pra-RS,',
            'evakuasi korban kecelakaan, armada ambulans',
            'siaga, dan rujukan terpadu 24 jam nonstop.'
        ],
        'mini_badge': 'CALL CENTER 119',
        'mini_text1': 'Siaga 24 Jam Nonstop',
        'mini_text2': 'Ambulans Reaksi Cepat',
        'status_label': 'Bebas Pulsa & Cepat Tanggap',
        'feature': 'Kesiapsiagaan Pertolongan Pertama Medis'
    }
]

# DAFTAR 3 PILAR TRANSFORMASI DENGAN WARNA BERBEDA:
PILARS = [
    {
        'file': 'cover_pilar_puskesmas.jpg',
        'grad_start': (15, 118, 110),    # Teal (#0f766e)
        'grad_end': (20, 184, 166),      # Teal Cerah (#14b8a6)
        'accent_rgb': (45, 212, 191),
        'light_rgb': (204, 251, 241),
        'symbol': 'cross',
        'category': 'Pilar 1: Layanan Primer',
        'title': ['Puskesmas Pelayanan', 'Kesehatan Masyarakat'],
        'desc': [
            'Jaringan faskes primer yang menyelenggarakan',
            'pelayanan rawat jalan, rawat inap, poli KIA,',
            'laboratorium, dan IGD 24 Jam di 12 kecamatan.'
        ],
        'mini_badge': 'JARINGAN FASKES',
        'mini_text1': 'UPTD Puskesmas',
        'mini_text2': 'Puskesmas Pembantu & Poskesdes',
        'status_label': 'Pelayanan Ramah & Bermartabat',
        'feature': 'Menjangkau Seluruh Pelosok Desa di Pinrang'
    },
    {
        'file': 'cover_pilar_germas.jpg',
        'grad_start': (21, 128, 61),     # Green (#15803d)
        'grad_end': (34, 197, 94),       # Bright Green (#22c55e)
        'accent_rgb': (74, 222, 128),
        'light_rgb': (220, 252, 231),
        'symbol': 'heart',
        'category': 'Pilar 2: Promotif & Preventif',
        'title': ['GERMAS Pinrang', 'Gerakan Hidup Sehat'],
        'desc': [
            'Pemberdayaan masyarakat melalui aktivitas fisik',
            'teratur, konsumsi buah dan sayur, skrining rutin,',
            'serta komitmen 100% Bebas Buang Air Besar (ODF).'
        ],
        'mini_badge': 'GERAKAN MASYARAKAT',
        'mini_text1': 'Perilaku Hidup Bersih & Sehat',
        'mini_text2': 'Inovasi STBM & Desa ODF',
        'status_label': 'Kabupaten Sehat Mandiri',
        'feature': 'Membangun Budaya Sehat Sejak dari Keluarga'
    },
    {
        'file': 'cover_pilar_psc119.jpg',
        'grad_start': (194, 65, 12),     # Orange (#c2410c)
        'grad_end': (249, 115, 22),      # Amber Orange (#f97316)
        'accent_rgb': (251, 146, 60),
        'light_rgb': (254, 237, 213),
        'symbol': 'siren',
        'category': 'Pilar 3: Ketahanan Kesehatan',
        'title': ['PSC 119 Pinrang', 'Respon Medis Cepat'],
        'desc': [
            'Pusat kendali kedaruratan terpadu untuk respon',
            'cepat penanganan medis darurat, evakuasi,',
            'dan rujukan berkesinambungan antar fasilitas.'
        ],
        'mini_badge': 'SISTEM RUJUKAN',
        'mini_text1': 'Kedaruratan 24 Jam',
        'mini_text2': 'Integrasi RSUD & Puskesmas',
        'status_label': 'Siaga Bencana & Kedaruratan',
        'feature': 'Pertolongan Medis Segera Menyelamatkan Nyawa'
    }
]

if __name__ == '__main__':
    print('Memulai proses generate visual cover...')
    for item in SERVICES:
        generate_cover(item['file'], item)
    for item in PILARS:
        generate_cover(item['file'], item)
    print('Seluruh 9 visual cover berhasil dibuat dengan resolusi tinggi!')
