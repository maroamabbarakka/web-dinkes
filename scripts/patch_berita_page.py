import re

with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Definisikan implementasi baru beritaPage() dengan Tab Kategori Dinamis & Poster Layout
new_berita_page = """// 6. BERITA & KEGIATAN DENGAN KATEGORISASI TERPISAH (beritaPage)
function beritaPage() {
  const articles = window.ARTICLES_CACHE || [];
  const currentTab = new URLSearchParams(location.search).get('tab') || 'semua';
  const searchQuery = new URLSearchParams(location.search).get('q') || '';
  
  // Hitung jumlah masing-masing kategori
  const countAll = articles.length;
  const countBerita = articles.filter(a => a.content_type === 'berita').length;
  const countArtikel = articles.filter(a => a.content_type === 'artikel').length;
  const countPromkes = articles.filter(a => a.content_type === 'promkes').length;
  const countDokumentasi = articles.filter(a => a.content_type === 'dokumentasi').length;

  // Filter artikel berdasarkan tab aktif dan search query
  let filtered = articles;
  if (currentTab === 'berita') {
    filtered = filtered.filter(a => a.content_type === 'berita');
  } else if (currentTab === 'artikel') {
    filtered = filtered.filter(a => a.content_type === 'artikel');
  } else if (currentTab === 'promkes') {
    filtered = filtered.filter(a => a.content_type === 'promkes');
  } else if (currentTab === 'dokumentasi') {
    filtered = filtered.filter(a => a.content_type === 'dokumentasi');
  }

  if (searchQuery) {
    const qLower = searchQuery.toLowerCase();
    filtered = filtered.filter(a => a.title.toLowerCase().includes(qLower) || (a.excerpt && a.excerpt.toLowerCase().includes(qLower)));
  }

  const tabs = [
    { id: 'semua', label: 'Semua Publikasi', count: countAll, icon: 'news' },
    { id: 'berita', label: 'Berita & Kegiatan Dinas', count: countBerita, icon: 'activity' },
    { id: 'artikel', label: 'Artikel Kesehatan & Edukasi', count: countArtikel, icon: 'heart' },
    { id: 'promkes', label: 'Materi Promkes & Poster', count: countPromkes, icon: 'image' },
    { id: 'dokumentasi', label: 'Dokumentasi Lapangan', count: countDokumentasi, icon: 'camera' }
  ];

  return pageHero('berita', 'Pusat Informasi & Publikasi', 'Kabar, Edukasi & Dokumentasi Kesehatan', 'Menyajikan liputan kegiatan dinas, artikel medis terpercaya, materi promosi kesehatan (GERMAS), dan dokumentasi lapangan se-Kabupaten Pinrang.') + `
  <section class="content" style="padding: 30px 0 60px 0;">
    <div class="container">
      
      <!-- TAB FILTER KATEGORI -->
      <div style="display:flex;gap:10px;overflow-x:auto;padding-bottom:16px;margin-bottom:24px;border-bottom:2px solid #e2e8f0;scrollbar-width:none;">
        ${tabs.map(t => {
          const isActive = currentTab === t.id;
          return `
            <a href="berita.html?tab=${t.id}${searchQuery ? '&q=' + encodeURIComponent(searchQuery) : ''}" 
               style="text-decoration:none;padding:10px 18px;border-radius:12px;font-size:13.5px;font-weight:700;display:inline-flex;align-items:center;gap:8px;white-space:nowrap;transition:all .2s;${isActive ? 'background:#087f89;color:#ffffff;box-shadow:0 4px 14px rgba(8,127,137,0.3);' : 'background:#f1f5f9;color:#475569;border:1px solid #e2e8f0;'}">
              ${t.label} <span style="background:${isActive ? 'rgba(255,255,255,0.25)' : '#e2e8f0'};padding:2px 8px;border-radius:20px;font-size:11px;">${t.count}</span>
            </a>
          `;
        }).join('')}
      </div>

      <!-- SEARCH BAR DALAM HALAMAN -->
      <div style="background:#ffffff;border:1px solid #dce8eb;border-radius:16px;padding:16px 20px;margin-bottom:30px;box-shadow:0 4px 20px rgba(0,0,0,0.02);display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px;">
        <form action="berita.html" method="GET" style="display:flex;flex-grow:1;gap:10px;max-width:600px;">
          <input type="hidden" name="tab" value="${currentTab}" />
          <div style="position:relative;flex-grow:1;">
            <input type="text" name="q" value="${searchQuery}" placeholder="Cari judul berita, topik stunting, nakes, atau kata kunci..." 
                   style="width:100%;padding:10px 16px 10px 38px;border:1px solid #cbd5e1;border-radius:10px;font-size:14px;outline:none;" />
            <div style="position:absolute;left:12px;top:50%;transform:translateY(-50%);color:#94a3b8;width:16px;height:16px;">
              ${ic('search')}
            </div>
          </div>
          <button type="submit" class="btn primary" style="padding:10px 20px;font-size:13.5px;font-weight:700;">Cari</button>
          ${searchQuery ? `<a href="berita.html?tab=${currentTab}" class="btn secondary" style="padding:10px 14px;font-size:13px;">Reset</a>` : ''}
        </form>
        <div style="font-size:13.5px;color:#64748b;font-weight:600;">
          Menampilkan <strong style="color:#087f89;">${filtered.length}</strong> publikasi
        </div>
      </div>

      <!-- RENDER KHUSUS: MATERI PROMKES & POSTER (ASPEK RASIO VERTIKAL, TIDAK TERPOTONG) -->
      ${currentTab === 'promkes' ? `
        <div class="grid grid-3" style="gap:24px;">
          ${filtered.map(item => `
            <article class="panel" style="background:#ffffff;border:1px solid #e2e8f0;border-radius:18px;overflow:hidden;box-shadow:0 6px 20px rgba(0,0,0,0.04);display:flex;flex-direction:column;">
              <div style="background:#0f172a;padding:12px;display:flex;align-items:center;justify-content:center;min-height:380px;">
                <img src="${item.featured_image || 'assets/kantor_dinkes_pinrang.jpg'}" alt="${item.title}" 
                     style="max-height:360px;width:auto;max-width:100%;object-fit:contain;border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,0.3);" />
              </div>
              <div style="padding:20px;display:flex;flex-direction:column;flex-grow:1;">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
                  <span style="background:#fef3c7;color:#b45309;font-size:11px;font-weight:800;padding:4px 10px;border-radius:6px;text-transform:uppercase;">Materi Promkes</span>
                  <span style="font-size:12px;color:#94a3b8;">${item.published_at || ''}</span>
                </div>
                <h3 style="font-size:17px;font-weight:800;color:#1e293b;line-height:1.35;margin-bottom:12px;">${item.title}</h3>
                <p style="font-size:13px;color:#64748b;line-height:1.55;margin-bottom:20px;flex-grow:1;">${item.excerpt ? item.excerpt.slice(0, 110) + '...' : 'Materi edukasi visual resmi Dinas Kesehatan Kabupaten Pinrang.'}</p>
                <div style="display:flex;gap:10px;">
                  <a href="${item.featured_image}" target="_blank" class="btn secondary" style="font-size:12.5px;padding:8px 12px;flex:1;justify-content:center;">
                    ${ic('search')} Gambar Utuh
                  </a>
                  <a href="berita-detail.html?id=${item.id}" class="btn primary" style="font-size:12.5px;padding:8px 14px;flex:1;justify-content:center;">
                    Detail ${ic('arrow')}
                  </a>
                </div>
              </div>
            </article>
          `).join('')}
        </div>
      ` : currentTab === 'artikel' ? `
        <!-- RENDER KHUSUS: ARTIKEL KESEHATAN & EDUKASI MEDIS -->
        <div class="grid grid-3" style="gap:24px;">
          ${filtered.map(item => `
            <article class="panel" style="background:#ffffff;border:1px solid #e2e8f0;border-radius:18px;overflow:hidden;box-shadow:0 6px 20px rgba(0,0,0,0.04);display:flex;flex-direction:column;transition:transform .2s;">
              <div style="height:200px;overflow:hidden;position:relative;">
                <img src="${item.featured_image || 'assets/kantor_dinkes_pinrang.jpg'}" alt="${item.title}" style="width:100%;height:100%;object-fit:cover;" />
                <span style="position:absolute;top:12px;left:12px;background:#087f89;color:#ffffff;font-size:11px;font-weight:800;padding:4px 10px;border-radius:6px;">Edukasi Medis</span>
              </div>
              <div style="padding:22px;display:flex;flex-direction:column;flex-grow:1;">
                <div style="font-size:12px;color:#94a3b8;margin-bottom:8px;">Terbit: ${item.published_at || ''} • Oleh: ${item.author || 'Tim Kesehatan'}</div>
                <h3 style="font-size:17px;font-weight:800;color:#1e293b;line-height:1.35;margin-bottom:12px;">
                  <a href="berita-detail.html?id=${item.id}" style="color:inherit;text-decoration:none;">${item.title}</a>
                </h3>
                <p style="font-size:13.5px;color:#64748b;line-height:1.6;margin-bottom:20px;flex-grow:1;">${item.excerpt ? item.excerpt.slice(0, 130) + '...' : 'Informasi dan panduan kesehatan dari nakes profesional Dinas Kesehatan Pinrang.'}</p>
                <a href="berita-detail.html?id=${item.id}" class="btn primary" style="font-size:13px;padding:9px 16px;align-self:flex-start;">
                  Baca Artikel ${ic('arrow')}
                </a>
              </div>
            </article>
          `).join('')}
        </div>
      ` : `
        <!-- RENDER UMUM: BERITA & KEGIATAN DINAS -->
        <div class="grid grid-3" style="gap:24px;">
          ${filtered.slice(0, 48).map(item => `
            <article class="panel" style="background:#ffffff;border:1px solid #e2e8f0;border-radius:18px;overflow:hidden;box-shadow:0 6px 20px rgba(0,0,0,0.04);display:flex;flex-direction:column;transition:transform .2s;">
              <div style="height:210px;overflow:hidden;position:relative;">
                <img src="${item.featured_image || 'assets/kantor_dinkes_pinrang.jpg'}" alt="${item.title}" style="width:100%;height:100%;object-fit:cover;" />
                <span style="position:absolute;top:12px;left:12px;background:rgba(16,43,86,0.85);backdrop-filter:blur(4px);color:#ffffff;font-size:11px;font-weight:800;padding:4px 10px;border-radius:6px;text-transform:uppercase;">
                  ${item.type_label || 'Berita Dinas'}
                </span>
              </div>
              <div style="padding:22px;display:flex;flex-direction:column;flex-grow:1;">
                <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:#94a3b8;margin-bottom:8px;">
                  ${ic('calendar')} ${item.published_at || ''} · ${item.author || 'Dinkes Pinrang'}
                </div>
                <h3 style="font-size:16.5px;font-weight:800;color:#1e293b;line-height:1.4;margin-bottom:12px;">
                  <a href="berita-detail.html?id=${item.id}" style="color:inherit;text-decoration:none;">${item.title}</a>
                </h3>
                <p style="font-size:13.5px;color:#64748b;line-height:1.6;margin-bottom:20px;flex-grow:1;">
                  ${item.excerpt ? item.excerpt.slice(0, 120) + '...' : 'Dokumentasi dan publikasi kegiatan Dinas Kesehatan Pemerintah Kabupaten Pinrang.'}
                </p>
                <a href="berita-detail.html?id=${item.id}" class="btn primary" style="font-size:13px;padding:8px 16px;align-self:flex-start;">
                  Baca Selengkapnya ${ic('arrow')}
                </a>
              </div>
            </article>
          `).join('')}
        </div>
      `}

    </div>
  </section>`;
}
"""

# Cari posisi fungsi beritaPage() lama
old_berita_pos = code.find('function beritaPage()')
if old_berita_pos != -1:
    next_func_pos = code.find('// 7. DETAIL BERITA', old_berita_pos)
    if next_func_pos == -1:
        next_func_pos = code.find('function beritaDetailPage()', old_berita_pos)
    
    code = code[:old_berita_pos] + new_berita_page + "\n" + code[next_func_pos:]
    print("beritaPage() berhasil diperbarui dengan tab pengelompokan terpisah!")
else:
    print("beritaPage() tidak ditemukan!")

with open('public/assets/app.js', 'w', encoding='utf-8') as f:
    f.write(code)

