# -*- coding: utf-8 -*-
import sys, io

with open('public/assets/app.v4.js', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = 'function header(page) {'
end_marker = 'function footer() {'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

print(f'start_idx: {start_idx}, end_idx: {end_idx}')

NEW_HEADER = '''function header(page) {
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
}

'''

text = text[:start_idx] + NEW_HEADER + text[end_idx:]

with open('public/assets/app.v4.js', 'w', encoding='utf-8') as f:
    f.write(text)

with open('public/assets/app.js', 'w', encoding='utf-8') as f:
    f.write(text)

print('Selesai mereplace header() di app.v4.js dan app.js!')
