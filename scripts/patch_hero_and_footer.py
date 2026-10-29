import re, json

with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Pastikan SVG memiliki arrowUp
if 'arrowUp:' not in code:
    code = code.replace("arrow:'<path d=\"M5 12h14M12 5l7 7-7 7\"/>',", "arrow:'<path d=\"M5 12h14M12 5l7 7-7 7\"/>',arrowUp:'<path d=\"M12 19V5M5 12l7-7 7 7\"/>',")
    print("SVG arrowUp ditambahkan.")

# 2. Perbaiki homePage() bagian HERO STAGE V4
old_hero_pattern = r'<!-- HERO STAGE V4 -->.*?<!-- EXECUTIVE GREETING CARD'
new_hero_html = """<!-- HERO STAGE V4 -->
  <section class="v4-mainstage">
    <div class="container v4-stage-grid">
      <div class="v4-feature-rail" style="background: linear-gradient(120deg, rgba(16, 43, 86, 0.94) 5%, rgba(19, 92, 177, 0.88) 58%, rgba(23, 142, 236, 0.82) 100%), url('assets/kantor_dinkes_pinrang.jpg') center/cover no-repeat;box-shadow: 0 16px 36px rgba(16, 43, 86, 0.22);">
        <div class="v4-feature-slide is-active">
          <div class="v4-feature-inner" style="position:relative;z-index:2;padding:48px 44px;display:flex;flex-direction:column;justify-content:center;height:100%;">
            <div class="v4-feature-deco" aria-hidden="true" style="opacity:0.25;">
              <span class="v4-cross">+</span><span class="v4-circle"></span><span class="v4-checkpulse">${ic('activity')}</span>
            </div>
            
            <div style="margin-bottom:16px;">
              <span style="background:rgba(255,255,255,0.18);color:#ffffff;border:1px solid rgba(255,255,255,0.28);padding:6px 14px;border-radius:30px;font-size:11px;font-weight:800;letter-spacing:0.08em;backdrop-filter:blur(6px);display:inline-flex;align-items:center;gap:6px;">
                ${ic('shield')} PORTAL RESMI DINAS KESEHATAN KABUPATEN PINRANG
              </span>
            </div>

            <h1 style="font-size:clamp(26px, 3.2vw, 40px);font-weight:900;line-height:1.2;margin:0 0 16px 0;letter-spacing:-0.03em;color:#ffffff;text-shadow:0 2px 10px rgba(0,0,0,0.2);">
              Transformasi Layanan Primer Menuju <em style="font-style:normal;background:linear-gradient(90deg,#5eead4,#a7f3d0);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Pinrang Sehat & Mandiri</em>
            </h1>
            <p style="font-size:clamp(14px, 1.2vw, 15.5px);line-height:1.65;color:#f0f9ff;max-width:550px;margin:0 0 24px 0;text-shadow:0 1px 4px rgba(0,0,0,0.2);">
              Pemerintah Kabupaten Pinrang menghadirkan pelayanan kesehatan yang berkualitas, terjangkau, dan mudah diakses melalui integrasi 19 UPTD Puskesmas, jaringan Posyandu di 12 kecamatan, serta sistem rujukan gawat darurat 24 Jam.
            </p>

            <!-- Stat Badges Berbasis Fakta -->
            <div style="display:flex;flex-wrap:wrap;gap:10px;margin-bottom:26px;">
              <span style="background:rgba(255,255,255,0.16);color:#ffffff;padding:6px 12px;border-radius:8px;font-size:12px;font-weight:700;display:inline-flex;align-items:center;gap:6px;border:1px solid rgba(255,255,255,0.2);">
                ${ic('hospital')} 19 Puskesmas Terakreditasi
              </span>
              <span style="background:rgba(255,255,255,0.16);color:#ffffff;padding:6px 12px;border-radius:8px;font-size:12px;font-weight:700;display:inline-flex;align-items:center;gap:6px;border:1px solid rgba(255,255,255,0.2);">
                ${ic('activity')} IGD & Bersalin 24 Jam
              </span>
              <span style="background:rgba(255,255,255,0.16);color:#ffffff;padding:6px 12px;border-radius:8px;font-size:12px;font-weight:700;display:inline-flex;align-items:center;gap:6px;border:1px solid rgba(255,255,255,0.2);">
                ${ic('check')} 100% ODF Se-Kabupaten
              </span>
            </div>

            <div class="v4-stage-actions" style="display:flex;gap:12px;flex-wrap:wrap;">
              <a href="layanan.html" class="btn primary" style="background:#02a7b0;border-color:#02a7b0;box-shadow:0 8px 20px rgba(2,167,176,0.35);font-weight:700;padding:10px 20px;">
                ${ic('heart')} Akses Layanan Publik
              </a>
              <a href="puskesmas.html" class="btn secondary" style="background:rgba(255,255,255,0.18);border:1px solid rgba(255,255,255,0.35);color:#fff;backdrop-filter:blur(6px);font-weight:700;padding:10px 20px;">
                ${ic('hospital')} Cari 19 Puskesmas
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- SISI KANAN SPOTLIGHT V4 DENGAN STYLING MODERN (TIDAK FLAT) -->
      <div class="v4-stage-side" style="display:grid;grid-template-rows:1fr 1fr;gap:18px;">
        <a class="v4-spotlight v4-spotlight-cyan" href="layanan-detail.html" style="text-decoration:none;cursor:pointer;">
          <span class="v4-spot-top">
            <span>PROGRAM UNGGULAN DAERAH</span>
            ${ic('arrow')}
          </span>
          <div class="v4-spot-icon">${ic('heart')}</div>
          <h2>Cek Kesehatan Gratis</h2>
          <p>Skrining riwayat kesehatan berkala di 19 UPTD Puskesmas se-Kabupaten Pinrang tanpa dipungut biaya.</p>
        </a>

        <a class="v4-spotlight v4-spotlight-violet" href="profil.html" style="text-decoration:none;cursor:pointer;">
          <span class="v4-spot-top">
            <span>KEPEMIMPINAN & VISI</span>
            ${ic('arrow')}
          </span>
          <div class="v4-spot-icon">${ic('shield')}</div>
          <h2>Profil Pimpinan & Visi Misi</h2>
          <p>Mengenal komitmen dr. H. Ramli Yunus, M.Kes dan arah kebijakan strategis pembangunan kesehatan daerah.</p>
        </a>
      </div>
    </div>
  </section>

  <!-- EXECUTIVE GREETING CARD"""

code = re.sub(old_hero_pattern, new_hero_html, code, flags=re.DOTALL)
print("Hero Stage berhasil diperbarui dengan v4-stage-side spotlight.")

# 3. Perbaiki footer: tambahkan kredit pengembang dan tombol Back to Top
old_footer_copy = r'© 2026 Dinas Kesehatan Pemerintah Kabupaten Pinrang\. Seluruh hak cipta dilindungi undang-undang\.'
new_footer_copy = """© 2026 Dinas Kesehatan Pemerintah Kabupaten Pinrang. Seluruh hak cipta dilindungi undang-undang.
      <div style="margin-top:8px;font-size:12.5px;color:#94a3b8;">
        Made with <span style="color:#ef4444;" aria-label="cinta">♥</span> by <a href="https://maroamedia.web.app/" target="_blank" rel="noopener" style="font-weight:700;color:#18c7ba;text-decoration:none;border-bottom:1px dashed #18c7ba;">MAROA Project</a>
      </div>"""

if 'MAROA Project' not in code:
    code = re.sub(old_footer_copy, new_footer_copy, code)
    print("Kredit MAROA Project berhasil disematkan di footer.")

with open('public/assets/app.js', 'w', encoding='utf-8') as f:
    f.write(code)
print("Berhasil menyimpan modifikasi awal app.js")
