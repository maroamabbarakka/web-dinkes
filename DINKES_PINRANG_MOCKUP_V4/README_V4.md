# Dinkes Pinrang — Master Mockup V4 (Komdigi-inspired)

## Tujuan
Redesain visual dari V3 (28 halaman) dengan mengadaptasi **prinsip layout** situs Komdigi: sorotan editorial utama, informasi populer, kartu layanan, komposisi asimetris, konten tematik, panel statistik, variasi warna dan ritme antarbagian. Tidak menyalin identitas, foto, atau kode resmi Komdigi.

## Cara membuka
Buka `index.html` di browser. Semua halaman memakai `assets/style.css`, `assets/v3.css`, `assets/v4.css`, dan JavaScript bersama. Tidak ada instalasi atau database untuk mockup. Gunakan tautan internal untuk menavigasi 28 halaman.

## Elemen V4
- Hero sorotan interaktif **manual** 3 topik dengan kontrol yang dapat diakses keyboard; tanpa autoplay.
- Dua kartu sorotan editorial di samping hero desktop, berpindah ke dua kolom di tablet/mobile.
- Pencarian informasi utama sebelum konten panjang.
- Bento layanan berwarna-warni; ikon besar dan komposisi tidak seragam.
- Berita lead + ringkasan sidebar (bukan tiga kartu identik).
- Program prioritas dengan kombinasi narasi dan komponen 2×2.
- Edukasi kesehatan dengan kartu utama dan 4 topik pendek.
- Panel data/transparansi berwarna navy tanpa statistik palsu.
- Galeri visual dengan grid tidak simetris.
- Variasi header tematik untuk semua 27 halaman selain beranda.
- Layout indeks berita/edukasi/layanan/galeri diperjelas dengan kartu lead.

## Batasan penting
MOCKUP DESAIN, BUKAN WEBSITE RESMI. Placeholder foto tidak mewakili dokumentasi asli. Lambang pemerintah diganti dengan placeholder berhuruf P. Metadata layanan dan kontak belum divalidasi. Konten dashboard tidak berisi angka kesehatan fiktif. Tidak ada backend, upload, pengaduan atau login; seluruh tindakan berisiko tetap mengarah ke kanal resmi atau dinonaktifkan.

## Persyaratan sebelum implementasi produksi
- Ganti foto placeholder dengan hasil migrasi foto **asli** dari `dinkes.pinrangkab.go.id` (hak guna terverifikasi); isi `alt`, kredit, metadata dan caption.
- Ganti logo dengan lambang resmi Kabupaten Pinrang; verifikasi nama pejabat, nomor, alamat, dan jadwal.
- Verifikasi tanggal/berita program dengan sumber asli; pertahankan canonical URL dan 301 redirect saat migrasi.
- Hubungkan CMS dan PPID, data agregat dan indikator yang disahkan, informasi Puskesmas yang mutakhir.
- Audit aksesibilitas WCAG 2.2 AA dan Core Web Vitals di server produksi serta uji pengguna nyata.

## Catatan referensi
- Referensi visual: https://www.komdigi.go.id/ (beranda) dan https://www.komdigi.go.id/berita
- Referensi konteks desain kesehatan: https://satusehat.kemkes.go.id/

Tanggal pemeriksaan: 29 Oktober 2026.
