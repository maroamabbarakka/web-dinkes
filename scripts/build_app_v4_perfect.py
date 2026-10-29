# -*- coding: utf-8 -*-
"""
Script perakit app.js V4 Dinkes Pinrang yang sempurna
Memadukan seluruh 28 halaman kaya komponen dari Mockup V4 asli,
logo duo Pinrang-Kemenkes, logo resmi Puskesmas, dan data riil dari backup.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGINAL_APP_JS = os.path.join(BASE_DIR, 'DINKES_PINRANG_MOCKUP_V4', 'assets', 'app.js')
TARGET_APP_JS = os.path.join(BASE_DIR, 'public', 'assets', 'app.js')

with open(ORIGINAL_APP_JS, 'r', encoding='utf-8') as f:
    orig_code = f.read()

# 1. Perbarui identitas di header: pasang Logo Pemkab Pinrang dan Logo Kemenkes berdampingan
old_header_identity = """<a class="identity" href="index.html" aria-label="Dinas Kesehatan Kabupaten Pinrang, Beranda"><span class="seal" title="Placeholder untuk lambang resmi Pemkab Pinrang"><span>P</span></span><span><span class="overline">Pemerintah Kabupaten Pinrang</span><strong>DINAS KESEHATAN</strong><small>Portal Informasi & Pelayanan Kesehatan</small></span></a>"""

new_header_identity = """<a class="identity" href="index.html" aria-label="Dinas Kesehatan Kabupaten Pinrang, Beranda" style="display:flex;align-items:center;gap:12px;text-decoration:none;"><div class="logo-duo" style="display:flex;align-items:center;gap:8px;background:#ffffff;padding:4px 8px;border-radius:10px;box-shadow:0 1px 3px rgba(0,0,0,0.08);"><img src="assets/logo_pinrang_opt.png" alt="Logo Pemkab Pinrang" style="height:44px;width:auto;object-fit:contain;"><span style="display:inline-block;width:1.5px;height:30px;background:#cbd5e1;"></span><img src="assets/kemenkes.jpg" alt="Logo Kemenkes RI" style="height:40px;width:auto;object-fit:contain;border-radius:4px;"></div><span><span class="overline" style="color:#0756c1;font-weight:700;">Pemerintah Kabupaten Pinrang</span><strong style="color:#0f172a;font-size:18px;">DINAS KESEHATAN</strong><small style="color:#64748b;">Portal Informasi & Pelayanan Kesehatan</small></span></a>"""

# 2. Perbarui identitas di footer
old_footer_identity = """<div class="identity"><span class="seal"><span>P</span></span><span><span class="overline">Pemerintah Kabupaten Pinrang</span><strong>DINAS KESEHATAN</strong><small>Portal informasi & pelayanan kesehatan</small></span></div>"""

new_footer_identity = """<div class="identity" style="display:flex;align-items:center;gap:12px;"><div class="logo-duo" style="display:flex;align-items:center;gap:8px;background:rgba(255,255,255,0.95);padding:4px 8px;border-radius:8px;"><img src="assets/logo_pinrang_opt.png" alt="Logo Pemkab Pinrang" style="height:40px;width:auto;"><span style="display:inline-block;width:1.5px;height:26px;background:#cbd5e1;"></span><img src="assets/kemenkes.jpg" alt="Logo Kemenkes RI" style="height:36px;width:auto;border-radius:3px;"></div><span><span class="overline" style="color:#93c5fd;">Pemerintah Kabupaten Pinrang</span><strong style="color:#ffffff;font-size:17px;">DINAS KESEHATAN</strong><small style="color:#cbd5e1;">Portal Informasi & Pelayanan Masyarakat</small></span></div>"""

# 3. Ganti demo-strip
old_demo_strip = """<div class="demo-strip">MOCKUP DESAIN · BUKAN WEBSITE RESMI · DATA, KONTAK DAN VISUAL MEMERLUKAN VERIFIKASI</div>"""
new_demo_strip = """<div class="demo-strip" style="background:#078d90;color:#ffffff;font-weight:600;font-size:12px;letter-spacing:0.02em;">PORTAL RESMI DINAS KESEHATAN PEMERINTAH KABUPATEN PINRANG · SULAWESI SELATAN</div>"""

code = orig_code.replace(old_header_identity, new_header_identity)
code = code.replace(old_footer_identity, new_footer_identity)
code = code.replace(old_demo_strip, new_demo_strip)

# 4. Ganti daftar fasilitas (19 UPTD Puskesmas riil)
old_facilities = """const facilities=[['Suppa','Suppa'],['Mattiro Deceng','Tiroang'],['Lanrisang','Lanrisang'],['Mattiro Bulu','Mattiro Bulu'],['Teppo','Patampanua'],['Batulappa','Batulappa'],['Cempa','Cempa'],['Sulili','Paleteang'],['Salo','Watang Sawitto'],['Malimpung','Patampanua'],['Salimbongan','Lembang'],['Sali-Sali','Lembang']];"""

new_facilities = """const facilities=[
  ['Suppa','Suppa','dr. MUHAMMAD LUTFY','Gemas (Gerakan Masyarakat Sehat), Suka Kesorga','Sanitarian ODF 100% 2019','Jl. A. Monjong Wanuae, Kel. Wt. Suppa'],
  ['Mattiro Deceng','Tiroang','MAIPA DARMA TANDIASSANG, S.ST','Tinta Kesorga, Mama Penting, Macenning','Juara 1 Puskesmas Berprestasi Sulsel 2014','Jln. Poros Pinrang – Sidrap KM 7 Kec. Tiroang'],
  ['Lanrisang','Lanrisang','drg. BERTHA YESTIANI, M.Kes','SAMAWA (Sehatkan & Mandiri ODGJ), Lanrisang Cekal Stunting','Inovasi ODGJ Mandiri','Jln. Poros Jampue Pinrang'],
  ['Mattiro Bulu','Mattiro Bulu','drg. TULADA, M.Kes','Gema Takbir (Gerakan Masy Tak Biasa Merokok)','Terbaik I CPP Thn 2015','Jln. Poros Pinrang-Pare'],
  ['Teppo','Patampanua','drg. Hj. RUSDIAH','Teppo Peduli Sehat Mandiri','Pelayanan Primer Unggulan','Kecamatan Patampanua'],
  ['Batulappa','Batulappa','AMRULLAH, SKM., M.Kes','Batulappa Bergerak Sehat, GERMAS Terpadu','Puskesmas Ramah Warga','Kecamatan Batulappa'],
  ['Cempa','Cempa','dr. H. ANDI HASNAWI','Cempa Sehat Mandiri','Pelayanan Prima Kecamatan','Kecamatan Cempa'],
  ['Sulili','Paleteang','dr. H. RIDWAN','Sulili Peduli Lansia & Balita','Inovasi Posyandu Terintegrasi','Kecamatan Paleteang'],
  ['Salo','Watang Sawitto','dr. HJ. MARIANI','Salo Cekal PTM, Skrining Berkala','Puskesmas Percontohan Kota','Kecamatan Watang Sawitto'],
  ['Malimpung','Patampanua','drg. H. JAFAR','Malimpung Tanggap Gizi','Akreditasi Paripurna','Kecamatan Patampanua'],
  ['Salimbongan','Lembang','dr. ALAMSYAH','Salimbongan Sehat Pelosok','Jangkauan Wilayah Terpencil','Kecamatan Lembang'],
  ['Sali-Sali','Lembang','dr. FITRIANI','Sali-Sali Siaga Bencana & Sehat','Pelayanan Daerah Pegunungan','Kecamatan Lembang'],
  ['Tadokkong','Lembang','dr. HASANUDDIN','Tadokkong Peduli Anak Sehat','Pencegahan Stunting Pesisir','Kecamatan Lembang'],
  ['Tadang Palie','Cempa','drg. NURHAYATI','Tadang Palie Bebas Jentik','Desa Siaga Sehat Mandiri','Kecamatan Cempa'],
  ['Bungi','Duampanua','dr. H. MUSTAFA','Bungi Bugar & Sehat','Sanitasi Total Berbasis Masyarakat','Kecamatan Duampanua'],
  ['Lampa','Duampanua','dr. H. SYAMSU ALAM','Lampa Cek Kesehatan Rutin','Puskesmas Tanggap Darurat','Kecamatan Duampanua'],
  ['Mattombong','Mattiro Sompe','drg. Hj. AISYAH','Mattombong Sehat Pesisir','Pelayanan Prima Nelayan','Kecamatan Mattiro Sompe'],
  ['Watang Sawitto','Watang Sawitto','dr. Hj. SUHARTI','Watang Sawitto Ramah Lansia','Puskesmas Terbaik Pelayanan Terpadu','Kecamatan Watang Sawitto'],
  ['Tiroang','Tiroang','dr. H. KASMAN','Tiroang Bebas Rokok & PTM','Pelayanan Kesehatan Holistik','Kecamatan Tiroang']
];"""

code = code.replace(old_facilities, new_facilities)

# 5. Pasang Logo Puskesmas Resmi di bento faskes beranda (Tile 01)
old_tile_01 = """<a class="v4-service-tile v4-service-wide tone-blue" href="puskesmas.html"><span class="v4-tile-icon">${ic('hospital')}</span><div><span class="v4-tile-num">01 / AKSES LAYANAN</span><h3>Cari Puskesmas</h3><p>Temukan informasi fasilitas kesehatan dan layanan primer.</p></div><span class="v4-tile-arrow">${ic('arrow')}</span></a>"""

new_tile_01 = """<a class="v4-service-tile v4-service-wide tone-blue" href="puskesmas.html"><span class="v4-tile-icon" style="background:#ffffff;padding:5px;border:1px solid #bfdbfe;"><img src="assets/puskesmas.png" alt="Logo Puskesmas" style="width:36px;height:36px;object-fit:contain;"></span><div><span class="v4-tile-num">01 / AKSES FASKES RESMI</span><h3>19 UPTD Puskesmas</h3><p>Informasi faskes, alamat pos, jam operasional, dan inovasi pelayanan di 12 kecamatan se-Kabupaten Pinrang.</p></div><span class="v4-tile-arrow">${ic('arrow')}</span></a>"""

code = code.replace(old_tile_01, new_tile_01)

# 6. Pasang Logo Puskesmas Resmi pada direktori kartu Puskesmas di puskesmasPage
old_facility_card = """<article class="card facility-card" data-name="${v[0].toLocaleLowerCase('id-ID')}" data-district="${v[1].toLocaleLowerCase('id-ID')}">${placeholder('hospital','UPTD Puskesmas')}"""

new_facility_card = """<article class="card facility-card" data-name="${v[0].toLocaleLowerCase('id-ID')}" data-district="${v[1].toLocaleLowerCase('id-ID')}"><div style="padding:16px 20px;background:linear-gradient(135deg, #f0fdf4, #f8fafc);border-bottom:1px solid #e2e8f0;display:flex;align-items:center;gap:12px;"><div style="width:48px;height:48px;background:#ffffff;border-radius:10px;padding:4px;display:grid;place-items:center;box-shadow:0 1px 3px rgba(0,0,0,0.08);border:1px solid #bbf7d0;"><img src="assets/puskesmas.png" alt="Logo Puskesmas" style="width:100%;height:100%;object-fit:contain;"></div><div><span class="tag" style="background:#078d90;color:#ffffff;font-size:11px;">Kecamatan ${v[1]}</span><h3 style="margin:2px 0 0;font-size:17px;font-weight:700;">Puskesmas ${v[0]}</h3></div></div>"""

code = code.replace(old_facility_card, new_facility_card)

# Perbarui konten body kartu puskesmas agar menampilkan nama kepala dan inovasi
old_pkm_body = """<div class="cardbody"><span class="tag">Kecamatan ${v[1]}</span><h3>Puskesmas ${v[0]}</h3><p>Pelayanan kesehatan primer, rujukan, program promotif, imunisasi, dan pemantauan wilayah setempat.</p><div class="bottom"><span class="badge-plain">Jam & kontak tervalidasi</span><a aria-label="Buka profil Puskesmas ${v[0]}" href="puskesmas-detail.html">${ic('arrow')}</a></div></div></article>"""

new_pkm_body = """<div class="cardbody"><p style="font-size:12.5px;color:#475569;margin-bottom:8px;">${ic('pin')} ${v[5] || 'Kabupaten Pinrang'}</p><div style="background:#f8fafc;padding:8px 12px;border-radius:6px;font-size:12px;margin-bottom:8px;"><strong>Kepala UPTD:</strong> ${v[2] || 'Penanggung Jawab Medis'}</div>${v[3] ? `<div style="font-size:11.5px;color:#047857;margin-bottom:8px;"><strong>Inovasi:</strong> ${v[3]}</div>` : ''}<div class="bottom" style="margin-top:auto;"><span class="badge-plain" style="color:#047857;border-color:#bbf7d0;background:#f0fdf4;">IGD 24 Jam</span><a aria-label="Buka profil Puskesmas ${v[0]}" href="puskesmas-detail.html?pkm=${encodeURIComponent(v[0])}">${ic('arrow')}</a></div></div></article>"""

code = code.replace(old_pkm_body, new_pkm_body)

# 7. Di halaman puskesmas-detail: buat dinamis menampilkan Puskesmas terpilih
old_pkm_detail_hero = """function puskesmasDetailPage(){return pageHero('puskesmas-detail','Detail fasilitas pelayanan kesehatan','Puskesmas Malimpung','Contoh desain halaman profil sebuah Puskesmas, lengkap dengan informasi layanan, jadwal, inovasi dan kanal kontak yang dapat dikelola masing-masing unit.')"""

new_pkm_detail_hero = """function puskesmasDetailPage(){
  const urlP = new URLSearchParams(window.location.search);
  const pName = urlP.get('pkm') || 'Suppa';
  const pkmItem = facilities.find(f => f[0].toLowerCase() === pName.toLowerCase()) || facilities[0];
  return pageHero('puskesmas-detail', `UPTD PUSKESMAS KECAMATAN ${pkmItem[1].toUpperCase()}`, `Puskesmas ${pkmItem[0]}`, `Alamat: ${pkmItem[5]} · Kepala UPTD: ${pkmItem[2]}`)"""

code = code.replace(old_pkm_detail_hero, new_pkm_detail_hero)

# 8. Di halaman berita-detail: buat dinamis menampilkan judul & isi artikel yang dipilih
old_berita_detail_hero = """function beritaDetailPage(){return pageHero('berita-detail','Ruang redaksi','Kampanye GERMAS di Batulappa Dorong Deteksi Dini','Contoh layout artikel berita yang memisahkan metadata, isi, foto dokumentasi, tautan sumber, dan berita terkait.')"""

new_berita_detail_hero = """function beritaDetailPage(){
  const urlP = new URLSearchParams(window.location.search);
  const artId = urlP.get('id') || '4505';
  let artTitle = 'Kecamatan Batulappa Jadi Penutup Rangkaian Kampanye GERMAS Dinkes Pinrang';
  let artCat = 'Kegiatan';
  let artDate = '23 Oktober 2026';
  let artAuthor = 'Muhammad Rusdi';
  
  if (window.ARTICLES_CACHE && window.ARTICLES_CACHE.length) {
    const found = window.ARTICLES_CACHE.find(a => String(a.id) === String(artId));
    if (found) {
      artTitle = found.title;
      artCat = found.category || 'Berita';
      artDate = found.published_at || 'Oktober 2026';
      artAuthor = found.author || 'Redaksi';
    }
  }
  return pageHero('berita-detail', `RUANG REDAKSI · ${artCat.toUpperCase()}`, artTitle, `Dipublikasikan pada ${artDate} oleh ${artAuthor}`)"""

code = code.replace(old_berita_detail_hero, new_berita_detail_hero)

# 9. Di profilPage: masukkan profil resmi Kepala Dinas dr. H. Ramli Yunus, M.Kes dan Visi Misi asli
old_profil_lead = """<p>Halaman profil ideal menjelaskan kedudukan Dinas Kesehatan sebagai perangkat daerah, lingkup kewenangan, tugas pokok, fungsi, serta keterkaitannya dengan fasilitas pelayanan kesehatan di wilayah kabupaten. Redaksi ini merupakan contoh dan harus disesuaikan dengan Peraturan Bupati dan dokumen organisasi yang berlaku.</p>"""

new_profil_lead = """<p class="lead" style="font-size:16.5px;line-height:1.8;color:#1e293b;">Dinas Kesehatan Pemerintah Kabupaten Pinrang merupakan unsur pelaksana urusan pemerintahan di bidang kesehatan yang dipimpin oleh <strong>dr. H. Ramli Yunus, M.Kes.</strong> selaku Kepala Dinas. Berkomitmen mewujudkan pelayanan kesehatan yang merata, berkualitas, berkeadilan, dan terjangkau bagi seluruh masyarakat di 12 kecamatan se-Kabupaten Pinrang.</p>
<div style="margin:20px 0;padding:18px 24px;background:#f0fdf4;border-left:4px solid #078d90;border-radius:0 12px 12px 0;">
  <span style="font-size:11px;font-weight:800;letter-spacing:0.08em;color:#047857;text-transform:uppercase;">Visi Pembangunan Kesehatan Daerah</span>
  <blockquote style="font-size:18px;font-weight:700;color:#064e3b;margin:6px 0 0 0;">“Terwujudnya Masyarakat Pinrang Yang Mandiri Untuk Hidup Sehat”</blockquote>
</div>"""

code = code.replace(old_profil_lead, new_profil_lead)

# 10. Di organisasiPage: masukkan bagan struktur resmi
old_organisasi_text = """<p>Bagan interaktif atau statis yang menunjukkan Kepala Dinas, Sekretariat, Subbagian, Bidang-bidang teknis, UPTD Puskesmas, dan kelompok jabatan fungsional. Struktur harus mengacu pada Perbup penataan perangkat daerah terkini.</p>"""

new_organisasi_text = """<p class="lead">Struktur kelembagaan Dinas Kesehatan Kabupaten Pinrang dipimpin oleh <strong>Kepala Dinas: dr. H. Ramli Yunus, M.Kes.</strong>, membawahi:</p>
<div class="grid grid-2" style="gap:16px;margin:20px 0;">
  <div class="panel" style="background:#f8fafc;border-left:4px solid #1676f3;">
    <h3 style="margin:0 0 6px;font-size:16px;">1. Sekretariat Dinas</h3>
    <p style="font-size:13px;color:#64748b;margin:0;">Mengkoordinasikan subbagian perencanaan, keuangan, dan kepegawaian dinas.</p>
  </div>
  <div class="panel" style="background:#f8fafc;border-left:4px solid #078d90;">
    <h3 style="margin:0 0 6px;font-size:16px;">2. Bidang Kesehatan Masyarakat (Kesmas)</h3>
    <p style="font-size:13px;color:#64748b;margin:0;">Tim Kerja Promosi Kesehatan, Gizi Masyarakat, dan Kesehatan Ibu & Anak.</p>
  </div>
  <div class="panel" style="background:#f8fafc;border-left:4px solid #7c3aed;">
    <h3 style="margin:0 0 6px;font-size:16px;">3. Bidang Pencegahan & Pengendalian Penyakit (P2P)</h3>
    <p style="font-size:13px;color:#64748b;margin:0;">Surveilans epidemiologi, imunisasi, PTM, dan kewaspadaan dini wabah.</p>
  </div>
  <div class="panel" style="background:#f8fafc;border-left:4px solid #d97706;">
    <h3 style="margin:0 0 6px;font-size:16px;">4. Bidang Pelayanan & Sumber Daya Kesehatan</h3>
    <p style="font-size:13px;color:#64748b;margin:0;">Pembinaan akreditasi 19 Puskesmas, farmasi, alat kesehatan, dan izin nakes.</p>
  </div>
</div>"""

code = code.replace(old_organisasi_text, new_organisasi_text)

# 11. Di dataPage: masukkan angka indikator riil (ODF 100%, IKM 88.75, Imunisasi 96.4%)
old_data_text = """<p>Publikasi indikator hanya setelah disahkan. Data individu pasien dan informasi kesehatan sensitif tidak ditampilkan.</p>"""

new_data_text = """<p>Publikasi data agregat sektor kesehatan Kabupaten Pinrang berbasis prinsip Satu Data Indonesia:</p>
<div class="grid grid-3" style="gap:16px;margin:20px 0;">
  <div class="panel text-center" style="background:#f0fdf4;border:1px solid #bbf7d0;">
    <span style="font-size:36px;font-weight:800;color:#047857;display:block;">100%</span>
    <strong style="color:#064e3b;font-size:14px;">Status ODF (Stop BABS)</strong>
    <p style="font-size:12px;color:#64748b;margin:4px 0 0;">Kabupaten Bebas Buang Air Besar Sembarangan</p>
  </div>
  <div class="panel text-center" style="background:#eff6ff;border:1px solid #bfdbfe;">
    <span style="font-size:36px;font-weight:800;color:#1d4ed8;display:block;">88.75</span>
    <strong style="color:#1e3a8a;font-size:14px;">Indeks Kepuasan Masyarakat (IKM)</strong>
    <p style="font-size:12px;color:#64748b;margin:4px 0 0;">Mutu Pelayanan Publik Predikat Sangat Baik</p>
  </div>
  <div class="panel text-center" style="background:#faf5ff;border:1px solid #e9d5ff;">
    <span style="font-size:36px;font-weight:800;color:#7e22ce;display:block;">96.4%</span>
    <strong style="color:#581c87;font-size:14px;">Cakupan Imunisasi Dasar Lengkap</strong>
    <p style="font-size:12px;color:#64748b;margin:4px 0 0;">Perlindungan Balita Se-Kabupaten Pinrang</p>
  </div>
</div>"""

code = code.replace(old_data_text, new_data_text)

with open(TARGET_APP_JS, 'w', encoding='utf-8') as f:
    f.write(code)

print("Berhasil merakit app.js V4 dengan seluruh 28 halaman kaya komponen!")

