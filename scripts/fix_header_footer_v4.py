# -*- coding: utf-8 -*-
import json
import os

with open('public/data/puskesmas.json', 'r', encoding='utf-8') as f:
    puskesmas_list = json.load(f)

with open('public/data/articles.json', 'r', encoding='utf-8') as f:
    articles_list = json.load(f)

compact_articles = []
for a in articles_list:
    exc = a.get('excerpt', '')
    if len(exc) > 170:
        exc = exc[:170] + '...'
    compact_articles.append({
        'id': str(a.get('id')),
        'title': a.get('title'),
        'slug': a.get('slug'),
        'published_at': a.get('published_at'),
        'author': a.get('author'),
        'category': a.get('category') or 'Berita',
        'featured_image': a.get('featured_image'),
        'excerpt': exc
    })

pkm_json_str = json.dumps(puskesmas_list, ensure_ascii=False)
art_json_str = json.dumps(compact_articles, ensure_ascii=False)

# Baca SVG dict dari DINKES_PINRANG_MOCKUP_V4/assets/app.js
with open('DINKES_PINRANG_MOCKUP_V4/assets/app.js', 'r', encoding='utf-8') as f:
    orig_app = f.read()

svg_part = orig_app.split('const SVG={')[1].split('};')[0]

header_footer_code = f"""// Dinas Kesehatan Pemerintah Kabupaten Pinrang - Portal Resmi Web App V4 Definitive
'use strict';

window.PUSKESMAS_DATA = {pkm_json_str};
window.ARTICLES_CACHE = {art_json_str};

function getSafeImageUrl(url) {{
  if (!url) return 'assets/logo_pinrang_opt.png';
  let clean = url.replace(/-\\d+x\\d+(\\.[a-zA-Z0-9]+)$/, '$1');
  if (location.hostname === 'localhost' || location.hostname === '127.0.0.1') {{
    return clean.replace('https://dinkes.pinrangkab.go.id/wp-content/uploads/', 'uploads/');
  }}
  return clean;
}}

const SVG={{{svg_part}}};
function ic(n,cls=''){{return `<svg aria-hidden="true" class="${{cls}}" viewBox="0 0 24 24">${{SVG[n]||SVG.heart}}</svg>`}}

const ROUTES=[
  ['index','Beranda','home'],
  ['profil','Profil Dinas','people'],
  ['organisasi','Struktur Organisasi','layers'],
  ['layanan','Layanan Kesehatan','heart'],
  ['layanan-detail','Detail Layanan','clipboard'],
  ['puskesmas','Direktori Puskesmas','hospital'],
  ['puskesmas-detail','Profil Puskesmas','hospital'],
  ['edukasi','Edukasi Kesehatan','book'],
  ['edukasi-detail','Artikel Edukasi','book'],
  ['berita','Berita & Kegiatan','news'],
  ['berita-detail','Detail Berita','news'],
  ['galeri','Galeri Foto','camera'],
  ['data','Data Kesehatan','chart'],
  ['indikator','Indikator','bars'],
  ['publikasi','Publikasi & Dokumen','file'],
  ['ppid','PPID','shield'],
  ['informasi','Permohonan Informasi','mail'],
  ['pengaduan','Pengaduan','message'],
  ['kontak','Kontak','pin'],
  ['inovasi','Inovasi','bulb'],
  ['faq','FAQ','info'],
  ['pencarian','Pencarian','search'],
  ['peta-situs','Peta Situs','layers'],
  ['privasi','Kebijakan Privasi','lock'],
  ['aksesibilitas','Aksesibilitas','heart'],
  ['skm','Survei Kepuasan (SKM)','star'],
  ['pengumuman','Pengumuman','bell'],
  ['tidak-ditemukan','Halaman Tidak Ditemukan','search']
];

const path=(id)=>ROUTES.find(r=>r[0]===id)?.[0]+'.html'||'#';
const link=(id,label,cls='')=>`<a class="${{cls?cls+' ':''}}nav-link" href="${{path(id)}}">${{label}}</a>`;

function header(page){{
  const group=(name,arr)=>`<div class="navgroup"><button type="button" aria-haspopup="true" aria-expanded="false">${{name}}${{ic('down')}}</button><div class="drop">${{arr.map(a=>link(a[0],a[1])).join('')}}</div></div>`;
  const menu=[['Informasi Publik',[['ppid','PPID'],['publikasi','Dokumen & Publikasi'],['informasi','Permohonan Informasi']]],['Tentang Dinas',[['profil','Profil Dinas'],['organisasi','Struktur Organisasi'],['inovasi','Inovasi & Prestasi'],['kontak','Kontak']]]];
  const mn=[['Layanan',[['layanan','Semua layanan'],['layanan-detail','Detail SOP layanan'],['puskesmas','Direktori Puskesmas']]],['Informasi',[['edukasi','Edukasi'],['berita','Berita & Kegiatan'],['galeri','Galeri Foto'],['data','Data Kesehatan']]],...menu];
  
  return `<a class="skip" href="#main">Langsung ke konten utama</a>
  <div class="govbar"><div class="container"><div>Pemerintah Kabupaten Pinrang · Sulawesi Selatan</div><div class="right"><a href="https://pinrangkab.go.id/" target="_blank" rel="noopener">Portal Pemkab ${{ic('external')}}</a>${{link('ppid','PPID')}}${{link('skm','SKM')}}${{link('faq','Bantuan')}}</div></div></div>
  <header class="brandbar"><div class="container"><a class="identity" href="index.html" aria-label="Dinas Kesehatan Kabupaten Pinrang, Beranda">
    <div style="display:flex;align-items:center;gap:10px;margin-right:12px;">
      <img src="assets/logo_pinrang_opt.png" alt="Logo Pemkab Pinrang" style="height:46px;width:auto;display:block;" />
      <img src="assets/kemenkes.jpg" alt="Logo Kemenkes RI" style="height:46px;width:auto;display:block;border-radius:4px;" />
    </div>
    <span><span class="overline">Pemerintah Kabupaten Pinrang</span><strong>DINAS KESEHATAN</strong><small>Portal Informasi & Pelayanan Kesehatan Masyarakat</small></span></a>
    <div class="header-controls"><a class="soft-link" href="puskesmas.html">${{ic('pin')}} Cari Fasilitas Kesehatan</a><button class="icon-button" type="button" id="fontToggle" title="Perbesar tulisan" aria-label="Perbesar tulisan">Aa</button><button class="icon-button" type="button" id="searchToggle" aria-label="Buka pencarian">${{ic('search')}}</button></div></div></header>
  <nav class="navwrap" aria-label="Navigasi utama"><div class="container navrow"><div class="navitems">${{link('index','Beranda',page==='index'?'active':'')}}${{group('Layanan',[['layanan','Layanan Kesehatan'],['layanan-detail','Standar SOP Layanan'],['puskesmas','Direktori 19 Puskesmas']])}}${{link('edukasi','Edukasi',page==='edukasi'?'active':'')}}${{link('data','Data Kesehatan',page==='data'?'active':'')}}${{link('berita','Berita & Kegiatan',page==='berita'?'active':'')}}${{group('Transparansi',[['ppid','PPID'],['publikasi','Publikasi & Dokumen'],['pengumuman','Pengumuman Penting'],['informasi','Permohonan Informasi']])}}${{group('Profil',[['profil','Tentang Dinas'],['organisasi','Struktur Organisasi'],['inovasi','Inovasi & Prestasi'],['galeri','Galeri Foto'],['kontak','Kontak']])}}</div><a class="nav-cta" href="pengaduan.html">${{ic('message')}} Pengaduan</a><button class="icon-button hamburger" id="mobileToggle" type="button" aria-label="Buka menu navigasi" aria-expanded="false">${{ic('menu')}}</button></div><div class="mobile-nav" id="mobileNav">${{link('index','Beranda')}}${{mn.map(([name,items])=>`<h4>${{name}}</h4>${{items.map(v=>link(v[0],v[1])).join('')}}`).join('')}}${{link('pengaduan','Pengaduan')}}${{link('kontak','Kontak')}}</div><div class="floating-search" id="quickSearch"><div class="container"><form id="quickSearchForm" action="pencarian.html"><input id="quickSearchInput" name="q" type="search" placeholder="Cari Puskesmas, layanan, berita, dokumen..." aria-label="Cari seluruh konten" required><button class="btn primary" type="submit">${{ic('search')}} Cari</button></form></div></div></nav>`;
}}

function footer(){{
  return `<footer class="footer"><div class="container"><div class="top">
    <div>
      <div class="identity">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
          <img src="assets/logo_pinrang_opt.png" alt="Logo Pemkab Pinrang" style="height:46px;width:auto;" />
          <img src="assets/kemenkes.jpg" alt="Logo Kemenkes RI" style="height:46px;width:auto;border-radius:4px;" />
        </div>
        <span><span class="overline">Pemerintah Kabupaten Pinrang</span><strong>DINAS KESEHATAN</strong><small>Portal Informasi & Pelayanan Kesehatan Masyarakat</small></span>
      </div>
      <p style="margin:12px 0 16px 0;font-size:14px;color:#cbd5e1;line-height:1.6;">
        Mewujudkan transformasi layanan kesehatan primer yang merata, berkualitas, berkeadilan, dan terjangkau di 12 kecamatan se-Kabupaten Pinrang.
      </p>
      <p><span class="tag" style="background:rgba(10,163,152,0.25);color:#5eead4;border:1px solid #0aa398;padding:4px 12px;border-radius:999px;font-size:12px;font-weight:700;">Membawahi 19 UPTD Puskesmas Resmi</span></p>
    </div>
    <div>
      <h3>Untuk Masyarakat</h3>
      ${{link('layanan','Standar & Layanan')}}
      ${{link('layanan-detail','SOP Rekomendasi Izin')}}
      ${{link('puskesmas','Direktori 19 Puskesmas')}}
      ${{link('edukasi','Edukasi Kesehatan')}}
      ${{link('pengaduan','Pengaduan Pelayanan')}}
    </div>
    <div>
      <h3>Informasi Publik</h3>
      ${{link('ppid','Layanan PPID')}}
      ${{link('publikasi','Publikasi & Dokumen (LKjIP)')}}
      ${{link('pengumuman','Pengumuman Penting')}}
      ${{link('data','Satu Data Kesehatan')}}
      ${{link('inovasi','Inovasi & Prestasi Daerah')}}
    </div>
    <div>
      <h3>Rujukan Resmi</h3>
      <a href="https://pinrangkab.go.id/" target="_blank" rel="noopener">Portal Pemkab Pinrang</a>
      <a href="https://kemkes.go.id/" target="_blank" rel="noopener">Kementerian Kesehatan RI</a>
      <a href="https://satusehat.kemkes.go.id/" target="_blank" rel="noopener">SATUSEHAT Kemenkes</a>
      <a href="https://www.lapor.go.id/" target="_blank" rel="noopener">SP4N-LAPOR!</a>
      <a href="https://ayosehat.kemkes.go.id/" target="_blank" rel="noopener">Ayo Sehat Kemenkes</a>
    </div>
  </div>
  <div class="copy" style="border-top:1px solid rgba(255,255,255,0.1);padding-top:20px;margin-top:28px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;">
    <span>© 2026 Dinas Kesehatan Pemerintah Kabupaten Pinrang. Seluruh hak cipta dilindungi undang-undang.</span>
    <span>${{link('privasi','Kebijakan Privasi')}} · ${{link('aksesibilitas','Aksesibilitas')}} · ${{link('peta-situs','Peta Situs')}}</span>
  </div>
  </div></footer>`;
}}

function pageHero(page,kicker,title,desc){{
  const heroIcon=({{profil:'people',organisasi:'layers',layanan:'heart','layanan-detail':'clipboard',puskesmas:'hospital','puskesmas-detail':'pin',edukasi:'book','edukasi-detail':'bulb',berita:'news','berita-detail':'news',galeri:'camera',data:'chart',indikator:'bars',publikasi:'file',ppid:'shield',informasi:'mail',pengaduan:'message',kontak:'pin',inovasi:'bulb',faq:'info',pencarian:'search','peta-situs':'layers',privasi:'lock',aksesibilitas:'heart',skm:'star',pengumuman:'bell','tidak-ditemukan':'search'}})[page]||'heart';
  return `<section class="pagehero v4-pagehero"><div class="container"><div class="crumbs"><a href="index.html">Beranda</a>${{ic('chevron')}}<span aria-current="page">${{ROUTES.find(r=>r[0]===page)?.[1]||page}}</span></div><div class="wrap"><div class="pagehero-copy"><span class="tinycap">${{kicker}}</span><h1>${{title}}</h1><p>${{desc}}</p></div><div class="pagehero-visual" aria-hidden="true"><span class="visual-ring ring-one"></span><span class="visual-ring ring-two"></span><span class="pagehero-icon">${{ic(heroIcon)}}</span><span class="decor-dot d1"></span><span class="decor-dot d2"></span></div></div></div></section>`;
}}

const side=(title,items)=>`<aside class="panel side-nav"><h3>${{title}}</h3>${{items.map(([id,label])=>link(id,`${{label}}${{ic('chevron')}}`,window.CURRENT_PAGE===id?'active':'')).join('')}}<div class="panel mt-20" style="background:#f0fdf9;border:1px solid #bbf7d0;padding:16px;border-radius:12px;"><h4 style="font-size:14px;font-weight:700;color:#065f46;margin-bottom:6px;">Kanal Pengaduan Resmi</h4><p style="font-size:12.5px;color:#475569;line-height:1.5;margin-bottom:10px;">Sampaikan saran dan aduan pelayanan kesehatan via WhatsApp resmi.</p><a href="https://wa.me/6285342172724" target="_blank" rel="noopener" class="btn primary" style="font-size:12.5px;padding:6px 12px;width:100%;text-align:center;justify-content:center;">${{ic('phone')}} WA: +62 853-4217-2724</a></div></aside>`;
"""

with open('scripts/build_definitive_app.py', 'w', encoding='utf-8') as f:
    f.write(header_footer_code)

print("Sukses update scripts/build_definitive_app.py dengan markup V4 asli!")

