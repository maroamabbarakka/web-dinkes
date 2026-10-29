import re

responsive_css = """
/* ==========================================================================
   SUPER RESPONSIF PORTAL DINAS KESEHATAN KABUPATEN PINRANG (DEFINITIVE MOBILE/TABLET/DESKTOP)
   ========================================================================== */

/* 1. Viewport & Kontainer Global Anti-Overflow */
html, body {
  overflow-x: hidden !important;
  max-width: 100vw !important;
  box-sizing: border-box;
}

*, *::before, *::after {
  box-sizing: inherit;
}

.container {
  width: 100%;
  max-width: 1240px;
  margin-inline: auto;
  padding-inline: clamp(14px, 3.5vw, 24px);
}

/* 2. Responsive Grid Utility Classes */
.grid {
  display: grid;
  gap: 24px;
}
.grid-2 {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}
.grid-3 {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}
.grid-4 {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

@media (max-width: 991px) {
  .grid-4 {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    gap: 20px;
  }
  .grid-3 {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    gap: 20px;
  }
}

@media (max-width: 640px) {
  .grid-4, .grid-3, .grid-2 {
    grid-template-columns: minmax(0, 1fr) !important;
    gap: 16px;
  }
}

/* 3. Hero Stage & Spotlight Side Cards */
.v4-stage-grid {
  display: grid;
  grid-template-columns: 1.55fr 0.85fr;
  gap: 24px;
  align-items: stretch;
}

.v4-stage-side {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.v4-stage-side .v4-spotlight {
  flex: 1;
}

@media (max-width: 991px) {
  .v4-stage-grid {
    grid-template-columns: 1fr !important;
    gap: 20px;
  }
  .v4-stage-side {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 16px !important;
  }
}

@media (max-width: 640px) {
  .v4-stage-side {
    display: flex !important;
    flex-direction: column !important;
    gap: 14px !important;
  }
  .v4-feature-inner {
    padding: 26px 18px !important;
  }
  .v4-feature-inner h1 {
    font-size: clamp(22px, 6.2vw, 29px) !important;
    line-height: 1.25 !important;
  }
  .v4-spotlight {
    padding: 20px 18px !important;
    min-height: auto !important;
  }
  .v4-spotlight h2 {
    font-size: 18px !important;
    margin: 10px 0 6px 0 !important;
  }
  .v4-spotlight p {
    font-size: 13px !important;
    line-height: 1.55 !important;
  }
}

/* 4. Berita & Kegiatan Grid (Fix Lead News & Side News Overflow) */
.v4-news-feature-grid {
  display: grid;
  grid-template-columns: 1.25fr 1fr;
  gap: 32px;
  align-items: start;
}

.v4-side-news-item {
  background: #ffffff;
  border: 1px solid #dce8eb;
  border-radius: 14px;
  padding: 16px;
  display: grid;
  grid-template-columns: 110px 1fr;
  gap: 16px;
  align-items: center;
  transition: all 0.25s ease;
}

.v4-side-news-item:hover {
  transform: translateY(-2px);
  border-color: #0aa398;
  box-shadow: 0 8px 24px rgba(8, 127, 137, 0.08);
}

.v4-side-news-thumb {
  width: 110px;
  height: 85px;
  border-radius: 10px;
  overflow: hidden;
  background: #e2e8f0;
  flex-shrink: 0;
}

.v4-side-news-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

@media (max-width: 991px) {
  .v4-news-feature-grid {
    grid-template-columns: 1fr !important;
    gap: 24px;
  }
}

@media (max-width: 480px) {
  .v4-side-news-item {
    grid-template-columns: 85px 1fr !important;
    gap: 12px !important;
    padding: 12px !important;
  }
  .v4-side-news-thumb {
    width: 85px !important;
    height: 70px !important;
  }
}

@media (max-width: 340px) {
  .v4-side-news-item {
    grid-template-columns: 1fr !important;
    gap: 10px !important;
  }
  .v4-side-news-thumb {
    width: 100% !important;
    height: 120px !important;
  }
}

/* 5. Executive Leadership Card Responsif */
@media (max-width: 860px) {
  .v4-exec-card {
    grid-template-columns: 1fr !important;
    text-align: center;
    gap: 20px;
    padding: 24px 18px !important;
  }
  .v4-exec-photo-wrap {
    max-width: 240px;
    margin: 0 auto;
  }
  .v4-exec-photo {
    height: 280px !important;
  }
  .v4-exec-quote {
    text-align: left;
    font-size: 14px;
    padding: 14px 16px;
  }
  .v4-exec-actions {
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .v4-exec-actions .btn {
    width: 100%;
    justify-content: center;
  }
}

/* 6. Puskesmas Grid Responsif */
@media (max-width: 640px) {
  .v4-pkm-grid {
    grid-template-columns: 1fr !important;
    gap: 16px;
  }
  .v4-pkm-card {
    padding: 18px 16px !important;
  }
}

/* 7. Header Brandbar & Topbar Responsif */
@media (max-width: 640px) {
  .brandbar .container {
    padding-block: 10px;
  }
  .brandbar-logos img {
    height: 36px;
  }
  .brandbar-title h1 {
    font-size: 14px;
  }
  .brandbar-title span {
    font-size: 10.5px;
  }
}
@media (max-width: 360px) {
  .brandbar-logos img {
    height: 30px;
  }
  .brandbar-title h1 {
    font-size: 12.5px;
  }
}

/* 8. Tab Switcher Horizontal di Mobile */
.tab-filter-container {
  display: flex;
  gap: 10px;
  overflow-x: auto;
  padding-bottom: 14px;
  margin-bottom: 24px;
  border-bottom: 2px solid #e2e8f0;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
}
.tab-filter-container::-webkit-scrollbar {
  display: none;
}
"""

with open('public/assets/style.css', 'r', encoding='utf-8') as f:
    style_content = f.read()

# Hapus injeksi lama jika ada
if '/* ==========================================================================' in style_content and 'SUPER RESPONSIF PORTAL DINAS KESEHATAN KABUPATEN PINRANG' in style_content:
    idx = style_content.find('/* ==========================================================================\n   SUPER RESPONSIF PORTAL DINAS KESEHATAN KABUPATEN PINRANG')
    style_content = style_content[:idx]

style_content = style_content.rstrip() + '\n\n' + responsive_css.strip() + '\n'

with open('public/assets/style.css', 'w', encoding='utf-8') as f:
    f.write(style_content)
print("Berhasil menyematkan responsive_css ke public/assets/style.css")

with open('public/assets/v4.css', 'r', encoding='utf-8') as f:
    v4_content = f.read()

# Hapus injeksi lama jika ada
if '/* ==========================================================================' in v4_content and 'SUPER RESPONSIF PORTAL DINAS KESEHATAN KABUPATEN PINRANG' in v4_content:
    idx = v4_content.find('/* ==========================================================================\n   SUPER RESPONSIF PORTAL DINAS KESEHATAN KABUPATEN PINRANG')
    v4_content = v4_content[:idx]

v4_content = v4_content.rstrip() + '\n\n' + responsive_css.strip() + '\n'

with open('public/assets/v4.css', 'w', encoding='utf-8') as f:
    f.write(v4_content)
print("Berhasil menyematkan responsive_css ke public/assets/v4.css")

