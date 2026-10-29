function homePage() {
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
}

// 2. PROFIL (profilPage)
function profilPage