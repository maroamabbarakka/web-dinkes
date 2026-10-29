import json

with open('public/data/gallery_albums.json', 'r', encoding='utf-8') as f:
    albums = json.load(f)

with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Sematkan window.GALLERY_ALBUMS di awal app.js jika belum ada
albums_json = json.dumps(albums, ensure_ascii=False)
if 'window.GALLERY_ALBUMS =' not in code:
    code = f"window.GALLERY_ALBUMS = {albums_json};\n" + code
    print("window.GALLERY_ALBUMS berhasil disematkan.")

# 2. Definisikan galeriPage() yang kaya fitur, berbasis album dan modal slide preview
new_galeri_page = """// 16. GALERI FOTO RESMI BERBASIS ALBUM & SLIDE MODAL (galeriPage)
function galeriPage() {
  const albums = window.GALLERY_ALBUMS || [];

  return pageHero('galeri', 'Dokumentasi Visual & Kegiatan', 'Galeri Dokumentasi Dinas Kesehatan', 'Koleksi album foto resmi kegiatan lapangan, pembinaan puskesmas, inovasi pelayanan, dan penganugerahan prestasi Pemerintah Kabupaten Pinrang.') + `
  <section class="content" style="padding: 30px 0 60px 0;">
    <div class="container">

      <!-- INTRO DOKUMENTASI RESMI -->
      <div style="background:linear-gradient(135deg,#f0fdf4 0%,#e6f7f5 100%);border-left:5px solid #087f89;border-radius:16px;padding:22px 26px;margin-bottom:36px;box-shadow:0 6px 20px rgba(8,127,137,0.06);">
        <h3 style="font-size:17px;font-weight:800;color:#065f46;margin:0 0 6px 0;">Dokumentasi Otentik Berbasis Fakta</h3>
        <p style="font-size:13.5px;color:#047857;line-height:1.6;margin:0;">
          Seluruh foto dokumentasi berasal dari kegiatan nyata Dinas Kesehatan Kabupaten Pinrang, jajaran 19 UPTD Puskesmas, dan kader kesehatan di 12 kecamatan. Foto disajikan dalam rasio proporsional utuh tanpa terpotong.
        </p>
      </div>

      <!-- GRID ALBUM KEGIATAN -->
      <div class="grid grid-2" style="gap:28px;">
        ${albums.map((album, aIdx) => `
          <div class="panel" style="background:#ffffff;border:1px solid #e2e8f0;border-radius:20px;overflow:hidden;box-shadow:0 8px 24px rgba(16,43,86,0.06);display:flex;flex-direction:column;">
            
            <!-- HEADER ALBUM DENGAN COVER -->
            <div style="height:260px;position:relative;background:#0f172a;overflow:hidden;">
              <img src="${album.cover}" alt="${album.title}" style="width:100%;height:100%;object-fit:cover;transition:transform .3s;" />
              <div style="position:absolute;inset:0;background:linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(15,23,42,0.85) 100%);"></div>
              
              <div style="position:absolute;top:16px;left:16px;display:flex;gap:8px;">
                <span style="background:#087f89;color:#ffffff;font-size:11.5px;font-weight:800;padding:5px 12px;border-radius:20px;box-shadow:0 2px 8px rgba(0,0,0,0.2);">
                  ${album.category}
                </span>
                <span style="background:rgba(255,255,255,0.25);backdrop-filter:blur(4px);color:#ffffff;font-size:11.5px;font-weight:700;padding:5px 12px;border-radius:20px;">
                  ${album.photos.length} Foto
                </span>
              </div>

              <div style="position:absolute;bottom:16px;left:20px;right:20px;color:#ffffff;">
                <div style="font-size:12px;color:#94a3b8;margin-bottom:4px;display:flex;align-items:center;gap:6px;">
                  ${ic('calendar')} ${album.date} · ${album.location}
                </div>
                <h3 style="font-size:18px;font-weight:800;color:#ffffff;line-height:1.3;margin:0;">${album.title}</h3>
              </div>
            </div>

            <!-- DESKRIPSI & THUMBNAILS FOTO -->
            <div style="padding:22px;display:flex;flex-direction:column;flex-grow:1;">
              <p style="font-size:13.5px;color:#64748b;line-height:1.6;margin-bottom:18px;">
                ${album.description}
              </p>

              <!-- MINI THUMBNAILS DALAM ALBUM -->
              <div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(75px, 1fr));gap:8px;margin-bottom:20px;">
                ${album.photos.map((p, pIdx) => `
                  <div style="height:70px;border-radius:8px;overflow:hidden;border:1px solid #cbd5e1;cursor:pointer;position:relative;" 
                       onclick="window.openAlbumModal(${aIdx}, ${pIdx})">
                    <img src="${p.url}" alt="${p.caption}" style="width:100%;height:100%;object-fit:cover;" />
                  </div>
                `).join('')}
              </div>

              <button type="button" class="btn primary" style="font-size:13px;padding:10px 18px;justify-content:center;font-weight:700;margin-top:auto;"
                      onclick="window.openAlbumModal(${aIdx}, 0)">
                ${ic('camera')} Buka Slide Album Foto (${album.photos.length} Gambar)
              </button>
            </div>
          </div>
        `).join('')}
      </div>

    </div>
  </section>

  <!-- MODAL CAROUSEL / LIGHTBOX SLIDE VIEW -->
  <div id="galleryModal" style="display:none;position:fixed;inset:0;background:rgba(15,23,42,0.92);backdrop-filter:blur(8px);z-index:99999;align-items:center;justify-content:center;padding:20px;">
    <div style="background:#0f172a;border:1px solid #334155;border-radius:20px;max-width:960px;width:100%;max-height:92vh;display:flex;flex-direction:column;overflow:hidden;box-shadow:0 25px 60px rgba(0,0,0,0.6);position:relative;">
      
      <!-- MODAL TOP BAR -->
      <div style="padding:16px 24px;border-bottom:1px solid #1e293b;display:flex;align-items:center;justify-content:space-between;color:#ffffff;">
        <div>
          <span id="modalAlbumCat" style="font-size:11px;font-weight:800;color:#2dd4bf;text-transform:uppercase;letter-spacing:0.05em;"></span>
          <h4 id="modalAlbumTitle" style="font-size:16px;font-weight:800;margin:2px 0 0 0;color:#ffffff;"></h4>
        </div>
        <div style="display:flex;align-items:center;gap:12px;">
          <span id="modalCounter" style="font-size:13px;color:#94a3b8;font-weight:600;"></span>
          <button type="button" onclick="window.closeAlbumModal()" style="background:#1e293b;color:#ffffff;border:none;width:36px;height:36px;border-radius:50%;cursor:pointer;display:flex;align-items:center;justify-content:center;">
            ✕
          </button>
        </div>
      </div>

      <!-- MODAL SLIDE STAGE -->
      <div style="position:relative;flex-grow:1;display:flex;align-items:center;justify-content:center;padding:24px;background:#020617;min-height:360px;">
        <button type="button" onclick="window.prevAlbumSlide()" style="position:absolute;left:16px;top:50%;transform:translateY(-50%);background:rgba(255,255,255,0.18);backdrop-filter:blur(4px);color:#ffffff;border:none;width:44px;height:44px;border-radius:50%;cursor:pointer;font-size:18px;display:flex;align-items:center;justify-content:center;z-index:10;">
          ◀
        </button>

        <img id="modalSlideImg" src="" alt="" style="max-height:55vh;max-width:100%;object-fit:contain;border-radius:10px;box-shadow:0 10px 30px rgba(0,0,0,0.5);" />

        <button type="button" onclick="window.nextAlbumSlide()" style="position:absolute;right:16px;top:50%;transform:translateY(-50%);background:rgba(255,255,255,0.18);backdrop-filter:blur(4px);color:#ffffff;border:none;width:44px;height:44px;border-radius:50%;cursor:pointer;font-size:18px;display:flex;align-items:center;justify-content:center;z-index:10;">
          ▶
        </button>
      </div>

      <!-- MODAL CAPTION BAR -->
      <div style="padding:18px 24px;border-top:1px solid #1e293b;background:#0f172a;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px;">
        <p id="modalSlideCaption" style="font-size:13.5px;color:#e2e8f0;line-height:1.5;margin:0;max-width:700px;"></p>
        <a id="modalFullBtn" href="" target="_blank" class="btn secondary" style="font-size:12px;padding:6px 14px;background:#1e293b;border-color:#334155;color:#ffffff;">
          ${ic('external')} Buka Ukuran Penuh
        </a>
      </div>

    </div>
  </div>`;
}
"""

old_galeri_pos = code.find('function galeriPage()')
if old_galeri_pos != -1:
    next_func_pos = code.find('// 17. PPID', old_galeri_pos)
    if next_func_pos == -1:
        next_func_pos = code.find('function ppidPage()', old_galeri_pos)
    
    code = code[:old_galeri_pos] + new_galeri_page + "\n" + code[next_func_pos:]
    print("galeriPage() berhasil diperbarui!")
else:
    print("galeriPage() tidak ditemukan!")

with open('public/assets/app.js', 'w', encoding='utf-8') as f:
    f.write(code)
