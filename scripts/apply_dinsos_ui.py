import os, re, glob

# Baca app.v4.js
with open('public/assets/app.v4.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Definisi Header Baru (Dinsos Architecture + Dinkes Palette)
new_header_func = """function header(page) {
  return `
  <!-- SERVICE STRIP (TOP BAR DINSOS STYLE) -->
  <div class="service-strip">
    <div class="container" style="display:flex;align-items:center;justify-content:space-between;min-height:36px;padding-inline:16px;">
      <span style="font-size:12px;font-weight:600;display:inline-flex;align-items:center;gap:6px;">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20M2 12h20"/></svg>
        Website Resmi Pemerintah Kabupaten Pinrang - Sulawesi Selatan
      </span>
      <div class="strip-links" style="display:flex;align-items:center;gap:18px;font-size:12px;">
        <a href="layanan-detail.html" style="text-decoration:none;display:inline-flex;align-items:center;gap:5px;">
          <span style="width:7px;height:7px;border-radius:50%;background:#5eead4;display:inline-block;"></span> Cek Kesehatan Gratis (CKG)
        </a>
        <a href="pengaduan.html" style="text-decoration:none;">
          Pengaduan (SP4N-LAPOR!)
        </a>
        <a href="https://pinrangkab.go.id" target="_blank" rel="noopener noreferrer" style="text-decoration:none;opacity:0.85;">
          Portal Pemkab ↗
        </a>
      </div>
    </div>
  </div>

  <!-- SITE HEADER (STICKY HEADER DINSOS STYLE) -->
  <header class="site-header">
    <div class="container header-inner" style="min-height:76px;display:flex;align-items:center;justify-content:space-between;">
      <div class="brand">
        <a href="index.html" style="display:flex;align-items:center;gap:10px;text-decoration:none;">
          <img src="assets/logo_pinrang_opt.png" alt="Logo Pemkab Pinrang" style="height:46px;width:auto;" />
          <img src="assets/kemenkes.jpg" alt="Logo Kemenkes RI" style="height:44px;width:auto;border-radius:6px;" />
        </a>
        <a class="site-name" href="index.html" style="text-decoration:none;margin-left:4px;">
          <span style="font-size:17.5px;font-weight:800;color:#103447;line-height:1.2;display:block;">Dinas Kesehatan</span>
          <small style="font-size:11.5px;color:#087f89;font-weight:700;display:block;">Kabupaten Pinrang</small>
        </a>
      </div>

      <!-- PRIMARY NAVIGATION -->
      <nav aria-label="Navigasi utama" class="primary-nav">
        <ul class="menu" style="display:flex;align-items:center;gap:4px;list-style:none;margin:0;padding:0;">
          <li class="${page==='index'?'current-menu-item':''}"><a href="index.html">Beranda</a></li>
          <li class="${['profil','organisasi'].includes(page)?'current-menu-item':''}"><a href="profil.html">Profil Dinas</a></li>
          <li class="${['layanan','layanan-detail'].includes(page)?'current-menu-item':''}"><a href="layanan.html">Layanan</a></li>
          <li class="${['data','indikator'].includes(page)?'current-menu-item':''}"><a href="data.html">Data Kesehatan</a></li>
          <li class="${['publikasi','ppid'].includes(page)?'current-menu-item':''}"><a href="publikasi.html">Informasi Publik</a></li>
          <li class="${['berita','berita-detail'].includes(page)?'current-menu-item':''}"><a href="berita.html">Berita & Kegiatan</a></li>
          <li class="${['puskesmas','puskesmas-detail'].includes(page)?'current-menu-item':''}"><a href="puskesmas.html">19 Puskesmas</a></li>
          <li class="${page==='galeri'?'current-menu-item':''}"><a href="galeri.html">Galeri</a></li>
          <li class="${page==='kontak'?'current-menu-item':''}"><a href="kontak.html">Kontak</a></li>
        </ul>
      </nav>

      <!-- RIGHT BUTTONS -->
      <div style="display:flex;align-items:center;gap:12px;">
        <a href="pengaduan.html" class="button" style="background:#087f89;border-color:#087f89;color:#fff;padding:0.55rem 1.15rem;border-radius:9999px;font-size:0.875rem;font-weight:750;text-decoration:none;display:inline-flex;align-items:center;gap:6px;">
          ${ic('message')} Pengaduan
        </a>
        <button aria-controls="primary-menu" aria-expanded="false" class="menu-toggle" type="button" onclick="document.querySelector('.primary-nav').classList.toggle('is-open')">
          <span class="sr-only">Buka menu</span>
          <span aria-hidden="true">☰</span>
        </button>
      </div>
    </div>
  </header>
  `;
}"""

# Definisi Footer Baru (Dinsos Architecture + Dinkes Palette)
new_footer_func = """function footer() {
  return `
  <!-- FOOTER DINSOS STYLE PERSIS DENGAN WARNA DINKES -->
  <footer class="site-footer">
    <div class="footer-accent"></div>
    <div class="container footer-grid">
      
      <!-- KOLOM 1: ABOUT & IDENTITY -->
      <section class="footer-about">
        <div class="brand" style="margin-bottom:1rem;">
          <a href="index.html" style="display:flex;align-items:center;gap:8px;text-decoration:none;">
            <img src="assets/logo_pinrang_opt.png" alt="Logo Pemkab Pinrang" style="height:44px;background:#fff;border-radius:8px;padding:3px;" />
            <img src="assets/kemenkes.jpg" alt="Logo Kemenkes RI" style="height:44px;background:#fff;border-radius:8px;padding:3px;" />
          </a>
          <div class="site-name" style="margin-left:4px;">
            <span style="color:#ffffff;font-size:1.15rem;font-weight:800;display:block;">Dinas Kesehatan</span>
            <small style="color:#5eead4;font-size:0.8rem;font-weight:700;display:block;">Kabupaten Pinrang</small>
          </div>
        </div>
        <p style="font-size:0.9rem;color:#cbd5e1;line-height:1.6;margin-bottom:1rem;">
          Website resmi pusat informasi, standar pelayanan kesehatan masyarakat, edukasi promotif-preventif, dan pengaduan masyarakat Kabupaten Pinrang.
        </p>
        <p class="footer-badge" style="border-left:3px solid #0aa398;padding-left:0.85rem;color:#ffffff;font-size:0.88rem;font-weight:650;margin-bottom:1.25rem;">
          Melayani dengan sepenuh hati, mewujudkan Pinrang sehat & mandiri.
        </p>
        <div class="footer-social" style="display:flex;gap:8px;">
          <a href="https://www.instagram.com/dinkespinrang/" target="_blank" rel="noopener noreferrer" class="footer-social-btn" title="Instagram" style="width:36px;height:36px;border-radius:50%;border:1px solid rgba(255,255,255,0.25);display:flex;align-items:center;justify-content:center;color:#ffffff;">
            <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
          </a>
          <a href="https://facebook.com/dinkespinrang" target="_blank" rel="noopener noreferrer" class="footer-social-btn" title="Facebook" style="width:36px;height:36px;border-radius:50%;border:1px solid rgba(255,255,255,0.25);display:flex;align-items:center;justify-content:center;color:#ffffff;">
            <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
          </a>
          <a href="https://youtube.com/@dinkespinrang" target="_blank" rel="noopener noreferrer" class="footer-social-btn" title="YouTube" style="width:36px;height:36px;border-radius:50%;border:1px solid rgba(255,255,255,0.25);display:flex;align-items:center;justify-content:center;color:#ffffff;">
            <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19.1c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33zM9.75 15.02V8.48l5.75 3.27-5.75 3.27z"/></svg>
          </a>
        </div>
      </section>

      <!-- KOLOM 2: TAUTAN CEPAT -->
      <nav aria-labelledby="footer-links-title">
        <h2 class="footer-title" id="footer-links-title" style="font-size:1.05rem;font-weight:800;color:#ffffff;margin:0 0 1rem 0;">Tautan Cepat</h2>
        <ul style="list-style:none;padding:0;margin:0;line-height:2.1;font-size:0.92rem;">
          <li><a href="index.html" style="color:#cbd5e1;text-decoration:none;">Beranda</a></li>
          <li><a href="puskesmas.html" style="color:#cbd5e1;text-decoration:none;">Direktori 19 Puskesmas</a></li>
          <li><a href="layanan.html" style="color:#cbd5e1;text-decoration:none;">Layanan Kesehatan</a></li>
          <li><a href="berita.html" style="color:#cbd5e1;text-decoration:none;">Berita & Kegiatan</a></li>
          <li><a href="publikasi.html" style="color:#cbd5e1;text-decoration:none;">Dokumen Publik (LKjIP)</a></li>
          <li><a href="pengaduan.html" style="color:#cbd5e1;text-decoration:none;">Kontak & Pengaduan</a></li>
          <li><a href="https://www.lapor.go.id" target="_blank" rel="noopener noreferrer" style="color:#cbd5e1;text-decoration:none;">SP4N-LAPOR! ↗</a></li>
        </ul>
      </nav>

      <!-- KOLOM 3: JAM PELAYANAN -->
      <section class="footer-hours-col">
        <h2 class="footer-title" style="font-size:1.05rem;font-weight:800;color:#ffffff;margin:0 0 1rem 0;">Jam Pelayanan</h2>
        <p style="font-size:0.92rem;color:#cbd5e1;margin:0 0 0.5rem 0;">
          <strong style="color:#ffffff;display:block;">Layanan Kantor:</strong>
          Senin–Jumat, 08.00–16.00 WITA
        </p>
        <div class="footer-hours-box" style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.14);border-radius:12px;padding:12px 14px;margin-top:14px;">
          <span style="display:block;font-size:0.75rem;font-weight:800;color:#5eead4;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:2px;">
            ${ic('activity')} LAYANAN KEDARURATAN MEDIS
          </span>
          <p style="font-size:0.85rem;color:#e2e8f0;margin:0 0 6px 0;">
            IGD Puskesmas, Bersalin & Rujukan
          </p>
          <span style="display:inline-block;background:#087f89;color:#ffffff;font-size:0.78rem;font-weight:800;padding:3px 10px;border-radius:9999px;">
            24 JAM NONSTOP
          </span>
        </div>
      </section>

      <!-- KOLOM 4: HUBUNGI KAMI -->
      <section>
        <h2 class="footer-title" style="font-size:1.05rem;font-weight:800;color:#ffffff;margin:0 0 1rem 0;">Hubungi Kami</h2>
        <address style="font-style:normal;font-size:0.92rem;color:#cbd5e1;line-height:1.65;margin-bottom:1rem;">
          Jalan Jenderal Sukawati No. 40, Watang Sawitto, Kabupaten Pinrang, Sulawesi Selatan 91212
        </address>
        <div style="font-size:0.88rem;color:#cbd5e1;line-height:1.8;">
          <div><span style="color:#5eead4;font-size:0.75rem;text-transform:uppercase;font-weight:700;">TELEPON:</span> (0421) 921046</div>
          <div><span style="color:#5eead4;font-size:0.75rem;text-transform:uppercase;font-weight:700;">WHATSAPP:</span> +62 853-4217-2724</div>
          <div><span style="color:#5eead4;font-size:0.75rem;text-transform:uppercase;font-weight:700;">SUREL:</span> dinkes@pinrangkab.go.id</div>
        </div>
      </section>

      <!-- KOLOM 5: PETA GOOGLE MAPS -->
      <section class="footer-location">
        <div class="footer-map-card" style="border:1px solid rgba(255,255,255,0.2);border-radius:14px;overflow:hidden;background:rgba(255,255,255,0.06);">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3977.807897288636!2d119.64684947474443!3d-3.7925019961814674!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2d95b5839ce6b251%3A0xe5a22bb0752179e8!2sDinas%20Kesehatan%20Kabupaten%20Pinrang!5e0!3m2!1sid!2sid!4v1709123456789!5m2!1sid!2sid" 
                  width="100%" height="145" style="border:0;display:block;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Peta Lokasi Kantor Dinas Kesehatan Pinrang"></iframe>
          <div style="padding:10px 14px;font-size:0.85rem;">
            <strong style="color:#ffffff;display:block;">Dinas Kesehatan Kab. Pinrang</strong>
            <small style="color:#94a3b8;display:block;margin-bottom:6px;">Jl. Jenderal Sukawati No. 40, Pinrang</small>
            <a href="https://maps.google.com/?q=Dinas+Kesehatan+Kabupaten+Pinrang" target="_blank" rel="noopener noreferrer" style="color:#5eead4;text-decoration:none;font-weight:750;display:inline-flex;align-items:center;gap:4px;">
              Buka di Google Maps →
            </a>
          </div>
        </div>
      </section>
    </div>

    <!-- FOOTER BOTTOM -->
    <div class="container footer-bottom" style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid rgba(255,255,255,0.15);padding-block:1.25rem;font-size:0.85rem;color:#94a3b8;flex-wrap:wrap;gap:12px;">
      <div>
        © 2026 Dinas Kesehatan Kabupaten Pinrang · Made with ♥ by <a href="https://maroamedia.web.app/" target="_blank" rel="noopener noreferrer" style="color:#5eead4;text-decoration:none;font-weight:700;">MAROA Project</a>
      </div>
      <div style="display:flex;gap:16px;">
        <a href="privasi.html" style="color:#cbd5e1;text-decoration:none;">Kebijakan Privasi</a>
        <a href="aksesibilitas.html" style="color:#cbd5e1;text-decoration:none;">Aksesibilitas</a>
        <a href="pengaduan.html" style="color:#cbd5e1;text-decoration:none;">Pengaduan</a>
      </div>
    </div>
  </footer>

  <!-- MOBILE DOCK BAR MELAYANG (PERSIS DINSOS PINRANG) -->
  <nav aria-label="Navigasi mobile" class="mobile-dock">
    <a href="index.html">
      <span aria-hidden="true" class="dock-icon">${ic('home')}</span>
      <span>Beranda</span>
    </a>
    <a href="layanan.html">
      <span aria-hidden="true" class="dock-icon">${ic('layers')}</span>
      <span>Layanan</span>
    </a>
    <a href="berita.html?q=">
      <span aria-hidden="true" class="dock-icon">${ic('search')}</span>
      <span>Cari</span>
    </a>
    <a href="puskesmas.html">
      <span aria-hidden="true" class="dock-icon">${ic('hospital')}</span>
      <span>Puskesmas</span>
    </a>
    <a class="dock-emphasis" href="pengaduan.html">
      <span aria-hidden="true" class="dock-icon dock-icon--alert">${ic('phone')}</span>
      <span>Pengaduan</span>
    </a>
  </nav>

  <!-- TOMBOL MELAYANG BACK TO TOP -->
  <button type="button" id="backToTopBtn" aria-label="Kembali ke atas" onclick="window.scrollTo({top:0,behavior:'smooth'})" 
          style="display:none;position:fixed;bottom:80px;right:22px;z-index:9999;width:44px;height:44px;border-radius:50%;background:#087f89;color:#ffffff;border:none;box-shadow:0 8px 24px rgba(8,127,137,0.35);cursor:pointer;align-items:center;justify-content:center;transition:all .3s ease;">
    <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="m18 15-6-6-6 6"/></svg>
  </button>
  `;
}"""

# Definisi HomePage Baru (Dinsos Architecture + Dinkes Palette)
new_homepage_func = """function homePage() {
  const articles = window.ARTICLES_CACHE || [];
  const latestNews = articles.slice(0, 3);
  
  return `
  <!-- 1. HERO SECTION (PERSIS DINSOS STYLE DENGAN WARNA DINKES) -->
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
          Informasi pelayanan kesehatan masyarakat, rekomendasi perizinan nakes & pangan, integrasi 19 UPTD Puskesmas, serta pencegahan penyakit Kabupaten Pinrang yang dihadirkan secara profesional, cepat, dan bermartabat.
        </p>
        
        <!-- INTEGRATED SEARCH FORM -->
        <form action="berita.html" class="hero-search-mockup" method="get" role="search">
          <label class="sr-only" for="hero-search-input">Cari layanan kesehatan atau puskesmas</label>
          <input id="hero-search-input" name="q" placeholder="Cari layanan yang Anda butuhkan (contoh: CKG, SIP Nakes, Puskesmas, Stunting...)" type="search" />
          <button aria-label="Cari" type="submit">
            <svg aria-hidden="true" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 24 24" width="20">
              <circle cx="11" cy="11" r="8"></circle>
              <path d="m21 21-4.35-4.35"></path>
            </svg>
          </button>
        </form>
      </div>

      <!-- HERO VISUAL MONTAGE DINKES -->
      <div class="hero-visual-col">
        <figure class="hero-illustration hero-illustration--mockup">
          <img src="assets/hero_illustration_dinkes.png" alt="Dinas Kesehatan Pemerintah Kabupaten Pinrang" style="max-height:490px;width:auto;margin:0 auto;display:block;" />
        </figure>
      </div>
    </div>
  </section>

  <!-- 2. QUICK ACCESS CARDS MELAYANG (PERSIS DINSOS STYLE) -->
  <section class="quick-access-mockup">
    <div class="container">
      <div class="quick-grid-mockup">
        <a href="layanan-detail.html" class="quick-access-card">
          <div class="quick-access-icon" style="background:#e6f7f5;color:#087f89;">
            ${ic('heart')}
          </div>
          <div class="quick-access-content">
            <h4>Cek Kesehatan (CKG)</h4>
            <p>Skrining riwayat kesehatan berkala gratis di 19 Puskesmas.</p>
          </div>
          <span class="quick-access-arrow">›</span>
        </a>

        <a href="puskesmas.html" class="quick-access-card">
          <div class="quick-access-icon" style="background:#ecfdf5;color:#047857;">
            <img src="assets/puskesmas.png" alt="Logo Puskesmas" style="width:28px;height:28px;object-fit:contain;" />
          </div>
          <div class="quick-access-content">
            <h4>19 UPTD Puskesmas</h4>
            <p>Lokasi, kontak IGD 24 Jam, dan profil dokter penanggung jawab.</p>
          </div>
          <span class="quick-access-arrow">›</span>
        </a>

        <a href="layanan-detail.html" class="quick-access-card">
          <div class="quick-access-icon" style="background:#fffbeb;color:#b45309;">
            ${ic('file')}
          </div>
          <div class="quick-access-content">
            <h4>SIP & SIK Nakes</h4>
            <p>Rekomendasi surat izin praktik tenaga medis & perawat online.</p>
          </div>
          <span class="quick-access-arrow">›</span>
        </a>

        <a href="pengaduan.html" class="quick-access-card">
          <div class="quick-access-icon" style="background:#f0fdf9;color:#059669;">
            ${ic('phone')}
          </div>
          <div class="quick-access-content">
            <h4>PSC 119 & Aduan</h4>
            <p>Kedaruratan medis 24 Jam & kanal resmi SP4N-LAPOR!.</p>
          </div>
          <span class="quick-access-arrow">›</span>
        </a>
      </div>
    </div>
  </section>

  <!-- 3. LAYANAN UTAMA SECTION (PERSIS GRID & CARD DINSOS STYLE) -->
  <section class="section section-services-mockup">
    <div class="container">
      <div class="section-head--mockup">
        <div>
          <h2 class="section-title-mockup">Layanan Utama</h2>
          <p class="section-sub-mockup">Akses layanan kesehatan Dinas Kesehatan Kabupaten Pinrang dengan mudah dan cepat.</p>
        </div>
        <a href="layanan.html" class="text-link" style="color:#087f89;font-weight:750;text-decoration:none;display:inline-flex;align-items:center;gap:6px;">
          Lihat semua layanan →
        </a>
      </div>

      <div class="service-grid--mockup">
        
        <!-- CARD 1: PUSKESMAS -->
        <article class="service-card--mockup">
          <div class="card-media" style="aspect-ratio:16/10;border-radius:12px;overflow:hidden;margin-bottom:1.25rem;background:#e2f4f2;">
            <img src="assets/kantor_dinkes_pinrang.jpg" alt="Pelayanan 19 UPTD Puskesmas" style="width:100%;height:100%;object-fit:cover;" />
          </div>
          <span class="service-badge-mockup">PELAYANAN KESEHATAN PRIMER</span>
          <h3><a href="puskesmas.html">Pelayanan 19 UPTD Puskesmas</a></h3>
          <p>Pelayanan rawat jalan, rawat inap, persalinan 24 Jam, poli umum, KIA, gigi, laboratorium, dan imunisasi di 12 kecamatan se-Kabupaten Pinrang.</p>
          <div class="service-pill-row">
            <span class="pill-free">Gratis / tidak dipungut biaya</span>
            <span class="pill-verify">Siaga 24 Jam (IGD)</span>
          </div>
          <div class="service-card-footer">
            <a href="puskesmas.html" class="text-link" style="color:#087f89;font-weight:750;text-decoration:none;">Lihat layanan →</a>
          </div>
        </article>

        <!-- CARD 2: SIP & SIK NAKES -->
        <article class="service-card--mockup">
          <div class="card-media" style="aspect-ratio:16/10;border-radius:12px;overflow:hidden;margin-bottom:1.25rem;background:#e2f4f2;">
            <img src="assets/galeri/struktur_organisasi_dinkes.jpeg" alt="Penerbitan Rekomendasi SIP & SIK Nakes" style="width:100%;height:100%;object-fit:cover;" />
          </div>
          <span class="service-badge-mockup">SUMBER DAYA KESEHATAN (SDK)</span>
          <h3><a href="layanan-detail.html">Rekomendasi SIP & SIK Nakes</a></h3>
          <p>Penerbitan surat rekomendasi izin praktik dokter, perawat, bidan, apoteker, dan tenaga kesehatan secara transparan dan akuntabel.</p>
          <div class="service-pill-row">
            <span class="pill-free">Gratis / tidak dipungut biaya</span>
            <span class="pill-verify">Perlu Verifikasi Persyaratan</span>
          </div>
          <div class="service-card-footer">
            <a href="layanan-detail.html" class="text-link" style="color:#087f89;font-weight:750;text-decoration:none;">Lihat layanan →</a>
          </div>
        </article>

        <!-- CARD 3: SPP-IRT PANGAN -->
        <article class="service-card--mockup">
          <div class="card-media" style="aspect-ratio:16/10;border-radius:12px;overflow:hidden;margin-bottom:1.25rem;background:#e2f4f2;">
            <img src="assets/galeri/ea1473c4-840a-4595-b375-61e9c0030936.jpeg" alt="Sertifikasi Pangan Industri Rumah Tangga" style="width:100%;height:100%;object-fit:cover;" />
          </div>
          <span class="service-badge-mockup">KEFARMASIAN & KEAMANAN PANGAN</span>
          <h3><a href="layanan-detail.html">Sertifikasi Pangan (SPP-IRT)</a></h3>
          <p>Penyuluhan keamanan pangan dan penerbitan sertifikat pemenuhan komitmen produksi pangan olahan industri rumah tangga agar aman konsumsi.</p>
          <div class="service-pill-row">
            <span class="pill-free">Gratis / tidak dipungut biaya</span>
            <span class="pill-verify">Perlu Verifikasi Persyaratan</span>
          </div>
          <div class="service-card-footer">
            <a href="layanan-detail.html" class="text-link" style="color:#087f89;font-weight:750;text-decoration:none;">Lihat layanan →</a>
          </div>
        </article>

        <!-- CARD 4: CEK KESEHATAN GRATIS -->
        <article class="service-card--mockup">
          <div class="card-media" style="aspect-ratio:16/10;border-radius:12px;overflow:hidden;margin-bottom:1.25rem;background:#e2f4f2;">
            <img src="assets/galeri/cbe0e611-4ec4-4b64-b3ca-7fce94ef85a7.jpeg" alt="Cek Kesehatan Gratis CKG" style="width:100%;height:100%;object-fit:cover;" />
          </div>
          <span class="service-badge-mockup">DETEKSI DINI & PREVENTIF</span>
          <h3><a href="layanan-detail.html">Cek Kesehatan Gratis (CKG)</a></h3>
          <p>Skrining kesehatan berkala meliputi tekanan darah, gula darah, deteksi dini faktor risiko penyakit tidak menular (PTM) di faskes primer.</p>
          <div class="service-pill-row">
            <span class="pill-free">Gratis / tidak dipungut biaya</span>
            <span class="pill-verify">Tanpa Syarat Rumit</span>
          </div>
          <div class="service-card-footer">
            <a href="layanan-detail.html" class="text-link" style="color:#087f89;font-weight:750;text-decoration:none;">Lihat layanan →</a>
          </div>
        </article>

        <!-- CARD 5: STUNTING & IMUNISASI -->
        <article class="service-card--mockup">
          <div class="card-media" style="aspect-ratio:16/10;border-radius:12px;overflow:hidden;margin-bottom:1.25rem;background:#e2f4f2;">
            <img src="assets/galeri/poster-stunting-64742fd008a8b563763892c2.jpeg" alt="Pencegahan Stunting dan Imunisasi" style="width:100%;height:100%;object-fit:cover;" />
          </div>
          <span class="service-badge-mockup">KESEHATAN MASYARAKAT & GIZI</span>
          <h3><a href="edukasi.html">Pencegahan Stunting & Imunisasi</a></h3>
          <p>Pemantauan rutin tumbuh kembang balita, imunisasi dasar lengkap, intervensi gizi terpadu, dan edukasi pola hidup bersih sehat di Posyandu.</p>
          <div class="service-pill-row">
            <span class="pill-free">Gratis / tidak dipungut biaya</span>
            <span class="pill-verify">Prioritas Nasional</span>
          </div>
          <div class="service-card-footer">
            <a href="edukasi.html" class="text-link" style="color:#087f89;font-weight:750;text-decoration:none;">Lihat layanan →</a>
          </div>
        </article>

        <!-- CARD 6: PSC 119 EMERGENCY -->
        <article class="service-card--mockup">
          <div class="card-media" style="aspect-ratio:16/10;border-radius:12px;overflow:hidden;margin-bottom:1.25rem;background:#e2f4f2;">
            <img src="assets/galeri/Biru-Oranye-Modern-Informasi-Darurat-Instagram-Post.png" alt="Layanan Kedaruratan Medis PSC 119" style="width:100%;height:100%;object-fit:cover;" />
          </div>
          <span class="service-badge-mockup">PENANGANAN KEGAWATDARURATAN</span>
          <h3><a href="pengaduan.html">Layanan Darurat Medis PSC 119</a></h3>
          <p>Pelayanan penjemputan ambulans darurat, pertolongan pertama kecelakaan, evakuasi medis, serta koordinasi rujukan pra-rumah sakit 24 Jam.</p>
          <div class="service-pill-row">
            <span class="pill-free">Gratis / tidak dipungut biaya</span>
            <span class="pill-verify">Siaga 24 Jam Nonstop</span>
          </div>
          <div class="service-card-footer">
            <a href="pengaduan.html" class="text-link" style="color:#087f89;font-weight:750;text-decoration:none;">Lihat layanan →</a>
          </div>
        </article>

      </div>
    </div>
  </section>

  <!-- 4. ALERT BANNER SECTION (PERSIS DINSOS STYLE) -->
  <section class="alert-mockup-section">
    <div class="container">
      <div class="alert-mockup-card">
        <div class="alert-mockup-left">
          <div class="alert-mockup-icon">
            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M18 8a6 6 0 1 0-12 0c0 7-3 7-3 9h18c0-2-3-2-3-9Z"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
          </div>
          <div>
            <span class="alert-mockup-title">Waspada Pungutan Liar & Penipuan!</span>
            <p class="alert-mockup-text">Seluruh penerbitan surat rekomendasi perizinan nakes dan layanan publik Dinas Kesehatan Kabupaten Pinrang tidak dipungut biaya ilegal. Laporkan jika ada oknum yang meminta imbalan.</p>
          </div>
        </div>
        <a href="pengaduan.html" class="alert-mockup-btn">
          Laporkan Sekarang ›
        </a>
      </div>
    </div>
  </section>

  <!-- 5. INFORMASI TERBARU & DOKUMEN PUBLIK (PERSIS 2 KOLOM DINSOS) -->
  <section class="section home-info-mockup-section">
    <div class="container">
      <div class="home-info-mockup-grid">
        
        <!-- SISI KIRI: INFORMASI TERBARU -->
        <div>
          <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:1.5rem;flex-wrap:wrap;gap:10px;">
            <h2 class="section-title-mockup" style="margin:0;">Informasi Terbaru</h2>
            <a href="berita.html" class="text-link" style="color:#087f89;font-weight:750;text-decoration:none;">Lihat semua berita →</a>
          </div>

          <div class="news-list-wrap">
            ${latestNews.map(item => `
              <article class="news-item-mockup">
                <a href="berita-detail.html?id=${item.id}" class="news-item-mockup-thumb">
                  <img src="${getSafeImageUrl(item.featured_image)}" alt="${item.title}" />
                </a>
                <div class="news-item-mockup-content">
                  <h3 class="news-item-mockup-title">
                    <a href="berita-detail.html?id=${item.id}">${item.title}</a>
                  </h3>
                  <p class="news-item-mockup-excerpt">
                    ${item.excerpt ? item.excerpt.slice(0, 110) + '...' : 'Informasi dan dokumentasi publikasi resmi Dinas Kesehatan Pemerintah Kabupaten Pinrang.'}
                  </p>
                  <div class="news-item-mockup-meta">
                    <span>${ic('calendar')} ${item.published_at || 'Terbaru'}</span>
                    <span>${ic('user')} ${item.author || 'Dinkes'}</span>
                  </div>
                </div>
              </article>
            `).join('')}
          </div>
        </div>

        <!-- SISI KANAN: DOKUMEN PUBLIK & SURVEI KEPUASAN -->
        <div>
          <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:1.5rem;flex-wrap:wrap;gap:10px;">
            <h2 class="section-title-mockup" style="margin:0;">Dokumen Publik</h2>
            <a href="publikasi.html" class="text-link" style="color:#087f89;font-weight:750;text-decoration:none;">Lihat semua dokumen →</a>
          </div>

          <!-- KARTU DOKUMEN DOWNLOAD -->
          <div class="doc-list-wrap">
            
            <div class="doc-card-mockup">
              <div style="width:40px;height:40px;border-radius:10px;background:#fef2f2;color:#ef4444;display:flex;align-items:center;justify-content:center;flex-shrink:0;">
                <svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6M8 13h8M8 17h8"/></svg>
              </div>
              <div style="flex-grow:1;">
                <strong style="font-size:0.92rem;color:#103447;display:block;line-height:1.35;margin-bottom:2px;">
                  Laporan Kinerja Instansi Pemerintah (LKjIP) Tahun 2026
                </strong>
                <span style="font-size:0.75rem;color:#94a3b8;">PDF · 1.8 MB · Diterbitkan Dinkes Pinrang</span>
              </div>
              <a href="publikasi.html" aria-label="Unduh Dokumen LKjIP" style="width:36px;height:36px;border-radius:8px;background:#e6f7f5;color:#087f89;display:flex;align-items:center;justify-content:center;text-decoration:none;">
                <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              </a>
            </div>

            <div class="doc-card-mockup">
              <div style="width:40px;height:40px;border-radius:10px;background:#fef2f2;color:#ef4444;display:flex;align-items:center;justify-content:center;flex-shrink:0;">
                <svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6M8 13h8M8 17h8"/></svg>
              </div>
              <div style="flex-grow:1;">
                <strong style="font-size:0.92rem;color:#103447;display:block;line-height:1.35;margin-bottom:2px;">
                  Rencana Strategis & Indikator Kinerja Utama (IKU)
                </strong>
                <span style="font-size:0.75rem;color:#94a3b8;">PDF · 2.1 MB · Dokumen Kebijakan Daerah</span>
              </div>
              <a href="publikasi.html" aria-label="Unduh Dokumen Renstra" style="width:36px;height:36px;border-radius:8px;background:#e6f7f5;color:#087f89;display:flex;align-items:center;justify-content:center;text-decoration:none;">
                <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              </a>
            </div>

            <div class="doc-card-mockup">
              <div style="width:40px;height:40px;border-radius:10px;background:#fef2f2;color:#ef4444;display:flex;align-items:center;justify-content:center;flex-shrink:0;">
                <svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6M8 13h8M8 17h8"/></svg>
              </div>
              <div style="flex-grow:1;">
                <strong style="font-size:0.92rem;color:#103447;display:block;line-height:1.35;margin-bottom:2px;">
                  Standar Pelayanan Publik & SOP Rekomendasi SIP
                </strong>
                <span style="font-size:0.75rem;color:#94a3b8;">PDF · 920 KB · Maklumat Pelayanan</span>
              </div>
              <a href="publikasi.html" aria-label="Unduh SOP Pelayanan" style="width:36px;height:36px;border-radius:8px;background:#e6f7f5;color:#087f89;display:flex;align-items:center;justify-content:center;text-decoration:none;">
                <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              </a>
            </div>

          </div>

          <!-- BANNER SURVEI KEPUASAN MASYARAKAT (SKM) PERSIS SEPERTI DINSOS -->
          <div style="background:#ffffff;border:1px solid #dce8eb;border-radius:16px;overflow:hidden;box-shadow:0 4px 16px rgba(16,52,71,0.04);margin-top:1.25rem;">
            <div style="padding:14px 18px;border-bottom:1px solid #f1f5f9;font-size:0.8rem;font-weight:800;color:#087f89;display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:0.05em;">
              ${ic('check')} SURVEI KEPUASAN MASYARAKAT (SKM)
            </div>
            <div style="padding:16px;background:linear-gradient(135deg, #087f89 0%, #103447 100%);color:#ffffff;">
              <span style="font-size:11px;font-weight:800;letter-spacing:0.08em;color:#5eead4;text-transform:uppercase;">EVALUASI PELAYANAN PUBLIK 2026</span>
              <h4 style="font-size:16px;font-weight:800;color:#ffffff;margin:4px 0 8px 0;line-height:1.35;">Bantu Tingkatkan Mutu Layanan Kesehatan Kami</h4>
              <p style="font-size:13px;color:#d1e7f7;margin:0 0 14px 0;line-height:1.5;">Partisipasi Anda dalam pengisian kuesioner SKM sangat berharga untuk transparansi dan integritas Dinas Kesehatan Pinrang.</p>
              <a href="skm.html" class="button" style="background:#ffffff;color:#087f89;font-weight:800;font-size:13px;padding:8px 18px;border-radius:9999px;text-decoration:none;display:inline-flex;align-items:center;gap:6px;">
                Beri Penilaian via Kuesioner ↗
              </a>
            </div>
          </div>

        </div>

      </div>
    </div>
  </section>

  <!-- 6. KEMITRAAN & PILAR KESEHATAN (PERSIS SEPERTI PSKS SECTION DINSOS) -->
  <section class="psks-section">
    <div class="container">
      <div class="psks-header">
        <span class="psks-badge-pill">
          <span class="psks-badge-dot"></span>
          KEMITRAAN & PILAR KESEHATAN DAERAH
        </span>
        <h2 class="psks-title">Pilar Transformasi Layanan Kesehatan</h2>
        <p class="psks-lead">
          Pilar pelayanan, pencegahan, dan kesiapsiagaan medis masyarakat yang berada di bawah koordinasi dan binaan Dinas Kesehatan Kabupaten Pinrang dalam mewujudkan derajat kesehatan yang optimal, merata, dan bermartabat.
        </p>
      </div>

      <div class="psks-grid">
        
        <!-- PILAR 1: 19 PUSKESMAS -->
        <article class="psks-card psks-card--tksk">
          <div class="psks-card-top">
            <a href="puskesmas.html" class="psks-logo-wrapper">
              <img src="assets/puskesmas.png" alt="Logo UPTD Puskesmas" class="psks-logo-img" />
            </a>
            <span class="psks-pill-badge">12 Kecamatan di Kab. Pinrang</span>
          </div>
          <div class="psks-card-body">
            <h3 class="psks-card-title"><a href="puskesmas.html">19 UPTD Puskesmas</a></h3>
            <span class="psks-card-subtitle">Fasilitas Pelayanan Kesehatan Primer</span>
            <p class="psks-card-desc">
              Jaringan fasilitas kesehatan tingkat pertama yang menyelenggarakan rawat jalan, rawat inap, poli KIA, laboratorium, dan IGD 24 Jam di seluruh kecamatan Kabupaten Pinrang.
            </p>
            <div class="psks-card-footer">
              <a href="puskesmas.html" class="psks-action-btn">
                <span>Profil & 19 Puskesmas</span>
                <span class="psks-arrow-icon">→</span>
              </a>
            </div>
          </div>
        </article>

        <!-- PILAR 2: GERMAS -->
        <article class="psks-card psks-card--pkh">
          <div class="psks-card-top">
            <a href="edukasi.html" class="psks-logo-wrapper">
              <img src="assets/kemenkes.jpg" alt="Logo Kemenkes GERMAS" class="psks-logo-img" style="border-radius:10px;" />
            </a>
            <span class="psks-pill-badge">Promosi & Deteksi Dini</span>
          </div>
          <div class="psks-card-body">
            <h3 class="psks-card-title"><a href="edukasi.html">GERMAS Pinrang</a></h3>
            <span class="psks-card-subtitle">Gerakan Masyarakat Hidup Sehat</span>
            <p class="psks-card-desc">
              Pemberdayaan masyarakat melalui aktivitas fisik teratur, konsumsi buah dan sayur, pemeriksaan kesehatan berkala, serta komitmen 100% Bebas Buang Air Besar Sembarangan (ODF).
            </p>
            <div class="psks-card-footer">
              <a href="edukasi.html" class="psks-action-btn">
                <span>Aksi & Kampanye GERMAS</span>
                <span class="psks-arrow-icon">→</span>
              </a>
            </div>
          </div>
        </article>

        <!-- PILAR 3: PSC 119 EMERGENCY -->
        <article class="psks-card psks-card--tagana">
          <div class="psks-card-top">
            <a href="pengaduan.html" class="psks-logo-wrapper">
              <img src="assets/galeri/Biru-Oranye-Modern-Informasi-Darurat-Instagram-Post.png" alt="Logo PSC 119 Emergency" class="psks-logo-img" />
            </a>
            <span class="psks-pill-badge">Tanggap Darurat 24 Jam</span>
          </div>
          <div class="psks-card-body">
            <h3 class="psks-card-title"><a href="pengaduan.html">PSC 119 Pinrang</a></h3>
            <span class="psks-card-subtitle">Public Safety Center & Rujukan Cepat</span>
            <p class="psks-card-desc">
              Layanan reaksi cepat penanganan kegawatdaruratan medis, evakuasi korban kecelakaan, armada ambulans siaga, dan koordinasi terpadu antar fasilitas rujukan daerah.
            </p>
            <div class="psks-card-footer">
              <a href="pengaduan.html" class="psks-action-btn">
                <span>Kesiapsiagaan PSC 119</span>
                <span class="psks-arrow-icon">→</span>
              </a>
            </div>
          </div>
        </article>

      </div>
    </div>
  </section>
  `;
}"""

# Fungsi pengganti di script
def replace_func(source, func_name, new_func_code):
    pos = source.find('function ' + func_name + '(')
    if pos == -1:
        print(f"Error: function {func_name} tidak ditemukan!")
        return source
    open_b = source.find('{', pos)
    count = 1
    i = open_b + 1
    while i < len(source) and count > 0:
        if source[i] == '{':
            count += 1
        elif source[i] == '}':
            count -= 1
        i += 1
    print(f"Mengganti function {func_name} (pos {pos} sampai {i})...")
    return source[:pos] + new_func_code + source[i:]

code = replace_func(code, 'header', new_header_func)
code = replace_func(code, 'footer', new_footer_func)
code = replace_func(code, 'homePage', new_homepage_func)

with open('public/assets/app.v4.js', 'w', encoding='utf-8') as f:
    f.write(code)
print("Berhasil memperbarui public/assets/app.v4.js!")

with open('public/assets/app.js', 'w', encoding='utf-8') as f:
    f.write(code)
print("Berhasil menyinkronkan ke public/assets/app.js!")
