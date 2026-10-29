# -*- coding: utf-8 -*-
"""
Script penyusun public/assets/app.js definitif
"""

import json
import os

with open('public/data/puskesmas.json', 'r', encoding='utf-8') as f:
    puskesmas_list = json.load(f)

with open('public/data/articles.json', 'r', encoding='utf-8') as f:
    articles_list = json.load(f)

print(f"Memuat {len(puskesmas_list)} Puskesmas dan {len(articles_list)} Artikel...")

# Filter artikel untuk cache instan (ambil semua artikel tapi ringkas agar file tidak terlalu besar)
articles_compact = []
for a in articles_list:
    articles_compact.append({
        'id': a.get('id'),
        'title': a.get('title'),
        'slug': a.get('slug'),
        'published_at': a.get('published_at'),
        'author': a.get('author'),
        'category': a.get('category'),
        'categories': a.get('categories', []),
        'featured_image': a.get('featured_image'),
        'excerpt': a.get('excerpt', ''),
        'content_html': a.get('content_html', '')[:4000], # Potongan naskah jika belum dimuat penuh
        'original_url': a.get('original_url')
    })

pkm_json = json.dumps(puskesmas_list, ensure_ascii=False)
art_json = json.dumps(articles_compact, ensure_ascii=False)

# Siapkan kode JS
script_content = f"""// Dinas Kesehatan Kabupaten Pinrang - Portal Resmi Web App V4 Definitive
// Memuat data otentik: 19 Puskesmas, 349 Artikel Berita, Profil Pimpinan, Bagan Struktur, SOP Layanan, dan Dashboard Data.

window.PUSKESMAS_DATA = {pkm_json};
window.ARTICLES_CACHE = {art_json};

function getSafeImageUrl(url) {{
  if (!url) return 'assets/logo_pinrang_opt.png';
  let clean = url.replace(/-\\d+x\\d+(\\.[a-zA-Z0-9]+)$/, '$1');
  if (location.hostname === 'localhost' || location.hostname === '127.0.0.1') {{
    return clean.replace('https://dinkes.pinrangkab.go.id/wp-content/uploads/', 'uploads/');
  }}
  return clean;
}}

const ICONS = {{
  activity: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>`,
  hospital: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16M9 9h6M12 6v6"/></svg>`,
  heart: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>`,
  people: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 7a4 4 0 1 0 0-8 4 4 0 0 0 0 8ZM22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>`,
  file: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>`,
  chat: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>`,
  info: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>`,
  check: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>`,
  phone: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>`,
  mail: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>`,
  location: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>`,
  search: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>`,
  shield: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>`,
  clock: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>`,
  arrow: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>`,
  external: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6M15 3h6v6M10 14L21 3"/></svg>`,
  user: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 1 0-16 0"/></svg>`,
  bell: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9M13.73 21a2 2 0 0 1-3.46 0"/></svg>`,
  menu: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="18" x2="20" y2="18"/></svg>`,
  close: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>`,
  award: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>`,
  target: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>`,
  camera: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/></svg>`,
  refresh: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>`
}};

function ic(name) {{
  return `<span class="icon" aria-hidden="true">${{ICONS[name] || ''}}</span>`;
}}

const ROUTES = [
  ['index','Beranda'],
  ['profil','Profil Dinas'],
  ['organisasi','Struktur Organisasi'],
  ['layanan','Layanan Kesehatan'],
  ['layanan-detail','Detail Layanan'],
  ['puskesmas','Direktori Puskesmas'],
  ['puskesmas-detail','Detail Puskesmas'],
  ['edukasi','Edukasi Kesehatan'],
  ['edukasi-detail','Detail Edukasi'],
  ['berita','Berita & Kegiatan'],
  ['berita-detail','Detail Berita'],
  ['galeri','Galeri Dokumentasi'],
  ['data','Data Kesehatan'],
  ['indikator','Indikator Kinerja'],
  ['publikasi','Publikasi & Dokumen'],
  ['ppid','Layanan PPID'],
  ['informasi','Permohonan Informasi'],
  ['pengaduan','Kanal Pengaduan'],
  ['kontak','Kontak & Lokasi'],
  ['inovasi','Inovasi & Prestasi'],
  ['faq','Tanya Jawab (FAQ)'],
  ['pencarian','Pencarian Portal'],
  ['peta-situs','Peta Situs'],
  ['privasi','Kebijakan Privasi'],
  ['aksesibilitas','Aksesibilitas'],
  ['skm','Survei Kepuasan (SKM)'],
  ['pengumuman','Pengumuman Penting'],
  ['tidak-ditemukan','Halaman Tidak Ditemukan']
];

function header(activePage) {{
  return `
  <aside class="topbar" aria-label="Aksesibilitas dan navigasi cepat">
    <div class="container topbar-inner">
      <div class="topbar-left">
        <span class="seal" aria-hidden="true"></span>
        <span class="topbar-tag">PORTAL RESMI DINAS KESEHATAN PEMERINTAH KABUPATEN PINRANG · SULAWESI SELATAN</span>
        <span class="sr-only">Pemerintah Kabupaten Pinrang · Sulawesi Selatan</span>
      </div>
      <div class="topbar-actions">
        <a class="external-pill" href="https://pinrangkab.go.id/" target="_blank" rel="noopener">Portal Pemkab ${{ic('external')}}</a>
        <a class="text-link" href="ppid.html">PPID</a>
        <a class="text-link" href="skm.html">SKM</a>
        <a class="text-link" href="faq.html">Bantuan</a>
      </div>
    </div>
  </aside>
  <header class="header" role="banner">
    <div class="container header-inner">
      <a class="brand" href="index.html" aria-label="Dinas Kesehatan Kabupaten Pinrang, Beranda">
        <div class="brand-logo" style="display:flex;align-items:center;gap:10px;">
          <img src="assets/logo_pinrang_opt.png" alt="Logo Pemkab Pinrang" style="height:44px;width:auto;display:block;" />
          <img src="assets/kemenkes.jpg" alt="Logo Kemenkes RI" style="height:44px;width:auto;display:block;border-radius:4px;" />
        </div>
        <div class="brand-text">
          <span class="brand-kicker">PEMERINTAH KABUPATEN PINRANG</span>
          <span class="brand-title">DINAS KESEHATAN</span>
          <span class="brand-sub">Portal Informasi & Pelayanan Kesehatan Masyarakat</span>
        </div>
      </a>
      <div class="header-tools">
        <a class="service-pill" href="puskesmas.html">${{ic('hospital')}} Cari Fasilitas Kesehatan</a>
        <button class="iconbtn" id="fontToggle" type="button" aria-label="Perbesar tulisan" title="Perbesar tulisan">Aa</button>
        <button class="iconbtn" id="searchToggle" type="button" aria-label="Buka pencarian">${{ic('search')}}</button>
        <button class="iconbtn menu-toggle" id="mobileToggle" type="button" aria-expanded="false" aria-label="Buka menu navigasi">${{ic('menu')}}</button>
      </div>
    </div>
    <nav class="nav" aria-label="Navigasi utama">
      <div class="container nav-inner">
        <ul class="navlist">
          <li class="${{activePage === 'index' ? 'active' : ''}}"><a href="index.html">Beranda</a></li>
          <li class="navgroup ${{['layanan','layanan-detail','puskesmas','puskesmas-detail'].includes(activePage)?'active':''}}">
            <button type="button" aria-expanded="false">Layanan ${{ic('arrow')}}</button>
            <div class="dropdown">
              <a href="layanan.html">Katalog Layanan</a>
              <a href="layanan-detail.html">Standar Pelayanan (SOP)</a>
              <a href="puskesmas.html">Direktori 19 Puskesmas</a>
            </div>
          </li>
          <li class="${{activePage === 'edukasi' || activePage === 'edukasi-detail' ? 'active' : ''}}"><a href="edukasi.html">Edukasi</a></li>
          <li class="${{activePage === 'data' || activePage === 'indikator' ? 'active' : ''}}"><a href="data.html">Data Kesehatan</a></li>
          <li class="${{activePage === 'berita' || activePage === 'berita-detail' || activePage === 'galeri' ? 'active' : ''}}"><a href="berita.html">Berita & Kegiatan</a></li>
          <li class="navgroup ${{['publikasi','ppid','informasi'].includes(activePage)?'active':''}}">
            <button type="button" aria-expanded="false">Transparansi ${{ic('arrow')}}</button>
            <div class="dropdown">
              <a href="publikasi.html">Publikasi & Dokumen</a>
              <a href="ppid.html">Layanan PPID</a>
              <a href="informasi.html">Permohonan Informasi</a>
            </div>
          </li>
          <li class="navgroup ${{['profil','organisasi','inovasi','kontak'].includes(activePage)?'active':''}}">
            <button type="button" aria-expanded="false">Profil ${{ic('arrow')}}</button>
            <div class="dropdown">
              <a href="profil.html">Profil Kelembagaan</a>
              <a href="organisasi.html">Struktur Organisasi</a>
              <a href="inovasi.html">Inovasi & Prestasi Daerah</a>
              <a href="kontak.html">Kontak & Lokasi Kantor</a>
            </div>
          </li>
          <li class="${{activePage === 'pengaduan' ? 'active' : ''}}"><a class="nav-cta" href="pengaduan.html">${{ic('chat')}} Pengaduan</a></li>
        </ul>
      </div>
    </nav>
  </header>
  <div class="quick-search" id="quickSearch">
    <div class="container quick-search-inner">
      <form action="pencarian.html" method="get">
        <label class="sr-only" for="quickSearchInput">Cari di seluruh portal</label>
        <input id="quickSearchInput" name="q" type="search" placeholder="Cari layanan, berita, puskesmas, SOP, atau dokumen..." />
        <button class="btn primary" type="submit">${{ic('search')}} Cari</button>
      </form>
    </div>
  </div>
  <div class="mobile-nav" id="mobileNav">
    <div class="container mobile-nav-inner">
      <div class="mobile-links">
        <a href="index.html">Beranda</a>
        <a href="profil.html">Profil Dinas & Pimpinan</a>
        <a href="organisasi.html">Struktur Organisasi</a>
        <a href="layanan.html">Katalog Layanan</a>
        <a href="puskesmas.html">Direktori 19 Puskesmas</a>
        <a href="edukasi.html">Edukasi Kesehatan</a>
        <a href="data.html">Data Kesehatan</a>
        <a href="berita.html">Berita & Kegiatan</a>
        <a href="inovasi.html">Inovasi & Prestasi</a>
        <a href="publikasi.html">Publikasi & Dokumen</a>
        <a href="pengaduan.html">Layanan Pengaduan</a>
        <a href="kontak.html">Kontak & Lokasi</a>
      </div>
    </div>
  </div>`;
}}

function footer() {{
  return `
  <footer class="footer" role="contentinfo">
    <div class="container footer-grid">
      <div class="footer-col footer-brand-col">
        <div class="footer-brand" style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
          <img src="assets/logo_pinrang_opt.png" alt="Logo Pemkab Pinrang" style="height:48px;width:auto;" />
          <img src="assets/kemenkes.jpg" alt="Logo Kemenkes RI" style="height:48px;width:auto;border-radius:4px;" />
          <div>
            <div style="font-size:11px;font-weight:800;letter-spacing:0.06em;color:#94a3b8;">PEMERINTAH KABUPATEN PINRANG</div>
            <div style="font-size:17px;font-weight:800;color:#ffffff;line-height:1.2;">DINAS KESEHATAN</div>
          </div>
        </div>
        <p class="footer-desc">
          Mewujudkan transformasi layanan kesehatan primer yang merata, berkualitas, berkeadilan, dan terjangkau di 12 kecamatan se-Kabupaten Pinrang.
        </p>
        <p style="font-size:13.5px;color:#cbd5e1;line-height:1.6;margin:12px 0;">
          ${{ic('location')}} Jl. Jenderal Sukawati No. 40, Pinrang, Sulawesi Selatan 91212<br>
          ${{ic('phone')}} Hotline / WhatsApp: +62 853-4217-2724<br>
          ${{ic('mail')}} Email: dinkes@pinrangkab.go.id
        </p>
        <div style="margin-top:14px;">
          <span style="display:inline-block;padding:6px 14px;background:rgba(10,163,152,0.25);border:1px solid #0aa398;border-radius:999px;font-size:12px;font-weight:700;color:#5eead4;">
            Membawahi 19 UPTD Puskesmas Resmi
          </span>
        </div>
      </div>
      <div class="footer-col">
        <h3 class="footer-title">Layanan Publik</h3>
        <ul class="footer-links">
          <li><a href="layanan.html">Katalog Standar Pelayanan</a></li>
          <li><a href="layanan-detail.html">SOP & Rekomendasi Izin</a></li>
          <li><a href="puskesmas.html">Direktori 19 Puskesmas</a></li>
          <li><a href="pengaduan.html">Kanal Pengaduan SP4N</a></li>
          <li><a href="skm.html">Survei Kepuasan (SKM)</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3 class="footer-title">Transparansi</h3>
        <ul class="footer-links">
          <li><a href="ppid.html">Portal PPID Dinkes</a></li>
          <li><a href="publikasi.html">Laporan Kinerja (LKjIP)</a></li>
          <li><a href="publikasi.html">Indikator Kinerja Utama</a></li>
          <li><a href="data.html">Satu Data Kesehatan</a></li>
          <li><a href="inovasi.html">Inovasi & Prestasi Daerah</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3 class="footer-title">Rujukan Resmi</h3>
        <ul class="footer-links">
          <li><a href="https://pinrangkab.go.id/" target="_blank" rel="noopener">Portal Pemkab Pinrang ${{ic('external')}}</a></li>
          <li><a href="https://kemkes.go.id/" target="_blank" rel="noopener">Kementerian Kesehatan RI ${{ic('external')}}</a></li>
          <li><a href="https://satusehat.kemkes.go.id/" target="_blank" rel="noopener">SATUSEHAT Kemenkes ${{ic('external')}}</a></li>
          <li><a href="https://www.lapor.go.id/" target="_blank" rel="noopener">SP4N-LAPOR! Nasional ${{ic('external')}}</a></li>
          <li><a href="https://ayosehat.kemkes.go.id/" target="_blank" rel="noopener">Ayo Sehat Kemenkes ${{ic('external')}}</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <div class="footer-copy">
        © 2026 Dinas Kesehatan Pemerintah Kabupaten Pinrang. Seluruh hak cipta dilindungi undang-undang.
      </div>
      <div class="footer-extra">
        <a href="privasi.html">Kebijakan Privasi</a> · 
        <a href="aksesibilitas.html">Aksesibilitas</a> · 
        <a href="peta-situs.html">Peta Situs</a>
      </div>
    </div>
  </footer>`;
}}

function pageHero(kicker, badge, title, lead) {{
  return `
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumbs" aria-label="Jejak navigasi">
        <a href="index.html">Beranda</a> / <span>${{badge}}</span>
      </div>
      <span class="hero-badge">${{kicker.toUpperCase()}}</span>
      <h1 class="hero-title">${{title}}</h1>
      <p class="hero-lead">${{lead}}</p>
    </div>
  </section>`;
}}

function side(title, links) {{
  return `
  <aside class="sidebar" aria-label="Menu terkait">
    <div class="panel">
      <h3 style="font-size:16px;font-weight:700;color:#103447;margin-bottom:14px;border-bottom:1px solid #edf2f3;padding-bottom:10px;">${{title}}</h3>
      <ul style="list-style:none;padding:0;margin:0;display:grid;gap:8px;">
        ${{links.map(([url, label]) => `
          <li>
            <a href="${{url.endsWith('.html') ? url : url + '.html'}}" style="display:flex;align-items:center;justify-content:space-between;padding:8px 12px;border-radius:8px;font-size:13.5px;color:#334155;text-decoration:none;background:#f8fafc;transition:all 0.2s ease;">
              <span>${{label}}</span>
              <span style="color:#087f89;">${{ic('arrow')}}</span>
            </a>
          </li>
        `).join('')}}
      </ul>
    </div>
    <div class="panel mt-20" style="background:#f0fdf9;border:1px solid #bbf7d0;">
      <h4 style="font-size:14px;font-weight:700;color:#065f46;margin-bottom:8px;">Kanal Pengaduan Resmi</h4>
      <p style="font-size:12.5px;color:#475569;line-height:1.5;margin-bottom:12px;">
        Sampaikan keluhan, aspirasi, atau permohonan informasi layanan kesehatan melalui WhatsApp resmi Dinas Kesehatan Pinrang.
      </p>
      <a href="https://wa.me/6285342172724" target="_blank" rel="noopener" class="btn primary" style="width:100%;text-align:center;justify-content:center;font-size:13px;padding:8px 12px;">
        ${{ic('phone')}} WhatsApp: +62 853-4217-2724
      </a>
    </div>
  </aside>`;
}}
"""

print("Helper dasar & struktur layout siap disusun.")

