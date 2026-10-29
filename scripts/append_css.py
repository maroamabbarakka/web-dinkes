css_addition = """
/* ==========================================================================
   ENHANCED EXECUTIVE & CONTENT STYLING (UPGRADE V4 DEFINITIVE)
   ========================================================================== */

/* Executive Leadership Card */
.v4-exec-card {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 32px;
  background: linear-gradient(135deg, #ffffff 0%, #f0fdf9 100%);
  border: 1px solid #ccebe6;
  border-radius: 20px;
  padding: 32px;
  box-shadow: 0 16px 40px rgba(8, 127, 137, 0.08);
  margin-bottom: 32px;
  align-items: center;
}
@media (max-width: 860px) {
  .v4-exec-card {
    grid-template-columns: 1fr;
    text-align: center;
    gap: 20px;
    padding: 24px;
  }
}
.v4-exec-photo-wrap {
  position: relative;
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 12px 28px rgba(16, 52, 71, 0.15);
  border: 4px solid #ffffff;
  background: #e2f4f2;
}
.v4-exec-photo {
  width: 100%;
  height: 340px;
  object-fit: cover;
  object-position: top center;
  display: block;
  transition: transform 0.4s ease;
}
.v4-exec-card:hover .v4-exec-photo {
  transform: scale(1.03);
}
.v4-exec-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  background: #087f89;
  color: #ffffff;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  border-radius: 999px;
  margin-bottom: 12px;
}
.v4-exec-title {
  font-size: 26px;
  font-weight: 800;
  color: #103447;
  line-height: 1.25;
  margin-bottom: 4px;
}
.v4-exec-sub {
  font-size: 15px;
  font-weight: 600;
  color: #087f89;
  margin-bottom: 16px;
}
.v4-exec-quote {
  font-size: 15.5px;
  line-height: 1.8;
  color: #334155;
  background: #ffffff;
  border-left: 4px solid #087f89;
  padding: 16px 20px;
  border-radius: 0 12px 12px 0;
  box-shadow: 0 4px 12px rgba(0,0,0,0.03);
  margin-bottom: 20px;
  font-style: italic;
}
.v4-exec-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

/* Bagan Struktur Organisasi */
.v4-structure-container {
  background: #ffffff;
  border: 1px solid #dce8eb;
  border-radius: 20px;
  padding: 24px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.04);
  margin-bottom: 28px;
}
.v4-structure-img {
  width: 100%;
  height: auto;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  display: block;
}

/* 19 Puskesmas Grid & Cards */
.v4-pkm-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 24px;
  margin-top: 24px;
}
.v4-pkm-card {
  background: #ffffff;
  border: 1px solid #dce8eb;
  border-radius: 18px;
  padding: 24px;
  box-shadow: 0 8px 24px rgba(16, 52, 71, 0.05);
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}
.v4-pkm-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 36px rgba(8, 127, 137, 0.12);
  border-color: #0aa398;
}
.v4-pkm-card-header {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 16px;
  border-bottom: 1px solid #edf2f3;
  padding-bottom: 14px;
}
.v4-pkm-logo {
  width: 48px;
  height: 48px;
  object-fit: contain;
  background: #f0fdf9;
  border-radius: 12px;
  padding: 6px;
  border: 1px solid #bbf7d0;
  flex-shrink: 0;
}
.v4-pkm-meta h3 {
  font-size: 17px;
  font-weight: 700;
  color: #103447;
  margin: 0;
  line-height: 1.3;
}
.v4-pkm-kec {
  font-size: 12px;
  font-weight: 600;
  color: #087f89;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.v4-pkm-head {
  font-size: 13.5px;
  color: #475569;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.v4-pkm-inovasi {
  font-size: 13px;
  color: #065f46;
  background: #ecfdf5;
  border-radius: 8px;
  padding: 10px 12px;
  margin-bottom: 16px;
  flex-grow: 1;
}
.v4-pkm-inovasi strong {
  display: block;
  font-size: 11.5px;
  text-transform: uppercase;
  color: #047857;
  margin-bottom: 4px;
}

/* Berita & Paginasi */
.v4-news-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 28px;
  margin-top: 24px;
}
.v4-news-card {
  background: #ffffff;
  border: 1px solid #dce8eb;
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(16, 52, 71, 0.05);
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
}
.v4-news-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 36px rgba(8, 127, 137, 0.12);
  border-color: #0aa398;
}
.v4-news-thumb-wrap {
  position: relative;
  width: 100%;
  padding-top: 56.25%; /* 16:9 */
  background: #e2e8f0;
  overflow: hidden;
}
.v4-news-thumb {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}
.v4-news-card:hover .v4-news-thumb {
  transform: scale(1.05);
}
.v4-news-body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}
.v4-news-tags {
  display: flex;
  gap: 8px;
  margin-bottom: 10px;
}
.v4-news-tag {
  font-size: 11px;
  font-weight: 700;
  color: #087f89;
  background: #e6f7f5;
  padding: 4px 10px;
  border-radius: 999px;
  text-transform: uppercase;
}
.v4-news-title {
  font-size: 17px;
  font-weight: 700;
  color: #103447;
  line-height: 1.4;
  margin-bottom: 10px;
}
.v4-news-excerpt {
  font-size: 13.5px;
  color: #64748b;
  line-height: 1.6;
  margin-bottom: 16px;
  flex-grow: 1;
}
.v4-news-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid #edf2f3;
  padding-top: 12px;
  font-size: 12.5px;
  color: #94a3b8;
}

/* Pagination */
.v4-pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  margin: 40px 0;
  flex-wrap: wrap;
}
.v4-page-btn {
  padding: 8px 16px;
  border: 1px solid #dce8eb;
  background: #ffffff;
  color: #103447;
  border-radius: 10px;
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s ease;
}
.v4-page-btn:hover {
  background: #e6f7f5;
  border-color: #087f89;
  color: #087f89;
}
.v4-page-btn.is-active {
  background: #087f89;
  border-color: #087f89;
  color: #ffffff;
}

/* Timeline Prestasi */
.v4-timeline {
  position: relative;
  padding-left: 28px;
  border-left: 3px solid #0aa398;
  margin: 24px 0;
}
.v4-timeline-item {
  position: relative;
  margin-bottom: 24px;
}
.v4-timeline-item::before {
  content: '';
  position: absolute;
  left: -35px;
  top: 4px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #087f89;
  border: 3px solid #ffffff;
  box-shadow: 0 0 0 2px #087f89;
}
.v4-timeline-badge {
  display: inline-block;
  font-size: 12px;
  font-weight: 700;
  color: #087f89;
  background: #e6f7f5;
  padding: 2px 10px;
  border-radius: 6px;
  margin-bottom: 6px;
}
.v4-timeline-title {
  font-size: 16px;
  font-weight: 700;
  color: #103447;
  margin-bottom: 4px;
}
.v4-timeline-desc {
  font-size: 14px;
  color: #475569;
  line-height: 1.6;
}
"""

with open('public/assets/style.css', 'r', encoding='utf-8', errors='ignore') as f:
    orig = f.read()

if 'ENHANCED EXECUTIVE & CONTENT STYLING' not in orig:
    with open('public/assets/style.css', 'a', encoding='utf-8') as f:
        f.write('\n' + css_addition)
    print('Sukses menambahkan CSS upgrade ke public/assets/style.css!')
else:
    print('CSS sudah ada di style.css.')
