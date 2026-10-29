# -*- coding: utf-8 -*-
"""
Script untuk menambahkan styling responsif mobile top bar dan visual cover di dinsos_theme.css
"""

CSS_ADDITIONS = '''
/* ==========================================================================
   ENHANCEMENTS: SERVICE STRIP RESPONSIVE ICONS & COLORFUL SERVICE COVERS
   ========================================================================== */

/* 1. SERVICE STRIP TOP BAR */
.service-strip {
  background: #0b2230;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  color: #f1f5f9;
}

.strip-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 38px;
  padding-inline: 16px;
}

.strip-brand {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-weight: 600;
  color: #e2e8f0;
}

.strip-icon {
  color: #0aa398;
  flex-shrink: 0;
}

.strip-links {
  display: flex;
  align-items: center;
  gap: 18px;
}

.strip-link-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: #cbd5e1;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.2s ease;
}

.strip-link-item:hover {
  color: #5eead4;
}

.strip-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #5eead4;
  display: inline-block;
  box-shadow: 0 0 6px #5eead4;
}

.strip-link-icon {
  color: #0aa398;
}

/* TAMPILAN DESKTOP */
@media (min-width: 641px) {
  .strip-title-mobile,
  .strip-label-mobile {
    display: none !important;
  }
  .strip-title-desktop,
  .strip-label-desktop {
    display: inline-block !important;
  }
}

/* TAMPILAN MOBILE: RAMPING, RAPI, TANPA TEKS MENUMPUK */
@media (max-width: 640px) {
  .service-strip {
    padding: 2px 0;
  }
  .strip-inner {
    min-height: 34px;
    padding-inline: 10px;
    gap: 8px;
  }
  .strip-title-desktop,
  .strip-label-desktop {
    display: none !important;
  }
  .strip-title-mobile {
    display: inline-block !important;
    font-size: 11px;
    font-weight: 800;
    color: #5eead4;
    letter-spacing: 0.04em;
  }
  .strip-label-mobile {
    display: inline-block !important;
    font-size: 11px;
    font-weight: 700;
  }
  .strip-links {
    gap: 6px !important;
  }
  .strip-link-item {
    font-size: 11px;
    padding: 3px 6px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 6px;
    color: #f8fafc;
  }
  .strip-link-item:active {
    background: #087f89;
  }
  .strip-dot {
    display: none;
  }
}

/* 2. HERO ILLUSTRATION KOLASE EMBLEM */
.hero-illustration--mockup {
  position: relative;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-illustration--mockup img {
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  border-radius: 24px;
}

.hero-illustration--mockup img:hover {
  transform: translateY(-6px) scale(1.02);
}

@media (max-width: 768px) {
  .hero-illustration--mockup img {
    max-width: 320px !important;
    margin: 1.5rem auto 0 !important;
  }
}

/* 3. SERVICE CARD STYLING & MEDIA COVER */
.service-card--mockup {
  position: relative;
  background: #ffffff;
  border-radius: 20px;
  padding: 1.5rem;
  border: 1px solid #e2e8f0;
  box-shadow: 0 4px 16px rgba(16, 52, 71, 0.04);
  transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
  display: flex;
  flex-direction: column;
}

.service-card--mockup:hover {
  transform: translateY(-5px);
  box-shadow: 0 16px 36px rgba(16, 52, 71, 0.1);
}

.service-card-media {
  border-radius: 14px;
  overflow: hidden;
  margin-bottom: 1.25rem;
  background: #f1f5f9;
}

.service-card-media img {
  width: 100%;
  height: 190px;
  object-fit: cover;
  display: block;
  transition: transform 0.35s ease;
}

.service-card--mockup:hover .service-card-media img {
  transform: scale(1.04);
}

/* Warna unik per card */
.service-card--mockup.card-emerald:hover { border-color: #059669; }
.service-card--mockup.card-sapphire:hover { border-color: #1d4ed8; }
.service-card--mockup.card-amber:hover { border-color: #d97706; }
.service-card--mockup.card-cyan:hover { border-color: #087f89; }
.service-card--mockup.card-rose:hover { border-color: #e11d48; }
.service-card--mockup.card-red:hover { border-color: #dc2626; }

/* 4. PROMKES POSTER CARD STYLING */
.promkes-poster-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 16px 32px rgba(16, 52, 71, 0.1) !important;
}

.promkes-poster-card:hover img {
  transform: scale(1.05);
}

.promkes-poster-card img {
  transition: transform 0.35s ease;
}

/* 5. PILAR KESEHATAN CARD STYLING */
.psks-card {
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.psks-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 16px 32px rgba(16, 52, 71, 0.1);
}
'''

with open('public/assets/dinsos_theme.css', 'a', encoding='utf-8') as f:
    f.write('\n' + CSS_ADDITIONS)

print('public/assets/dinsos_theme.css berhasil di-append dengan gaya responsive baru!')
