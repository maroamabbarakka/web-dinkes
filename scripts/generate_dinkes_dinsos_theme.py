import re

with open('scripts/dinsos_main.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Pemetaan variabel & warna Dinsos ke Palet Dinkes
color_map = {
    r'--forest:\s*#[a-fA-F0-9]{3,6}': '--forest: #087f89',
    r'--emerald:\s*#[a-fA-F0-9]{3,6}': '--emerald: #0aa398',
    r'--gold:\s*#[a-fA-F0-9]{3,6}': '--gold: #d97706',
    r'--ink:\s*#[a-fA-F0-9]{3,6}': '--ink: #103447',
    r'--mist:\s*#[a-fA-F0-9]{3,6}': '--mist: #f4f9fc',
    r'--line:\s*#[a-fA-F0-9]{3,6}': '--line: #dce8eb',
    r'#075b3a': '#087f89',
    r'#0c7a4b': '#0aa398',
    r'#063f2a': '#103447',
    r'#043f2b': '#0d2837',
    r'#064e3b': '#103447',
    r'#062f21': '#0b2331',
    r'#053724': '#0f3c63',
    r'#e7f2eb': '#e6f7f5',
    r'#f3f7f4': '#f4f9fc',
    r'#f6faf7': '#f0fdf9',
    r'#dce6df': '#dce8eb',
    r'rgba\(5,\s*55,\s*36,': 'rgba(16, 52, 71,',
    r'rgba\(7,\s*91,\s*58,': 'rgba(8, 127, 137,',
    r'rgba\(8,\s*50,\s*32,': 'rgba(16, 52, 71,',
    r'rgba\(6,\s*78,\s*59,': 'rgba(16, 52, 71,',
}

new_css = css
for pattern, repl in color_map.items():
    new_css = re.sub(pattern, repl, new_css, flags=re.IGNORECASE)

# Tambahkan custom override untuk Dinkes
dinkes_overrides = """
/* ==========================================================================
   DINKES PINRANG THEME OVERRIDES (DINSOS ARCHITECTURE WITH DINKES PALETTE)
   ========================================================================== */
:root {
  --forest: #087f89;
  --forest-dark: #05646c;
  --emerald: #0aa398;
  --gold: #d97706;
  --ink: #103447;
  --muted: #587084;
  --mist: #f4f9fc;
  --white: #ffffff;
  --line: #dce8eb;
  --shadow: 0 12px 36px rgba(16, 52, 71, 0.08);
  --radius: 18px;
}

body {
  font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif !important;
  color: var(--ink);
  background: #ffffff;
  overflow-x: hidden;
}

.service-strip {
  background: #0d2837 !important;
  color: #d1e7f7 !important;
  font-size: 0.82rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}
.service-strip a {
  color: #ffffff !important;
  font-weight: 600;
}
.service-strip a:hover {
  color: #5eead4 !important;
}

.site-header {
  background: rgba(255, 255, 255, 0.98) !important;
  border-bottom: 1px solid var(--line) !important;
  box-shadow: 0 4px 18px rgba(16, 52, 71, 0.04);
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
}
.brand-logos {
  display: flex;
  align-items: center;
  gap: 8px;
}
.brand-logos img {
  height: 48px;
  width: auto;
  object-fit: contain;
}
.site-name {
  color: #103447 !important;
}
.site-name span {
  font-size: 1.15rem;
  font-weight: 800;
  color: #103447;
  line-height: 1.15;
}
.site-name small {
  color: #087f89;
  font-weight: 700;
  font-size: 0.8rem;
}

.primary-nav a {
  color: #1e293b;
  font-weight: 650;
  font-size: 0.93rem;
  transition: all 0.2s;
}
.primary-nav a:hover,
.primary-nav .current-menu-item > a {
  background: #e6f7f5 !important;
  color: #087f89 !important;
}

/* HERO SECTION DINSOS ADAPTED FOR DINKES */
.hero--mockup {
  position: relative;
  background: linear-gradient(135deg, #e6f7f5 0%, #ffffff 60%, #e0f2fe 100%) !important;
  padding: 4.5rem 0 5.5rem !important;
  overflow: hidden;
  border-bottom: 1px solid #dce8eb;
}
.hero-badge-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #e6f7f5 !important;
  color: #087f89 !important;
  border: 1px solid #bbf7d0 !important;
  font-size: 0.78rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 0.4rem 1rem;
  border-radius: 9999px;
  box-shadow: 0 2px 8px rgba(8, 127, 137, 0.08);
}
.hero--mockup .hero-heading {
  font-size: clamp(2.3rem, 4.2vw, 3.6rem);
  font-weight: 900;
  color: #103447 !important;
  line-height: 1.15;
  margin: 0.6rem 0 1.25rem 0;
  letter-spacing: -0.03em;
}
.hero--mockup .hero-lead {
  font-size: 1.1rem;
  color: #475569;
  line-height: 1.7;
  margin-bottom: 2rem;
  max-width: 580px;
}
.hero-search-mockup {
  border: 2px solid #087f89 !important;
  box-shadow: 0 10px 25px rgba(8, 127, 137, 0.15) !important;
}
.hero-search-mockup button {
  background: #087f89 !important;
}
.hero-search-mockup button:hover {
  background: #05646c !important;
}

/* QUICK ACCESS CARDS */
.quick-access-mockup {
  position: relative;
  margin-top: -3.25rem;
  z-index: 20;
  padding-bottom: 2rem;
}
.quick-grid-mockup {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
}
.quick-access-card {
  background: #ffffff;
  border: 1px solid #dce8eb;
  border-radius: 18px;
  padding: 1.25rem 1.4rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  text-decoration: none;
  box-shadow: 0 8px 24px rgba(16, 52, 71, 0.06);
  transition: all 0.25s ease;
}
.quick-access-card:hover {
  transform: translateY(-4px);
  border-color: #087f89;
  box-shadow: 0 16px 36px rgba(8, 127, 137, 0.14);
}
.quick-access-icon {
  width: 48px;
  height: 48px;
  border-radius: 14px;
  background: #e6f7f5;
  color: #087f89;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.quick-access-content h4 {
  font-size: 1.05rem;
  font-weight: 800;
  color: #103447;
  margin: 0 0 3px 0;
}
.quick-access-content p {
  font-size: 0.8rem;
  color: #64748b;
  margin: 0;
  line-height: 1.4;
}
.quick-access-arrow {
  margin-left: auto;
  color: #94a3b8;
  font-weight: 800;
  font-size: 1.2rem;
  transition: transform 0.2s;
}
.quick-access-card:hover .quick-access-arrow {
  color: #087f89;
  transform: translateX(3px);
}

/* LAYANAN UTAMA CARDS */
.service-card--mockup {
  background: #ffffff;
  border: 1px solid #dce8eb;
  border-radius: 20px;
  padding: 1.75rem;
  display: flex;
  flex-direction: column;
  transition: all 0.25s ease;
  box-shadow: 0 4px 16px rgba(16, 52, 71, 0.04);
}
.service-card--mockup:hover {
  transform: translateY(-5px);
  box-shadow: 0 16px 36px rgba(8, 127, 137, 0.12);
  border-color: #087f89;
}
.service-badge-mockup {
  font-size: 0.72rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #087f89;
  margin-bottom: 0.6rem;
}
.service-card--mockup h3 {
  font-size: 1.2rem;
  font-weight: 800;
  color: #103447;
  line-height: 1.35;
  margin: 0 0 0.5rem 0;
}
.service-card--mockup h3 a {
  color: inherit;
  text-decoration: none;
  transition: color 0.2s;
}
.service-card--mockup h3 a:hover {
  color: #087f89;
}
.service-card--mockup p {
  font-size: 0.88rem;
  color: #64748b;
  line-height: 1.6;
  margin-bottom: 1rem;
}
.service-pill-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 1.25rem;
}
.pill-free {
  background: #ecfdf5;
  color: #047857;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.25rem 0.65rem;
  border-radius: 9999px;
  border: 1px solid #bbf7d0;
}
.pill-verify {
  background: #fffbeb;
  color: #b45309;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.25rem 0.65rem;
  border-radius: 9999px;
  border: 1px solid #fef3c7;
}

/* ALERT BANNER DINKES */
.alert-mockup-card {
  background: linear-gradient(135deg, #087f89 0%, #103447 100%) !important;
  box-shadow: 0 12px 30px rgba(8, 127, 137, 0.25) !important;
  border-radius: 20px;
  padding: 1.75rem 2.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 2rem;
  color: #ffffff;
}
.alert-mockup-btn {
  background: #ffffff !important;
  color: #087f89 !important;
}
.alert-mockup-btn:hover {
  background: #e6f7f5 !important;
  color: #05646c !important;
  transform: translateY(-2px);
}

/* BERITA & DOKUMEN */
.news-item-mockup:hover {
  border-color: #087f89 !important;
  box-shadow: 0 8px 24px rgba(8, 127, 137, 0.1) !important;
}
.news-item-mockup-title a:hover {
  color: #087f89 !important;
}
.doc-card-mockup:hover {
  border-color: #087f89 !important;
  box-shadow: 0 6px 16px rgba(8, 127, 137, 0.1) !important;
}

/* PILAR KESEHATAN (PSKS-STYLE) */
.psks-section::before {
  background: linear-gradient(90deg, transparent, rgba(8, 127, 137, 0.4), transparent) !important;
}
.psks-badge-pill {
  background: #e6f7f5 !important;
  color: #087f89 !important;
  border-color: #bbf7d0 !important;
}
.psks-badge-dot {
  background: #087f89 !important;
}

/* FOOTER DINKES */
.site-footer {
  background: #0d2837 !important;
  color: #cbd5e1 !important;
}
.footer-accent {
  height: 5px;
  background: #d97706; /* Garis emas */
}
.footer-badge {
  border-left-color: #0aa398 !important;
}
.footer-hours-box {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 12px;
  padding: 12px 14px;
  margin-top: 10px;
}
.footer-hours-box strong {
  color: #5eead4;
  font-size: 0.8rem;
  text-transform: uppercase;
  display: block;
}
.footer-hours-box span {
  color: #ffffff;
  font-size: 0.95rem;
  font-weight: 800;
}

/* MOBILE DOCK */
.mobile-dock {
  background: #0d2837 !important;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
.dock-emphasis span {
  background: #087f89 !important;
  color: #ffffff !important;
}
"""

with open('public/assets/dinsos_theme.css', 'w', encoding='utf-8') as f:
    f.write(new_css + '\n\n' + dinkes_overrides)

print("Berhasil menghasilkan public/assets/dinsos_theme.css!")

