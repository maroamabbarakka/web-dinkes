# -*- coding: utf-8 -*-
"""
Script untuk memperbarui app.v4.js dan app.js:
1. Ganti gambar hero menjadi kolase_emblem_dinkes_pinrang_opt.png
2. Visual cover profesional untuk 6 Layanan Utama dan 3 Pilar Transformasi (warna berbeda per card)
3. Hapus angka jumlah puskesmas di judul/menu (cukup Puskesmas / UPTD Puskesmas)
4. Pengelompokan terpisah secara profesional:
   - Liputan Berita & Artikel
   - Poster & Materi Promosi Kesehatan (Promkes)
   - Data, Struktur & Pengumuman
5. Menu atas versi mobile super rapi dengan icon profesional (tidak menumpuk)
"""

import re

with open('public/assets/app.v4.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. PERBARUI FUNGSI HEADER (SERVICE STRIP & MENU NAVIGASI)
old_header_pat = r'function header\(page\)\s*\{[\s\S]*?return `[\s\S]*?<\/header>`;\s*\}'

new_header_code = '''function header(page) {
  return `
  <!-- SERVICE STRIP (TOP BAR DINSOS STYLE - RESPONSIVE CLEAN ICONS ON MOBILE) -->
  <div class="service-strip">
    <div class="container strip-inner">
      <div class="strip-brand">
        <svg class="strip-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
          <circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20M2 12h20"/>
        </svg>
        <span class="strip-title-desktop">Website Resmi Pemerintah Kabupaten Pinrang - Sulawesi Selatan</span>
        <span class="strip-title-mobile">PINRANGKAB.GO.ID</span>
      </div>
      <div class="strip-links">
        <a href="layanan-detail.html" class="strip-link-item" title="Cek Kesehatan Gratis (CKG)">
          <span class="strip-dot"></span>
          <svg class="strip-link-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>
          <span class="strip-label-desktop">Cek Kesehatan Gratis (CKG)</span>
          <span class="strip-label-mobile">CKG</span>
        </a>
        <a href="pengaduan.html" class="strip-link-item" title="Kanal Pengaduan Resmi (SP4N-LAPOR!)">
          <svg class="strip-link-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
          <span class="strip-label-desktop">Pengaduan (SP4N-LAPOR!)</span>
          <span class="strip-label-mobile">Aduan</span>
        </a>
        <a href="https://pinrangkab.go.id" target="_blank" rel="noopener noreferrer" class="strip-link-item" title="Portal Resmi Pemerintah Kabupaten Pinrang">
          <svg class="strip-link-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          <span class="strip-label-desktop">Portal Pemkab ↗</span>
          <span class="strip-label-mobile">Pemkab</span>
        </a>
      </div>
    </div>
  </div>

  <!-- SITE HEADER (STICKY HEADER DINSOS STYLE) -->
  <header class="site-header">
    <div class="container header-inner">
      <div class="brand">
        <a href="index.html" class="brand-logos" aria-label="Beranda Dinas Kesehatan Kabupaten Pinrang">
          <img src="assets/logo_pinrang_opt.png" alt="Logo Pemkab Pinrang" class="logo-pemkab" />
          <img src="assets/kemenkes.jpg" alt="Logo Kemenkes RI" class="logo-kemenkes" />
        </a>
        <a class="site-name" href="index.html">
          <span class="instansi-name">Dinas Kesehatan</span>
          <small class="instansi-sub">Kabupaten Pinrang</small>
        </a>
      </div>

      <!-- PRIMARY NAVIGATION (TANPA ANGKA JUMLAH PUSKESMAS) -->
      <nav aria-label="Navigasi utama" class="primary-nav">
        <ul class="menu">
          <li class="${page==='index'?'current-menu-item':''}"><a href="index.html">Beranda</a></li>
          <li class="${['profil','organisasi'].includes(page)?'current-menu-item':''}"><a href="profil.html">Profil Dinas</a></li>
          <li class="${['layanan','layanan-detail'].includes(page)?'current-menu-item':''}"><a href="layanan.html">Layanan</a></li>
          <li class="${['data','indikator'].includes(page)?'current-menu-item':''}"><a href="data.html">Data Kesehatan</a></li>
          <li class="${['publikasi','ppid','pengumuman'].includes(page)?'current-menu-item':''}"><a href="publikasi.html">Informasi Publik</a></li>
          <li class="${['berita','berita-detail'].includes(page)?'current-menu-item':''}"><a href="berita.html">Berita & Kegiatan</a></li>
          <li class="${['edukasi','edukasi-detail'].includes(page)?'current-menu-item':''}"><a href="edukasi.html">Promkes & Poster</a></li>
          <li class="${['puskesmas','puskesmas-detail'].includes(page)?'current-menu-item':''}"><a href="puskesmas.html">Puskesmas</a></li>
          <li class="${page==='galeri'?'current-menu-item':''}"><a href="galeri.html">Galeri</a></li>
        </ul>
      </nav>

      <!-- HEADER ACTIONS (PENGADUAN & HAMBURGER) -->
      <div class="header-actions">
        <a href="pengaduan.html" class="btn-pengaduan-header" aria-label="Layanan Pengaduan Kesehatan">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
          <span class="btn-text">Pengaduan</span>
        </a>
        <button aria-controls="mobile-nav" aria-expanded="false" aria-label="Buka navigasi menu" class="nav-toggle" type="button">
          <span class="nav-toggle-icon" aria-hidden="true">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
          </span>
        </button>
      </div>
    </div>
  </header>`;
}'''

code = re.sub(old_header_pat, new_header_code, code)

# 2. PERBARUI FUNGSI HOMEPAGE DENGAN PENGELOMPOKAN TERPISAH SECARA PROFESIONAL
old_home_pat = r'function homePage\(\)\s*\{[\s\S]*?\nfunction profilPage\(\)'

new_home_code = '''function homePage() {
  const articles = window.ARTICLES_CACHE || [];
  
  // PENGELOMPOKAN TERPISAH YANG JELAS & PROFESIONAL
  // 1. Berita & Liputan Kegiatan Resmi Dinas (bukan poster!)
  const newsOnly = articles.filter(a => (a.content_type === 'berita' || a.content_type === 'artikel') && !a.title.toLowerCase().includes('poster')).slice(0, 3);
  
  // 2. Poster Edukasi & Materi Promosi Kesehatan (Promkes)
  const postersOnly = articles.filter(a => a.content_type === 'promkes' || a.category === 'promkes' || a.title.toLowerCase().includes('poster')).slice(0, 4);

  return `
  <!-- 1. HERO SECTION (DINSOS MOCKUP STYLE DENGAN GAMBAR KOLASE EMBLEM RESMI) -->
  <section class="hero hero--mockup">
    <div aria-hidden="true" class="hero-pattern"></div>
    <div class="container hero-inner hero-inner--mockup">
      <div class="hero-copy">
        <div class="hero-kicker-row" style="margin-bottom:14px;">
          <span class="hero-badge-pill">
            ${ic('shield')} Pelayanan Kesehatan Terbuka & Akuntabel
          </span>
        </div>
        <h1 class="hero-heading">
          Melayani dengan Sepenuh Hati, Mewujudkan Pinrang Sehat & Mandiri
        </h1>
        <p class="hero-lead">
          Informasi pelayanan kesehatan masyarakat, rekomendasi perizinan nakes & pangan, integrasi jaringan Puskesmas, serta pencegahan penyakit Kabupaten Pinrang yang dihadirkan secara profesional, cepat, dan bermartabat.
        </p>
        
        <!-- INTEGRATED SEARCH FORM -->
        <form action="berita.html" class="hero-search-mockup" method="get" role="search">
          <label class="sr-only" for="hero-search-input">Cari layanan kesehatan atau puskesmas</label>
          <input id="hero-search-input" name="q" placeholder="Cari layanan kesehatan, nakes, izin, puskesmas, stunting..." type="search" />
          <button aria-label="Cari" type="submit">
            <svg aria-hidden="true" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="20">
              <circle cx="11" cy="11" r="8"></circle>
              <path d="m21 21-4.35-4.35"></path>
            </svg>
          </button>
        </form>
      </div>

      <!-- VISUAL KOLASE EMBLEM RESMI DINAS KESEHATAN KABUPATEN PINRANG -->
      <div class="hero-illustration hero-illustration--mockup">
        <img alt="Kolase Emblem Resmi Dinas Kesehatan Kabupaten Pinrang" 
             src="assets/kolase_emblem_dinkes_pinrang_opt.png" 
             loading="eager" 
             style="filter:drop-shadow(0 20px 40px rgba(16,52,71,0.22));max-width:540px;width:100%;height:auto;display:block;margin:0 auto;" />
      </div>
    </div>
  </section>

  <!-- 2. QUICK ACCESS CARDS MELAYANG (PERSIS DINSOS STYLE) -->
  <section class="quick-access-mockup">
    <div class="container">
      <div class="quick-access-grid-mockup">
        <a class="quick-card-mockup" href="layanan-detail.html">
          <div class="quick-card-icon" style="background:#f0fdf9;color:#0aa398;">
            <svg fill="none" height="22" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="22"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>
          </div>
          <div class="quick-card-content">
            <h3>Cek Kesehatan (CKG)</h3>
            <p>Skrining riwayat kesehatan berkala gratis di seluruh Puskesmas.</p>
          </div>
          <div class="quick-card-arrow">${ic('chevron')}</div>
        </a>

        <a class="quick-card-mockup" href="puskesmas.html">
          <div class="quick-card-icon" style="background:#f0fdf4;color:#16a34a;">
            <svg fill="none" height="22" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="22"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 8v8"/><path d="M8 12h8"/></svg>
          </div>
          <div class="quick-card-content">
            <h3>Puskesmas</h3>
            <p>Lokasi, kontak IGD 24 Jam, dan profil dokter penanggung jawab.</p>
          </div>
          <div class="quick-card-arrow">${ic('chevron')}</div>
        </a>

        <a class="quick-card-mockup" href="layanan.html">
          <div class="quick-card-icon" style="background:#fffbeb;color:#d97706;">
            <svg fill="none" height="22" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="22"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
          </div>
          <div class="quick-card-content">
            <h3>SIP & SIK Nakes</h3>
            <p>Rekomendasi surat izin praktik tenaga medis & perawat online.</p>
          </div>
          <div class="quick-card-arrow">${ic('chevron')}</div>
        </a>

        <a class="quick-card-mockup" href="pengaduan.html">
          <div class="quick-card-icon" style="background:#f0f9ff;color:#0284c7;">
            <svg fill="none" height="22" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="22"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          </div>
          <div class="quick-card-content">
            <h3>PSC 119 & Aduan</h3>
            <p>Kedaruratan medis 24 Jam & kanal resmi SP4N-LAPOR!.</p>
          </div>
          <div class="quick-card-arrow">${ic('chevron')}</div>
        </a>
      </div>
    </div>
  </section>

  <!-- 3. LAYANAN UTAMA SECTION (6 KARTU DENGAN VISUAL COVER FOTO RIIL & WARNA BERBEDA) -->
  <section class="section-services-mockup">
    <div class="container">
      <div class="section-head--mockup">
        <div>
          <h2 class="section-title--mockup" style="font-size:2.2rem;font-weight:800;color:#103447;margin:0 0 0.5rem;">Layanan Utama</h2>
          <p class="section-sub--mockup" style="font-size:1.05rem;color:#475569;margin:0;">Akses layanan kesehatan Dinas Kesehatan Kabupaten Pinrang dengan mudah, transparan, dan terpadu.</p>
        </div>
        <div>
          <a class="btn-all-services-mockup" href="layanan.html">Lihat semua layanan →</a>
        </div>
      </div>

      <div class="service-grid--mockup">
        <!-- 1. Puskesmas (Emerald Hijau) -->
        <article class="service-card--mockup card-emerald" style="border-top:4px solid #059669;">
          <div class="service-card-media" style="border-radius:14px;overflow:hidden;margin-bottom:1.25rem;">
            <img src="assets/covers/service_puskesmas.jpg" alt="Pelayanan Puskesmas" style="width:100%;height:190px;object-fit:cover;display:block;" />
          </div>
          <span class="service-card-kicker" style="color:#059669;font-weight:700;font-size:0.8rem;text-transform:uppercase;">Pelayanan Kesehatan Primer</span>
          <h3><a href="puskesmas.html">Pelayanan Rawat Puskesmas</a></h3>
          <p>Pelayanan rawat jalan, rawat inap, persalinan 24 jam, poli umum, KIA, gigi, laboratorium, dan imunisasi di seluruh kecamatan se-Kabupaten Pinrang.</p>
          <div class="service-card-meta" style="margin-top:1rem;display:flex;gap:8px;flex-wrap:wrap;">
            <span class="badge-status-mockup" style="background:#ecfdf5;color:#065f46;border:1px solid #a7f3d0;">Gratis / tidak dipungut biaya</span>
            <span class="badge-status-mockup" style="background:#fef3c7;color:#92400e;border:1px solid #fde68a;">Siaga 24 Jam (IGD)</span>
          </div>
          <a class="service-card-link" href="puskesmas.html" style="color:#059669;margin-top:1.2rem;display:inline-flex;align-items:center;gap:6px;font-weight:700;text-decoration:none;">Lihat layanan →</a>
        </article>

        <!-- 2. SIP & SIK Nakes (Sapphire Blue) -->
        <article class="service-card--mockup card-sapphire" style="border-top:4px solid #1d4ed8;">
          <div class="service-card-media" style="border-radius:14px;overflow:hidden;margin-bottom:1.25rem;">
            <img src="assets/covers/service_sip_nakes.jpg" alt="Rekomendasi SIP & SIK Nakes" style="width:100%;height:190px;object-fit:cover;display:block;" />
          </div>
          <span class="service-card-kicker" style="color:#1d4ed8;font-weight:700;font-size:0.8rem;text-transform:uppercase;">Sumber Daya Kesehatan (SDK)</span>
          <h3><a href="layanan-detail.html">Rekomendasi SIP & SIK Nakes</a></h3>
          <p>Penerbitan surat rekomendasi izin praktik dokter, perawat, bidan, apoteker, dan tenaga kesehatan secara transparan dan akuntabel.</p>
          <div class="service-card-meta" style="margin-top:1rem;display:flex;gap:8px;flex-wrap:wrap;">
            <span class="badge-status-mockup" style="background:#ecfdf5;color:#065f46;border:1px solid #a7f3d0;">Gratis / tidak dipungut biaya</span>
            <span class="badge-status-mockup" style="background:#eff6ff;color:#1e40af;border:1px solid #bfdbfe;">Perlu Verifikasi Persyaratan</span>
          </div>
          <a class="service-card-link" href="layanan-detail.html" style="color:#1d4ed8;margin-top:1.2rem;display:inline-flex;align-items:center;gap:6px;font-weight:700;text-decoration:none;">Lihat layanan →</a>
        </article>

        <!-- 3. Sertifikasi Pangan (Golden Amber) -->
        <article class="service-card--mockup card-amber" style="border-top:4px solid #d97706;">
          <div class="service-card-media" style="border-radius:14px;overflow:hidden;margin-bottom:1.25rem;">
            <img src="assets/covers/service_pangan_sppirt.jpg" alt="Sertifikasi Pangan SPP-IRT" style="width:100%;height:190px;object-fit:cover;display:block;" />
          </div>
          <span class="service-card-kicker" style="color:#d97706;font-weight:700;font-size:0.8rem;text-transform:uppercase;">Kefarmasian & Keamanan Pangan</span>
          <h3><a href="layanan-detail.html">Sertifikasi Pangan (SPP-IRT)</a></h3>
          <p>Penyuluhan keamanan pangan dan penerbitan sertifikat pemenuhan komitmen produksi pangan olahan industri rumah tangga agar aman konsumsi.</p>
          <div class="service-card-meta" style="margin-top:1rem;display:flex;gap:8px;flex-wrap:wrap;">
            <span class="badge-status-mockup" style="background:#ecfdf5;color:#065f46;border:1px solid #a7f3d0;">Gratis / tidak dipungut biaya</span>
            <span class="badge-status-mockup" style="background:#fffbeb;color:#b45309;border:1px solid #fde68a;">Fasilitasi Pembinaan Pemkab</span>
          </div>
          <a class="service-card-link" href="layanan-detail.html" style="color:#d97706;margin-top:1.2rem;display:inline-flex;align-items:center;gap:6px;font-weight:700;text-decoration:none;">Lihat layanan →</a>
        </article>

        <!-- 4. Cek Kesehatan Gratis (Cyan Toska) -->
        <article class="service-card--mockup card-cyan" style="border-top:4px solid #087f89;">
          <div class="service-card-media" style="border-radius:14px;overflow:hidden;margin-bottom:1.25rem;">
            <img src="assets/covers/service_ckg.jpg" alt="Cek Kesehatan Gratis CKG" style="width:100%;height:190px;object-fit:cover;display:block;" />
          </div>
          <span class="service-card-kicker" style="color:#087f89;font-weight:700;font-size:0.8rem;text-transform:uppercase;">Deteksi Dini & Preventif</span>
          <h3><a href="layanan-detail.html">Cek Kesehatan Gratis (CKG)</a></h3>
          <p>Skrining kesehatan berkala meliputi tekanan darah, gula darah, deteksi dini faktor risiko penyakit tidak menular (PTM) di faskes primer.</p>
          <div class="service-card-meta" style="margin-top:1rem;display:flex;gap:8px;flex-wrap:wrap;">
            <span class="badge-status-mockup" style="background:#ecfdf5;color:#065f46;border:1px solid #a7f3d0;">Gratis / tidak dipungut biaya</span>
            <span class="badge-status-mockup" style="background:#f0fdf9;color:#0f766e;border:1px solid #99f6e4;">Tanpa Syarat Rumit</span>
          </div>
          <a class="service-card-link" href="layanan-detail.html" style="color:#087f89;margin-top:1.2rem;display:inline-flex;align-items:center;gap:6px;font-weight:700;text-decoration:none;">Lihat layanan →</a>
        </article>

        <!-- 5. Stunting & Imunisasi (Coral Rose) -->
        <article class="service-card--mockup card-rose" style="border-top:4px solid #e11d48;">
          <div class="service-card-media" style="border-radius:14px;overflow:hidden;margin-bottom:1.25rem;">
            <img src="assets/covers/service_stunting_gizi.jpg" alt="Pencegahan Stunting & Imunisasi" style="width:100%;height:190px;object-fit:cover;display:block;" />
          </div>
          <span class="service-card-kicker" style="color:#e11d48;font-weight:700;font-size:0.8rem;text-transform:uppercase;">Kesehatan Masyarakat & Gizi</span>
          <h3><a href="edukasi.html">Pencegahan Stunting & Imunisasi</a></h3>
          <p>Pemantauan rutin tumbuh kembang balita, imunisasi dasar lengkap, intervensi gizi terpadu, dan edukasi pola hidup bersih sehat di Posyandu.</p>
          <div class="service-card-meta" style="margin-top:1rem;display:flex;gap:8px;flex-wrap:wrap;">
            <span class="badge-status-mockup" style="background:#ecfdf5;color:#065f46;border:1px solid #a7f3d0;">Gratis / tidak dipungut biaya</span>
            <span class="badge-status-mockup" style="background:#fff1f2;color:#be123c;border:1px solid #fecdd3;">Prioritas Nasional</span>
          </div>
          <a class="service-card-link" href="edukasi.html" style="color:#e11d48;margin-top:1.2rem;display:inline-flex;align-items:center;gap:6px;font-weight:700;text-decoration:none;">Lihat layanan →</a>
        </article>

        <!-- 6. Kedaruratan PSC 119 (Crimson Red) -->
        <article class="service-card--mockup card-red" style="border-top:4px solid #dc2626;">
          <div class="service-card-media" style="border-radius:14px;overflow:hidden;margin-bottom:1.25rem;">
            <img src="assets/covers/service_psc119.jpg" alt="Layanan Darurat Medis PSC 119" style="width:100%;height:190px;object-fit:cover;display:block;" />
          </div>
          <span class="service-card-kicker" style="color:#dc2626;font-weight:700;font-size:0.8rem;text-transform:uppercase;">Penanganan Kegawatdaruratan</span>
          <h3><a href="pengaduan.html">Layanan Darurat Medis PSC 119</a></h3>
          <p>Pelayanan penjemputan ambulans darurat, pertolongan pertama kecelakaan, evakuasi medis, serta koordinasi rujukan pra-rumah sakit 24 jam.</p>
          <div class="service-card-meta" style="margin-top:1rem;display:flex;gap:8px;flex-wrap:wrap;">
            <span class="badge-status-mockup" style="background:#ecfdf5;color:#065f46;border:1px solid #a7f3d0;">Gratis / tidak dipungut biaya</span>
            <span class="badge-status-mockup" style="background:#fef2f2;color:#b91c1c;border:1px solid #fecaca;">Siaga 24 Jam Nonstop</span>
          </div>
          <a class="service-card-link" href="pengaduan.html" style="color:#dc2626;margin-top:1.2rem;display:inline-flex;align-items:center;gap:6px;font-weight:700;text-decoration:none;">Lihat layanan →</a>
        </article>
      </div>
    </div>
  </section>

  <!-- 4. ALERT BANNER SECTION (ANTI-PUNGLI & PENIPUAN) -->
  <section class="alert-mockup-section">
    <div class="container">
      <div class="alert-mockup-card">
        <div class="alert-mockup-icon" style="background:#ffffff;color:#dc2626;">
          <svg fill="none" height="26" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="26"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
        </div>
        <div class="alert-mockup-content">
          <h4>Waspada Pungutan Liar & Penipuan!</h4>
          <p>Seluruh penerbitan surat rekomendasi perizinan nakes dan layanan publik Dinas Kesehatan Kabupaten Pinrang tidak dipungut biaya ilegal. Laporkan jika ada oknum yang meminta imbalan.</p>
        </div>
        <div class="alert-mockup-action">
          <a class="btn-alert-mockup" href="pengaduan.html">Laporkan Sekarang ›</a>
        </div>
      </div>
    </div>
  </section>

  <!-- 5. INFORMASI BERITA TERBARU & DOKUMEN PUBLIK (PENGELOMPOKAN TERPISAH) -->
  <section class="home-info-mockup-section">
    <div class="container">
      <div class="home-info-mockup-grid">
        <!-- Kolom Kiri: KHUSUS Liputan Berita & Kegiatan Resmi (Bukan Poster!) -->
        <div class="home-news-col">
          <div class="home-section-head-mockup">
            <h3 style="display:flex;align-items:center;gap:8px;">
              <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#0aa398;"></span>
              Berita & Liputan Kegiatan Dinas
            </h3>
            <a class="home-link-all" href="berita.html">Lihat semua berita →</a>
          </div>

          <div class="home-news-list-mockup">
            ${newsOnly.map(a => `
              <article class="news-card-mockup">
                <a class="news-card-thumb-link" href="berita-detail.html?slug=${a.slug}">
                  <img alt="${a.title}" src="${getSafeImageUrl(a.image)}" />
                </a>
                <div class="news-card-info">
                  <span class="news-card-badge">${a.category || 'Berita Kesehatan'}</span>
                  <h4><a href="berita-detail.html?slug=${a.slug}">${a.title}</a></h4>
                  <p>${(a.excerpt || a.description || '').slice(0, 110)}...</p>
                  <div class="news-card-meta">
                    <span>${ic('calendar')} ${a.date || 'Terbaru'}</span>
                    <span>${ic('people')} ${a.author || 'Humas Dinkes'}</span>
                  </div>
                </div>
              </article>
            `).join('')}
          </div>
        </div>

        <!-- Kolom Kanan: Dokumen Kinerja Publik & Pengumuman -->
        <div class="home-docs-col">
          <div class="home-section-head-mockup">
            <h3 style="display:flex;align-items:center;gap:8px;">
              <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#d97706;"></span>
              Dokumen Kinerja & Pengumuman
            </h3>
            <a class="home-link-all" href="publikasi.html">Lihat semua dokumen →</a>
          </div>

          <div class="home-docs-list-mockup">
            <div class="doc-card-mockup">
              <div class="doc-card-icon" style="background:#fee2e2;color:#dc2626;">
                <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
              </div>
              <div class="doc-card-info">
                <div class="doc-card-title">Laporan Kinerja Instansi Pemerintah (LKjIP) Tahun 2026</div>
                <div class="doc-card-meta">PDF · 1.8 MB · Diterbitkan Dinkes Pinrang</div>
              </div>
              <a class="doc-card-download" href="assets/kantor_dinkes_pinrang.jpg" target="_blank" title="Unduh Dokumen LKjIP">
                <svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="18"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              </a>
            </div>

            <div class="doc-card-mockup">
              <div class="doc-card-icon" style="background:#fee2e2;color:#dc2626;">
                <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
              </div>
              <div class="doc-card-info">
                <div class="doc-card-title">Rencana Strategis & Indikator Kinerja Utama (IKU)</div>
                <div class="doc-card-meta">PDF · 2.1 MB · Dokumen Kebijakan Daerah</div>
              </div>
              <a class="doc-card-download" href="assets/kantor_dinkes_pinrang.jpg" target="_blank" title="Unduh Rencana Strategis">
                <svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="18"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              </a>
            </div>

            <div class="doc-card-mockup">
              <div class="doc-card-icon" style="background:#fee2e2;color:#dc2626;">
                <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
              </div>
              <div class="doc-card-info">
                <div class="doc-card-title">Standar Pelayanan Publik & SOP Rekomendasi SIP</div>
                <div class="doc-card-meta">PDF · 920 KB · Maklumat Pelayanan</div>
              </div>
              <a class="doc-card-download" href="assets/kantor_dinkes_pinrang.jpg" target="_blank" title="Unduh Standar Pelayanan">
                <svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="18"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              </a>
            </div>
          </div>

          <!-- BANNER SURVEI KEPUASAN MASYARAKAT (SKM) -->
          <div class="skm-banner-mockup">
            <span class="skm-badge-pill">✓ Survei Kepuasan Masyarakat (SKM)</span>
            <h4>Bantu Tingkatkan Mutu Layanan Kesehatan Kami</h4>
            <p>Partisipasi Anda dalam pengisian kuesioner SKM sangat berharga untuk transparansi dan integritas Dinas Kesehatan Pinrang.</p>
            <a class="btn-skm-mockup" href="skm.html">Beri Penilaian via Kuesioner ›</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 6. SECTION KHUSUS: POSTER EDUKASI & PROMOSI KESEHATAN (TERPISAH & PROFESIONAL) -->
  <section class="promkes-poster-section" style="padding:4rem 0;background:#f8fafc;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0;">
    <div class="container">
      <div class="section-head--mockup">
        <div>
          <span style="font-size:0.85rem;font-weight:700;color:#087f89;text-transform:uppercase;letter-spacing:0.05em;display:block;margin-bottom:4px;">
            Materi Edukasi Masyarakat
          </span>
          <h2 style="font-size:2.2rem;font-weight:800;color:#103447;margin:0 0 0.5rem;">Poster & Promosi Kesehatan</h2>
          <p style="font-size:1.05rem;color:#475569;margin:0;">Koleksi infografis, poster kampanye PHBS, lembar balik posyandu, dan panduan hidup sehat.</p>
        </div>
        <div>
          <a class="btn-all-services-mockup" href="edukasi.html">Lihat semua materi edukasi →</a>
        </div>
      </div>

      <div class="promkes-poster-grid" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(250px, 1fr));gap:24px;margin-top:2rem;">
        ${postersOnly.map(p => `
          <article class="promkes-poster-card" style="background:#ffffff;border:1px solid #e2e8f0;border-radius:18px;overflow:hidden;box-shadow:0 6px 18px rgba(16,52,71,0.04);transition:transform 0.25s ease, box-shadow 0.25s ease;">
            <div class="poster-thumb-wrap" style="position:relative;height:260px;overflow:hidden;background:#f1f5f9;">
              <img src="${getSafeImageUrl(p.image)}" alt="${p.title}" style="width:100%;height:100%;object-fit:cover;object-position:top;display:block;" />
              <span style="position:absolute;top:12px;left:12px;background:rgba(16,52,71,0.85);color:#ffffff;font-size:11px;font-weight:700;padding:4px 10px;border-radius:20px;backdrop-filter:blur(4px);">
                POSTER EDUKASI
              </span>
            </div>
            <div class="poster-body" style="padding:18px;">
              <h4 style="font-size:16px;font-weight:700;color:#103447;margin:0 0 8px;line-height:1.4;">
                <a href="edukasi-detail.html?slug=${p.slug}" style="color:inherit;text-decoration:none;">${p.title}</a>
              </h4>
              <p style="font-size:13px;color:#64748b;line-height:1.5;margin:0 0 14px;">${(p.excerpt || p.description || 'Materi edukasi dan publikasi resmi kesehatan masyarakat.').slice(0, 90)}...</p>
              <a href="edukasi-detail.html?slug=${p.slug}" class="btn" style="width:100%;text-align:center;justify-content:center;font-size:12.5px;padding:8px 12px;background:#f0fdf9;color:#087f89;border:1px solid #99f6e4;border-radius:10px;font-weight:700;text-decoration:none;">
                Lihat & Unduh Poster →
              </a>
            </div>
          </article>
        `).join('')}
      </div>
    </div>
  </section>

  <!-- 7. PILAR TRANSFORMASI LAYANAN KESEHATAN (3 PILAR DENGAN WARNA BERBEDA) -->
  <section class="psks-section">
    <div class="container">
      <div style="text-align:center;margin-bottom:3rem;">
        <span class="psks-badge-pill">• KEMITRAAN & PILAR KESEHATAN DAERAH</span>
        <h2 class="psks-heading">Pilar Transformasi Layanan Kesehatan</h2>
        <p class="psks-sub">Pilar pelayanan, pencegahan, dan kesiapsiagaan medis masyarakat yang berada di bawah koordinasi dan binaan Dinas Kesehatan Kabupaten Pinrang demi mewujudkan derajat kesehatan yang optimal, merata, dan bermartabat.</p>
      </div>

      <div class="psks-grid">
        <!-- Pilar 1: UPTD Puskesmas (Teal) -->
        <div class="psks-card" style="border-top:4px solid #0f766e;">
          <div style="border-radius:12px;overflow:hidden;margin-bottom:1.25rem;">
            <img src="assets/covers/pilar_puskesmas.jpg" alt="UPTD Puskesmas" style="width:100%;height:160px;object-fit:cover;display:block;" />
          </div>
          <span class="psks-card-badge" style="background:#ccfbf1;color:#0f766e;">12 Kecamatan di Kab. Pinrang</span>
          <h3>UPTD Puskesmas</h3>
          <p>Fasilitas Pelayanan Kesehatan Primer jaringan fasilitas kesehatan tingkat pertama yang menyelenggarakan rawat jalan, rawat inap, poli KIA, laboratorium, dan IGD 24 Jam di seluruh kecamatan Kabupaten Pinrang.</p>
          <a class="btn-psks" href="puskesmas.html" style="background:#0f766e;color:#ffffff;">Profil Puskesmas →</a>
        </div>

        <!-- Pilar 2: GERMAS Pinrang (Green) -->
        <div class="psks-card" style="border-top:4px solid #15803d;">
          <div style="border-radius:12px;overflow:hidden;margin-bottom:1.25rem;">
            <img src="assets/covers/pilar_germas.jpg" alt="GERMAS Pinrang" style="width:100%;height:160px;object-fit:cover;display:block;" />
          </div>
          <span class="psks-card-badge" style="background:#dcfce7;color:#15803d;">Promosi & Deteksi Dini</span>
          <h3>GERMAS Pinrang</h3>
          <p>Gerakan Masyarakat Hidup Sehat. Pemberdayaan masyarakat melalui aktivitas fisik teratur, konsumsi buah dan sayur, pemeriksaan kesehatan berkala, serta komitmen 100% Bebas Buang Air Besar Sembarangan (ODF).</p>
          <a class="btn-psks" href="edukasi.html" style="background:#15803d;color:#ffffff;">Aksi & Kampanye GERMAS →</a>
        </div>

        <!-- Pilar 3: PSC 119 Pinrang (Amber Orange) -->
        <div class="psks-card" style="border-top:4px solid #c2410c;">
          <div style="border-radius:12px;overflow:hidden;margin-bottom:1.25rem;">
            <img src="assets/covers/pilar_psc119.jpg" alt="PSC 119 Pinrang" style="width:100%;height:160px;object-fit:cover;display:block;" />
          </div>
          <span class="psks-card-badge" style="background:#ffedd5;color:#c2410c;">Tanggap Darurat 24 Jam</span>
          <h3>PSC 119 Pinrang</h3>
          <p>Public Safety Center & Rujukan Cepat. Layanan reaksi cepat penanganan kegawatdaruratan medis, evakuasi korban kecelakaan, armada ambulans siaga, dan koordinasi terpadu antar fasilitas rujukan daerah.</p>
          <a class="btn-psks" href="pengaduan.html" style="background:#c2410c;color:#ffffff;">Kesiapsiagaan PSC 119 →</a>
        </div>
      </div>
    </div>
  </section>`;
}
function profilPage()'''

code = re.sub(old_home_pat, new_home_code, code)

# 3. HAPUS KATA "19" DARI MENU DAN JUDUL PUSKESMAS DI SELURUH BERKAS
code = code.replace('>19 Puskesmas<', '>Puskesmas<')
code = code.replace('>19 UPTD Puskesmas<', '>Puskesmas<')
code = code.replace('Direktori 19 UPTD Puskesmas', 'Direktori Puskesmas')
code = code.replace('19 UPTD Puskesmas Kabupaten Pinrang', 'UPTD Puskesmas Kabupaten Pinrang')

with open('public/assets/app.v4.js', 'w', encoding='utf-8') as f:
    f.write(code)

with open('public/assets/app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print('app.v4.js dan app.js berhasil diperbarui!')
