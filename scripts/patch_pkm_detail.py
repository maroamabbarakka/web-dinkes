# -*- coding: utf-8 -*-
with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

target = """<section class="content"><div class="container twocol"><div class="stack"><div class="panel"><div class="columns2"><div><span class="tag">Fasilitas kesehatan primer</span><h2>Puskesmas Malimpung</h2><p>Halaman profil fasilitas akan memuat informasi resmi Puskesmas, wilayah layanan, jadwal operasional, layanan unggulan, dan kanal komunikasi setelah dikonfirmasi.</p><div class="btnrow">${button('layanan','Layanan kesehatan','secondary')}</div></div><div class="cover-photo" style="height:220px">${ic('hospital')}<p>Tempat foto bangunan Puskesmas yang sebenarnya</p></div></div></div>"""

replacement = """<section class="content"><div class="container twocol"><div class="stack"><div class="panel"><div class="columns2"><div><div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;"><div style="width:52px;height:52px;background:#f0fdf4;border-radius:12px;padding:6px;display:grid;place-items:center;border:1px solid #bbf7d0;"><img src="assets/puskesmas.png" alt="Logo Puskesmas" style="width:100%;height:100%;object-fit:contain;"></div><div><span class="tag" style="background:#078d90;color:#fff;">Kecamatan ${pkmItem[1]}</span><h2 style="margin:4px 0 0;font-size:24px;">Puskesmas ${pkmItem[0]}</h2></div></div><p>Fasilitas Pelayanan Kesehatan Tingkat Pertama (FKTP) resmi di bawah pembinaan Dinas Kesehatan Kabupaten Pinrang. Menyelenggarakan pelayanan promotif, preventif, kuratif, dan rehabilitatif.</p><div style="background:#f8fafc;padding:12px 16px;border-radius:8px;font-size:13.5px;margin:14px 0;"><p style="margin:0 0 6px;"><strong>Kepala UPTD:</strong> ${pkmItem[2]}</p><p style="margin:0 0 6px;"><strong>Alamat:</strong> ${pkmItem[5]}</p><p style="margin:0;"><strong>Inovasi Unggulan:</strong> ${pkmItem[3] || 'Pelayanan Primer Terpadu'}</p>${pkmItem[4] ? `<p style="margin:6px 0 0;color:#b45309;">🏆 <strong>Penghargaan:</strong> ${pkmItem[4]}</p>` : ''}</div><div class="btnrow">${button('puskesmas','Lihat 19 Puskesmas Lainnya','secondary')}</div></div><div class="cover-photo" style="height:260px;background:#ffffff;border:1px solid #e2e8f0;display:grid;place-items:center;padding:20px;"><img src="assets/puskesmas.png" alt="Logo Puskesmas Resmi" style="width:110px;height:110px;object-fit:contain;"><p style="margin-top:10px;font-weight:600;color:#078d90;font-size:13px;">Lambang Fasilitas Pelayanan Kesehatan Primer</p></div></div></div>"""

if target in text:
    text = text.replace(target, replacement)
    with open('public/assets/app.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Patch puskesmasDetailPage berhasil!")
else:
    print("Target tidak ditemukan di app.js.")

