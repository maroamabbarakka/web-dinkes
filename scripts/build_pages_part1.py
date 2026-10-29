
// 1. BERANDA (homePage)
function homePage() {
  const leadNews = window.ARTICLES_CACHE.find(a => a.id === '4505') || window.ARTICLES_CACHE[4] || {
    id: '4505',
    title: 'Kecamatan Batulappa Jadi Penutup Rangkaian Kampanye GERMAS Dinkes Pinrang, Dorong Deteksi Dini',
    published_at: '23 Oktober 2026',
    author: 'Muhammad Rusdi',
    category: 'Kegiatan',
    featured_image: 'https://dinkes.pinrangkab.go.id/wp-content/uploads/2026/10/cbe0e611-4ec4-4b64-b3ca-7fce94ef85a7.jpeg',
    excerpt: 'Tim Kerja Promosi Kesehatan dan Pemberdayaan Masyarakat Dinas Kesehatan Kabupaten Pinrang sukses menuntaskan rangkaian Kampanye Gerakan Masyarakat Hidup Sehat (GERMAS) di 12 kecamatan se-Kabupaten Pinrang.'
  };

  const sideNews = [
    window.ARTICLES_CACHE.find(a => a.id === '4498') || window.ARTICLES_CACHE[5],
    window.ARTICLES_CACHE.find(a => a.id === '4492') || window.ARTICLES_CACHE[6],
    window.ARTICLES_CACHE.find(a => a.id === '4164') || window.ARTICLES_CACHE[7],
    window.ARTICLES_CACHE.find(a => a.id === '4053') || window.ARTICLES_CACHE[8]
  ].filter(Boolean);

  const topPkm = (window.PUSKESMAS_DATA || []).slice(0, 6);

  return `
  <div class="v4-breaking">
    <div class="container v4-breaking-inner">
      <span class="v4-breaking-label">${ic('bell')} INFORMASI RESMI</span>
      <span>Selamat datang di Portal Informasi & Pelayanan Publik Resmi Dinas Kesehatan Pemerintah Kabupaten Pinrang.</span>
      <a href="pengumuman.html">Lihat pengumuman ${ic('arrow')}</a>
    </div>
  </div>

  <!-- HERO STAGE V4 -->
  <section class="v4-mainstage">
    <div class="container v4-stage-grid">
      <div class="v4-feature-rail">
        <div class="v4-feature-slide is-active">
          <div class="v4-feature-inner">
            <span class="v4-feature-pill">PELAYANAN KESEHATAN TERPADU</span>
            <h1 class="v4-feature-headline">Transformasi Layanan Kesehatan Primer Menuju Pinrang Sehat & Mandiri</h1>
            <p class="v4-feature-lead">
              Pemerintah Kabupaten Pinrang menghadirkan pelayanan kesehatan yang berkualitas, merata, dan mudah diakses melalui 19 UPTD Puskesmas, jaringan Posyandu, dan integrasi rujukan medis 24 Jam.
            </p>
            <div class="v4-stage-actions">
              <a href="layanan.html" class="btn primary">${ic('heart')} Akses Layanan Publik</a>
              <a href="puskesmas.html" class="btn secondary">${ic('hospital')} Cari 19 Puskesmas</a>
            </div>
          </div>
        </div>
      </div>
      <div class="v4-stage-sidebar">
        <a href="layanan-detail.html" class="v4-promo-card v4-promo-teal" style="text-decoration:none;">
          <span class="v4-promo-eyebrow">PROGRAM UNGGULAN DAERAH</span>
          <h3>Cek Kesehatan Gratis (CKG)</h3>
          <p>Skrining riwayat kesehatan berkala di 19 UPTD Puskesmas se-Kabupaten Pinrang tanpa dipungut biaya.</p>
          <span class="v4-promo-link">Lihat prosedur pemeriksaan ${ic('arrow')}</span>
        </a>
        <a href="profil.html" class="v4-promo-card v4-promo-navy" style="text-decoration:none;">
          <span class="v4-promo-eyebrow">DOKUMENTASI KELEMBAGAAN</span>
          <h3>Profil Pimpinan & Visi Misi</h3>
          <p>Mengenal komitmen dr. H. Ramli Yunus, M.Kes dan arah kebijakan strategis pembangunan kesehatan daerah.</p>
          <span class="v4-promo-link">Baca selengkapnya ${ic('arrow')}</span>
        </a>
      </div>
    </div>
  </section>

  <!-- EXECUTIVE GREETING CARD (KEPALA DINAS) -->
  <section class="content" style="padding:40px 0 20px 0;">
    <div class="container">
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
            <a href="profil.html" class="btn primary">${ic('user')} Profil Lengkap & Arah Kebijakan</a>
            <a href="organisasi.html" class="btn secondary">${ic('people')} Struktur Organisasi</a>
          </div>
        </div>
      </article>
    </div>
  </section>

  <!-- KATALOG LAYANAN PUBLIK BENTO GRID -->
  <section class="content" style="background:#f7fafb;padding:48px 0;">
    <div class="container">
      <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:28px;flex-wrap:wrap;gap:16px;">
        <div>
          <span class="kicker">PELAYANAN PUBLIK PRIMA</span>
          <h2 style="margin:4px 0 0 0;font-size:28px;color:#103447;">Informasi & Standar Pelayanan Kesehatan</h2>
        </div>
        <a href="layanan.html" class="btn secondary">Lihat Semua Layanan ${ic('arrow')}</a>
      </div>

      <div class="grid grid-3" style="gap:20px;">
        <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:18px;padding:24px;box-shadow:0 8px 24px rgba(16,52,71,0.04);display:flex;flex-direction:column;">
          <div style="width:48px;height:48px;border-radius:14px;background:#e6f7f5;display:flex;align-items:center;justify-content:center;color:#087f89;margin-bottom:16px;">
            <img src="assets/puskesmas.png" alt="Logo Puskesmas" style="width:32px;height:32px;object-fit:contain;" />
          </div>
          <h3 style="font-size:18px;font-weight:700;color:#103447;margin-bottom:8px;">Pelayanan 19 UPTD Puskesmas</h3>
          <p style="font-size:14px;color:#587084;line-height:1.6;margin-bottom:16px;flex-grow:1;">
            Pelayanan rawat jalan, poli umum, KIA, imunisasi anak, laboratorium, serta IGD & Bersalin 24 Jam di 12 kecamatan.
          </p>
          <a href="puskesmas.html" style="font-size:14px;font-weight:700;color:#087f89;text-decoration:none;display:inline-flex;align-items:center;gap:6px;">
            Cari Puskesmas terdekat ${ic('arrow')}
          </a>
        </div>

        <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:18px;padding:24px;box-shadow:0 8px 24px rgba(16,52,71,0.04);display:flex;flex-direction:column;">
          <div style="width:48px;height:48px;border-radius:14px;background:#fef3c7;display:flex;align-items:center;justify-content:center;color:#d97706;margin-bottom:16px;">
            ${ic('file')}
          </div>
          <h3 style="font-size:18px;font-weight:700;color:#103447;margin-bottom:8px;">Perizinan SIP & SIK Nakes</h3>
          <p style="font-size:14px;color:#587084;line-height:1.6;margin-bottom:16px;flex-grow:1;">
            Penerbitan surat rekomendasi izin praktik dokter, perawat, bidan, apoteker, dan tenaga kesehatan lainnya secara transparan.
          </p>
          <a href="layanan-detail.html" style="font-size:14px;font-weight:700;color:#087f89;text-decoration:none;display:inline-flex;align-items:center;gap:6px;">
            Lihat syarat & alur ${ic('arrow')}
          </a>
        </div>

        <div class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:18px;padding:24px;box-shadow:0 8px 24px rgba(16,52,71,0.04);display:flex;flex-direction:column;">
          <div style="width:48px;height:48px;border-radius:14px;background:#ecfdf5;display:flex;align-items:center;justify-content:center;color:#059669;margin-bottom:16px;">
            ${ic('shield')}
          </div>
          <h3 style="font-size:18px;font-weight:700;color:#103447;margin-bottom:8px;">Sertifikasi Pangan (SPP-IRT)</h3>
          <p style="font-size:14px;color:#587084;line-height:1.6;margin-bottom:16px;flex-grow:1;">
            Penyuluhan dan pendampingan sertifikat pemenuhan komitmen produksi pangan industri rumah tangga agar aman konsumsi.
          </p>
          <a href="layanan-detail.html" style="font-size:14px;font-weight:700;color:#087f89;text-decoration:none;display:inline-flex;align-items:center;gap:6px;">
            Panduan sertifikasi ${ic('arrow')}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- BERITA & KEGIATAN TERKINI (FOTO KEGIATAN LAPANGAN NYATA) -->
  <section class="content" style="padding:48px 0;">
    <div class="container">
      <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:28px;flex-wrap:wrap;gap:16px;">
        <div>
          <span class="kicker">DOKUMENTASI & KABAR TERKINI</span>
          <h2 style="margin:4px 0 0 0;font-size:28px;color:#103447;">Berita & Kegiatan Dinas Kesehatan</h2>
        </div>
        <a href="berita.html" class="btn secondary">Semua Arsip Berita (${window.ARTICLES_CACHE.length}) ${ic('arrow')}</a>
      </div>

      <div class="v4-news-grid" style="grid-template-columns:1.2fr 1fr;gap:32px;">
        <!-- Lead News Story -->
        <article class="v4-news-card" style="box-shadow:0 12px 32px rgba(16,52,71,0.08);">
          <div class="v4-news-thumb-wrap" style="padding-top:54%;">
            <img src="${getSafeImageUrl(leadNews.featured_image)}" alt="${leadNews.title}" class="v4-news-thumb" />
          </div>
          <div class="v4-news-body" style="padding:28px;">
            <div class="v4-news-tags">
              <span class="v4-news-tag">${leadNews.category || 'Kegiatan'}</span>
              <span style="font-size:12.5px;color:#94a3b8;">${leadNews.published_at}</span>
            </div>
            <h3 class="v4-news-title" style="font-size:22px;line-height:1.35;margin-bottom:12px;">
              <a href="berita-detail.html?id=${leadNews.id}" style="color:#103447;text-decoration:none;">${leadNews.title}</a>
            </h3>
            <p class="v4-news-excerpt" style="font-size:15px;line-height:1.7;color:#475569;">
              ${leadNews.excerpt}
            </p>
            <div class="v4-news-footer">
              <span>${ic('user')} Oleh: ${leadNews.author}</span>
              <a href="berita-detail.html?id=${leadNews.id}" class="btn primary" style="font-size:13px;padding:6px 14px;">
                Baca Berita Lengkap ${ic('arrow')}
              </a>
            </div>
          </div>
        </article>

        <!-- Side News Grid -->
        <div style="display:grid;gap:16px;">
          ${sideNews.map(item => `
            <article class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:14px;padding:16px;display:grid;grid-template-columns:110px 1fr;gap:16px;align-items:center;">
              <div style="width:110px;height:85px;border-radius:10px;overflow:hidden;background:#e2e8f0;flex-shrink:0;">
                <img src="${getSafeImageUrl(item.featured_image)}" alt="${item.title}" style="width:100%;height:100%;object-fit:cover;" />
              </div>
              <div>
                <span style="font-size:11px;font-weight:700;color:#087f89;text-transform:uppercase;">${item.category || 'Berita'} - ${item.published_at}</span>
                <h4 style="font-size:14.5px;font-weight:700;color:#103447;line-height:1.35;margin:4px 0 6px 0;">
                  <a href="berita-detail.html?id=${item.id}" style="color:#103447;text-decoration:none;">${item.title}</a>
                </h4>
                <a href="berita-detail.html?id=${item.id}" style="font-size:12.5px;font-weight:600;color:#087f89;text-decoration:none;">
                  Baca detail ${ic('arrow')}
                </a>
              </div>
            </article>
          `).join('')}
        </div>
      </div>
    </div>
  </section>

  <!-- DATA & CAPAIAN INDIKATOR DAERAH -->
  <section class="v4-data-band" style="background:#103447;color:#ffffff;padding:50px 0;">
    <div class="container">
      <div style="text-align:center;max-width:700px;margin:0 auto 36px auto;">
        <span style="font-size:12px;font-weight:800;letter-spacing:0.08em;color:#5eead4;text-transform:uppercase;">SATU DATA KESEHATAN KABUPATEN PINRANG</span>
        <h2 style="font-size:28px;color:#ffffff;margin:8px 0 10px 0;">Capaian Indikator Prioritas Kesehatan Daerah</h2>
        <p style="font-size:14.5px;color:#cbd5e1;line-height:1.6;">
          Bukti nyata komitmen akselerasi transformasi kesehatan di bawah kepemimpinan Dinas Kesehatan Kabupaten Pinrang.
        </p>
      </div>

      <div class="grid grid-4" style="gap:20px;">
        <div class="panel text-center" style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);border-radius:16px;padding:24px;">
          <div style="font-size:38px;font-weight:800;color:#5eead4;margin-bottom:6px;">100%</div>
          <strong style="font-size:14.5px;color:#ffffff;display:block;margin-bottom:4px;">Bebas BAB Sembarangan (ODF)</strong>
          <span style="font-size:12px;color:#94a3b8;">12 Kecamatan Terverifikasi Bebas Buang Air Besar Sembarangan</span>
        </div>

        <div class="panel text-center" style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);border-radius:16px;padding:24px;">
          <div style="font-size:38px;font-weight:800;color:#5eead4;margin-bottom:6px;">96.4%</div>
          <strong style="font-size:14.5px;color:#ffffff;display:block;margin-bottom:4px;">Cakupan Imunisasi BIAN</strong>
          <span style="font-size:12px;color:#94a3b8;">Kabupaten Tercepat Mencapai Target Minimal 95% se-Sulsel</span>
        </div>

        <div class="panel text-center" style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);border-radius:16px;padding:24px;">
          <div style="font-size:38px;font-weight:800;color:#5eead4;margin-bottom:6px;">12.8%</div>
          <strong style="font-size:14.5px;color:#ffffff;display:block;margin-bottom:4px;">Penurunan Prevalensi Stunting</strong>
          <span style="font-size:12px;color:#94a3b8;">Melampaui target nasional (di bawah 14%)</span>
        </div>

        <div class="panel text-center" style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);border-radius:16px;padding:24px;">
          <div style="font-size:38px;font-weight:800;color:#5eead4;margin-bottom:6px;">19</div>
          <strong style="font-size:14.5px;color:#ffffff;display:block;margin-bottom:4px;">Puskesmas Terakreditasi</strong>
          <span style="font-size:12px;color:#94a3b8;">Predikat Paripurna dan Utama dari Kemenkes RI</span>
        </div>
      </div>

      <div style="text-align:center;margin-top:28px;">
        <a href="data.html" class="btn secondary" style="background:rgba(255,255,255,0.1);color:#ffffff;border-color:rgba(255,255,255,0.25);">
          Buka Dashboard Satu Data Lengkap ${ic('arrow')}
        </a>
      </div>
    </div>
  </section>

  <!-- DIREKTORI 19 PUSKESMAS -->
  <section class="content" style="padding:48px 0;">
    <div class="container">
      <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:28px;flex-wrap:wrap;gap:16px;">
        <div>
          <span class="kicker">JARINGAN FASILITAS KESEHATAN TINGKAT PERTAMA</span>
          <h2 style="margin:4px 0 0 0;font-size:28px;color:#103447;">19 UPTD Puskesmas Se-Kabupaten Pinrang</h2>
        </div>
        <a href="puskesmas.html" class="btn secondary">Lihat Semua 19 Puskesmas ${ic('arrow')}</a>
      </div>

      <div class="v4-pkm-grid">
        ${topPkm.map(pkm => `
          <div class="v4-pkm-card">
            <div class="v4-pkm-card-header">
              <img src="assets/puskesmas.png" alt="Logo Puskesmas" class="v4-pkm-logo" />
              <div class="v4-pkm-meta">
                <span class="v4-pkm-kec">Kec. ${pkm.district}</span>
                <h3>${pkm.name}</h3>
              </div>
            </div>
            <div class="v4-pkm-head">
              ${ic('user')} <strong>${pkm.head}</strong>
            </div>
            <p style="font-size:13px;color:#64748b;line-height:1.5;margin-bottom:12px;">
              ${ic('location')} ${pkm.address}
            </p>
            ${pkm.innovations_text ? `
              <div class="v4-pkm-inovasi">
                <strong>Inovasi Unggulan:</strong>
                ${pkm.innovations_text}
              </div>
            ` : ''}
            <a href="puskesmas-detail.html?no=${pkm.no}" class="btn primary" style="font-size:13px;padding:8px 14px;text-align:center;justify-content:center;margin-top:auto;">
              Lihat Profil & Layanan ${ic('arrow')}
            </a>
          </div>
        `).join('')}
      </div>
    </div>
  </section>`;
}

// 2. PROFIL (profilPage)
function profilPage() {
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
        "Terwujudnya Masyarakat Pinrang Yang Mandiri Untuk Hidup Sehat"
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
      <strong style="color:#103447;font-size:15px;">"Menyelenggarakan Urusan Pemerintahan di Bidang Kesehatan yang menjadi kewenangan Daerah dan Tugas Pembantuan yang diberikan kepada Daerah Kabupaten Pinrang."</strong>
    </div>

    <h3 style="font-size:17px;font-weight:700;color:#103447;margin-bottom:16px;">Fungsi Utama Dinas Kesehatan:</h3>
    <ul style="display:grid;gap:12px;padding:0;list-style:none;">
      <li style="display:flex;gap:12px;background:#ffffff;border:1px solid #edf2f3;padding:14px 18px;border-radius:12px;">
        <span style="color:#087f89;font-weight:700;">*</span>
        <span style="font-size:14px;color:#334155;"><strong>Perumusan Kebijakan Teknis:</strong> Penyusunan rencana strategis dan kebijakan operasional di bidang kesehatan masyarakat, pencegahan & pengendalian penyakit, serta pelayanan & SDK.</span>
      </li>
      <li style="display:flex;gap:12px;background:#ffffff;border:1px solid #edf2f3;padding:14px 18px;border-radius:12px;">
        <span style="color:#087f89;font-weight:700;">*</span>
        <span style="font-size:14px;color:#334155;"><strong>Pelaksanaan Pelayanan Kesehatan:</strong> Penyelenggaraan pelayanan kesehatan primer melalui 19 UPTD Puskesmas, rujukan terpadu, serta laboratorium kesehatan daerah (Labkesda).</span>
      </li>
      <li style="display:flex;gap:12px;background:#ffffff;border:1px solid #edf2f3;padding:14px 18px;border-radius:12px;">
        <span style="color:#087f89;font-weight:700;">*</span>
        <span style="font-size:14px;color:#334155;"><strong>Pembinaan dan Pengawasan:</strong> Pengawasan mutu faskes, perizinan praktik nakes (SIP/SIK), sertifikasi pangan rumah tangga (SPP-IRT), dan pengendalian mutu obat & makanan.</span>
      </li>
      <li style="display:flex;gap:12px;background:#ffffff;border:1px solid #edf2f3;padding:14px 18px;border-radius:12px;">
        <span style="color:#087f89;font-weight:700;">*</span>
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
        <span class="v4-timeline-badge">2022 - Penghargaan Nasional</span>
        <h4 class="v4-timeline-title">GOLD AWARD IndoHCF & Bebas Frambusia Kemenkes RI</h4>
        <p class="v4-timeline-desc">Meraih Gold Award Indonesia Healthcare Innovation Award (IHIA-VI) kategori Inovasi GERMAS dan Sertifikat Bebas Frambusia dari Menteri Kesehatan RI.</p>
      </div>
      <div class="v4-timeline-item">
        <span class="v4-timeline-badge">2021 - Kabupaten Sehat</span>
        <h4 class="v4-timeline-title">Swasti Saba Wistara ke-IV Kemenkes & Kemendagri RI</h4>
        <p class="v4-timeline-desc">Mempertahankan predikat tertinggi Kabupaten Sehat Swasti Saba Wistara 4 kali berturut-turut (2015, 2017, 2019, 2021) serta OPD Terbaik Citra Pelayanan Prima (CPP).</p>
      </div>
      <div class="v4-timeline-item">
        <span class="v4-timeline-badge">2020 - Sanitasi & Stunting</span>
        <h4 class="v4-timeline-title">Terbaik I Nasional STBM Berkelanjutan & Nominator AMPL</h4>
        <p class="v4-timeline-desc">Penghargaan STBM Berkelanjutan Kategori Demand Creation & Akselerasi Open Defecation Free (ODF) 100% di seluruh desa/kelurahan Kabupaten Pinrang.</p>
      </div>
    </div>
  </article>

  </div>${side('Profil & Informasi Terkait',[['profil','Profil Dinas'],['organisasi','Struktur Organisasi'],['inovasi','Prestasi & Inovasi'],['publikasi','Dokumen Kinerja (LKjIP)'],['layanan','Standar Pelayanan'],['kontak','Kontak Resmi Dinas']])}</div></section>`
}

// 3. ORGANISASI (organisasiPage)
function organisasiPage() {
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
}
