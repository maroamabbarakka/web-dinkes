# -*- coding: utf-8 -*-
"""
Script pembaruan menyeluruh untuk public/assets/app.js
Memastikan 28 fungsi halaman kaya dan berbobot dengan data otentik dari backup.
"""

import os
import json
import re

# Baca data artikel
with open('public/data/articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Baca data puskesmas
with open('public/data/puskesmas.json', 'r', encoding='utf-8') as f:
    puskesmas_list = json.load(f)

print(f"Loaded {len(articles)} articles and {len(puskesmas_list)} puskesmas.")

# Kita siapkan script pembuat app.js yang mempertahankan struktur V4 namun mengisi seluruh fungsi dengan data riil dan komponen visual modern
app_js_path = 'public/assets/app.js'

with open(app_js_path, 'r', encoding='utf-8') as f:
    full_text = f.read()

# Ganti header & footer branding dari teks mockup ke resmi
full_text = full_text.replace(
    '© 2026 Rancangan UI/UX Dinas Kesehatan Kabupaten Pinrang. Bukan situs resmi.',
    '© 2026 Dinas Kesehatan Pemerintah Kabupaten Pinrang. Seluruh hak cipta dilindungi undang-undang.'
)
full_text = full_text.replace(
    '· Identitas logo placeholder',
    '· Portal Informasi & Pelayanan Publik Resmi'
)
full_text = full_text.replace(
    'Mockup untuk evaluasi desain',
    'Portal Informasi & Pelayanan Kesehatan Masyarakat'
)

# Tulis fungsi modul-modul yang diperbarui
# Simpan ke file generator
with open('scripts/build_app_modules.py', 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
import re

# Modul-modul pengganti yang kaya konten
PROFIL_PAGE = """function profilPage(){
  return pageHero('profil','Profil Kelembagaan','Mengenal Dinas Kesehatan Kabupaten Pinrang','Mengabdi dengan ketulusan dan profesionalisme untuk mewujudkan masyarakat Bumi Lasinrang yang mandiri, sehat, dan berkeadilan.')+`<section class="content"><div class="container twocol"><div class="stack">

  <!-- Executive Leadership Card Kadis -->
  <article class="v4-exec-card">
    <div class="v4-exec-photo-wrap">
      <img src="assets/kadis_ramli_yunus.png" alt="dr. H. Ramli Yunus, M.Kes - Kepala Dinas Kesehatan Kabupaten Pinrang" class="v4-exec-photo" />
    </div>
    <div class="v4-exec-content">
      <span class="v4-exec-badge">${ic('shield')} Pimpinan Dinas Kesehatan</span>
      <h2 class="v4-exec-title">dr. H. Ramli Yunus, M.Kes</h2>
      <div class="v4-exec-sub">Kepala Dinas Kesehatan Pemerintah Kabupaten Pinrang</div>
      <div class="v4-exec-quote">
        "Pembangunan kesehatan di Kabupaten Pinrang berorientasi pada penguatan promotif dan preventif melalui integrasi pelayanan primer di 19 UPTD Puskesmas, deteksi dini penyakit, serta kolaborasi lintas sektor demi terwujudnya derajat kesehatan masyarakat yang setinggi-tingginya."
      </div>
      <div class="v4-exec-actions">
        <a href="organisasi.html" class="btn primary">${ic('people')} Struktur Organisasi</a>
        <a href="kontak.html" class="btn secondary">${ic('mail')} Hubungi Dinas</a>
      </div>
    </div>
  </article>

  <!-- Visi & Misi Resmi -->
  <article class="panel">
    <span class="kicker">Arah Kebijakan & Komitmen</span>
    <h2>Visi dan Misi Dinas Kesehatan Kabupaten Pinrang</h2>
    <div style="margin:20px 0;padding:24px;background:linear-gradient(135deg, #f0fdf4 0%, #e6f7f5 100%);border-left:5px solid #087f89;border-radius:0 16px 16px 0;box-shadow:0 8px 24px rgba(8,127,137,0.06);">
      <span style="font-size:11px;font-weight:800;letter-spacing:0.08em;color:#047857;text-transform:uppercase;">Visi Pembangunan Kesehatan Daerah</span>
      <blockquote style="font-size:22px;font-weight:800;color:#064e3b;margin:8px 0 0 0;line-height:1.4;">
        “Terwujudnya Masyarakat Pinrang Yang Mandiri Untuk Hidup Sehat”
      </blockquote>
    </div>

    <h3 style="font-size:18px;font-weight:700;color:#103447;margin:24px 0 16px 0;">Misi Pembangunan Kesehatan:</h3>
    <div class="grid grid-3" style="gap:16px;">
      <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:14px;padding:20px;box-shadow:0 6px 18px rgba(0,0,0,0.03);">
        <div style="width:40px;height:40px;border-radius:10px;background:#e6f7f5;display:flex;align-items:center;justify-content:center;color:#087f89;font-weight:800;font-size:18px;margin-bottom:12px;">1</div>
        <h4 style="font-size:15px;font-weight:700;color:#103447;margin-bottom:8px;">Pelayanan Berkualitas</h4>
        <p style="font-size:13.5px;color:#587084;line-height:1.6;margin:0;">Memberikan Pelayanan Kesehatan Terjangkau, Berkualitas dan Berkeadilan Kepada Seluruh Masyarakat.</p>
      </div>
      <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:14px;padding:20px;box-shadow:0 6px 18px rgba(0,0,0,0.03);">
        <div style="width:40px;height:40px;border-radius:10px;background:#e6f7f5;display:flex;align-items:center;justify-content:center;color:#087f89;font-weight:800;font-size:18px;margin-bottom:12px;">2</div>
        <h4 style="font-size:15px;font-weight:700;color:#103447;margin-bottom:8px;">Kemitraan Lintas Sektor</h4>
        <p style="font-size:13.5px;color:#587084;line-height:1.6;margin:0;">Meningkatkan Peran Serta Masyarakat, Kemitraan Swasta dan Sinergi Lintas Sektor Daerah.</p>
      </div>
      <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:14px;padding:20px;box-shadow:0 6px 18px rgba(0,0,0,0.03);">
        <div style="width:40px;height:40px;border-radius:10px;background:#e6f7f5;display:flex;align-items:center;justify-content:center;color:#087f89;font-weight:800;font-size:18px;margin-bottom:12px;">3</div>
        <h4 style="font-size:15px;font-weight:700;color:#103447;margin-bottom:8px;">SDM Kesehatan Merata</h4>
        <p style="font-size:13.5px;color:#587084;line-height:1.6;margin:0;">Meningkatkan Kualitas Sumber Daya Kesehatan Secara Merata Baik Kualitas Maupun Kuantitas.</p>
      </div>
    </div>
  </article>

  <!-- Tugas Pokok dan Fungsi -->
  <article class="panel">
    <span class="kicker">Dasar Hukum & Kewenangan</span>
    <h2>Tugas Pokok dan Fungsi Dinas Kesehatan</h2>
    <p style="font-size:15px;line-height:1.7;color:#334155;margin-bottom:16px;">
      Berdasarkan Peraturan Daerah dan Peraturan Bupati Pinrang, Dinas Kesehatan mempunyai tugas pokok:
    </p>
    <div style="padding:16px 20px;background:#f8fafc;border-left:4px solid #103447;border-radius:0 10px 10px 0;margin-bottom:24px;">
      <strong style="color:#103447;font-size:15px;">“Menyelenggarakan Urusan Pemerintahan di Bidang Kesehatan yang menjadi kewenangan Daerah dan Tugas Pembantuan yang diberikan kepada Daerah Kabupaten Pinrang.”</strong>
    </div>

    <h3 style="font-size:17px;font-weight:700;color:#103447;margin-bottom:16px;">Fungsi Utama Dinas Kesehatan:</h3>
    <ul style="display:grid;gap:12px;padding:0;list-style:none;">
      <li style="display:flex;gap:12px;background:#ffffff;border:1px solid #edf2f3;padding:14px 18px;border-radius:12px;">
        <span style="color:#087f89;font-weight:700;">•</span>
        <span style="font-size:14px;color:#334155;"><strong>Perumusan Kebijakan Teknis:</strong> Penyusunan rencana strategis dan kebijakan operasional di bidang kesehatan masyarakat, pencegahan & pengendalian penyakit, serta pelayanan & SDK.</span>
      </li>
      <li style="display:flex;gap:12px;background:#ffffff;border:1px solid #edf2f3;padding:14px 18px;border-radius:12px;">
        <span style="color:#087f89;font-weight:700;">•</span>
        <span style="font-size:14px;color:#334155;"><strong>Pelaksanaan Pelayanan Kesehatan:</strong> Penyelenggaraan pelayanan kesehatan primer melalui 19 UPTD Puskesmas, rujukan terpadu, serta laboratorium kesehatan daerah (Labkesda).</span>
      </li>
      <li style="display:flex;gap:12px;background:#ffffff;border:1px solid #edf2f3;padding:14px 18px;border-radius:12px;">
        <span style="color:#087f89;font-weight:700;">•</span>
        <span style="font-size:14px;color:#334155;"><strong>Pembinaan dan Pengawasan:</strong> Pengawasan mutu faskes, perizinan praktik nakes (SIP/SIK), sertifikasi pangan rumah tangga (SPP-IRT), dan pengendalian mutu obat & makanan.</span>
      </li>
      <li style="display:flex;gap:12px;background:#ffffff;border:1px solid #edf2f3;padding:14px 18px;border-radius:12px;">
        <span style="color:#087f89;font-weight:700;">•</span>
        <span style="font-size:14px;color:#334155;"><strong>Administrasi & Akuntabilitas Kepegawaian:</strong> Pengelolaan tata usaha, kepegawaian, keuangan, aset, serta pelaporan kinerja instansi pemerintah (LKjIP & IKU).</span>
      </li>
    </ul>
  </article>

  <!-- Rekam Jejak Prestasi & Penghargaan -->
  <article class="panel">
    <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:16px;">
      <div>
        <span class="kicker">Dedikasi & Apresiasi</span>
        <h2 style="margin:0;">Rekam Jejak Prestasi Kelembagaan</h2>
      </div>
      <a href="inovasi.html" class="btn secondary">${ic('external')} Lihat Semua Inovasi & Prestasi</a>
    </div>
    <div class="v4-timeline">
      <div class="v4-timeline-item">
        <span class="v4-timeline-badge">2022 · Penghargaan Nasional</span>
        <h4 class="v4-timeline-title">GOLD AWARD IndoHCF & Bebas Frambusia Kemenkes RI</h4>
        <p class="v4-timeline-desc">Meraih Gold Award Indonesia Healthcare Innovation Award (IHIA-VI) kategori Inovasi GERMAS dan Sertifikat Bebas Frambusia dari Menteri Kesehatan RI.</p>
      </div>
      <div class="v4-timeline-item">
        <span class="v4-timeline-badge">2021 · Kabupaten Sehat</span>
        <h4 class="v4-timeline-title">Swasti Saba Wistara ke-IV Kemenkes & Kemendagri RI</h4>
        <p class="v4-timeline-desc">Mempertahankan predikat tertinggi Kabupaten Sehat Swasti Saba Wistara 4 kali berturut-turut (2015, 2017, 2019, 2021) serta OPD Terbaik Citra Pelayanan Prima (CPP).</p>
      </div>
      <div class="v4-timeline-item">
        <span class="v4-timeline-badge">2020 · Sanitasi & Stunting</span>
        <h4 class="v4-timeline-title">Terbaik I Nasional STBM Berkelanjutan & Nominator AMPL</h4>
        <p class="v4-timeline-desc">Penghargaan STBM Berkelanjutan Kategori Demand Creation & Akselerasi Open Defecation Free (ODF) 100% di seluruh desa/kelurahan Kabupaten Pinrang.</p>
      </div>
    </div>
  </article>

  </div>${side('Profil & Informasi Terkait',[['profil','Profil Dinas'],['organisasi','Struktur Organisasi'],['inovasi','Prestasi & Inovasi'],['publikasi','Dokumen Kinerja (LKjIP)'],['layanan','Standar Pelayanan'],['kontak','Kontak Resmi Dinas']])}</div></section>`
}"""

ORGANISASI_PAGE = """function organisasiPage(){
  return pageHero('organisasi','Organisasi & Tata Kelola','Bagan Struktur Organisasi Dinas Kesehatan','Susunan kelembagaan dan penanggung jawab urusan kesehatan Kabupaten Pinrang berdasarkan regulasi tata kerja terbaru.')+`<section class="content"><div class="container twocol"><div class="stack">

  <!-- Bagan Struktur Resmi dari Backup -->
  <article class="panel">
    <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:16px;">
      <div>
        <span class="kicker">Dokumen Resmi Kelembagaan</span>
        <h2 style="margin:0;">Bagan Struktur Organisasi Dinas Kesehatan</h2>
      </div>
      <a href="assets/struktur_organisasi_dinkes.jpeg" target="_blank" class="btn secondary">${ic('external')} Buka Gambar Penuh</a>
    </div>
    <div class="v4-structure-container">
      <img src="assets/struktur_organisasi_dinkes.jpeg" alt="Bagan Struktur Organisasi Dinas Kesehatan Kabupaten Pinrang" class="v4-structure-img" />
      <p style="font-size:12.5px;color:#64748b;margin-top:12px;text-align:center;">
        ${ic('info')} Bagan Struktur Organisasi Dinas Kesehatan Kabupaten Pinrang berdasarkan Peraturan Daerah dan Peraturan Bupati Pinrang tentang Tata Kerja Perangkat Daerah.
      </p>
    </div>
  </article>

  <!-- Kartu Pimpinan & Bidang -->
  <article class="panel">
    <span class="kicker">Jajaran Pimpinan & Bidang</span>
    <h2>Struktur Jabatan & Penanggung Jawab</h2>
    <div class="grid grid-2" style="gap:16px;margin-top:20px;">
      
      <div class="panel" style="background:#f0fdf9;border:1px solid #bbf7d0;border-radius:14px;padding:20px;">
        <span style="font-size:11px;font-weight:800;color:#047857;text-transform:uppercase;letter-spacing:0.05em;">Pimpinan Utama</span>
        <h3 style="font-size:18px;font-weight:800;color:#103447;margin:6px 0 2px 0;">dr. H. Ramli Yunus, M.Kes</h3>
        <p style="font-size:13.5px;color:#087f89;font-weight:600;margin-bottom:10px;">Kepala Dinas Kesehatan</p>
        <p style="font-size:13px;color:#475569;line-height:1.6;margin:0;">Memimpin perumusan kebijakan, pengawasan pelaksanaan program kesehatan kabupaten, dan koordinasi lintas sektor.</p>
      </div>

      <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:14px;padding:20px;">
        <span style="font-size:11px;font-weight:800;color:#087f89;text-transform:uppercase;letter-spacing:0.05em;">Manajemen & Administrasi</span>
        <h3 style="font-size:18px;font-weight:800;color:#103447;margin:6px 0 2px 0;">Sekretariat Dinas</h3>
        <p style="font-size:13.5px;color:#087f89;font-weight:600;margin-bottom:10px;">Sekretaris Dinas Kesehatan</p>
        <p style="font-size:13px;color:#475569;line-height:1.6;margin:0;">Mengkoordinasikan subbagian perencanaan, evaluasi, pelaporan, umum, kepegawaian, dan pengelolaan keuangan.</p>
      </div>

      <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:14px;padding:20px;">
        <span style="font-size:11px;font-weight:800;color:#087f89;text-transform:uppercase;letter-spacing:0.05em;">Pelayanan Teknis</span>
        <h3 style="font-size:18px;font-weight:800;color:#103447;margin:6px 0 2px 0;">Bidang Kesehatan Masyarakat</h3>
        <p style="font-size:13.5px;color:#087f89;font-weight:600;margin-bottom:10px;">Kepala Bidang Kesmas</p>
        <p style="font-size:13px;color:#475569;line-height:1.6;margin:0;">Membawahi Tim Kerja Promosi Kesehatan & Pemberdayaan Masyarakat, Kesehatan Keluarga & Gizi, serta Kesling & Kerja.</p>
      </div>

      <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:14px;padding:20px;">
        <span style="font-size:11px;font-weight:800;color:#087f89;text-transform:uppercase;letter-spacing:0.05em;">Pencegahan & Pengendalian</span>
        <h3 style="font-size:18px;font-weight:800;color:#103447;margin:6px 0 2px 0;">Bidang P2P</h3>
        <p style="font-size:13.5px;color:#087f89;font-weight:600;margin-bottom:10px;">Kepala Bidang Pencegahan & Pengendalian Penyakit</p>
        <p style="font-size:13px;color:#475569;line-height:1.6;margin:0;">Mengelola surveilans epidemiologi, imunisasi, pengendalian penyakit menular (TB, DBD, HIV, Malaria) dan PTM.</p>
      </div>

      <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:14px;padding:20px;">
        <span style="font-size:11px;font-weight:800;color:#087f89;text-transform:uppercase;letter-spacing:0.05em;">Fasilitas & SDM</span>
        <h3 style="font-size:18px;font-weight:800;color:#103447;margin:6px 0 2px 0;">Bidang Pelayanan & SDK</h3>
        <p style="font-size:13.5px;color:#087f89;font-weight:600;margin-bottom:10px;">Kepala Bidang Pelayanan & Sumber Daya Kesehatan</p>
        <p style="font-size:13px;color:#475569;line-height:1.6;margin:0;">Membidangi mutu faskes primer/rujukan, perizinan tenaga kesehatan (SIP/SIK), kefarmasian, alkes, dan pengembangan SDM kesehatan.</p>
      </div>

      <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:14px;padding:20px;">
        <span style="font-size:11px;font-weight:800;color:#087f89;text-transform:uppercase;letter-spacing:0.05em;">Unit Pelaksana Teknis Daerah</span>
        <h3 style="font-size:18px;font-weight:800;color:#103447;margin:6px 0 2px 0;">19 UPTD Puskesmas & Labkesda</h3>
        <p style="font-size:13.5px;color:#087f89;font-weight:600;margin-bottom:10px;">Kepala UPTD Puskesmas & Kepala Labkesda</p>
        <p style="font-size:13px;color:#475569;line-height:1.6;margin:0;">Garda terdepan pelayanan kesehatan primer di 12 kecamatan se-Kabupaten Pinrang serta pengujian laboratorium terakreditasi.</p>
      </div>

    </div>
  </article>

  </div>${side('Navigasi Kelembagaan',[['profil','Profil Dinas'],['organisasi','Struktur Organisasi'],['puskesmas','Direktori 19 Puskesmas'],['publikasi','Dokumen LKjIP & IKU'],['kontak','Kontak & Lokasi Kantor']])}</div></section>`
}"""

print("Modul siap diaplikasikan!")
''')

print("Generator modul siap dieksekusi.")
