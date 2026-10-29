'use strict';

import * as DataService from './data-service.js';

// Koleksi Ikon SVG Vektor Konsisten
const SVG = {
  heart: '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8Z"/><path d="M3.2 12h4l2-3 3 6 2-3h6.6"/>',
  activity: '<path d="M2 12h4l3-7 5 14 3-7h5"/>',
  hospital: '<rect x="4" y="3" width="16" height="19" rx="2"/><path d="M12 6v7M8.5 9.5h7M9 22v-5h6v5"/>',
  file: '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6M8 13h8M8 17h8"/>',
  news: '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 8h6M7 12h4M15 8h3v8h-3M7 16h4"/>',
  map: '<path d="m3 6 6-3 6 3 6-3v15l-6 3-6-3-6 3Z"/><path d="M9 3v15M15 6v15"/>', 
  pin: '<path d="M20 10c0 5-8 12-8 12S4 15 4 10a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
  book: '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2Z"/><path d="M8 7h8M8 11h8"/>',
  people: '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M16 3.2a4 4 0 0 1 0 7.6M22 21v-2a4 4 0 0 0-3-3.9"/><circle cx="9" cy="7" r="4"/>',
  chart: '<path d="M3 3v18h18M7 15l4-5 4 2 5-7"/><path d="M16 5h4v4"/>',
  shield: '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/>',
  message: '<path d="M21 11.5a8.5 8.5 0 0 1-8.5 8.5 9 9 0 0 1-4-.9L3 21l1.9-5.5a9 9 0 0 1-.9-4 8.5 8.5 0 0 1 8.5-8.5A8.5 8.5 0 0 1 21 11.5Z"/><path d="M8 11h9M8 15h6"/>',
  search: '<circle cx="10.8" cy="10.8" r="7"/><path d="m16 16 5 5"/>',
  arrow: '<path d="M5 12h14m-6-6 6 6-6 6"/>',
  chevron: '<path d="m9 18 6-6-6-6"/>',
  down: '<path d="m6 9 6 6 6-6"/>',
  menu: '<path d="M4 6h16M4 12h16M4 18h16"/>',
  close: '<path d="M18 6 6 18M6 6l12 12"/>',
  calendar: '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M7 2v6M17 2v6M3 10h18"/>',
  clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
  download: '<path d="M12 3v12m-4-4 4 4 4-4M4 17v4h16v-4"/>',
  info: '<circle cx="12" cy="12" r="10"/><path d="M12 11v6M12 7h.01"/>',
  globe: '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
  external: '<path d="M13 5h6v6M19 5l-9 9"/><path d="M19 13v6H5V5h6"/>',
  camera: '<path d="M4 7h4l2-3h4l2 3h4v13H4Z"/><circle cx="12" cy="13" r="4"/>',
  star: '<path d="m12 2 3.1 6.3 6.9 1-5 4.8 1.2 6.9-6.2-3.3L5.8 21l1.2-6.9-5-4.8 6.9-1Z"/>',
  bulb: '<path d="M9 18h6m-5 3h4M8 14c-2-1.3-3-3.2-3-5.6a7 7 0 0 1 14 0c0 2.4-1 4.3-3 5.6l-1 4H9l-1-4Z"/>',
  clipboard: '<rect x="5" y="4" width="14" height="18" rx="2"/><rect x="9" y="2" width="6" height="4" rx="1"/><path d="m9 14 2 2 4-4"/>',
  home: '<path d="m3 10 9-7 9 7v11H3Z"/><path d="M9 21v-8h6v8"/>',
  bell: '<path d="M18 8a6 6 0 1 0-12 0c0 7-3 7-3 9h18c0-2-3-2-3-9ZM10 21h4"/>',
  phone: '<path d="M22 16.9v3a2 2 0 0 1-2.2 2A19 19 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7l.4 2.6a2 2 0 0 1-.6 1.8L7.3 9.7a16 16 0 0 0 7 7l1.6-1.6a2 2 0 0 1 1.8-.6l2.6.4a2 2 0 0 1 1.7 2Z"/>',
  user: '<circle cx="12" cy="8" r="4"/><path d="M4 22v-3a8 8 0 0 1 16 0v3"/>',
  check: '<path d="m4 12 5 5L20 6"/>'
};

function ic(n, cls = '') {
  return `<svg aria-hidden="true" class="${cls}" viewBox="0 0 24 24">${SVG[n] || SVG.heart}</svg>`;
}

const ROUTES = [
  ['index', 'Beranda'],
  ['profil', 'Profil Dinas'],
  ['organisasi', 'Struktur Organisasi'],
  ['layanan', 'Layanan Kesehatan'],
  ['layanan-detail', 'Detail Layanan'],
  ['puskesmas', 'Direktori Puskesmas'],
  ['puskesmas-detail', 'Profil Puskesmas'],
  ['edukasi', 'Edukasi Kesehatan'],
  ['edukasi-detail', 'Artikel Edukasi'],
  ['berita', 'Berita & Kegiatan'],
  ['berita-detail', 'Detail Berita'],
  ['galeri', 'Galeri Foto'],
  ['data', 'Data Kesehatan'],
  ['indikator', 'Detail Indikator'],
  ['publikasi', 'Publikasi & Dokumen'],
  ['ppid', 'PPID'],
  ['informasi', 'Permohonan Informasi'],
  ['pengaduan', 'Pengaduan'],
  ['kontak', 'Kontak'],
  ['inovasi', 'Inovasi Daerah'],
  ['faq', 'FAQ'],
  ['pencarian', 'Pencarian'],
  ['peta-situs', 'Peta Situs'],
  ['privasi', 'Kebijakan Privasi'],
  ['aksesibilitas', 'Aksesibilitas'],
  ['skm', 'Survei Kepuasan'],
  ['pengumuman', 'Pengumuman Penting'],
  ['tidak-ditemukan', 'Halaman Tidak Ditemukan']
];

const link = (id, label, cls = '') => `<a href="${id}.html" class="${cls}">${label}</a>`;

function getCategoryClass(catName = '') {
  const c = catName.toLowerCase();
  if (c.includes('germas')) return 'cat-germas';
  if (c.includes('kegiatan')) return 'cat-kegiatan';
  if (c.includes('promosi') || c.includes('promkes')) return 'cat-promkes';
  if (c.includes('pembinaan')) return 'cat-pembinaan';
  return 'cat-default';
}

// ----------------- HEADER DENGAN LOGO PINRANG & KEMENKES BERDAMPINGAN -----------------
function header(page) {
  const group = (name, arr) => `
    <div class="navgroup">
      <button type="button" aria-haspopup="true" aria-expanded="false">${name} ${ic('down')}</button>
      <div class="drop">${arr.map(a => link(a[0], a[1])).join('')}</div>
    </div>`;

  return `
  <a class="skip" href="#main">Langsung ke konten utama</a>
  <div class="govbar">
    <div class="container">
      <div>Pemerintah Kabupaten Pinrang · Dinas Kesehatan Resmi</div>
      <div class="right">
        <a href="https://pinrangkab.go.id/" target="_blank" rel="noopener">Portal Pemkab ${ic('external')}</a>
        ${link('ppid', 'PPID')}
        ${link('skm', 'SKM')}
        ${link('faq', 'Bantuan')}
      </div>
    </div>
  </div>
  <header class="brandbar">
    <div class="container">
      <a class="brand-duo" href="index.html" aria-label="Beranda Dinas Kesehatan Kabupaten Pinrang">
        <div class="logo-group">
          <img class="logo-pinrang" src="assets/logo_pinrang_opt.png" alt="Logo Pemkab Pinrang" title="Pemerintah Kabupaten Pinrang">
          <span class="logo-divider" aria-hidden="true"></span>
          <img class="logo-kemenkes" src="assets/kemenkes.jpg" alt="Logo Kementerian Kesehatan RI" title="Kementerian Kesehatan Republik Indonesia">
        </div>
        <div class="brand-text">
          <span class="overline">Pemerintah Kabupaten Pinrang</span>
          <strong>DINAS KESEHATAN</strong>
          <small>Portal Informasi & Pelayanan Kesehatan Masyarakat</small>
        </div>
      </a>
      <div class="header-controls">
        <a class="soft-link" href="puskesmas.html">${ic('pin')} Cari Puskesmas</a>
        <button class="icon-button" type="button" id="fontToggle" title="Perbesar tulisan" aria-label="Perbesar tulisan">Aa</button>
        <button class="icon-button" type="button" id="searchToggle" aria-label="Buka pencarian">${ic('search')}</button>
      </div>
    </div>
  </header>
  <nav class="navwrap" aria-label="Navigasi utama">
    <div class="container navrow">
      <div class="navitems">
        ${link('index', 'Beranda', page === 'index' ? 'active' : '')}
        ${group('Layanan', [['layanan', 'Layanan Kesehatan'], ['puskesmas', 'Direktori Puskesmas']])}
        ${link('edukasi', 'Edukasi', page === 'edukasi' ? 'active' : '')}
        ${link('data', 'Data Kesehatan', page === 'data' ? 'active' : '')}
        ${link('berita', 'Berita & Kegiatan', page === 'berita' ? 'active' : '')}
        ${group('Transparansi', [['ppid', 'PPID'], ['publikasi', 'Publikasi & Dokumen'], ['pengumuman', 'Pengumuman Penting'], ['informasi', 'Permohonan Informasi']])}
        ${group('Tentang Dinas', [['profil', 'Profil Dinas'], ['organisasi', 'Struktur Organisasi'], ['inovasi', 'Inovasi Daerah'], ['galeri', 'Galeri Foto'], ['kontak', 'Kontak']])}
      </div>
      <a class="nav-cta" href="pengaduan.html">${ic('message')} Pengaduan</a>
      <button class="icon-button hamburger" id="mobileToggle" type="button" aria-label="Buka menu navigasi" aria-expanded="false">${ic('menu')}</button>
    </div>
    <div class="mobile-nav" id="mobileNav">
      ${link('index', 'Beranda')}
      <h4>Layanan</h4>
      ${link('layanan', 'Layanan Kesehatan')}
      ${link('puskesmas', 'Direktori Puskesmas')}
      <h4>Informasi</h4>
      ${link('berita', 'Berita & Kegiatan')}
      ${link('edukasi', 'Edukasi Kesehatan')}
      ${link('data', 'Data Kesehatan')}
      ${link('galeri', 'Galeri Foto')}
      <h4>Transparansi & Profil</h4>
      ${link('ppid', 'PPID')}
      ${link('profil', 'Profil Dinas')}
      ${link('organisasi', 'Struktur Organisasi')}
      ${link('pengaduan', 'Pengaduan')}
      ${link('kontak', 'Kontak')}
    </div>
    <div class="floating-search" id="quickSearch">
      <div class="container">
        <form id="quickSearchForm" action="pencarian.html">
          <input id="quickSearchInput" name="q" type="search" placeholder="Cari Puskesmas, layanan, berita, dokumen…" aria-label="Cari seluruh konten" required>
          <button class="btn primary" type="submit">${ic('search')} Cari</button>
        </form>
      </div>
    </div>
  </nav>`;
}

// ----------------- FOOTER DENGAN LOGO PINRANG & KEMENKES -----------------
function footer() {
  return `
  <footer class="footer">
    <div class="container">
      <div class="top">
        <div>
          <div class="brand-duo" style="color:#ffffff;">
            <div class="logo-group" style="background:rgba(255,255,255,0.95);padding:4px 8px;border-radius:8px;">
              <img class="logo-pinrang" src="assets/logo_pinrang_opt.png" alt="Logo Pemkab Pinrang" style="height:40px;">
              <span class="logo-divider" style="height:28px;"></span>
              <img class="logo-kemenkes" src="assets/kemenkes.jpg" alt="Logo Kementerian Kesehatan" style="height:36px;border-radius:3px;">
            </div>
            <div class="brand-text">
              <span class="overline" style="color:#93c5fd;">Pemerintah Kabupaten Pinrang</span>
              <strong style="color:#ffffff;font-size:18px;">DINAS KESEHATAN</strong>
              <small style="color:#cbd5e1;">Portal Informasi & Pelayanan Masyarakat</small>
            </div>
          </div>
          <p class="mt-20" style="color:#cbd5e1;line-height:1.6;font-size:13.5px;">
            Jl. Jenderal Sukawati, Kabupaten Pinrang, Sulawesi Selatan 91212.<br>
            Kanal Pengaduan & Informasi WhatsApp: +62 853-4217-2724
          </p>
          <p><span class="tag" style="background:#078d90;color:#fff;">Membawahi 19 UPTD Puskesmas Resmi</span></p>
        </div>
        <div>
          <h3>Layanan Masyarakat</h3>
          ${link('layanan', 'Standar & Layanan Kesehatan')}
          ${link('puskesmas', 'Direktori 19 Puskesmas')}
          ${link('edukasi', 'Edukasi Kesehatan')}
          ${link('pengaduan', 'Kanal Pengaduan Resmi')}
        </div>
        <div>
          <h3>Transparansi Publik</h3>
          ${link('ppid', 'Layanan PPID')}
          ${link('publikasi', 'Dokumen Kinerja (IKU, Renja, LKjIP)')}
          ${link('pengumuman', 'Pengumuman Resmi')}
          ${link('data', 'Data & Indikator Kesehatan')}
          ${link('inovasi', 'Inovasi Puskesmas Daerah')}
        </div>
        <div>
          <h3>Rujukan Resmi</h3>
          <a href="https://pinrangkab.go.id/" target="_blank" rel="noopener">Portal Pemkab Pinrang</a>
          <a href="https://satusehat.kemkes.go.id/" target="_blank" rel="noopener">SATUSEHAT Kemenkes RI</a>
          <a href="https://www.lapor.go.id/" target="_blank" rel="noopener">SP4N-LAPOR!</a>
          <a href="https://ayosehat.kemkes.go.id/" target="_blank" rel="noopener">Ayo Sehat Kemenkes</a>
        </div>
      </div>
      <div class="copy">
        <span>© 2026 Dinas Kesehatan Pemerintah Kabupaten Pinrang. Seluruh hak cipta dilindungi.</span>
        <span>${link('privasi', 'Kebijakan Privasi')} · ${link('aksesibilitas', 'Aksesibilitas')} · ${link('peta-situs', 'Peta Situs')}</span>
      </div>
    </div>
  </footer>`;
}

function pageHero(page, kicker, title, desc) {
  const iconName = ({
    profil: 'people', organisasi: 'layers', layanan: 'heart', 'layanan-detail': 'clipboard',
    puskesmas: 'hospital', 'puskesmas-detail': 'pin', edukasi: 'book', 'edukasi-detail': 'bulb',
    berita: 'news', 'berita-detail': 'news', galeri: 'camera', data: 'chart', indikator: 'bars',
    publikasi: 'file', ppid: 'shield', informasi: 'file', pengaduan: 'message', kontak: 'pin',
    inovasi: 'bulb', faq: 'info', pencarian: 'search', 'peta-situs': 'layers', privasi: 'lock',
    aksesibilitas: 'heart', skm: 'star', pengumuman: 'bell', 'tidak-ditemukan': 'search'
  })[page] || 'heart';

  const routeItem = ROUTES.find(r => r[0] === page);
  const pageTitle = routeItem ? routeItem[1] : page;

  return `
  <section class="pagehero v4-pagehero">
    <div class="container">
      <div class="crumbs">
        <a href="index.html">Beranda</a>${ic('chevron')}
        <span aria-current="page">${pageTitle}</span>
      </div>
      <div class="wrap">
        <div class="pagehero-copy">
          <span class="tinycap">${kicker}</span>
          <h1>${title}</h1>
          <p>${desc}</p>
        </div>
        <div class="pagehero-visual" aria-hidden="true">
          <span class="visual-ring ring-one"></span>
          <span class="visual-ring ring-two"></span>
          <span class="pagehero-icon">${ic(iconName)}</span>
          <span class="decor-dot d1"></span>
          <span class="decor-dot d2"></span>
        </div>
      </div>
    </div>
  </section>`;
}

// ----------------- RENDER HALAMAN BERANDA -----------------
async function renderHome() {
  const articles = await DataService.getArticles();
  const puskesmas = await DataService.getPuskesmasList();
  const latestArticles = articles.slice(0, 4);

  const heroArticle = latestArticles[0] || {
    id: '4505',
    title: 'Kecamatan Batulappa Jadi Penutup Rangkaian Kampanye GERMAS Dinkes Pinrang, Dorong Masyarakat Lakukan Deteksi Dini',
    excerpt: 'Tim Kerja Promosi Kesehatan dan Pemberdayaan Masyarakat Dinas Kesehatan Kabupaten Pinrang sukses menuntaskan rangkaian Kampanye GERMAS di 12 kecamatan...',
    published_at: '23 Oktober 2026',
    author: 'Muhammad Rusdi',
    category: 'Kegiatan',
    featured_image: 'assets/puskesmas.png'
  };

  const sideArticles = latestArticles.slice(1, 4);

  return `
  <div class="v4-breaking">
    <div class="container v4-breaking-inner">
      <span class="v4-breaking-label">${ic('bell')} INFORMASI RESMI</span>
      <span>Portal Terpadu Dinas Kesehatan Kabupaten Pinrang — Akses 19 UPTD Puskesmas, Edukasi, dan Publikasi Kinerja Daerah.</span>
      <a href="pengumuman.html">Lihat pengumuman ${ic('arrow')}</a>
    </div>
  </div>

  <section class="v4-mainstage">
    <div class="container v4-stage-grid">
      <div class="v4-feature-rail" aria-roledescription="carousel" aria-label="Sorotan utama portal kesehatan">
        <div class="v4-feature-slide is-active" data-slide="0">
          <div class="v4-feature-inner">
            <div class="v4-feature-deco" aria-hidden="true">
              <span class="v4-cross">+</span><span class="v4-circle"></span><span class="v4-checkpulse">${ic('activity')}</span>
            </div>
            <span class="v4-feature-kicker">PELAYANAN KESEHATAN PRIMER</span>
            <h1>Lebih dekat dengan <em>layanan kesehatan Pinrang.</em></h1>
            <p>Temukan informasi lengkap 19 UPTD Puskesmas di 12 kecamatan, standar pelayanan medis, dan program Cek Kesehatan Gratis.</p>
            <a class="v4-feature-action" href="puskesmas.html">Temukan 19 Puskesmas ${ic('arrow')}</a>
          </div>
        </div>
        <div class="v4-feature-slide" data-slide="1" hidden>
          <div class="v4-feature-inner">
            <div class="v4-feature-deco" aria-hidden="true">
              <span class="v4-cross">+</span><span class="v4-circle"></span><span class="v4-checkpulse">${ic('book')}</span>
            </div>
            <span class="v4-feature-kicker">GERAKAN MASYARAKAT HIDUP SEHAT</span>
            <h2>Informasi tepercaya, <em>keluarga Pinrang lebih sehat.</em></h2>
            <p>Panduan gizi seimbang, imunisasi lengkap, pencegahan stunting, serta deteksi dini penyakit tidak menular.</p>
            <a class="v4-feature-action" href="edukasi.html">Jelajahi Panduan Edukasi ${ic('arrow')}</a>
          </div>
        </div>
        <div class="v4-feature-slide" data-slide="2" hidden>
          <div class="v4-feature-inner">
            <div class="v4-feature-deco" aria-hidden="true">
              <span class="v4-cross">+</span><span class="v4-circle"></span><span class="v4-checkpulse">${ic('shield')}</span>
            </div>
            <span class="v4-feature-kicker">TRANSPARANSI & AKUNTABILITAS</span>
            <h2>Data terbuka, <em>layanan publik akuntabel.</em></h2>
            <p>Akses dokumen Indikator Kinerja Utama (IKU), LKjIP, Renja, serta layanan permohonan informasi PPID.</p>
            <a class="v4-feature-action" href="ppid.html">Layanan Informasi PPID ${ic('arrow')}</a>
          </div>
        </div>
        <div class="v4-stage-controls">
          <div class="v4-slide-dots" role="group" aria-label="Pilih sorotan">
            <button type="button" class="active" data-slide-to="0" aria-label="Sorotan 1" aria-current="true">01</button>
            <button type="button" data-slide-to="1" aria-label="Sorotan 2">02</button>
            <button type="button" data-slide-to="2" aria-label="Sorotan 3">03</button>
          </div>
          <div class="v4-arrow-controls">
            <button type="button" class="v4-circle-btn" data-slide-step="-1" aria-label="Sorotan sebelumnya">${ic('arrow')}</button>
            <button type="button" class="v4-circle-btn" data-slide-step="1" aria-label="Sorotan berikutnya">${ic('arrow')}</button>
          </div>
        </div>
      </div>

      <div class="v4-stage-side">
        <a class="v4-spotlight v4-spotlight-cyan" href="layanan-detail.html">
          <span class="v4-spot-top"><span>PROGRAM UNGGULAN</span>${ic('arrow')}</span>
          <div class="v4-spot-icon">${ic('heart')}</div>
          <h2>Cek Kesehatan Gratis</h2>
          <p>Skrining kesehatan rutin di Puskesmas untuk deteksi dini risiko PTM.</p>
        </a>
        <a class="v4-spotlight v4-spotlight-violet" href="berita.html">
          <span class="v4-spot-top"><span>KABAR TERBARU</span>${ic('arrow')}</span>
          <div class="v4-spot-icon">${ic('news')}</div>
          <h2>Kiprah & Kegiatan Dinas</h2>
          <p>Pantau kegiatan dinas di 12 kecamatan se-Kabupaten Pinrang.</p>
        </a>
      </div>
    </div>
  </section>

  <section class="v4-search-zone">
    <div class="container">
      <form class="v4-search-box" role="search" action="pencarian.html">
        <span class="v4-search-icon">${ic('search')}</span>
        <div class="v4-search-content">
          <label for="v4Search">Sedang mencari informasi atau layanan apa?</label>
          <input id="v4Search" name="q" type="search" placeholder="Cari nama Puskesmas, imunisasi, izin SPP-IRT, dokumen IKU…" autocomplete="off" required>
        </div>
        <button class="btn primary" type="submit">Cari informasi ${ic('arrow')}</button>
      </form>
      <div class="v4-search-chips">
        <span>Pencarian Cepat:</span>
        <a href="puskesmas.html">Puskesmas Suppa</a>
        <a href="puskesmas.html">Puskesmas Lanrisang</a>
        <a href="layanan-detail.html">Izin SPP-IRT</a>
        <a href="layanan.html">Cek Kesehatan Gratis</a>
        <a href="publikasi.html">Dokumen Kinerja LKjIP</a>
      </div>
    </div>
  </section>

  <!-- Bento Layanan Cepat -->
  <section class="v4-section v4-service-area" id="layanan-utama">
    <div class="container">
      <div class="v4-section-head">
        <div>
          <span class="v4-overline">AKSES CEPAT WARGA</span>
          <h2>Informasi dan Layanan Publik, <span>Lebih Mudah.</span></h2>
          <p>Pilih kategori kebutuhan Anda melalui layanan dengan tata letak terstruktur.</p>
        </div>
        <a href="layanan.html" class="v4-text-link">Semua layanan ${ic('arrow')}</a>
      </div>
      <div class="v4-bento-services">
        <a href="puskesmas.html" class="v4-bento-card bento-cyan bento-wide">
          <div class="v4-bento-badge">Fasilitas Kesehatan Resmi</div>
          <div class="v4-bento-icon-lg" style="background:#ffffff;padding:8px;border-radius:16px;">
            <img src="assets/puskesmas.png" alt="Logo Puskesmas" style="width:100%;height:100%;object-fit:contain;">
          </div>
          <h3>Direktori 19 Puskesmas</h3>
          <p>Alamat pos, nama kepala puskesmas, dan inovasi pelayanan di 12 kecamatan se-Pinrang.</p>
          <span class="v4-bento-btn">Buka Direktori ${ic('arrow')}</span>
        </a>
        <a href="layanan.html" class="v4-bento-card bento-teal">
          <div class="v4-bento-icon">${ic('clipboard')}</div>
          <h3>Standar & SOP Pelayanan</h3>
          <p>Syarat izin praktik nakes, sertifikasi pangan IRT, rekomendasi klinik & apotek.</p>
          <span class="v4-bento-btn">Lihat Standar ${ic('arrow')}</span>
        </a>
        <a href="edukasi.html" class="v4-bento-card bento-violet">
          <div class="v4-bento-icon">${ic('book')}</div>
          <h3>Edukasi Kesehatan</h3>
          <p>Panduan gizi seimbang, pencegahan stunting, PHBS, serta imunisasi anak.</p>
          <span class="v4-bento-btn">Baca Edukasi ${ic('arrow')}</span>
        </a>
        <a href="data.html" class="v4-bento-card bento-amber">
          <div class="v4-bento-icon">${ic('chart')}</div>
          <h3>Data & Indikator</h3>
          <p>Capaian imunisasi, persalinan faskes, stunting, dan status ODF 100%.</p>
          <span class="v4-bento-btn">Eksplorasi Data ${ic('arrow')}</span>
        </a>
        <a href="publikasi.html" class="v4-bento-card bento-blue">
          <div class="v4-bento-icon">${ic('file')}</div>
          <h3>Dokumen & PPID</h3>
          <p>Akses berkas Renja, Renstra, Laporan Kinerja Instansi Pemerintah (LKjIP).</p>
          <span class="v4-bento-btn">Unduh Dokumen ${ic('arrow')}</span>
        </a>
        <a href="pengaduan.html" class="v4-bento-card bento-coral">
          <div class="v4-bento-icon">${ic('message')}</div>
          <h3>Kanal Pengaduan Warga</h3>
          <p>Sampaikan aspirasi dan laporan melalui integrasi SP4N-LAPOR! dan WhatsApp.</p>
          <span class="v4-bento-btn">Kirim Aduan ${ic('arrow')}</span>
        </a>
      </div>
    </div>
  </section>

  <!-- Berita Unggulan Bergaya Editorial -->
  <section class="v4-section v4-news-strip" style="background:#f8fafc;">
    <div class="container">
      <div class="v4-section-head">
        <div>
          <span class="v4-overline">DOKUMENTASI & KABAR DAERAH</span>
          <h2>Berita dan Kegiatan <span>Terkini.</span></h2>
          <p>Kabar resmi seputar gerakan kesehatan masyarakat dan pembinaan UPTD di Pinrang.</p>
        </div>
        <a href="berita.html" class="v4-text-link">Semua berita (${articles.length}) ${ic('arrow')}</a>
      </div>

      <!-- Lead Story Card -->
      <article class="editorial-lead-card">
        <div class="lead-thumb">
          <img src="${heroArticle.featured_image || 'assets/puskesmas.png'}" alt="${heroArticle.title}" loading="lazy">
          <span class="cat-badge ${getCategoryClass(heroArticle.category)}" style="position:absolute;top:16px;left:16px;">
            ${heroArticle.category || 'Kegiatan'}
          </span>
        </div>
        <div class="lead-body">
          <span class="lead-badge">${ic('news')} BERITA UTAMA HARI INI</span>
          <h2><a href="berita-detail.html?id=${heroArticle.id}">${heroArticle.title}</a></h2>
          <p class="lead-excerpt">${heroArticle.excerpt}</p>
          <div class="lead-meta">
            <span>${ic('calendar')} ${heroArticle.published_at}</span>
            <span>${ic('user')} ${heroArticle.author}</span>
            <a href="berita-detail.html?id=${heroArticle.id}" class="v4-readmore" style="margin-left:auto;">
              Baca Selengkapnya ${ic('arrow')}
            </a>
          </div>
        </div>
      </article>

      <!-- 3 Kartu Berita Sekunder -->
      <div class="news-grid-pro" style="grid-template-columns: repeat(3, minmax(0, 1fr));">
        ${sideArticles.map(art => `
          <article class="news-card-pro">
            <div class="thumb-wrap">
              <img src="${art.featured_image || 'assets/puskesmas.png'}" alt="${art.title}" loading="lazy">
              <span class="cat-badge ${getCategoryClass(art.category)}">${art.category || 'Berita'}</span>
            </div>
            <div class="card-content">
              <div class="card-meta">
                <span>${ic('calendar')} ${art.published_at}</span>
                <span>${ic('clock')} 3 mnt baca</span>
              </div>
              <h3><a href="berita-detail.html?id=${art.id}">${art.title}</a></h3>
              <p class="snippet">${art.excerpt}</p>
              <div class="card-footer">
                <span class="author-info">${ic('user')} ${art.author}</span>
                <a href="berita-detail.html?id=${art.id}" class="read-action">Baca ${ic('arrow')}</a>
              </div>
            </div>
          </article>
        `).join('')}
      </div>
    </div>
  </section>

  <!-- Panel Data Kontras Navy -->
  <section class="v4-section v4-data-panel">
    <div class="container">
      <div class="v4-panel-head">
        <div>
          <span class="v4-overline-light">SATU DATA KESEHATAN KABUPATEN PINRANG</span>
          <h2>Akuntabilitas Capaian & Indikator Kinerja</h2>
          <p>Data agregat resmi sektor kesehatan untuk mewujudkan transparansi tata kelola.</p>
        </div>
        <a href="data.html" class="btn secondary">Lihat Indikator Lengkap ${ic('arrow')}</a>
      </div>
      <div class="v4-data-cards">
        <div class="v4-data-card">
          <span class="v4-data-number">19</span>
          <span class="v4-data-label">UPTD Puskesmas Aktif</span>
          <p>Melayani seluruh warga di 12 kecamatan dengan ragam inovasi promotif & kuratif.</p>
        </div>
        <div class="v4-data-card">
          <span class="v4-data-number">100%</span>
          <span class="v4-data-label">Status ODF (Stop BABS)</span>
          <p>Kabupaten Pinrang meraih predikat bebas buang air besar sembarangan secara paripurna.</p>
        </div>
        <div class="v4-data-card">
          <span class="v4-data-number">88.75</span>
          <span class="v4-data-label">Indeks Kepuasan Masyarakat</span>
          <p>Predikat Sangat Puas pada standar mutu pelayanan kesehatan publik daerah.</p>
        </div>
        <div class="v4-data-card">
          <span class="v4-data-number">96.4%</span>
          <span class="v4-data-label">Cakupan Imunisasi Dasar</span>
          <p>Perlindungan anak dari penyakit menular melampaui target nasional.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Faskes Puskesmas dengan Logo Resmi Puskesmas -->
  <section class="v4-section">
    <div class="container">
      <div class="v4-section-head">
        <div>
          <span class="v4-overline">PELAYANAN KESEHATAN TERDEKAT</span>
          <h2>19 UPTD Puskesmas Kabupaten Pinrang</h2>
          <p>Fasilitas kesehatan tingkat pertama resmi dengan inovasi pelayanan masyarakat.</p>
        </div>
        <a href="puskesmas.html" class="v4-text-link">Semua 19 Puskesmas ${ic('arrow')}</a>
      </div>
      <div class="grid grid-3">
        ${puskesmas.slice(0, 3).map(p => `
          <div class="pkm-card-pro">
            <div class="pkm-header">
              <div class="pkm-logo-box">
                <img src="assets/puskesmas.png" alt="Logo Puskesmas">
              </div>
              <div class="pkm-title-group">
                <span class="pkm-kecamatan-tag">Kecamatan ${p.kecamatan}</span>
                <h3>${p.name}</h3>
              </div>
            </div>
            <div class="pkm-body">
              <div class="pkm-head-officer">
                <span>${ic('user')}</span>
                <div>
                  <small style="color:#64748b;display:block;">Kepala UPTD:</small>
                  <strong>${p.head}</strong>
                </div>
              </div>
              <p style="font-size:13px;color:#64748b;margin-bottom:12px;">${ic('pin')} ${p.address}</p>
              ${p.innovations && p.innovations.length ? `
                <div class="pkm-innovations">
                  <span class="pkm-innovations-title">${ic('bulb')} Inovasi Unggulan:</span>
                  <ul>
                    ${p.innovations.slice(0, 2).map(inv => `<li>${inv}</li>`).join('')}
                  </ul>
                </div>
              ` : ''}
            </div>
            <div class="pkm-footer">
              <a href="puskesmas-detail.html?id=${p.id}" class="btn primary" style="width:100%;justify-content:center;">
                Lihat Profil Faskes ${ic('arrow')}
              </a>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  </section>
  `;
}

// ----------------- RENDER HALAMAN BERITA EDITORIAL MODERN -----------------
async function renderBerita() {
  const articles = await DataService.getArticles();
  const urlParams = new URLSearchParams(window.location.search);
  const selectedCat = urlParams.get('kategori') || 'semua';
  const pageNum = parseInt(urlParams.get('hal') || '1', 10);
  const perPage = 9;

  let filtered = articles;
  if (selectedCat !== 'semua') {
    filtered = articles.filter(a => 
      (a.category && a.category.toLowerCase().includes(selectedCat.toLowerCase())) || 
      (a.categories && a.categories.some(c => c.toLowerCase().includes(selectedCat.toLowerCase())))
    );
  }

  const totalPages = Math.ceil(filtered.length / perPage) || 1;
  const startIdx = (pageNum - 1) * perPage;
  const leadArticle = pageNum === 1 ? filtered[0] : null;
  const gridArticles = pageNum === 1 ? filtered.slice(1, perPage) : filtered.slice(startIdx, startIdx + perPage);

  return `
  ${pageHero('berita', 'DOKUMENTASI KEGIATAN & SIARAN PERS', 'Berita & Kegiatan Dinas Kesehatan', 'Informasi terkini kegiatan kampanye GERMAS, pembinaan UPTD Puskesmas, dan edukasi kesehatan di Pinrang.')}
  <section class="v4-section" style="background:#f8fafc;padding-top:30px;">
    <div class="container">
      <div class="heading-split" style="margin-bottom:30px;background:#ffffff;padding:16px 20px;border-radius:14px;border:1px solid #e2e8f0;">
        <div class="v4-search-chips" style="gap:8px;">
          <span style="font-weight:700;">Filter Kategori:</span>
          <a href="berita.html?kategori=semua" class="${selectedCat === 'semua' ? 'active-chip' : ''}">Semua (${articles.length})</a>
          <a href="berita.html?kategori=kegiatan" class="${selectedCat === 'kegiatan' ? 'active-chip' : ''}">Kegiatan</a>
          <a href="berita.html?kategori=germas" class="${selectedCat === 'germas' ? 'active-chip' : ''}">GERMAS</a>
          <a href="berita.html?kategori=promosi" class="${selectedCat === 'promosi' ? 'active-chip' : ''}">Promosi Kesehatan</a>
          <a href="berita.html?kategori=pembinaan" class="${selectedCat === 'pembinaan' ? 'active-chip' : ''}">Pembinaan</a>
        </div>
        <form action="pencarian.html" style="display:flex;gap:8px;">
          <input type="search" name="q" placeholder="Cari topik berita…" style="padding:8px 14px;border:1px solid #cbd5e1;border-radius:8px;font-size:13px;width:200px;">
          <button type="submit" class="btn primary" style="padding:8px 14px;">${ic('search')}</button>
        </form>
      </div>

      <!-- Lead Story Card (Khusus Halaman 1) -->
      ${leadArticle ? `
        <article class="editorial-lead-card">
          <div class="lead-thumb">
            <img src="${leadArticle.featured_image || 'assets/puskesmas.png'}" alt="${leadArticle.title}" loading="lazy">
            <span class="cat-badge ${getCategoryClass(leadArticle.category)}" style="position:absolute;top:16px;left:16px;">
              ${leadArticle.category || 'Kegiatan'}
            </span>
          </div>
          <div class="lead-body">
            <span class="lead-badge">${ic('star')} SOROTAN UTAMA REDAKSI</span>
            <h2><a href="berita-detail.html?id=${leadArticle.id}">${leadArticle.title}</a></h2>
            <p class="lead-excerpt">${leadArticle.excerpt}</p>
            <div class="lead-meta">
              <span>${ic('calendar')} ${leadArticle.published_at}</span>
              <span>${ic('user')} ${leadArticle.author}</span>
              <a href="berita-detail.html?id=${leadArticle.id}" class="v4-readmore" style="margin-left:auto;">
                Baca Ulasan Lengkap ${ic('arrow')}
              </a>
            </div>
          </div>
        </article>
      ` : ''}

      <!-- Grid Berita Pro -->
      <div class="news-grid-pro">
        ${gridArticles.map(art => `
          <article class="news-card-pro">
            <div class="thumb-wrap">
              <img src="${art.featured_image || 'assets/puskesmas.png'}" alt="${art.title}" loading="lazy">
              <span class="cat-badge ${getCategoryClass(art.category)}">${art.category || 'Berita'}</span>
            </div>
            <div class="card-content">
              <div class="card-meta">
                <span>${ic('calendar')} ${art.published_at}</span>
                <span>${ic('clock')} 3 mnt baca</span>
              </div>
              <h3><a href="berita-detail.html?id=${art.id}">${art.title}</a></h3>
              <p class="snippet">${art.excerpt}</p>
              <div class="card-footer">
                <span class="author-info">${ic('user')} ${art.author}</span>
                <a href="berita-detail.html?id=${art.id}" class="read-action">Baca ${ic('arrow')}</a>
              </div>
            </div>
          </article>
        `).join('')}
      </div>

      <!-- Pagination Pro -->
      <div style="display:flex;justify-content:center;align-items:center;gap:12px;margin-top:48px;">
        ${pageNum > 1 ? `<a href="berita.html?kategori=${selectedCat}&hal=${pageNum - 1}" class="btn secondary">« Halaman Sebelumnya</a>` : ''}
        <span style="display:inline-flex;align-items:center;padding:8px 18px;background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;font-weight:700;font-size:14px;color:#1e293b;">
          Halaman ${pageNum} dari ${totalPages} (${filtered.length} Berita)
        </span>
        ${pageNum < totalPages ? `<a href="berita.html?kategori=${selectedCat}&hal=${pageNum + 1}" class="btn primary">Halaman Berikutnya »</a>` : ''}
      </div>
    </div>
  </section>`;
}

// ----------------- RENDER SINGLE POST / DETAIL BERITA EDITORIAL -----------------
async function renderBeritaDetail() {
  const urlParams = new URLSearchParams(window.location.search);
  const idOrSlug = urlParams.get('id') || urlParams.get('slug') || '4505';
  const article = await DataService.getArticleById(idOrSlug);
  const allArticles = await DataService.getArticles();
  const relatedArticles = allArticles.filter(a => String(a.id) !== String(article?.id)).slice(0, 3);

  if (!article) {
    return `
    ${pageHero('berita', 'BERITA TIDAK DITEMUKAN', 'Artikel Tidak Ditemukan', 'Maaf, artikel yang Anda cari tidak tersedia.')}
    <div class="container text-center py-60">
      <p>Artikel dengan identifikasi tersebut tidak ditemukan di arsip publik.</p>
      <a href="berita.html" class="btn primary mt-20">Kembali ke Daftar Berita</a>
    </div>`;
  }

  const shareText = encodeURIComponent(`${article.title} - Dinas Kesehatan Kabupaten Pinrang`);
  const shareUrl = encodeURIComponent(window.location.href);

  return `
  <section class="pagehero v4-pagehero" style="padding-bottom:20px;">
    <div class="container">
      <div class="crumbs">
        <a href="index.html">Beranda</a>${ic('chevron')}
        <a href="berita.html">Berita & Kegiatan</a>${ic('chevron')}
        <span aria-current="page">${article.category}</span>
      </div>
    </div>
  </section>

  <main class="container py-20" style="max-width:1000px;">
    <!-- Editorial Post Header -->
    <header class="editorial-post-header">
      <span class="post-tag-pill">${ic('news')} ${article.category.toUpperCase()}</span>
      <h1 class="post-title">${article.title}</h1>
      
      <!-- Bar Penulis & Waktu -->
      <div class="editorial-author-bar">
        <div class="author-profile">
          <div class="author-avatar">${article.author.charAt(0)}</div>
          <div class="author-details">
            <strong>${article.author}</strong>
            <small>Redaksi Media Informasi Dinas Kesehatan Pinrang · ${article.published_at}</small>
          </div>
        </div>
        <div style="display:flex;gap:8px;">
          <a href="https://api.whatsapp.com/send?text=${shareText}%20${shareUrl}" target="_blank" rel="noopener" class="btn secondary" style="font-size:12.5px;padding:7px 12px;background:#25D366;color:#ffffff;border-color:#25D366;">
            ${ic('phone')} WhatsApp
          </a>
          <button type="button" class="btn secondary" style="font-size:12.5px;padding:7px 12px;" onclick="navigator.clipboard.writeText(window.location.href);alert('Tautan berita berhasil disalin ke clipboard!');">
            ${ic('clipboard')} Salin Tautan
          </button>
        </div>
      </div>
    </header>

    <!-- Gambar Unggulan Utama -->
    ${article.featured_image ? `
      <figure class="article-hero-media">
        <img src="${article.featured_image}" alt="${article.title}">
        <figcaption>Dokumentasi resmi liputan kegiatan Dinas Kesehatan Kabupaten Pinrang.</figcaption>
      </figure>
    ` : ''}

    <!-- Isi Bacaan Editorial -->
    <div class="editorial-reading-container">
      ${article.content_html || `<p>${article.excerpt}</p>`}
    </div>

    <!-- Tombol Navigasi Bawah & Share -->
    <div style="max-width:820px;margin:50px auto 40px;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;display:flex;align-items:center;justify-content:space-between;flex-wrap:gap:16px;">
      <div>
        <h4 style="margin:0 0 4px;font-size:15px;color:#0f172a;">Bagikan artikel ini:</h4>
        <small style="color:#64748b;">Dukung penyebarluasan informasi kesehatan masyarakat Kabupaten Pinrang.</small>
      </div>
      <div style="display:flex;gap:10px;">
        <a href="https://api.whatsapp.com/send?text=${shareText}%20${shareUrl}" target="_blank" rel="noopener" class="btn primary" style="background:#25D366;border-color:#25D366;">
          ${ic('phone')} Bagikan ke WhatsApp
        </a>
        <a href="berita.html" class="btn secondary">
          ${ic('arrow')} Indeks Berita
        </a>
      </div>
    </div>

    <!-- Rekomendasi Berita Terkait -->
    <section style="margin-top:60px;padding-top:40px;border-top:2px solid #e2e8f0;">
      <div class="heading-split" style="margin-bottom:24px;">
        <div>
          <span class="v4-overline">BACA JUGA</span>
          <h2 style="font-size:24px;font-weight:800;color:#0f172a;margin:4px 0 0;">Berita & Kegiatan Terkait</h2>
        </div>
        <a href="berita.html" class="v4-text-link">Semua berita ${ic('arrow')}</a>
      </div>
      <div class="news-grid-pro" style="grid-template-columns: repeat(3, minmax(0, 1fr));">
        ${relatedArticles.map(art => `
          <article class="news-card-pro">
            <div class="thumb-wrap">
              <img src="${art.featured_image || 'assets/puskesmas.png'}" alt="${art.title}" loading="lazy">
              <span class="cat-badge ${getCategoryClass(art.category)}">${art.category}</span>
            </div>
            <div class="card-content">
              <div class="card-meta">
                <span>${ic('calendar')} ${art.published_at}</span>
              </div>
              <h3 style="font-size:15px;"><a href="berita-detail.html?id=${art.id}">${art.title}</a></h3>
              <div class="card-footer" style="margin-top:auto;">
                <a href="berita-detail.html?id=${art.id}" class="read-action">Baca Ulasan ${ic('arrow')}</a>
              </div>
            </div>
          </article>
        `).join('')}
      </div>
    </section>
  </main>`;
}

// ----------------- RENDER DIREKTORI PUSKESMAS DENGAN LOGO RESMI PUSKESMAS -----------------
async function renderPuskesmas() {
  const puskesmas = await DataService.getPuskesmasList();
  const urlParams = new URLSearchParams(window.location.search);
  const selectedKec = urlParams.get('kecamatan') || 'semua';

  let filtered = puskesmas;
  if (selectedKec !== 'semua') {
    filtered = puskesmas.filter(p => p.kecamatan.toLowerCase() === selectedKec.toLowerCase());
  }

  const kecamatanList = Array.from(new Set(puskesmas.map(p => p.kecamatan))).sort();

  return `
  ${pageHero('puskesmas', 'FASILITAS PELAYANAN KESEHATAN TINGKAT PERTAMA', 'Direktori 19 UPTD Puskesmas', 'Temukan Puskesmas terdekat di 12 kecamatan Kabupaten Pinrang beserta dokter/kepala, inovasi program, dan pelayanannya.')}
  <section class="v4-section" style="background:#f8fafc;padding-top:30px;">
    <div class="container">
      <div class="heading-split" style="margin-bottom:30px;background:#ffffff;padding:16px 20px;border-radius:14px;border:1px solid #e2e8f0;">
        <div class="v4-search-chips" style="gap:8px;">
          <span style="font-weight:700;">Filter Kecamatan:</span>
          <a href="puskesmas.html?kecamatan=semua" class="${selectedKec === 'semua' ? 'active-chip' : ''}">Semua Wilayah (${puskesmas.length})</a>
          ${kecamatanList.map(kec => `
            <a href="puskesmas.html?kecamatan=${encodeURIComponent(kec)}" class="${selectedKec.toLowerCase() === kec.toLowerCase() ? 'active-chip' : ''}">${kec}</a>
          `).join('')}
        </div>
      </div>

      <div class="grid grid-3">
        ${filtered.map(p => `
          <div class="pkm-card-pro">
            <div class="pkm-header">
              <div class="pkm-logo-box">
                <img src="assets/puskesmas.png" alt="Logo Resmi Puskesmas">
              </div>
              <div class="pkm-title-group">
                <span class="pkm-kecamatan-tag">Kecamatan ${p.kecamatan}</span>
                <h3>${p.name}</h3>
              </div>
            </div>
            <div class="pkm-body">
              <div class="pkm-head-officer">
                <span>${ic('user')}</span>
                <div>
                  <small style="color:#64748b;display:block;">Kepala UPTD:</small>
                  <strong>${p.head}</strong>
                </div>
              </div>
              <p style="font-size:13px;color:#64748b;margin-bottom:14px;">${ic('pin')} ${p.address}</p>
              ${p.innovations && p.innovations.length ? `
                <div class="pkm-innovations">
                  <span class="pkm-innovations-title">${ic('bulb')} Inovasi Unggulan:</span>
                  <ul>
                    ${p.innovations.slice(0, 3).map(inv => `<li>${inv}</li>`).join('')}
                  </ul>
                </div>
              ` : ''}
              ${p.awards && p.awards.length ? `
                <div style="font-size:12px;color:#b45309;background:#fef3c7;padding:6px 10px;border-radius:6px;margin-bottom:12px;">
                  🏆 <strong>Penghargaan:</strong> ${p.awards[0]}
                </div>
              ` : ''}
            </div>
            <div class="pkm-footer">
              <a href="puskesmas-detail.html?id=${p.id}" class="btn primary" style="width:100%;justify-content:center;">
                Lihat Detail & Layanan ${ic('arrow')}
              </a>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  </section>`;
}

// ----------------- RENDER DETAIL PUSKESMAS DENGAN LOGO RESMI PUSKESMAS -----------------
async function renderPuskesmasDetail() {
  const urlParams = new URLSearchParams(window.location.search);
  const idOrSlug = urlParams.get('id') || 'pkm-01';
  const pkm = await DataService.getPuskesmasById(idOrSlug);

  if (!pkm) {
    return `
    ${pageHero('puskesmas', 'PUSKESMAS TIDAK DITEMUKAN', 'Puskesmas Tidak Ditemukan', '')}
    <div class="container text-center py-60">
      <a href="puskesmas.html" class="btn primary">Kembali ke Direktori Puskesmas</a>
    </div>`;
  }

  return `
  <section class="pagehero v4-pagehero">
    <div class="container">
      <div class="crumbs">
        <a href="index.html">Beranda</a>${ic('chevron')}
        <a href="puskesmas.html">Direktori Puskesmas</a>${ic('chevron')}
        <span aria-current="page">${pkm.name}</span>
      </div>
      <div class="wrap" style="align-items:center;">
        <div class="pagehero-copy">
          <span class="tinycap">UPTD PUSKESMAS WILAYAH KECAMATAN ${pkm.kecamatan.toUpperCase()}</span>
          <h1>${pkm.name}</h1>
          <p>Alamat: ${pkm.address}</p>
        </div>
        <div style="background:#ffffff;padding:16px;border-radius:20px;box-shadow:0 8px 25px rgba(0,0,0,0.12);display:grid;place-items:center;">
          <img src="assets/puskesmas.png" alt="Logo Puskesmas" style="width:96px;height:96px;object-fit:contain;">
        </div>
      </div>
    </div>
  </section>

  <div class="container layout-with-sidebar py-40">
    <div class="main-content">
      <div class="panel" style="margin-bottom:24px;">
        <h2 style="font-size:1.4rem;margin-bottom:16px;border-bottom:2px solid #078d90;padding-bottom:8px;">Profil Fasilitas & Manajemen</h2>
        <table style="width:100%;border-collapse:collapse;font-size:14.5px;">
          <tr style="border-bottom:1px solid #e2e8f0;"><td style="padding:12px 0;width:35%;font-weight:600;color:#64748b;">Nama Fasilitas:</td><td><strong>${pkm.name}</strong></td></tr>
          <tr style="border-bottom:1px solid #e2e8f0;"><td style="padding:12px 0;font-weight:600;color:#64748b;">Wilayah Kecamatan:</td><td>${pkm.kecamatan}</td></tr>
          <tr style="border-bottom:1px solid #e2e8f0;"><td style="padding:12px 0;font-weight:600;color:#64748b;">Alamat Lengkap:</td><td>${pkm.address}</td></tr>
          <tr style="border-bottom:1px solid #e2e8f0;"><td style="padding:12px 0;font-weight:600;color:#64748b;">Kepala UPTD Puskesmas:</td><td><strong>${pkm.head}</strong></td></tr>
          <tr><td style="padding:12px 0;font-weight:600;color:#64748b;">Jam Operasional:</td><td>Senin - Sabtu (08.00 - 14.00 WITA) · <strong>Instalasi Gawat Darurat (IGD) 24 Jam</strong></td></tr>
        </table>
      </div>

      <div class="panel" style="margin-bottom:24px;">
        <h2 style="font-size:1.4rem;margin-bottom:14px;border-bottom:2px solid #1676f3;padding-bottom:8px;">Inovasi Pelayanan Kesehatan</h2>
        ${pkm.innovations && pkm.innovations.length ? `
          <ul class="styled-list">
            ${pkm.innovations.map(inv => `<li><strong>${inv}</strong></li>`).join('')}
          </ul>
        ` : '<p>Inovasi sedang dalam proses verifikasi dan pemutakhiran berkas.</p>'}
      </div>

      <div class="panel">
        <h2 style="font-size:1.4rem;margin-bottom:14px;border-bottom:2px solid #d97706;padding-bottom:8px;">Riwayat Prestasi & Penghargaan</h2>
        ${pkm.awards && pkm.awards.length ? `
          <ul class="styled-list">
            ${pkm.awards.map(aw => `<li>${aw}</li>`).join('')}
          </ul>
        ` : '<p>Puskesmas terus meningkatkan standar mutu akreditasi pelayanan primer di Kabupaten Pinrang.</p>'}
      </div>
    </div>

    <aside class="sidebar">
      <div class="panel" style="border-top:4px solid #078d90;">
        <div style="text-align:center;margin-bottom:16px;">
          <img src="assets/puskesmas.png" alt="Logo Puskesmas" style="width:64px;height:64px;object-fit:contain;">
          <h3 style="margin-top:10px;font-size:17px;">Layanan Poli Medis</h3>
        </div>
        <ul style="padding-left:18px;margin-top:10px;line-height:1.9;font-size:13.5px;color:#334155;">
          ${(pkm.services || []).map(s => `<li>${s}</li>`).join('')}
        </ul>
        <a href="puskesmas.html" class="btn secondary mt-20" style="width:100%;text-align:center;justify-content:center;">
          Lihat Semua 19 Puskesmas
        </a>
      </div>
    </aside>
  </div>`;
}

// ----------------- RENDER PENCARIAN -----------------
async function renderPencarian() {
  const urlParams = new URLSearchParams(window.location.search);
  const q = urlParams.get('q') || '';
  const result = await DataService.searchAll(q);

  return `
  ${pageHero('pencarian', 'MESIN PENCARI PORTAL', `Hasil Pencarian: "${q}"`, `Ditemukan ${result.articles.length} artikel dan ${result.puskesmas.length} Puskesmas yang relevan.`)}
  <div class="container py-40">
    <div style="max-width:700px;margin:0 auto 30px;">
      <form action="pencarian.html" class="v4-search-box" style="margin:0;">
        <span class="v4-search-icon">${ic('search')}</span>
        <input name="q" value="${q}" placeholder="Cari topik kesehatan, nama puskesmas, perizinan…" style="flex:1;border:none;outline:none;font-size:1rem;" required>
        <button type="submit" class="btn primary">Cari Ulang</button>
      </form>
    </div>

    ${result.puskesmas.length ? `
      <div style="margin-bottom:40px;">
        <h2 style="font-size:1.3rem;margin-bottom:16px;border-bottom:2px solid #1676f3;padding-bottom:6px;">Fasilitas Kesehatan Terkait</h2>
        <div class="grid grid-3">
          ${result.puskesmas.map(p => `
            <div class="pkm-card-pro">
              <div class="pkm-header">
                <div class="pkm-logo-box"><img src="assets/puskesmas.png" alt="Logo Puskesmas"></div>
                <div class="pkm-title-group">
                  <span class="pkm-kecamatan-tag">Kecamatan ${p.kecamatan}</span>
                  <h3>${p.name}</h3>
                </div>
              </div>
              <div class="pkm-body">
                <p style="font-size:13px;color:#64748b;">${p.address}</p>
                <div class="bottom mt-10">
                  <span>Kepala: <strong>${p.head}</strong></span>
                  <a href="puskesmas-detail.html?id=${p.id}">${ic('arrow')}</a>
                </div>
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    ` : ''}

    <div>
      <h2 style="font-size:1.3rem;margin-bottom:16px;border-bottom:2px solid #078d90;padding-bottom:6px;">Artikel & Berita Terkait</h2>
      ${result.articles.length ? `
        <div class="news-grid-pro">
          ${result.articles.map(a => `
            <article class="news-card-pro">
              <div class="thumb-wrap">
                <img src="${a.featured_image || 'assets/puskesmas.png'}" alt="${a.title}" loading="lazy">
                <span class="cat-badge ${getCategoryClass(a.category)}">${a.category}</span>
              </div>
              <div class="card-content">
                <div class="card-meta"><span>${ic('calendar')} ${a.published_at}</span></div>
                <h3><a href="berita-detail.html?id=${a.id}">${a.title}</a></h3>
                <p class="snippet">${a.excerpt}</p>
                <div class="card-footer">
                  <a href="berita-detail.html?id=${a.id}" class="read-action">Baca Ulasan ${ic('arrow')}</a>
                </div>
              </div>
            </article>
          `).join('')}
        </div>
      ` : '<p>Tidak ada artikel yang cocok dengan kata kunci pencarian.</p>'}
    </div>
  </div>`;
}

// ----------------- RENDER HALAMAN KELEMBAGAAN UMUM -----------------
async function renderGenericPage(page) {
  const pageMap = {
    profil: ['PROFIL INSTANSI', 'Profil Dinas Kesehatan Kabupaten Pinrang', 'Mengabdi untuk masyarakat Pinrang menuju derajat kesehatan yang mandiri dan optimal.'],
    organisasi: ['TATA KELOLA PEMERINTAHAN', 'Struktur Organisasi Dinas Kesehatan', 'Bagan hierarki kelembagaan, pembagian tugas bidang, dan koordinasi 19 UPTD Puskesmas.'],
    layanan: ['STANDAR PELAYANAN PUBLIK', 'Pelayanan Kesehatan Masyarakat', 'Informasi mengenai alur, standar, serta persyaratan layanan medis dan perizinan kesehatan daerah.'],
    'layanan-detail': ['PROGRAM KESEHATAN', 'Cek Kesehatan Gratis & Layanan Medis', 'Skrining kesehatan berkala dan panduan persiapan pemeriksaan gratis bagi warga.'],
    edukasi: ['PROMOSI KESEHATAN', 'Edukasi & Pembiasaan Hidup Sehat', 'Informasi kesehatan keluarga, gizi, imunisasi, dan pencegahan penyakit menular.'],
    'edukasi-detail': ['PANDUAN KESEHATAN', 'Gizi Seimbang & Pencegahan Stunting', 'Langkah nyata keluarga dalam memastikan asupan nutrisi optimal bagi ibu dan anak.'],
    galeri: ['DOKUMENTASI VISUAL', 'Galeri Kegiatan Dinas Kesehatan', 'Dokumentasi otentik pelaksanaan program kesehatan masyarakat di 12 kecamatan Pinrang.'],
    data: ['SATU DATA DAERAH', 'Data & Statistik Kesehatan', 'Data indikator capaian sektor kesehatan Kabupaten Pinrang yang akuntabel.'],
    indikator: ['AKUNTABILITAS KINERJA', 'Indikator Kinerja Utama (IKU)', 'Tolak ukur keberhasilan program kerja pembangunan kesehatan daerah.'],
    publikasi: ['DOKUMEN RESMI', 'Publikasi, Laporan & Perencanaan', 'Akses unduh Renja, Renstra, Laporan Kinerja Instansi Pemerintah (LKjIP), dan buletin SKDR.'],
    ppid: ['KETERBUKAAN INFORMASI PUBLIK', 'Pejabat Pengelola Informasi & Dokumentasi', 'Akses hak warga untuk memperoleh informasi publik secara transparan dan bertanggung jawab.'],
    informasi: ['PERMOHONAN INFORMASI', 'Formulir Keterbukaan Informasi Publik', 'Prosedur dan pengajuan permohonan informasi resmi kepada PPID Dinas Kesehatan.'],
    pengaduan: ['PARTISIPASI MASYARAKAT', 'Layanan Pengaduan & Aspirasi', 'Salurkan keluhan, kritik, dan saran pelayanan melalui SP4N-LAPOR! dan WhatsApp resmi.'],
    kontak: ['HUBUNGI KAMI', 'Kontak & Lokasi Kantor', 'Informasi alamat kantor, peta lokasi, nomor WhatsApp, serta media sosial resmi dinas.'],
    inovasi: ['PRAKTIK BAIK DAERAH', 'Inovasi UPTD Puskesmas Pinrang', 'Ragam inovasi pelayanan dari 19 Puskesmas untuk meningkatkan mutu taraf hidup warga.'],
    faq: ['PUSAT BANTUAN', 'Pertanyaan Umum (FAQ)', 'Jawaban atas pertanyaan yang sering diajukan seputar pelayanan dan fasilitas kesehatan.'],
    'peta-situs': ['NAVIGASI SITUS', 'Peta Situs Portal Terpadu', 'Struktur navigasi menyeluruh 28 laman portal informasi kesehatan Kabupaten Pinrang.'],
    privasi: ['PERLINDUNGAN DATA', 'Kebijakan Privasi', 'Komitmen perlindungan data dan privasi pengguna dalam pemanfaatan portal layanan publik.'],
    aksesibilitas: ['INKLUSIVITAS', 'Standar Aksesibilitas Web (WCAG 2.2)', 'Panduan aksesibilitas untuk memastikan kenyamanan pengguna disabilitas dan lansia.'],
    skm: ['MUTU PELAYANAN', 'Survei Kepuasan Masyarakat', 'Partisipasi publik dalam mengevaluasi mutu dan profesionalitas pelayanan kesehatan.'],
    pengumuman: ['SIARAN RESMI', 'Pengumuman Penting Pemerintah', 'Informasi resmi, surat edaran, serta himbauan kesehatan masyarakat terkini.'],
    'tidak-ditemukan': ['404 ERROR', 'Halaman Tidak Ditemukan', 'Halaman yang Anda tuju mungkin telah dipindahkan atau tautan tidak valid.']
  };

  const [kicker, title, desc] = pageMap[page] || ['DINAS KESEHATAN', 'Informasi Publik', ''];
  const pagesData = await DataService.getPages();
  const matchedData = pagesData.find(p => p.slug === page || p.slug.includes(page));

  return `
  ${pageHero(page, kicker, title, desc)}
  <div class="container layout-with-sidebar py-40">
    <div class="main-content">
      <div class="panel">
        ${matchedData ? matchedData.content : `
          <p class="lead">${desc}</p>
          <div class="good-note mt-20">
            Seluruh data dan informasi kelembagaan bersumber dari dokumentasi resmi Dinas Kesehatan Kabupaten Pinrang.
          </div>
          <p class="mt-20">Untuk informasi lebih lanjut dan permohonan konfirmasi langsung, hubungi kantor Dinas Kesehatan di <strong>Jl. Jenderal Sukawati, Kabupaten Pinrang</strong> atau melalui WhatsApp resmi <strong>+62 853-4217-2724</strong>.</p>
        `}
      </div>
    </div>
    <aside class="sidebar">
      <div class="panel side-nav">
        <h3>Menu Terkait</h3>
        ${link('profil', 'Profil Dinas')}
        ${link('organisasi', 'Struktur Organisasi')}
        ${link('layanan', 'Layanan Kesehatan')}
        ${link('puskesmas', 'Direktori 19 Puskesmas')}
        ${link('publikasi', 'Dokumen Kinerja (LKjIP)')}
        ${link('pengaduan', 'Layanan Pengaduan')}
        ${link('kontak', 'Kontak Dinas')}
      </div>
    </aside>
  </div>`;
}

// ----------------- INISIALISASI APLIKASI -----------------
async function initApp() {
  const page = document.body.dataset.page || 'index';
  const appContainer = document.getElementById('app');
  if (!appContainer) return;

  let bodyContent = '';
  if (page === 'index') {
    bodyContent = await renderHome();
  } else if (page === 'berita') {
    bodyContent = await renderBerita();
  } else if (page === 'berita-detail') {
    bodyContent = await renderBeritaDetail();
  } else if (page === 'puskesmas') {
    bodyContent = await renderPuskesmas();
  } else if (page === 'puskesmas-detail') {
    bodyContent = await renderPuskesmasDetail();
  } else if (page === 'pencarian') {
    bodyContent = await renderPencarian();
  } else {
    bodyContent = await renderGenericPage(page);
  }

  appContainer.innerHTML = `
    ${header(page)}
    <main id="main">
      ${bodyContent}
    </main>
    ${footer()}
  `;

  // Pasang event listener Font Resizer (Aa)
  const fontToggle = document.getElementById('fontToggle');
  if (fontToggle) {
    fontToggle.addEventListener('click', () => {
      document.body.classList.toggle('large-font');
    });
  }

  // Pasang event listener Mobile Menu
  const mobileToggle = document.getElementById('mobileToggle');
  const mobileNav = document.getElementById('mobileNav');
  if (mobileToggle && mobileNav) {
    mobileToggle.addEventListener('click', () => {
      const open = mobileNav.classList.toggle('is-open');
      mobileToggle.setAttribute('aria-expanded', String(open));
    });
  }

  // Pasang event listener Quick Search
  const searchToggle = document.getElementById('searchToggle');
  const quickSearch = document.getElementById('quickSearch');
  if (searchToggle && quickSearch) {
    searchToggle.addEventListener('click', () => {
      const open = quickSearch.classList.toggle('is-open');
      if (open) document.getElementById('quickSearchInput')?.focus();
    });
  }

  // Inisialisasi Hero Slider jika ada
  if (page === 'index') {
    const slides = Array.from(document.querySelectorAll('.v4-feature-slide'));
    const dots = Array.from(document.querySelectorAll('[data-slide-to]'));
    let slideIdx = 0;

    function showSlide(next) {
      slideIdx = (next + slides.length) % slides.length;
      slides.forEach((s, i) => {
        const active = i === slideIdx;
        s.hidden = !active;
        s.classList.toggle('is-active', active);
      });
      dots.forEach((d, i) => {
        d.classList.toggle('active', i === slideIdx);
      });
    }

    dots.forEach(d => d.addEventListener('click', () => showSlide(Number(d.dataset.slideTo))));
    document.querySelectorAll('[data-slide-step]').forEach(b => {
      b.addEventListener('click', () => showSlide(slideIdx + Number(b.dataset.slideStep)));
    });
  }
}

// Jalankan ketika DOM siap
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initApp);
} else {
  initApp();
}
