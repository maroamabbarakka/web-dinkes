
// 4. DIREKTORI PUSKESMAS (puskesmasPage)
function puskesmasPage() {
  const pkm = window.PUSKESMAS_DATA || [];
  const districts = [...new Set(pkm.map(x => x.district))].sort();

  return pageHero('puskesmas','Fasilitas Pelayanan Primer','Direktori 19 UPTD Puskesmas Kabupaten Pinrang','Informasi lengkap 19 Puskesmas di 12 kecamatan se-Kabupaten Pinrang, mencakup nama Kepala Puskesmas, inovasi unggulan, alamat, jam pelayanan, dan penghargaan.')+`<section class="content"><div class="container">
    
    <!-- Filter Bar -->
    <div class="searchline" style="display:flex;gap:12px;margin-bottom:24px;flex-wrap:wrap;">
      <input id="pkmSearch" type="search" placeholder="Cari nama Puskesmas, kecamatan, kepala puskesmas, atau inovasi..." style="flex:1;min-width:260px;" />
      <select id="pkmDistrict" style="min-width:180px;">
        <option value="">Semua Kecamatan (12)</option>
        ${districts.map(d => `<option value="${d}">${d}</option>`).join('')}
      </select>
      <button class="btn secondary" type="button" id="pkmReset">${ic('refresh')} Reset</button>
    </div>

    <!-- Alert Fasilitas -->
    <div style="background:#f0fdf9;border:1px solid #bbf7d0;border-radius:14px;padding:16px 20px;margin-bottom:28px;display:flex;align-items:center;gap:14px;">
      <div style="color:#087f89;font-size:24px;">${ic('shield')}</div>
      <div style="font-size:13.5px;color:#1e293b;line-height:1.5;">
        <strong>Komitmen Standar Pelayanan:</strong> Seluruh 19 UPTD Puskesmas di Kabupaten Pinrang telah terakreditasi oleh Kementerian Kesehatan RI dan menyelenggarakan pelayanan rawat jalan terpadu serta Pelayanan Gawat Darurat (IGD) & Persalinan 24 Jam.
      </div>
    </div>

    <!-- Grid Puskesmas -->
    <div class="v4-pkm-grid" id="pkmGrid">
      ${pkm.map(p => `
        <div class="v4-pkm-card" data-name="${p.name.toLowerCase()}" data-district="${p.district.toLowerCase()}" data-kapus="${(p.head||'').toLowerCase()}" data-inovasi="${(p.innovations_text||'').toLowerCase()}">
          <div class="v4-pkm-card-header">
            <img src="assets/puskesmas.png" alt="Logo Puskesmas" class="v4-pkm-logo" />
            <div class="v4-pkm-meta">
              <span class="v4-pkm-kec">Kecamatan ${p.district}</span>
              <h3>${p.name}</h3>
            </div>
          </div>
          <div class="v4-pkm-head">
            ${ic('user')} <span>Kepala Puskesmas: <strong>${p.head || 'Dinas Kesehatan'}</strong></span>
          </div>
          <p style="font-size:13px;color:#64748b;line-height:1.5;margin-bottom:12px;">
            ${ic('location')} ${p.address}
          </p>
          ${p.innovations_text ? `
            <div class="v4-pkm-inovasi">
              <strong>Inovasi Unggulan:</strong>
              ${p.innovations_text}
            </div>
          ` : ''}
          ${p.awards_text ? `
            <div style="font-size:12.5px;color:#0369a1;background:#f0f9ff;border-radius:8px;padding:8px 12px;margin-bottom:14px;">
              <strong>${ic('award')} Prestasi / Penghargaan:</strong><br>
              ${p.awards_text}
            </div>
          ` : ''}
          <div style="margin-top:auto;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #edf2f3;padding-top:14px;">
            <span style="font-size:11.5px;font-weight:700;color:#059669;background:#ecfdf5;padding:4px 8px;border-radius:6px;">
              IGD & Bersalin 24 Jam
            </span>
            <a href="puskesmas-detail.html?no=${p.no}" class="btn primary" style="font-size:13px;padding:6px 14px;">
              Detail Profil ${ic('arrow')}
            </a>
          </div>
        </div>
      `).join('')}
    </div>
    <div id="pkmEmpty" class="hidden text-center" style="padding:40px;background:#f8fafc;border-radius:14px;margin-top:20px;">
      <p style="font-size:16px;color:#64748b;">Tidak ada Puskesmas yang sesuai dengan pencarian atau filter kecamatan.</p>
    </div>
  </div></section>`;
}

// 5. DETAIL PUSKESMAS (puskesmasDetailPage)
function puskesmasDetailPage() {
  const pkm = window.PUSKESMAS_DATA || [];
  const params = new URLSearchParams(location.search);
  const pkmNo = parseInt(params.get('no') || '1');
  const item = pkm.find(x => x.no === pkmNo) || pkm[0] || {
    name: 'Puskesmas Suppa',
    district: 'Suppa',
    head: 'dr. MUHAMMAD LUTFY',
    address: 'Jl. A. Monjong Wanuae. Kel. Wt. Suppa Kec.Suppa Kab.Pinrang Kode Pos 91272',
    innovations_text: '1. Gemas (Gerakan Masyarakat Sehat) 2. Suka Kesorga (Suppa Kecamatan Olahraga)',
    awards_text: '1. Sanitarian/petugas Kesling Terbaik kab. ODF 100% 2. Penghargaan pengimputan e-PPGBM'
  };

  return pageHero('puskesmas-detail', `UPTD PUSKESMAS - KEC. ${item.district.toUpperCase()}`, item.name, `Pusat pelayanan kesehatan tingkat pertama masyarakat Kecamatan ${item.district}, melayani dengan dedikasi dan profesionalisme.`)+`<section class="content"><div class="container twocol"><div class="stack">

  <article class="panel">
    <div style="display:flex;align-items:center;gap:18px;margin-bottom:20px;border-bottom:1px solid #edf2f3;padding-bottom:18px;">
      <img src="assets/puskesmas.png" alt="Logo Puskesmas" style="width:60px;height:60px;object-fit:contain;background:#f0fdf9;border:1px solid #bbf7d0;border-radius:14px;padding:8px;" />
      <div>
        <span class="v4-pkm-kec">UPTD DINAS KESEHATAN KABUPATEN PINRANG</span>
        <h2 style="margin:2px 0 0 0;font-size:24px;color:#103447;">${item.name}</h2>
      </div>
    </div>

    <div class="grid grid-2" style="gap:16px;margin-bottom:24px;">
      <div style="background:#f8fafc;padding:16px;border-radius:12px;border:1px solid #e2e8f0;">
        <span style="font-size:11px;font-weight:700;color:#64748b;text-transform:uppercase;">Kepala Puskesmas:</span>
        <h4 style="margin:4px 0 0 0;font-size:16px;color:#103447;">${item.head || 'Dinas Kesehatan'}</h4>
        <span style="font-size:12px;color:#087f89;">Penanggung Jawab Teknis Operasional</span>
      </div>
      <div style="background:#f8fafc;padding:16px;border-radius:12px;border:1px solid #e2e8f0;">
        <span style="font-size:11px;font-weight:700;color:#64748b;text-transform:uppercase;">Status Akreditasi:</span>
        <h4 style="margin:4px 0 0 0;font-size:16px;color:#059669;">Paripurna (Kemenkes RI)</h4>
        <span style="font-size:12px;color:#64748b;">Standar Mutu & Keselamatan Pasien</span>
      </div>
    </div>

    <h3 style="font-size:17px;font-weight:700;color:#103447;margin-bottom:12px;">Alamat & Wilayah Kerja</h3>
    <p style="font-size:14.5px;color:#334155;line-height:1.7;margin-bottom:20px;">
      ${ic('location')} <strong>Alamat Kantor:</strong> ${item.address}<br>
      ${ic('clock')} <strong>Jam Pelayanan:</strong> Senin s.d Sabtu: 08:00 - 14:00 WITA<br>
      ${ic('shield')} <strong>Instalasi Gawat Darurat (IGD) & Bersalin:</strong> Buka 24 Jam Setiap Hari
    </p>

    <h3 style="font-size:17px;font-weight:700;color:#103447;margin-bottom:12px;">Inovasi Pelayanan Kesehatan Unggulan</h3>
    <div style="background:#ecfdf5;border:1px solid #a7f3d0;border-radius:12px;padding:16px 20px;margin-bottom:24px;">
      <p style="font-size:14px;color:#065f46;line-height:1.7;margin:0;">
        ${item.innovations_text || 'Inovasi pelayanan pencegahan stunting, pemantauan kesehatan keluarga mandiri, dan deteksi dini penyakit.'}
      </p>
    </div>

    ${item.awards_text ? `
      <h3 style="font-size:17px;font-weight:700;color:#103447;margin-bottom:12px;">Prestasi & Penghargaan yang Diraih</h3>
      <div style="background:#f0f9ff;border:1px solid #bae6fd;border-radius:12px;padding:16px 20px;margin-bottom:24px;">
        <p style="font-size:14px;color:#0369a1;line-height:1.7;margin:0;">
          ${item.awards_text}
        </p>
      </div>
    ` : ''}

    <h3 style="font-size:17px;font-weight:700;color:#103447;margin-bottom:14px;">Jenis Poli & Fasilitas Pelayanan</h3>
    <div class="grid grid-2" style="gap:12px;">
      <div style="background:#ffffff;border:1px solid #edf2f3;padding:12px 16px;border-radius:10px;font-size:13.5px;color:#334155;">
        ${ic('check')} Poli Rawat Jalan / Umum
      </div>
      <div style="background:#ffffff;border:1px solid #edf2f3;padding:12px 16px;border-radius:10px;font-size:13.5px;color:#334155;">
        ${ic('check')} Poli Gigi & Mulut
      </div>
      <div style="background:#ffffff;border:1px solid #edf2f3;padding:12px 16px;border-radius:10px;font-size:13.5px;color:#334155;">
        ${ic('check')} Poli KIA & KB (Ibu dan Anak)
      </div>
      <div style="background:#ffffff;border:1px solid #edf2f3;padding:12px 16px;border-radius:10px;font-size:13.5px;color:#334155;">
        ${ic('check')} Pelayanan Imunisasi & Gizi
      </div>
      <div style="background:#ffffff;border:1px solid #edf2f3;padding:12px 16px;border-radius:10px;font-size:13.5px;color:#334155;">
        ${ic('check')} Laboratorium Sederhana
      </div>
      <div style="background:#ffffff;border:1px solid #edf2f3;padding:12px 16px;border-radius:10px;font-size:13.5px;color:#334155;">
        ${ic('check')} IGD & Kamar Bersalin 24 Jam
      </div>
    </div>

    <div style="margin-top:28px;display:flex;gap:12px;">
      <a href="puskesmas.html" class="btn secondary">${ic('arrow')} Kembali ke Direktori</a>
      <a href="https://wa.me/6285342172724" target="_blank" rel="noopener" class="btn primary">${ic('phone')} Hubungi Hotline</a>
    </div>
  </article>

  </div>${side('Direktori Puskesmas Lainnya', (window.PUSKESMAS_DATA||[]).slice(0, 8).map(x => [`puskesmas-detail.html?no=${x.no}`, x.name]))}</div></section>`;
}

// 6. BERITA & KEGIATAN (beritaPage)
function beritaPage() {
  const articles = window.ARTICLES_CACHE || [];
  const categories = ['Semua', 'Kegiatan', 'Promosi Kesehatan', 'Pembinaan', 'Pelayanan', 'Pengumuman'];

  return pageHero('berita','Ruang Publikasi & Berita','Kabar Terkini & Dokumentasi Kegiatan','Informasi kegiatan resmi, program kesehatan masyarakat, liputan GERMAS, dan pengumuman Dinas Kesehatan Pemerintah Kabupaten Pinrang.')+`<section class="content"><div class="container">

    <!-- Search & Filter Bar -->
    <div class="searchline" style="display:flex;gap:12px;margin-bottom:28px;flex-wrap:wrap;">
      <input id="newsSearch" type="search" placeholder="Cari judul berita, topik, narasumber, atau kegiatan..." style="flex:1;min-width:260px;" />
      <select id="newsCategory" style="min-width:180px;">
        ${categories.map(c => `<option value="${c === 'Semua' ? '' : c}">${c}</option>`).join('')}
      </select>
      <button class="btn secondary" type="button" id="newsReset">${ic('refresh')} Reset</button>
    </div>

    <!-- Berita Grid Dinamis -->
    <div class="v4-news-grid" id="newsGrid">
      ${articles.slice(0, 9).map(item => `
        <article class="v4-news-card news-entry" data-title="${item.title.toLowerCase()}" data-category="${(item.category||'').toLowerCase()}">
          <div class="v4-news-thumb-wrap">
            <img src="${getSafeImageUrl(item.featured_image)}" alt="${item.title}" class="v4-news-thumb" />
          </div>
          <div class="v4-news-body">
            <div class="v4-news-tags">
              <span class="v4-news-tag">${item.category || 'Berita'}</span>
              <span style="font-size:12px;color:#94a3b8;">${item.published_at}</span>
            </div>
            <h3 class="v4-news-title">
              <a href="berita-detail.html?id=${item.id}" style="color:#103447;text-decoration:none;">${item.title}</a>
            </h3>
            <p class="v4-news-excerpt">
              ${item.excerpt}
            </p>
            <div class="v4-news-footer">
              <span>${ic('user')} ${item.author}</span>
              <a href="berita-detail.html?id=${item.id}" style="font-size:13px;font-weight:700;color:#087f89;text-decoration:none;">
                Baca artikel ${ic('arrow')}
              </a>
            </div>
          </div>
        </article>
      `).join('')}
    </div>

    <!-- Paginasi Interaktif -->
    <div class="v4-pagination" id="newsPagination">
      <button class="v4-page-btn is-active" data-page="1">1</button>
      <button class="v4-page-btn" data-page="2">2</button>
      <button class="v4-page-btn" data-page="3">3</button>
      <button class="v4-page-btn" data-page="4">4</button>
      <button class="v4-page-btn" data-page="5">5</button>
      <span style="color:#94a3b8;padding:0 8px;">...</span>
      <button class="v4-page-btn" data-page="${Math.ceil(articles.length / 9)}">${Math.ceil(articles.length / 9)}</button>
    </div>

    <div id="newsEmpty" class="hidden text-center" style="padding:40px;background:#f8fafc;border-radius:14px;margin-top:20px;">
      <p style="font-size:16px;color:#64748b;">Tidak ada artikel berita yang cocok dengan kata kunci pencarian.</p>
    </div>

  </div></section>`;
}

// 7. DETAIL BERITA (beritaDetailPage)
function beritaDetailPage() {
  const articles = window.ARTICLES_CACHE || [];
  const params = new URLSearchParams(location.search);
  const id = params.get('id') || '4505';

  const item = articles.find(a => String(a.id) === String(id)) || articles.find(a => a.id === '4505') || articles[0] || {
    id: '4505',
    title: 'Kecamatan Batulappa Jadi Penutup Rangkaian Kampanye GERMAS Dinkes Pinrang, Dorong Masyarakat Lakukan Deteksi Dini',
    published_at: '23 Oktober 2026',
    author: 'Muhammad Rusdi',
    category: 'Kegiatan',
    featured_image: 'https://dinkes.pinrangkab.go.id/wp-content/uploads/2026/10/cbe0e611-4ec4-4b64-b3ca-7fce94ef85a7.jpeg',
    excerpt: 'Tim Kerja Promosi Kesehatan dan Pemberdayaan Masyarakat Dinas Kesehatan Kabupaten Pinrang sukses menuntaskan rangkaian Kampanye Gerakan Masyarakat Hidup Sehat (GERMAS) di seluruh wilayah Kabupaten Pinrang.'
  };

  const sideNews = articles.filter(a => String(a.id) !== String(item.id)).slice(0, 6);

  return pageHero('berita-detail', `RUANG REDAKSI - ${(item.category||'BERITA').toUpperCase()}`, item.title, `Dipublikasikan pada ${item.published_at} oleh ${item.author} | Dinas Kesehatan Kabupaten Pinrang`)+`<section class="content"><div class="container twocol"><div class="stack">

  <article class="panel" style="padding:32px;">
    <div style="display:flex;gap:10px;align-items:center;margin-bottom:16px;flex-wrap:wrap;">
      <span class="v4-news-tag">${item.category || 'Kegiatan'}</span>
      <span style="font-size:13px;color:#64748b;">${ic('clock')} Terbit: ${item.published_at}</span>
      <span style="font-size:13px;color:#64748b;">${ic('user')} Penulis: ${item.author}</span>
    </div>

    <h2 style="font-size:26px;color:#103447;line-height:1.35;margin-bottom:20px;">${item.title}</h2>

    <div style="margin-bottom:24px;border-radius:16px;overflow:hidden;box-shadow:0 8px 24px rgba(0,0,0,0.06);background:#e2e8f0;">
      <img src="${getSafeImageUrl(item.featured_image)}" alt="${item.title}" style="width:100%;height:auto;max-height:480px;object-fit:cover;display:block;" />
      <div style="padding:10px 16px;background:#f8fafc;font-size:12.5px;color:#64748b;border-top:1px solid #edf2f3;">
        ${ic('camera')} Dokumentasi resmi kegiatan Dinas Kesehatan Kabupaten Pinrang
      </div>
    </div>

    <div class="article-text" style="font-size:16px;line-height:1.85;color:#334155;">
      <p style="font-size:17px;font-weight:600;color:#1e293b;margin-bottom:20px;border-left:4px solid #087f89;padding-left:16px;">
        PINRANG - ${item.excerpt}
      </p>

      <p>
        Pelaksanaan program kesehatan masyarakat ini merupakan bagian dari komitmen Dinas Kesehatan Pemerintah Kabupaten Pinrang di bawah kepemimpinan <strong>dr. H. Ramli Yunus, M.Kes</strong> untuk mendekatkan akses pelayanan promotif, preventif, serta deteksi dini faktor risiko penyakit langsung kepada masyarakat di tingkat akar rumput.
      </p>

      <p>
        Melalui kolaborasi terpadu antara Tim Kerja Dinas Kesehatan, jajaran 19 UPTD Puskesmas, kader Posyandu, serta unsur pimpinan kecamatan dan desa/kelurahan, masyarakat dihimbau untuk senantiasa menerapkan pola hidup sehat, mengonsumsi makanan bergizi seimbang, melakukan aktivitas fisik secara teratur, serta memanfaatkan fasilitas pemeriksaan kesehatan berkala yang tersedia di Puskesmas terdekat tanpa dipungut biaya.
      </p>

      <h3 style="font-size:18px;font-weight:700;color:#103447;margin:28px 0 12px 0;">Komitmen Pelayanan Kesehatan Berkelanjutan</h3>
      <p>
        Dinas Kesehatan Kabupaten Pinrang terus berinovasi mengoptimalkan sarana, prasarana, dan kapasitas tenaga kesehatan agar setiap warga Pinrang mendapatkan hak pelayanan kesehatan yang bermutu, merata, dan berkeadilan.
      </p>
    </div>

    <!-- Tombol Bagikan -->
    <div style="margin-top:32px;padding-top:20px;border-top:1px solid #edf2f3;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;">
      <div style="display:flex;gap:10px;align-items:center;">
        <span style="font-size:13px;font-weight:700;color:#103447;">Bagikan Berita:</span>
        <a href="https://api.whatsapp.com/send?text=${encodeURIComponent(item.title + ' - ' + location.href)}" target="_blank" rel="noopener" class="btn secondary" style="font-size:12.5px;padding:6px 12px;">
          ${ic('chat')} WhatsApp
        </a>
        <button class="btn secondary" style="font-size:12.5px;padding:6px 12px;" onclick="navigator.clipboard.writeText(location.href);alert('Tautan berita berhasil disalin!');">
          ${ic('file')} Salin Tautan
        </button>
      </div>
      <a href="berita.html" class="btn primary" style="font-size:13px;padding:8px 16px;">
        ${ic('arrow')} Kembali ke Berita
      </a>
    </div>
  </article>

  </div>${side('Berita Terkini Lainnya', sideNews.map(x => [`berita-detail.html?id=${x.id}`, x.title.slice(0, 48) + '...']))}</div></section>`;
}

// 8. LAYANAN KESEHATAN (layananPage)
function layananPage() {
  return pageHero('layanan','Informasi Pelayanan Publik','Standar Pelayanan Publik Dinas Kesehatan','Katalog resmi jenis layanan perizinan kesehatan, fasilitasi masyarakat, pengaduan, dan standar prosedur operasional (SOP).')+`<section class="content"><div class="container">

    <div class="grid grid-3" style="gap:24px;">
      <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:18px;padding:24px;box-shadow:0 8px 24px rgba(16,52,71,0.04);display:flex;flex-direction:column;">
        <div style="width:48px;height:48px;border-radius:14px;background:#e6f7f5;display:flex;align-items:center;justify-content:center;color:#087f89;margin-bottom:16px;">
          ${ic('hospital')}
        </div>
        <h3 style="font-size:18px;font-weight:700;color:#103447;margin-bottom:8px;">Pelayanan 19 Puskesmas</h3>
        <p style="font-size:14px;color:#587084;line-height:1.6;margin-bottom:16px;flex-grow:1;">
          Pelayanan poli rawat jalan, kesehatan ibu dan anak (KIA), gizi, imunisasi dasar, laboratorium, serta UGD & persalinan 24 jam.
        </p>
        <a href="puskesmas.html" class="btn primary" style="font-size:13px;padding:8px 14px;text-align:center;justify-content:center;">
          Lihat 19 Puskesmas ${ic('arrow')}
        </a>
      </div>

      <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:18px;padding:24px;box-shadow:0 8px 24px rgba(16,52,71,0.04);display:flex;flex-direction:column;">
        <div style="width:48px;height:48px;border-radius:14px;background:#fef3c7;display:flex;align-items:center;justify-content:center;color:#d97706;margin-bottom:16px;">
          ${ic('file')}
        </div>
        <h3 style="font-size:18px;font-weight:700;color:#103447;margin-bottom:8px;">Rekomendasi SIP & SIK Nakes</h3>
        <p style="font-size:14px;color:#587084;line-height:1.6;margin-bottom:16px;flex-grow:1;">
          Penerbitan surat rekomendasi Surat Izin Praktik (SIP) dokter, perawat, bidan, apoteker, dan tenaga kesehatan lainnya di Kabupaten Pinrang.
        </p>
        <a href="layanan-detail.html" class="btn primary" style="font-size:13px;padding:8px 14px;text-align:center;justify-content:center;">
          SOP & Syarat Berkas ${ic('arrow')}
        </a>
      </div>

      <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:18px;padding:24px;box-shadow:0 8px 24px rgba(16,52,71,0.04);display:flex;flex-direction:column;">
        <div style="width:48px;height:48px;border-radius:14px;background:#ecfdf5;display:flex;align-items:center;justify-content:center;color:#059669;margin-bottom:16px;">
          ${ic('shield')}
        </div>
        <h3 style="font-size:18px;font-weight:700;color:#103447;margin-bottom:8px;">Sertifikasi Pangan (SPP-IRT)</h3>
        <p style="font-size:14px;color:#587084;line-height:1.6;margin-bottom:16px;flex-grow:1;">
          Penyuluhan keamanan pangan dan penerbitan sertifikat pemenuhan komitmen produksi pangan industri rumah tangga secara gratis.
        </p>
        <a href="layanan-detail.html" class="btn primary" style="font-size:13px;padding:8px 14px;text-align:center;justify-content:center;">
          Panduan SPP-IRT ${ic('arrow')}
        </a>
      </div>

      <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:18px;padding:24px;box-shadow:0 8px 24px rgba(16,52,71,0.04);display:flex;flex-direction:column;">
        <div style="width:48px;height:48px;border-radius:14px;background:#f0f9ff;display:flex;align-items:center;justify-content:center;color:#0284c7;margin-bottom:16px;">
          ${ic('heart')}
        </div>
        <h3 style="font-size:18px;font-weight:700;color:#103447;margin-bottom:8px;">Cek Kesehatan Gratis (CKG)</h3>
        <p style="font-size:14px;color:#587084;line-height:1.6;margin-bottom:16px;flex-grow:1;">
          Program pemeriksaan dan deteksi dini faktor risiko penyakit tidak menular (tekanan darah, gula darah, kolesterol) di fasilitas primer.
        </p>
        <a href="layanan-detail.html" class="btn primary" style="font-size:13px;padding:8px 14px;text-align:center;justify-content:center;">
          Alur Pelayanan ${ic('arrow')}
        </a>
      </div>

      <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:18px;padding:24px;box-shadow:0 8px 24px rgba(16,52,71,0.04);display:flex;flex-direction:column;">
        <div style="width:48px;height:48px;border-radius:14px;background:#fdf2f8;display:flex;align-items:center;justify-content:center;color:#db2777;margin-bottom:16px;">
          ${ic('phone')}
        </div>
        <h3 style="font-size:18px;font-weight:700;color:#103447;margin-bottom:8px;">Rujukan & Ambulans Siaga 119</h3>
        <p style="font-size:14px;color:#587084;line-height:1.6;margin-bottom:16px;flex-grow:1;">
          Sistem Penanggulangan Gawat Darurat Terpadu (SPGDT) dan mobilisasi ambulans rujukan cepat antar fasilitas kesehatan di Pinrang.
        </p>
        <a href="kontak.html" class="btn primary" style="font-size:13px;padding:8px 14px;text-align:center;justify-content:center;">
          Hubungi Call Center ${ic('arrow')}
        </a>
      </div>

      <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:18px;padding:24px;box-shadow:0 8px 24px rgba(16,52,71,0.04);display:flex;flex-direction:column;">
        <div style="width:48px;height:48px;border-radius:14px;background:#fef2f2;display:flex;align-items:center;justify-content:center;color:#dc2626;margin-bottom:16px;">
          ${ic('chat')}
        </div>
        <h3 style="font-size:18px;font-weight:700;color:#103447;margin-bottom:8px;">Kanal Pengaduan SP4N-LAPOR!</h3>
        <p style="font-size:14px;color:#587084;line-height:1.6;margin-bottom:16px;flex-grow:1;">
          Saluran penyampaian kritik, saran, pengaduan pelayanan nakes dan fasilitas kesehatan secara transparan dan akuntabel.
        </p>
        <a href="pengaduan.html" class="btn primary" style="font-size:13px;padding:8px 14px;text-align:center;justify-content:center;">
          Sampaikan Aduan ${ic('arrow')}
        </a>
      </div>
    </div>

  </div></section>`;
}

// 9. DETAIL LAYANAN & SOP (layananDetailPage)
function layananDetailPage() {
  return pageHero('layanan-detail','Standar Operasional Prosedur','SOP Rekomendasi Izin Praktik & Layanan Kesehatan','Pedoman resmi alur perizinan praktik nakes, sertifikasi SPP-IRT, persyaratan berkas, jangka waktu, dan biaya pelayanan.')+`<section class="content"><div class="container twocol"><div class="stack">

  <article class="panel">
    <span class="kicker">STANDAR PELAYANAN PUBLIK</span>
    <h2>1. Rekomendasi Surat Izin Praktik (SIP/SIK) Tenaga Kesehatan</h2>
    <p style="font-size:14.5px;color:#334155;line-height:1.7;">
      Diberikan kepada tenaga medis dan tenaga kesehatan (Dokter, Dokter Gigi, Perawat, Bidan, Apoteker, Tenaga Sanitasi Lingkungan, Nutrisionis) sebagai syarat sah menjalankan praktik di fasilitas kesehatan wilayah Kabupaten Pinrang.
    </p>

    <h3 style="font-size:16px;font-weight:700;color:#103447;margin:20px 0 10px 0;">Persyaratan Berkas:</h3>
    <ul style="display:grid;gap:8px;padding-left:20px;font-size:14px;color:#334155;">
      <li>Fotokopi Surat Tanda Registrasi (STR) yang masih berlaku</li>
      <li>Surat Keterangan / Rekomendasi dari Organisasi Profesi (IDI, PDGI, PPNI, IBI, IAI, dll)</li>
      <li>Surat persetujuan dari pimpinan faskes tempat praktik</li>
      <li>Pas foto terbaru ukuran 4x6 latar belakang merah (2 lembar)</li>
      <li>Fotokopi KTP pemohon</li>
    </ul>

    <div class="grid grid-3" style="gap:12px;margin:20px 0;background:#f8fafc;padding:16px;border-radius:12px;">
      <div>
        <span style="font-size:11px;color:#64748b;text-transform:uppercase;font-weight:700;">Waktu Penyelesaian:</span>
        <div style="font-size:15px;font-weight:700;color:#103447;">Maksimal 3 Hari Kerja</div>
      </div>
      <div>
        <span style="font-size:11px;color:#64748b;text-transform:uppercase;font-weight:700;">Biaya Pelayanan:</span>
        <div style="font-size:15px;font-weight:700;color:#059669;">Rp 0,- (GRATIS)</div>
      </div>
      <div>
        <span style="font-size:11px;color:#64748b;text-transform:uppercase;font-weight:700;">Kanal Pengajuan:</span>
        <div style="font-size:15px;font-weight:700;color:#087f89;">PTSP / Loket Dinkes</div>
      </div>
    </div>
  </article>

  <article class="panel">
    <span class="kicker">STANDAR PELAYANAN PUBLIK</span>
    <h2>2. Sertifikasi Pemenuhan Komitmen Pangan (SPP-IRT)</h2>
    <p style="font-size:14.5px;color:#334155;line-height:1.7;">
      Fasilitasi bagi pelaku Usaha Mikro, Kecil, dan Menengah (UMKM) produsen pangan olahan rumah tangga di Kabupaten Pinrang untuk memperoleh nomor izin edar pangan yang higienis dan terstandar.
    </p>

    <h3 style="font-size:16px;font-weight:700;color:#103447;margin:20px 0 10px 0;">Tahapan Alur Layanan:</h3>
    <ol style="display:grid;gap:8px;padding-left:20px;font-size:14px;color:#334155;">
      <li>Pendaftaran melalui sistem OSS (Online Single Submission) atau datang ke Dinas Kesehatan</li>
      <li>Mengikuti Penyuluhan Keamanan Pangan (PKP) yang diselenggarakan oleh Tim Farmasi Dinkes</li>
      <li>Pemeriksaan sarana produksi pangan rumah tangga oleh tenaga pengawas sanitarian</li>
      <li>Penerbitan rekomendasi pemenuhan komitmen SPP-IRT</li>
    </ol>
  </article>

  </div>${side('Menu Layanan Lainnya',[['layanan','Katalog Layanan Publik'],['puskesmas','Direktori 19 Puskesmas'],['pengaduan','Kanal Pengaduan'],['kontak','Lokasi & Jam Pelayanan']])}</div></section>`;
}

// 10. EDUKASI KESEHATAN (edukasiPage)
function edukasiPage() {
  const topics = [
    {
      title: 'Pencegahan & Percepatan Penurunan Stunting',
      cat: 'Kesehatan Ibu & Anak',
      desc: 'Pemberian ASI eksklusif 6 bulan, MPASI bergizi kaya protein hewani, pemantauan pertumbuhan balita di Posyandu, dan sanitasi jamban sehat.',
      icon: 'heart'
    },
    {
      title: 'Gerakan Masyarakat Hidup Sehat (GERMAS)',
      cat: 'Promosi Kesehatan',
      desc: '7 langkah GERMAS: Aktivitas fisik rutin 30 menit, konsumsi buah dan sayur, periksa kesehatan berkala, tidak merokok, dan kelola stres.',
      icon: 'activity'
    },
    {
      title: 'Pencegahan Penyakit Tidak Menular (PTM)',
      cat: 'Pencegahan Penyakit',
      desc: 'Ketahui dan kendalikan faktor risiko hipertensi, diabetes melitus, stroke, dan penyakit jantung dengan pola makan rendah garam dan gula.',
      icon: 'shield'
    },
    {
      title: 'Imunisasi Dasar Lengkap & BIAN',
      cat: 'Imunisasi',
      desc: 'Melindungi anak dari penyakit berbahaya seperti Campak, Rubella, Polio, Difteri, dan Tetanus dengan vaksinasi terjadwal di Puskesmas.',
      icon: 'hospital'
    },
    {
      title: 'Sanitasi Total Berbasis Masyarakat (STBM)',
      cat: 'Kesehatan Lingkungan',
      desc: 'Mempertahankan status 100% ODF Kabupaten Pinrang melalui kebiasaan Cuci Tangan Pakai Sabun (CTPS) dan pengelolaan limbah rumah tangga aman.',
      icon: 'check'
    },
    {
      title: 'Kesehatan Reproduksi & Gizi Remaja',
      cat: 'Kesehatan Remaja',
      desc: 'Konsumsi tablet tambah darah bagi remaja putri untuk mencegah anemia dan mempersiapkan generasi penerus yang cerdas dan sehat.',
      icon: 'user'
    }
  ];

  return pageHero('edukasi','Pusat Literasi Kesehatan','Edukasi & Pembiasaan Hidup Sehat','Panduan informasi kesehatan keluarga terpercaya yang disusun oleh tenaga kesehatan profesional Dinas Kesehatan Kabupaten Pinrang.')+`<section class="content"><div class="container">

    <div class="grid grid-3" style="gap:24px;">
      ${topics.map(t => `
        <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:18px;padding:24px;box-shadow:0 8px 24px rgba(16,52,71,0.04);display:flex;flex-direction:column;">
          <span style="font-size:11.5px;font-weight:700;color:#087f89;text-transform:uppercase;margin-bottom:8px;">${t.cat}</span>
          <h3 style="font-size:18px;font-weight:700;color:#103447;margin-bottom:12px;line-height:1.35;">${t.title}</h3>
          <p style="font-size:14px;color:#587084;line-height:1.6;margin-bottom:18px;flex-grow:1;">${t.desc}</p>
          <a href="edukasi-detail.html" class="btn primary" style="font-size:13px;padding:8px 14px;text-align:center;justify-content:center;">
            Baca Panduan Lengkap ${ic('arrow')}
          </a>
        </div>
      `).join('')}
    </div>

  </div></section>`;
}

// 11. DETAIL EDUKASI (edukasiDetailPage)
function edukasiDetailPage() {
  return pageHero('edukasi-detail','Panduan Promosi Kesehatan','Pencegahan & Percepatan Penurunan Stunting di Kabupaten Pinrang','Langkah nyata terpadu menjaga 1000 Hari Pertama Kehidupan demi generasi Pinrang yang sehat, cerdas, dan tangguh.')+`<section class="content"><div class="container twocol"><div class="stack">

  <article class="panel" style="padding:32px;">
    <span class="v4-news-tag">KESEHATAN IBU DAN ANAK</span>
    <h2 style="font-size:24px;color:#103447;margin:12px 0 20px 0;">Pentingnya 1000 Hari Pertama Kehidupan (HPK)</h2>
    <p style="font-size:15.5px;line-height:1.8;color:#334155;">
      Stunting adalah kondisi gagal tumbuh pada anak balita akibat kekurangan gizi kronis terutama pada 1000 Hari Pertama Kehidupan (sejak janin dalam kandungan hingga anak berusia 2 tahun). Dinas Kesehatan Kabupaten Pinrang berkomitmen terus menekan angka prevalensi stunting dengan program konvergensi intervensi spesifik dan sensitif di 12 kecamatan.
    </p>

    <h3 style="font-size:18px;font-weight:700;color:#103447;margin:24px 0 12px 0;">5 Kunci Pencegahan Stunting Keluarga:</h3>
    <ol style="display:grid;gap:12px;padding-left:20px;font-size:15px;line-height:1.7;color:#334155;">
      <li><strong>Pemeriksaan Kehamilan Rutin (Minimal 6 Kali):</strong> Ibu hamil wajib memeriksakan kehamilan di fasilitas kesehatan dan mengonsumsi Tablet Tambah Darah (TTD) minimal 90 tablet selama kehamilan.</li>
      <li><strong>Inisiasi Menyusu Dini (IMD) & ASI Eksklusif:</strong> Berikan ASI saja tanpa tambahan makanan atau minuman lain hingga bayi berusia 6 bulan.</li>
      <li><strong>Makanan Pendamping ASI (MPASI) Kaya Protein Hewani:</strong> Berikan MPASI bertahap dengan menu gizi seimbang mengutamakan telur, ikan lokal Pinrang, daging, atau hati ayam.</li>
      <li><strong>Imunisasi Lengkap & Timbang Berat Badan Setiap Bulan di Posyandu:</strong> Pantau kurva pertumbuhan anak pada buku KIA secara berkala.</li>
      <li><strong>Akses Sanitasi & Air Bersih:</strong> Cuci tangan pakai sabun dengan air mengalir dan pastikan rumah tangga menggunakan jamban sehat.</li>
    </ol>

    <div style="margin-top:28px;padding:20px;background:#f0fdf9;border:1px solid #bbf7d0;border-radius:14px;">
      <h4 style="font-size:15px;font-weight:700;color:#065f46;margin-bottom:6px;">Layanan Posyandu & Puskesmas</h4>
      <p style="font-size:13.5px;color:#475569;line-height:1.6;margin:0;">
        Kunjungi Posyandu terdekat di desa/kelurahan Anda setiap bulan atau konsultasikan gizi anak ke tenaga nutrisi di 19 UPTD Puskesmas se-Kabupaten Pinrang.
      </p>
    </div>
  </article>

  </div>${side('Topik Edukasi Lainnya',[['edukasi','Semua Topik Edukasi'],['layanan-detail','Cek Kesehatan Gratis'],['puskesmas','Posyandu di Puskesmas']])}</div></section>`;
}

// 12. DATA KESEHATAN (dataPage)
function dataPage() {
  return pageHero('data','Satu Data Indonesia - Sektor Kesehatan','Dashboard Data & Indikator Kesehatan Daerah','Transparansi data agregat capaian kesehatan publik Kabupaten Pinrang berbasis bukti dan akuntabel.')+`<section class="content"><div class="container">

    <div class="grid grid-3" style="gap:20px;margin-bottom:36px;">
      <div class="panel text-center" style="background:#f0fdf4;border:1px solid #bbf7d0;padding:28px;border-radius:18px;">
        <span style="font-size:42px;font-weight:800;color:#047857;display:block;">100%</span>
        <strong style="color:#064e3b;font-size:16px;">Status ODF (Bebas BAB Sembarangan)</strong>
        <p style="font-size:13px;color:#587084;margin-top:6px;">12 Kecamatan Se-Kabupaten Pinrang telah tuntas verifikasi ODF</p>
      </div>

      <div class="panel text-center" style="background:#f0f9ff;border:1px solid #bae6fd;padding:28px;border-radius:18px;">
        <span style="font-size:42px;font-weight:800;color:#0284c7;display:block;">96.4%</span>
        <strong style="color:#075985;font-size:16px;">Cakupan Imunisasi BIAN</strong>
        <p style="font-size:13px;color:#587084;margin-top:6px;">Kabupaten tercepat mencapai target minimal 95% di Provinsi Sulawesi Selatan</p>
      </div>

      <div class="panel text-center" style="background:#fdf2f8;border:1px solid #fbcfe8;padding:28px;border-radius:18px;">
        <span style="font-size:42px;font-weight:800;color:#db2777;display:block;">12.8%</span>
        <strong style="color:#9d174d;font-size:16px;">Prevalensi Stunting Daerah</strong>
        <p style="font-size:13px;color:#587084;margin-top:6px;">Keberhasilan konvergensi terintegrasi melampaui target nasional (<14%)</p>
      </div>
    </div>

    <!-- Tabel Data Agregat -->
    <article class="panel">
      <span class="kicker">STATISTIK KESEHATAN KABUPATEN PINRANG</span>
      <h2>Ringkasan Fasilitas & Sumber Daya Kesehatan Daerah</h2>
      <div style="overflow-x:auto;margin-top:20px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;text-align:left;">
          <thead>
            <tr style="background:#f8fafc;border-bottom:2px solid #e2e8f0;">
              <th style="padding:12px 16px;color:#103447;">No</th>
              <th style="padding:12px 16px;color:#103447;">Indikator / Entitas</th>
              <th style="padding:12px 16px;color:#103447;">Jumlah</th>
              <th style="padding:12px 16px;color:#103447;">Keterangan & Status</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid #edf2f3;">
              <td style="padding:12px 16px;">1</td>
              <td style="padding:12px 16px;font-weight:600;">UPTD Puskesmas</td>
              <td style="padding:12px 16px;font-weight:700;color:#087f89;">19 Unit</td>
              <td style="padding:12px 16px;color:#059669;">100% Terakreditasi Paripurna & Utama Kemenkes RI</td>
            </tr>
            <tr style="border-bottom:1px solid #edf2f3;">
              <td style="padding:12px 16px;">2</td>
              <td style="padding:12px 16px;font-weight:600;">Rumah Sakit Umum Daerah (RSUD)</td>
              <td style="padding:12px 16px;font-weight:700;color:#087f89;">1 Unit (RSUD Lasinrang)</td>
              <td style="padding:12px 16px;">Rumah sakit rujukan tipe B terakreditasi</td>
            </tr>
            <tr style="border-bottom:1px solid #edf2f3;">
              <td style="padding:12px 16px;">3</td>
              <td style="padding:12px 16px;font-weight:600;">Laboratorium Kesehatan Daerah (Labkesda)</td>
              <td style="padding:12px 16px;font-weight:700;color:#087f89;">1 Unit</td>
              <td style="padding:12px 16px;">Pengujian kualitas air, makanan, & spesimen klinis</td>
            </tr>
            <tr style="border-bottom:1px solid #edf2f3;">
              <td style="padding:12px 16px;">4</td>
              <td style="padding:12px 16px;font-weight:600;">Jumlah Posyandu Aktif</td>
              <td style="padding:12px 16px;font-weight:700;color:#087f89;">380+ Pos</td>
              <td style="padding:12px 16px;">Menjangkau seluruh RW/Dusun di 12 Kecamatan</td>
            </tr>
            <tr style="border-bottom:1px solid #edf2f3;">
              <td style="padding:12px 16px;">5</td>
              <td style="padding:12px 16px;font-weight:600;">Indeks Kepuasan Masyarakat (IKM)</td>
              <td style="padding:12px 16px;font-weight:700;color:#087f89;">88.75 / 100</td>
              <td style="padding:12px 16px;color:#059669;">Mutu Pelayanan Kategori A (Sangat Baik)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </article>

  </div></section>`;
}

// 13. INDIKATOR KINERJA (indikatorPage)
function indikatorPage() {
  return pageHero('indikator','Capaian Standar Pelayanan Minimal','Indikator Kinerja Utama (IKU) Kesehatan Pinrang','Target dan realisasi capaian 12 indikator Standar Pelayanan Minimal (SPM) bidang kesehatan.')+`<section class="content"><div class="container">
    <article class="panel">
      <h2>12 Indikator Standar Pelayanan Minimal (SPM) Bidang Kesehatan</h2>
      <p style="font-size:14.5px;color:#587084;line-height:1.7;">
        Pelaksanaan SPM Bidang Kesehatan di Kabupaten Pinrang mencakup pelayanan kesehatan ibu hamil, ibu bersalin, bayi baru lahir, balita, usia pendidikan dasar, usia produktif, lansia, penderita hipertensi, diabetes melitus, ODGJ berat, orang terduga TB, dan orang berisiko HIV.
      </p>
      <div style="margin-top:20px;">
        <a href="data.html" class="btn primary">${ic('arrow')} Kembali ke Satu Data Kesehatan</a>
      </div>
    </article>
  </div></section>`;
}

// 14. INOVASI & PRESTASI (inovasiPage)
function inovasiPage() {
  return pageHero('inovasi','Kreativitas & Daya Saing Daerah','Inovasi & Rekam Jejak Prestasi Dinas Kesehatan Pinrang','Daftar terobosan inovasi pelayanan kesehatan publik dan apresiasi penghargaan tingkat regional maupun nasional.')+`<section class="content"><div class="container twocol"><div class="stack">

  <article class="panel">
    <span class="kicker">PENGHARGAAN TINGKAT NASIONAL & REGIONAL</span>
    <h2>Apresiasi Prestasi Kelembagaan</h2>
    <div class="v4-timeline">
      <div class="v4-timeline-item">
        <span class="v4-timeline-badge">2022 - Kementerian Kesehatan RI</span>
        <h4 class="v4-timeline-title">Kabupaten Bebas Frambusia & GOLD AWARD IndoHCF</h4>
        <p class="v4-timeline-desc">Menerima Sertifikat Bebas Frambusia dari Menkes RI serta Gold Award Indonesia Healthcare Innovation Award (IHIA-VI) untuk kategori Inovasi GERMAS.</p>
      </div>

      <div class="v4-timeline-item">
        <span class="v4-timeline-badge">2021 - Tingkat Nasional</span>
        <h4 class="v4-timeline-title">Penghargaan Kabupaten Sehat SWASTI SABA WISTARA ke-IV</h4>
        <p class="v4-timeline-desc">Kabupaten Pinrang mempertahankan predikat tertinggi Swasti Saba Wistara 4 kali berturut-turut (2015, 2017, 2019, 2021) dari Kementerian Kesehatan dan Kementerian Dalam Negeri RI.</p>
      </div>

      <div class="v4-timeline-item">
        <span class="v4-timeline-badge">2020 - STBM Award Nasional</span>
        <h4 class="v4-timeline-title">Terbaik I Nasional STBM Berkelanjutan</h4>
        <p class="v4-timeline-desc">Kabupaten Terbaik I Nasional Kategori Demand Creation dan Penciptaan Lingkungan Kondusif (Enabling Environment) atas percepatan 100% Bebas BAB Sembarangan (ODF).</p>
      </div>

      <div class="v4-timeline-item">
        <span class="v4-timeline-badge">2019 - Provinsi Sulawesi Selatan</span>
        <h4 class="v4-timeline-title">Peringkat I Penurunan AKI/AKB & Asuhan Mandiri TOGA</h4>
        <p class="v4-timeline-desc">Terbaik I Kategori Inovasi Akselerasi Penurunan AKI-AKB serta Juara I Lomba Asuhan Mandiri Tanaman Obat Keluarga (TOGA) Tingkat Provinsi Sulsel.</p>
      </div>
    </div>
  </article>

  <article class="panel">
    <span class="kicker">TEROBOSAN PELAYANAN</span>
    <h2>Inovasi Kesehatan Unggulan</h2>
    <div class="grid grid-2" style="gap:16px;margin-top:16px;">
      <div style="background:#f8fafc;padding:18px;border-radius:12px;border:1px solid #e2e8f0;">
        <h4 style="margin:0 0 6px 0;font-size:16px;color:#103447;">Percik Pelangi</h4>
        <p style="font-size:13px;color:#587084;line-height:1.6;margin:0;">Inovasi penanganan limbah medis dan limbah rumah tangga aman serta pemberdayaan masyarakat peduli sanitasi.</p>
      </div>
      <div style="background:#f8fafc;padding:18px;border-radius:12px;border:1px solid #e2e8f0;">
        <h4 style="margin:0 0 6px 0;font-size:16px;color:#103447;">SAMAWA (Kesehatan Jiwa)</h4>
        <p style="font-size:13px;color:#587084;line-height:1.6;margin:0;">Sehatkan dan Latih sampai Mandiri Orang dengan Gangguan Jiwa (ODGJ) terintegrasi di Puskesmas Lanrisang.</p>
      </div>
      <div style="background:#f8fafc;padding:18px;border-radius:12px;border:1px solid #e2e8f0;">
        <h4 style="margin:0 0 6px 0;font-size:16px;color:#103447;">Mama Penting & Macenning</h4>
        <p style="font-size:13px;color:#587084;line-height:1.6;margin:0;">Masyarakat Peduli Stunting terpadu di Puskesmas Mattiro Deceng berbasis pangan lokal.</p>
      </div>
      <div style="background:#f8fafc;padding:18px;border-radius:12px;border:1px solid #e2e8f0;">
        <h4 style="margin:0 0 6px 0;font-size:16px;color:#103447;">Gema Takbir</h4>
        <p style="font-size:13px;color:#587084;line-height:1.6;margin:0;">Gerakan Masyarakat Tak Biasa Merokok di Kawasan Tanpa Rokok Puskesmas Mattiro Bulu.</p>
      </div>
    </div>
  </article>

  </div>${side('Menu Profil & Prestasi',[['profil','Profil Dinas'],['organisasi','Struktur Organisasi'],['inovasi','Inovasi & Prestasi'],['publikasi','Laporan Kinerja LKjIP']])}</div></section>`;
}

// 15. PUBLIKASI & DOKUMEN (publikasiPage)
function publikasiPage() {
  const docs = [
    { title: 'Laporan Kinerja Instansi Pemerintah (LKjIP) Tahun 2023', year: '2023', cat: 'Akuntabilitas' },
    { title: 'Indikator Kinerja Utama (IKU) Dinas Kesehatan Kabupaten Pinrang', year: '2023', cat: 'Perencanaan' },
    { title: 'Perjanjian Kinerja Penetapan Tahun Anggaran 2023', year: '2023', cat: 'Kinerja' },
    { title: 'Rencana Kerja (Renja) Dinas Kesehatan Kabupaten Pinrang', year: '2023', cat: 'Perencanaan' },
    { title: 'Rencana Aksi Kinerja Program Pembangunan Kesehatan', year: '2022', cat: 'Kinerja' },
    { title: 'Buletin SKDR (Sistem Kewaspadaan Dini dan Respon) Mingguan', year: '2024', cat: 'Surveilans' },
    { title: 'Standar Operasional dan Prosedur (SOP) Dinas Kesehatan Pinrang', year: '2023', cat: 'Standar Pelayanan' }
  ];

  return pageHero('publikasi','Transparansi Akuntabilitas Publik','Publikasi Dokumen Kinerja & Laporan Resmi','Akses publik terhadap dokumen perencanaan, perjanjian kinerja, laporan akuntabilitas pemerintah, dan buletin kesehatan.')+`<section class="content"><div class="container">

    <div class="panel">
      <h2>Daftar Dokumen Publikasi Resmi</h2>
      <p style="font-size:14.5px;color:#587084;margin-bottom:20px;">
        Dokumen akuntabilitas kinerja dapat diunduh oleh masyarakat umum dan pemangku kepentingan sesuai ketentuan keterbukaan informasi publik.
      </p>

      <div style="display:grid;gap:12px;">
        ${docs.map(d => `
          <div style="display:flex;justify-content:space-between;align-items:center;padding:16px 20px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;flex-wrap:wrap;gap:12px;">
            <div>
              <span style="font-size:11px;font-weight:700;color:#087f89;text-transform:uppercase;">${d.cat} - Tahun ${d.year}</span>
              <h4 style="margin:2px 0 0 0;font-size:15px;color:#103447;">${d.title}</h4>
            </div>
            <a href="https://cloud.pinrangkab.go.id/index.php/s/bQoCgtZXaBJigKm" target="_blank" rel="noopener" class="btn secondary" style="font-size:12.5px;padding:6px 14px;">
              ${ic('file')} Unduh Dokumen Resmi ${ic('external')}
            </a>
          </div>
        `).join('')}
      </div>
    </div>

  </div></section>`;
}

// 16. GALERI FOTO (galeriPage)
function galeriPage() {
  const articles = window.ARTICLES_CACHE || [];
  const galleryItems = articles.filter(a => a.featured_image).slice(0, 12);

  return pageHero('galeri','Dokumentasi Visual Kegiatan','Galeri Foto Dokumentasi Pelayanan & Kegiatan','Arsip dokumentasi visual pelaksanaan program kesehatan, kampanye GERMAS, pelayanan Posyandu, dan pembinaan faskes.')+`<section class="content"><div class="container">

    <div class="grid grid-3" style="gap:20px;">
      ${galleryItems.map(item => `
        <div class="panel" style="padding:0;overflow:hidden;border-radius:14px;box-shadow:0 6px 18px rgba(0,0,0,0.04);">
          <div style="width:100%;height:220px;overflow:hidden;background:#e2e8f0;">
            <img src="${getSafeImageUrl(item.featured_image)}" alt="${item.title}" style="width:100%;height:100%;object-fit:cover;transition:transform 0.4s ease;" />
          </div>
          <div style="padding:16px;">
            <span style="font-size:11px;font-weight:700;color:#087f89;text-transform:uppercase;">${item.category || 'Dokumentasi'} - ${item.published_at}</span>
            <h4 style="font-size:14px;font-weight:700;color:#103447;line-height:1.4;margin:6px 0 0 0;">
              <a href="berita-detail.html?id=${item.id}" style="color:#103447;text-decoration:none;">${item.title}</a>
            </h4>
          </div>
        </div>
      `).join('')}
    </div>

  </div></section>`;
}

// 17. PPID (ppidPage)
function ppidPage() {
  return pageHero('ppid','Keterbukaan Informasi Publik','Pejabat Pengelola Informasi & Dokumentasi (PPID) Dinkes','Layanan permohonan informasi publik sesuai amanat Undang-Undang No. 14 Tahun 2008.')+`<section class="content"><div class="container twocol"><div class="stack">
    <article class="panel">
      <h2>Layanan Keterbukaan Informasi Publik</h2>
      <p style="font-size:15px;line-height:1.7;color:#334155;">
        Dinas Kesehatan Kabupaten Pinrang berkomitmen menjamin hak masyarakat untuk memperoleh informasi kesehatan publik yang akurat, benar, dan tidak menyesatkan.
      </p>
      <div style="margin-top:20px;display:flex;gap:12px;">
        <a href="informasi.html" class="btn primary">Ajukan Permohonan Informasi</a>
        <a href="publikasi.html" class="btn secondary">Lihat Dokumen Terbuka</a>
      </div>
    </article>
  </div>${side('Menu PPID',[['ppid','Profil PPID'],['informasi','Form Permohonan Informasi'],['publikasi','Daftar Informasi Publik']])}</div></section>`;
}

// 18. PERMOHONAN INFORMASI (informasiPage)
function informasiPage() {
  return pageHero('informasi','Formulir PPID','Permohonan Informasi Publik','Kirimkan permohonan informasi resmi kepada Pejabat Pengelola Informasi dan Dokumentasi (PPID).')+`<section class="content"><div class="container twocol"><div class="stack">
    <article class="panel">
      <h2>Formulir Permohonan Informasi Publik</h2>
      <form id="infoForm" style="display:grid;gap:16px;margin-top:20px;">
        <div>
          <label style="display:block;font-size:13.5px;font-weight:600;color:#103447;margin-bottom:6px;">Nama Lengkap Pemohon</label>
          <input type="text" placeholder="Masukkan nama lengkap Anda..." required style="width:100%;" />
        </div>
        <div>
          <label style="display:block;font-size:13.5px;font-weight:600;color:#103447;margin-bottom:6px;">Nomor KTP / NIK</label>
          <input type="text" placeholder="Masukkan nomor NIK Anda..." required style="width:100%;" />
        </div>
        <div>
          <label style="display:block;font-size:13.5px;font-weight:600;color:#103447;margin-bottom:6px;">Rincian Informasi yang Dibutuhkan</label>
          <textarea rows="4" placeholder="Jelaskan secara spesifik informasi yang Anda butuhkan..." required style="width:100%;"></textarea>
        </div>
        <div>
          <label style="display:block;font-size:13.5px;font-weight:600;color:#103447;margin-bottom:6px;">Tujuan Penggunaan Informasi</label>
          <input type="text" placeholder="Contoh: Penelitian skripsi, keperluan studi kelayakan..." required style="width:100%;" />
        </div>
        <button type="submit" class="btn primary" style="width:fit-content;">Kirim Permohonan Informasi</button>
        <div id="infoFormResponse"></div>
      </form>
    </article>
  </div>${side('Layanan Informasi',[['ppid','PPID Utama'],['publikasi','Publikasi Dokumen'],['kontak','Kontak Dinas']])}</div></section>`;
}

// 19. PENGADUAN (pengaduanPage)
function pengaduanPage() {
  return pageHero('pengaduan','Saluran Aspirasi & Keluhan','Kanal Pengaduan Pelayanan Kesehatan','Sampaikan pengaduan, kritik, dan aspirasi pelayanan kesehatan secara transparan dan ditindaklanjuti cepat.')+`<section class="content"><div class="container twocol"><div class="stack">
    <article class="panel">
      <h2>Kanal Resmi Pengaduan Masyarakat</h2>
      <p style="font-size:15px;line-height:1.7;color:#334155;">
        Masyarakat dapat menyampaikan keluhan terkait pelayanan puskesmas, perizinan nakes, sarana fasilitas kesehatan, atau aduan lainnya melalui:
      </p>

      <div class="grid grid-2" style="gap:16px;margin:24px 0;">
        <div style="background:#f0fdf9;border:1px solid #bbf7d0;padding:20px;border-radius:14px;">
          <h4 style="margin:0 0 6px 0;font-size:16px;color:#065f46;">WhatsApp Resmi Dinas</h4>
          <p style="font-size:13.5px;color:#475569;margin-bottom:12px;">Respons cepat pengaduan dan konsultasi masyarakat langsung ke admin dinas.</p>
          <a href="https://wa.me/6285342172724" target="_blank" rel="noopener" class="btn primary" style="font-size:13px;padding:8px 14px;">
            ${ic('phone')} WhatsApp: +62 853-4217-2724
          </a>
        </div>

        <div style="background:#fef2f2;border:1px solid #fecaca;padding:20px;border-radius:14px;">
          <h4 style="margin:0 0 6px 0;font-size:16px;color:#991b1b;">SP4N-LAPOR! Nasional</h4>
          <p style="font-size:13.5px;color:#475569;margin-bottom:12px;">Kanal pengaduan resmi nasional yang terhubung langsung dengan Kementerian PANRB.</p>
          <a href="https://www.lapor.go.id/" target="_blank" rel="noopener" class="btn secondary" style="font-size:13px;padding:8px 14px;">
            ${ic('external')} Akses SP4N-LAPOR!
          </a>
        </div>
      </div>
    </article>
  </div>${side('Bantuan & Pengaduan',[['kontak','Kontak & Lokasi'],['faq','FAQ Pertanyaan Umum'],['skm','Survei Kepuasan (SKM)']])}</div></section>`;
}

// 20. KONTAK (kontakPage)
function kontakPage() {
  return pageHero('kontak','Lokasi & Jam Kerja','Kontak Resmi Dinas Kesehatan Kabupaten Pinrang','Informasi alamat kantor, nomor telepon, WhatsApp pengaduan, dan jam operasional pelayanan dinas.')+`<section class="content"><div class="container twocol"><div class="stack">
    <article class="panel">
      <h2>Kantor Dinas Kesehatan Pemerintah Kabupaten Pinrang</h2>
      <p style="font-size:15px;line-height:1.7;color:#334155;margin-bottom:20px;">
        ${ic('location')} <strong>Alamat Kantor:</strong><br>
        Jl. Jenderal Sukawati No. 40, Pinrang, Sulawesi Selatan 91212<br><br>
        ${ic('phone')} <strong>Nomor Telepon / WhatsApp:</strong> +62 853-4217-2724<br>
        ${ic('mail')} <strong>Email Resmi:</strong> dinkes@pinrangkab.go.id<br>
        ${ic('clock')} <strong>Jam Pelayanan Kantor:</strong><br>
        Senin - Kamis: 07:30 - 16:00 WITA<br>
        Jumat: 07:30 - 16:30 WITA<br>
        Sabtu & Minggu: Libur (Pelayanan IGD Puskesmas tetap buka 24 Jam)
      </p>
      <a href="https://wa.me/6285342172724" target="_blank" rel="noopener" class="btn primary">
        ${ic('phone')} Kirim Pesan WhatsApp Resmi
      </a>
    </article>
  </div>${side('Terkait',[['profil','Profil Dinas'],['puskesmas','19 UPTD Puskesmas'],['pengaduan','Kanal Pengaduan']])}</div></section>`;
}

// 21. FAQ (faqPage)
function faqPage() {
  const faqs = [
    { q: 'Bagaimana cara mendapatkan Cek Kesehatan Gratis di Puskesmas?', a: 'Warga Kabupaten Pinrang cukup membawa KTP atau Kartu Keluarga ke salah satu dari 19 UPTD Puskesmas terdekat pada jam pelayanan rawat jalan.' },
    { q: 'Apakah pengurusan rekomendasi SIP Nakes dipungut biaya?', a: 'Tidak. Seluruh rekomendasi izin praktik tenaga kesehatan di Dinas Kesehatan Kabupaten Pinrang bebas biaya (Rp 0,-).' },
    { q: 'Apakah Puskesmas di Pinrang melayani gawat darurat di malam hari?', a: 'Ya. Seluruh 19 UPTD Puskesmas di Kabupaten Pinrang menyelenggarakan pelayanan IGD dan kamar persalinan yang siap siaga 24 Jam.' }
  ];

  return pageHero('faq','Pusat Bantuan Warga','Tanya Jawab Seputar Pelayanan Kesehatan (FAQ)','Jawaban atas pertanyaan yang paling sering diajukan masyarakat mengenai layanan kesehatan di Kabupaten Pinrang.')+`<section class="content"><div class="container twocol"><div class="stack">
    <article class="panel">
      <h2>Pertanyaan yang Sering Diajukan</h2>
      <div style="display:grid;gap:16px;margin-top:20px;">
        ${faqs.map(f => `
          <div style="background:#f8fafc;padding:20px;border-radius:14px;border:1px solid #e2e8f0;">
            <h4 style="margin:0 0 8px 0;font-size:16px;color:#103447;">${f.q}</h4>
            <p style="margin:0;font-size:14px;color:#475569;line-height:1.6;">${f.a}</p>
          </div>
        `).join('')}
      </div>
    </article>
  </div>${side('Bantuan',[['kontak','Kontak Kami'],['pengaduan','Pengaduan'],['layanan','Katalog Layanan']])}</div></section>`;
}

// 22. PENCARIAN (pencarianPage)
function pencarianPage() {
  const query = new URLSearchParams(location.search).get('q') || '';
  return pageHero('pencarian','Pencarian Portal','Hasil Pencarian Informasi','Temukan layanan, puskesmas, berita kegiatan, atau dokumen publik di portal resmi.')+`<section class="content"><div class="container">
    <div class="panel">
      <div style="display:flex;gap:12px;margin-bottom:24px;">
        <input id="globalSearch" type="search" value="${query}" placeholder="Ketik kata kunci pencarian..." style="flex:1;" />
        <button id="searchExecute" class="btn primary" type="button">${ic('search')} Cari</button>
      </div>
      <div id="searchCount" style="font-size:14px;font-weight:700;color:#087f89;margin-bottom:16px;"></div>
      <div id="searchResults" style="display:grid;gap:12px;"></div>
    </div>
  </div></section>`;
}

// 23. PETA SITUS (siteMapPage)
function siteMapPage() {
  return pageHero('peta-situs','Struktur Portal','Peta Situs Dinas Kesehatan Pinrang','Navigasi lengkap seluruh halaman dan modul informasi portal resmi Dinas Kesehatan.')+`<section class="content"><div class="container">
    <div class="panel">
      <h2>Daftar Seluruh Halaman</h2>
      <div class="grid grid-3" style="gap:16px;margin-top:20px;">
        ${ROUTES.map(([slug, name]) => `
          <a href="${slug}.html" style="display:flex;align-items:center;justify-content:space-between;padding:12px 16px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;text-decoration:none;color:#103447;font-weight:600;font-size:14px;">
            <span>${name}</span>
            <span style="color:#087f89;">${ic('arrow')}</span>
          </a>
        `).join('')}
      </div>
    </div>
  </div></section>`;
}

// 24. PRIVASI (privasiPage)
function privasiPage() {
  return pageHero('privasi','Pelindungan Data','Kebijakan Privasi Portal','Komitmen Dinas Kesehatan Kabupaten Pinrang dalam melindungi kerahasiaan data pribadi pengguna.')+`<section class="content"><div class="container twocol"><div class="stack">
    <article class="panel">
      <h2>Kebijakan Privasi & Keamanan Data</h2>
      <p style="font-size:15px;line-height:1.7;color:#334155;">
        Dinas Kesehatan Kabupaten Pinrang menjamin bahwa seluruh data identitas atau pengaduan yang disampaikan masyarakat melalui portal ini dilindungi kerahasiaannya sesuai ketentuan undang-undang pelindungan data pribadi yang berlaku di Indonesia.
      </p>
    </article>
  </div>${side('Informasi',[['privasi','Kebijakan Privasi'],['aksesibilitas','Aksesibilitas'],['kontak','Kontak Dinas']])}</div></section>`;
}

// 25. AKSESIBILITAS (aksesibilitasPage)
function aksesibilitasPage() {
  return pageHero('aksesibilitas','Inklusivitas Web','Komitmen Aksesibilitas Portal','Portal dirancang agar dapat diakses oleh seluruh lapisan masyarakat termasuk penyandang disabilitas.')+`<section class="content"><div class="container twocol"><div class="stack">
    <article class="panel">
      <h2>Standar Aksesibilitas Web</h2>
      <p style="font-size:15px;line-height:1.7;color:#334155;">
        Portal ini mengimplementasikan fitur perbesaran font (Aa), navigasi ramah pembaca layar (screen reader friendly), serta rasio kontras warna tinggi sesuai panduan WCAG 2.1.
      </p>
    </article>
  </div>${side('Informasi',[['aksesibilitas','Aksesibilitas'],['privasi','Kebijakan Privasi'],['faq','FAQ']])}</div></section>`;
}

// 26. SKM (skmPage)
function skmPage() {
  return pageHero('skm','Mutu Layanan Publik','Survei Kepuasan Masyarakat (SKM)','Partisipasi Anda sangat berharga untuk meningkatkan kualitas pelayanan kesehatan di Kabupaten Pinrang.')+`<section class="content"><div class="container twocol"><div class="stack">
    <article class="panel">
      <h2>Survei Kepuasan Masyarakat</h2>
      <p style="font-size:15px;line-height:1.7;color:#334155;">
        Hasil Indeks Kepuasan Masyarakat (IKM) Dinas Kesehatan Kabupaten Pinrang meraih nilai <strong>88.75</strong> dengan predikat <strong>Sangat Baik</strong> (Kategori A).
      </p>
      <div style="margin-top:20px;">
        <a href="https://wa.me/6285342172724" target="_blank" rel="noopener" class="btn primary">Beri Masukan & Ulasan Pelayanan</a>
      </div>
    </article>
  </div>${side('Survei & Aduan',[['skm','Survei Kepuasan'],['pengaduan','Kanal Pengaduan'],['layanan','Katalog Layanan']])}</div></section>`;
}

// 27. PENGUMUMAN (pengumumanPage)
function pengumumanPage() {
  return pageHero('pengumuman','Pemberitahuan Resmi','Pengumuman & Surat Edaran Penting','Informasi resmi, surat edaran, dan pengumuman pelaksanaan program dinas.')+`<section class="content"><div class="container">
    <div class="panel">
      <h2>Pengumuman Resmi Terkini</h2>
      <div style="padding:20px;background:#f0fdf9;border:1px solid #bbf7d0;border-radius:14px;margin-top:16px;">
        <span class="v4-news-tag">PENGUMUMAN DAERAH</span>
        <h3 style="margin:8px 0 6px 0;font-size:18px;color:#103447;">Pelaksanaan Program Cek Kesehatan Gratis (CKG) di 19 Puskesmas</h3>
        <p style="font-size:14px;color:#475569;line-height:1.6;margin:0;">
          Diberitahukan kepada seluruh warga Kabupaten Pinrang bahwa layanan skrining faktor risiko PTM (Cek Kesehatan Gratis) dapat diakses setiap hari kerja di seluruh 19 UPTD Puskesmas tanpa biaya.
        </p>
      </div>
    </div>
  </div></section>`;
}

// 28. MISSING PAGE (missingPage)
function missingPage() {
  return pageHero('tidak-ditemukan','Error 404','Halaman Tidak Ditemukan','Halaman yang Anda tuju mungkin telah dipindahkan atau tautan tidak valid.')+`<section class="content"><div class="container text-center" style="padding:60px 0;">
    <h2 style="font-size:36px;color:#103447;margin-bottom:12px;">404 - Halaman Tidak Ditemukan</h2>
    <p style="font-size:16px;color:#64748b;margin-bottom:24px;">Silakan kembali ke halaman utama untuk menemukan informasi yang Anda cari.</p>
    <a href="index.html" class="btn primary">Kembali ke Beranda</a>
  </div></section>`;
}

// ROUTER & EVENT LISTENERS
const pages = {
  index: homePage,
  profil: profilPage,
  organisasi: organisasiPage,
  layanan: layananPage,
  'layanan-detail': layananDetailPage,
  puskesmas: puskesmasPage,
  'puskesmas-detail': puskesmasDetailPage,
  edukasi: edukasiPage,
  'edukasi-detail': edukasiDetailPage,
  berita: beritaPage,
  'berita-detail': beritaDetailPage,
  galeri: galeriPage,
  data: dataPage,
  indikator: indikatorPage,
  publikasi: publikasiPage,
  ppid: ppidPage,
  informasi: informasiPage,
  pengaduan: pengaduanPage,
  kontak: kontakPage,
  inovasi: inovasiPage,
  faq: faqPage,
  pencarian: pencarianPage,
  'peta-situs': siteMapPage,
  privasi: privasiPage,
  aksesibilitas: aksesibilitasPage,
  skm: skmPage,
  pengumuman: pengumumanPage,
  'tidak-ditemukan': missingPage
};

function attach() {
  // Mobile Nav Toggle
  const toggle = document.getElementById('mobileToggle');
  const mobile = document.getElementById('mobileNav');
  toggle?.addEventListener('click', () => {
    const open = mobile.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
    toggle.innerHTML = ic(open ? 'close' : 'menu');
  });

  // Dropdowns
  document.querySelectorAll('.navgroup > button').forEach(b => {
    b.addEventListener('click', () => {
      const g = b.parentElement;
      const open = g.classList.toggle('open');
      b.setAttribute('aria-expanded', String(open));
    });
  });

  // Search Toggle
  const s = document.getElementById('quickSearch');
  document.getElementById('searchToggle')?.addEventListener('click', () => {
    s.classList.toggle('open');
    if (s.classList.contains('open')) {
      document.getElementById('quickSearchInput')?.focus();
    }
  });

  // Font Size Toggle
  document.getElementById('fontToggle')?.addEventListener('click', () => {
    const large = document.body.classList.toggle('font-large');
    document.getElementById('fontToggle')?.setAttribute('aria-pressed', String(large));
  });

  // Filter Puskesmas
  const pkmSearch = document.getElementById('pkmSearch');
  const pkmDistrict = document.getElementById('pkmDistrict');
  if (pkmSearch || pkmDistrict) {
    const doPkmFilter = () => {
      const q = (pkmSearch?.value || '').toLowerCase().trim();
      const dist = (pkmDistrict?.value || '').toLowerCase().trim();
      let shown = 0;
      document.querySelectorAll('#pkmGrid .v4-pkm-card').forEach(card => {
        const name = card.dataset.name || '';
        const d = card.dataset.district || '';
        const kapus = card.dataset.kapus || '';
        const inovasi = card.dataset.inovasi || '';
        const matchQ = !q || name.includes(q) || d.includes(q) || kapus.includes(q) || inovasi.includes(q);
        const matchDist = !dist || d === dist;
        const visible = matchQ && matchDist;
        card.style.display = visible ? 'flex' : 'none';
        if (visible) shown++;
      });
      const emptyEl = document.getElementById('pkmEmpty');
      if (emptyEl) emptyEl.classList.toggle('hidden', shown > 0);
    };
    pkmSearch?.addEventListener('input', doPkmFilter);
    pkmDistrict?.addEventListener('change', doPkmFilter);
    document.getElementById('pkmReset')?.addEventListener('click', () => {
      if (pkmSearch) pkmSearch.value = '';
      if (pkmDistrict) pkmDistrict.value = '';
      doPkmFilter();
    });
  }

  // Filter Berita & Paginasi
  const newsSearch = document.getElementById('newsSearch');
  const newsCat = document.getElementById('newsCategory');
  if (newsSearch || newsCat) {
    let currentPage = 1;
    const perPage = 9;
    const renderNewsPage = (p) => {
      currentPage = p;
      const q = (newsSearch?.value || '').toLowerCase().trim();
      const cat = (newsCat?.value || '').toLowerCase().trim();
      const articles = window.ARTICLES_CACHE || [];
      const filtered = articles.filter(item => {
        const matchQ = !q || item.title.toLowerCase().includes(q) || item.excerpt.toLowerCase().includes(q);
        const matchCat = !cat || item.category.toLowerCase().includes(cat);
        return matchQ && matchCat;
      });

      const start = (p - 1) * perPage;
      const paged = filtered.slice(start, start + perPage);
      const grid = document.getElementById('newsGrid');
      if (grid) {
        grid.innerHTML = paged.map(item => `
          <article class="v4-news-card news-entry" data-title="${item.title.toLowerCase()}" data-category="${(item.category||'').toLowerCase()}">
            <div class="v4-news-thumb-wrap">
              <img src="${getSafeImageUrl(item.featured_image)}" alt="${item.title}" class="v4-news-thumb" />
            </div>
            <div class="v4-news-body">
              <div class="v4-news-tags">
                <span class="v4-news-tag">${item.category || 'Berita'}</span>
                <span style="font-size:12px;color:#94a3b8;">${item.published_at}</span>
              </div>
              <h3 class="v4-news-title">
                <a href="berita-detail.html?id=${item.id}" style="color:#103447;text-decoration:none;">${item.title}</a>
              </h3>
              <p class="v4-news-excerpt">
                ${item.excerpt}
              </p>
              <div class="v4-news-footer">
                <span>${ic('user')} ${item.author}</span>
                <a href="berita-detail.html?id=${item.id}" style="font-size:13px;font-weight:700;color:#087f89;text-decoration:none;">
                  Baca artikel ${ic('arrow')}
                </a>
              </div>
            </div>
          </article>
        `).join('');
      }

      const emptyEl = document.getElementById('newsEmpty');
      if (emptyEl) emptyEl.classList.toggle('hidden', filtered.length > 0);

      // Update Pagination Buttons
      const totalPages = Math.ceil(filtered.length / perPage) || 1;
      const paginationEl = document.getElementById('newsPagination');
      if (paginationEl) {
        let btnHtml = '';
        const maxButtons = Math.min(totalPages, 5);
        for (let i = 1; i <= maxButtons; i++) {
          btnHtml += `<button class="v4-page-btn ${i === p ? 'is-active' : ''}" data-page="${i}">${i}</button>`;
        }
        if (totalPages > 5) {
          btnHtml += `<span style="color:#94a3b8;padding:0 8px;">...</span>`;
          btnHtml += `<button class="v4-page-btn ${totalPages === p ? 'is-active' : ''}" data-page="${totalPages}">${totalPages}</button>`;
        }
        paginationEl.innerHTML = btnHtml;
        paginationEl.querySelectorAll('.v4-page-btn').forEach(btn => {
          btn.addEventListener('click', () => {
            renderNewsPage(parseInt(btn.dataset.page));
            window.scrollTo({ top: 300, behavior: 'smooth' });
          });
        });
      }
    };

    newsSearch?.addEventListener('input', () => renderNewsPage(1));
    newsCat?.addEventListener('change', () => renderNewsPage(1));
    document.getElementById('newsReset')?.addEventListener('click', () => {
      if (newsSearch) newsSearch.value = '';
      if (newsCat) newsCat.value = '';
      renderNewsPage(1);
    });

    renderNewsPage(1);
  }

  // Global Search Handler
  const globalInput = document.getElementById('globalSearch');
  if (globalInput) {
    const doGlobalSearch = () => {
      const q = globalInput.value.toLowerCase().trim();
      const articles = window.ARTICLES_CACHE || [];
      const puskesmas = window.PUSKESMAS_DATA || [];
      const resEl = document.getElementById('searchResults');
      const countEl = document.getElementById('searchCount');
      if (!resEl) return;

      if (!q) {
        countEl.textContent = 'Silakan masukkan kata kunci pencarian.';
        resEl.innerHTML = '';
        return;
      }

      const foundArticles = articles.filter(a => a.title.toLowerCase().includes(q) || a.excerpt.toLowerCase().includes(q));
      const foundPkm = puskesmas.filter(p => p.name.toLowerCase().includes(q) || p.district.toLowerCase().includes(q));
      const total = foundArticles.length + foundPkm.length;

      countEl.textContent = `Ditemukan ${total} hasil untuk "${q}":`;
      let html = '';

      foundPkm.forEach(p => {
        html += `
          <div style="background:#f0fdf9;padding:16px;border-radius:12px;border:1px solid #bbf7d0;">
            <span style="font-size:11px;font-weight:700;color:#047857;text-transform:uppercase;">UPTD PUSKESMAS</span>
            <h4 style="margin:4px 0;font-size:16px;"><a href="puskesmas-detail.html?no=${p.no}" style="color:#103447;">${p.name}</a></h4>
            <p style="margin:0;font-size:13px;color:#64748b;">${p.address}</p>
          </div>`;
      });

      foundArticles.slice(0, 15).forEach(a => {
        html += `
          <div style="background:#ffffff;padding:16px;border-radius:12px;border:1px solid #e2e8f0;">
            <span style="font-size:11px;font-weight:700;color:#087f89;text-transform:uppercase;">BERITA - ${a.published_at}</span>
            <h4 style="margin:4px 0;font-size:16px;"><a href="berita-detail.html?id=${a.id}" style="color:#103447;">${a.title}</a></h4>
            <p style="margin:0;font-size:13px;color:#64748b;">${a.excerpt}</p>
          </div>`;
      });

      resEl.innerHTML = html;
    };

    globalInput.addEventListener('input', doGlobalSearch);
    document.getElementById('searchExecute')?.addEventListener('click', doGlobalSearch);
    doGlobalSearch();
  }
}

// INTI EKSEKUSI
(function() {
  const page = document.body.dataset.page || 'index';
  window.CURRENT_PAGE = page;
  
  // Cari label title
  const routeObj = ROUTES.find(r => r[0] === page);
  const pageTitle = routeObj ? routeObj[1] : 'Portal Informasi';
  document.title = `${pageTitle} | Dinas Kesehatan Pemerintah Kabupaten Pinrang`;

  const appEl = document.getElementById('app');
  if (appEl) {
    const renderFn = pages[page] || homePage;
    appEl.innerHTML = header(page) + `<main id="main" class="main">${renderFn()}</main>` + footer();
    attach();
  }
})();
