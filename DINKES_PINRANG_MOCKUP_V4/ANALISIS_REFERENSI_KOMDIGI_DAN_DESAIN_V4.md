# Analisis komposisi portal Komdigi dan penerapan V4 Dinkes Pinrang
Tanggal: 29 Oktober 2026

## Ruang lingkup
Sumber referensi publik diperiksa dari https://www.komdigi.go.id/, https://www.komdigi.go.id/berita dan https://www.komdigi.go.id/transformasi-digital. Pemeriksaan sumber menggunakan konten halaman publik. Ini **bukan** audit kode, aksesibilitas atau metrik performa situs Komdigi dan bukan duplikasi desain pixel-perfect.

## A. Pola UI/UX yang menonjol dari Komdigi
1. **Sorotan utama berformat carousel:** konten penting mendapat ruang dominan dengan beberapa sorotan yang dapat dipilih.
2. **Berita populer bersisian dengan sorotan:** selain headline utama, pengunjung melihat informasi alternatif tanpa harus melakukan banyak scroll.
3. **Klasifikasi layanan:** akses layanan dikelompokkan menurut kebutuhan pengguna, bukan semata-mata struktur organisasi.
4. **Narasi program + ilustrasi + subprogram:** halaman tidak monoton karena blok program menggunakan hierarki berbeda.
5. **Capaian dan indikator:** data dimunculkan sebagai narasi capaian; untuk Dinkes angka harus terverifikasi dengan metadata sumber/periode.
6. **Berita bertopik, media dan galeri:** memadukan kartu besar, kartu kecil, daftar, serta eksplorasi kategori.
7. **Pola ritme halaman:** pergantian latar terang, blok berwarna, ruang kosong yang terkontrol, dan panel kontras.

## B. Yang diadaptasi untuk Dinkes Pinrang
| Pola referensi | Adaptasi V4 | Fungsi pengguna |
|---|---|---|
| Headline/carousel | Hero 3 sorotan, penggantian manual, tanpa autoplay | Layanan, edukasi, PPID |
| Popular/side stories | Dua kartu tematik di sisi hero | CKG, berita daerah |
| Klasifikasi layanan | Bento berwarna dengan ikon besar | Puskesmas, layanan, edukasi, data, dokumen, pengaduan |
| Topical content | Berita unggulan besar + 3 berita pendukung | Percepat pemindaian berita |
| Program pillars | Narasi besar + 4 kartu program | Ibu-anak, skrining, pencegahan, layanan primer |
| Topical learning | Kartu unggulan edukasi + 4 topik | Jalur edukasi berdasarkan kebutuhan |
| Performance/data section | Panel kontras navy, 3 jalur informasi | Data agregat, dokumen kinerja, PPID |
| Media/gallery | Galeri bervariasi (mosaik) | Foto kegiatan asli setelah migrasi |

## C. Hierarki & desain visual
- Warna utama: biru terang #1976F3, teal #06A89D, navy #123955; warna sekunder untuk kategori.
- Tipografi: Plus Jakarta Sans dengan fallback system-ui, teks isi utama ±15–16 px, judul skala responsif.
- Grid: 2 kolom asimetris untuk hero; 3 kolom area layanan; bento berita; 2×2 program dan edukasi; 3 kolom data.
- Efek: gradien transparan, bentuk geometris, border lembut, elevated shadow, hover lift ringan, visual SVG, bukan animasi berat.
- Pencarian ditempatkan setelah hero, sebelum penjelajahan konten lebih panjang.
- Akses keyboard dan preferensi reduced-motion dipertahankan.
- Tidak menggunakan foto kegiatan hasil fabrikasi atau angka statistik kesehatan fiktif. Area media ditandai placeholder untuk arsip foto asli.

## D. Rincian adaptasi menurut halaman
- Beranda: komposisi editorial berlapis, 8 blok dengan ritme kontras.
- Berita: lead card melebar 2 kolom dan grid pendukung.
- Edukasi: lead content melebar, warna keluarga edukasi dominan lilac.
- Layanan: kartu layanan pertama mendapat ruang dua kali kartu biasa.
- Galeri: item utama memimpin grid, siap diganti foto riil.
- Data/indikator dan publikasi/PPID: header keluarga data biru, panel konten dominan putih untuk keterbacaan dan verifikasi data.
- Puskesmas: direktori/filter tetap fungsional; tidak dikorbankan demi dekorasi.
- Profil, organisasi, inovasi: tema lembaga dengan identitas konsisten.
- Kontak, pengaduan, formulir PPID: efek visual dibatasi, aksi prioritas jelas dan tanpa pengumpulan data pribadi melalui mockup.

## E. Rekomendasi lanjutan sebelum produksi
1. Masukkan lambang resmi dan identitas kelembagaan yang disahkan.
2. Migrasikan foto dan berita **asli**, termasuk alt text, tanggal, kredit, galeri, dan URL asal.
3. Verifikasi data 19 Puskesmas (jumlah, alamat, jam, kontak, layanan)—mockup tidak menjadikan data lama sebagai data terkini.
4. Uji performa aktual di jaringan mobile, audit WCAG 2.2 AA dan akses keyboard/screen reader.
5. Integrasi formulir hanya melalui layanan resmi yang memiliki kebijakan perlindungan data; jangan tampilkan formulir simulasi sebagai sistem aktif.
6. Lakukan pengujian tugas nyata (cari Puskesmas, cari informasi CKG, cari dokumen, buka pengaduan) dengan warga berbeda usia.

## F. Hasil uji teknis mockup
Diuji dengan headless Chromium di lebar beranda **320, 360, 390, 768, 1024, 1440, 1920 px**. Seluruh **28 halaman** diuji di lebar **390 dan 1440 px**. Tidak ditemukan overflow horizontal atau error JavaScript dalam uji ini. Kontrol carousel dan tombol navigasi mobile juga lulus uji dasar. Ini **belum** uji server produksi, kualitas konten, kompatibilitas semua perangkat, atau sertifikasi aksesibilitas.

Dokumen dibuat untuk evaluasi internal desain dan bukan penilaian resmi atas kualitas situs rujukan.
