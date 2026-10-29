# MASTER MOCKUP V3 — DINAS KESEHATAN KABUPATEN PINRANG

Ini adalah **mockup interaktif UI/UX**, bukan website resmi pemerintah dan belum dihubungkan ke CMS/server. Semua 28 halaman HTML dari V2 dipertahankan, kemudian diberi sistem warna dan ikon baru secara konsisten.

## Apa yang baru dari V2?

- **Biru terang** (`#1676F3`) ditambahkan sebagai aksen yang kuat pada CTA, navigasi, hero, kartu Puskesmas, dan visual layanan.
- **Teal kesehatan** (`#078D90`) tetap menjadi identitas pendamping; biru dan teal tidak menggantikan lambang resmi Kabupaten Pinrang.
- Kartu akses cepat mempunyai enam palet berbasis kegunaan: **blue** (Puskesmas), **teal** (layanan), **violet** (edukasi), **amber** (data), **cyan** (dokumen), **coral** (pengaduan).
- Ikon SVG dalam kartu akses cepat diperbesar menjadi 40px dalam wadah 74px di desktop dan 34px dalam wadah 64px di mobile 390px. Tidak memerlukan gambar raster untuk ikon.
- Teks dasar dinaikkan menjadi **16px**. Banyak teks kartu, metadata dan paragraf juga diperbesar dibanding V2.
- Halaman detail memiliki header tematik dengan ikon besar dan aksen berbeda menurut jenis halaman.
- Tombol floating demo yang sebelumnya menutupi konten **dihapus**.
- Pada mobile, gambar hero dekoratif disembunyikan agar pencarian lebih cepat ditemukan; tombol hero dibuat dua kolom.

## Buka mockup

1. Ekstrak ZIP.
2. Buka `index.html` dengan browser modern.
3. Klik menu, kategori, atau navigasi untuk menjelajahi 28 halaman.
4. Untuk uji font Google Plus Jakarta Sans, perangkat perlu terhubung internet. Jika offline, digunakan fallback font sistem. File font tidak disertakan.

## Berkas utama

- `index.html` — halaman beranda
- `*.html` — total 28 mockup halaman
- `assets/app.js` — komponen, konten demonstrasi, navigasi, filter
- `assets/style.css` — pondasi UI dari V2
- `assets/v3.css` — **override tema V3 untuk semua halaman**
- `previews/hero_desktop.png`, `previews/hero_mobile.png` — tampilan hero
- `previews/kartu_akses_cepat_desktop.png`, `previews/kartu_akses_cepat_mobile.png` — perbandingan kartu
- `previews/PREVIEW_28_HALAMAN_V3.png` — contact sheet seluruh halaman
- `PENGUJIAN_168_TAMPILAN.txt` — hasil pengujian 28 halaman × 6 ukuran layar

## Status pengujian

Seluruh 28 halaman diperiksa pada **320, 360, 390, 768, 1024, dan 1440 px (168 kondisi layout)**. Tidak ada horizontal overflow dan masing-masing mempunyai satu judul utama. Pemeriksaan halaman pada lebar 390px dan 1440px juga tidak menemukan kesalahan JavaScript dalam pengujian saat pembuatan. Navigasi mobile dapat dibuka. Pengujian di perangkat nyata, keyboard/screen reader, Core Web Vitals produksi, audit lengkap WCAG 2.2 AA, dan uji pengguna masih diperlukan.

## Batasan yang disengaja

Identitas huruf `P` adalah **placeholder** karena lambang daerah resmi belum disertakan. Foto dan ilustrasi artikel yang belum diverifikasi adalah **placeholder**, bukan dokumentasi aktual. Data fasilitas, nama pejabat, jam layanan, angka kesehatan, dan formulir tetap contoh; perlu verifikasi instansi sebelum produksi. Desain terinspirasi gaya SATUSEHAT tetapi **tidak mengklaim menyalin palet resmi atau identitas mereknya secara persis**.
