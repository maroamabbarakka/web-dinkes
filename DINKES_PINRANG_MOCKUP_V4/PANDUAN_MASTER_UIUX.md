# MASTER RANCANGAN UI/UX WEBSITE DINAS KESEHATAN KABUPATEN PINRANG
**Versi:** 2.0 · **Tanggal:** 29 Oktober 2026 · **Cakupan:** 28 template halaman publik.

## A. Visi produk dan prinsip desain
**Identitas institusi:** Dinas Kesehatan Kabupaten Pinrang. "Pinrang Sehat" hanya ide nama pengalaman digital, bukan pengganti nama instansi atau identitas resmi yang telah ditetapkan.

**Tujuan:** portal informasi dan pelayanan publik yang memudahkan warga mencari fasilitas, memahami layanan, memperoleh edukasi terpercaya, mengakses informasi publik, serta berpartisipasi dalam perbaikan pelayanan. Situs tidak boleh menyamar sebagai aplikasi rekam medis.

Prinsip:
1. **Masyarakat lebih dulu.** Layanan, pencarian, Puskesmas, edukasi, dan pengaduan berada lebih menonjol daripada berita seremonial.
2. **Otoritatif tetapi ramah.** Nama instansi dan lambang resmi tetap dominan, konten ditulis ringkas dan mudah dipahami.
3. **Terpercaya.** Tampilkan sumber, tanggal terakhir ditinjau, penanggung jawab dan pembaruan; hindari data/foto yang belum tervalidasi.
4. **Inklusif.** Mobile-first, target sentuh cukup besar, kontrol keyboard, teks alternatif, kontras memadai, responsif dan bahasa jelas.
5. **Tertib kelola.** Hak akses penerbitan, persetujuan medis, alur PPID, pengaduan resmi, arsip, serta perlindungan data.
6. **Bisa tumbuh.** Konten terstruktur agar nanti dapat dipindahkan ke CMS modern tanpa mengubah design system.

## B. Rujukan regulasi dan standardisasi (bukan klaim sertifikasi)
| Kerangka | Penerapan pada website baru |
|---|---|
| Perpres 95/2018 tentang SPBE | Integrasi tata kelola, layanan elektronik, interoperabilitas dengan ekosistem kabupaten |
| Perpres 132/2022 tentang Arsitektur SPBE Nasional | Penyesuaian desain teknis dengan arsitektur SPBE pemerintah daerah |
| Perpres 82/2023 | Tidak membangun layanan kesehatan yang terisolasi dan berpotensi duplikasi layanan digital nasional |
| UU 25/2009 tentang Pelayanan Publik & PermenPANRB 15/2014 | Standar pelayanan, prosedur, persyaratan, biaya/tarif jika berlaku, waktu, produk dan pengaduan |
| UU 14/2008 & PerKI 1/2021 | Informasi publik berkala, setiap saat, serta-merta; mekanisme PPID dan daftar informasi publik |
| Perpres 39/2019 tentang Satu Data Indonesia | Metadata, definisi indikator, sumber, keterlacakan, interoperabilitas dan pemutakhiran data |
| UU 27/2022 tentang Pelindungan Data Pribadi | Minimisasi data, hak subjek data, pengaturan akses, kebijakan privasi, tata kelola foto dan formulir |
| WCAG 2.2 level AA (target kualitas) | Navigasi keyboard, kontras, teks alternatif, formulir terlabel, responsif, struktur heading |
| Core Web Vitals (target performa) | LCP ≤2,5 detik; INP ≤200 ms; CLS ≤0,1 pada persentil ke-75 pengukuran lapangan |

Rujukan: https://peraturan.go.id/ · https://jdih.menpan.go.id/ · https://eppid.komisiinformasi.go.id/ · https://www.w3.org/TR/WCAG22/ · https://web.dev/articles/vitals

## C. Struktur navigasi
- **Beranda** — pencarian dan akses cepat.
- **Layanan Kesehatan** — katalog layanan, detail standar pelayanan.
- **Direktori Puskesmas** — daftar dan profil fasilitas.
- **Edukasi Kesehatan** — topik dan artikel terverifikasi.
- **Data Kesehatan** — dashboard agregat dan metadata indikator.
- **Berita & Kegiatan** — indeks, artikel detail, galeri.
- **Transparansi** — PPID, dokumen, permohonan informasi, pengumuman penting.
- **Tentang Dinas** — profil, struktur, inovasi, kontak.
- **Bantuan & partisipasi** — pengaduan, SKM, FAQ, pencarian.
- **Kebijakan & utilitas** — privasi, aksesibilitas, peta situs, 404.

## D. Design system (dipakai bersama oleh 28 halaman)
- **Warna utama:** teal #087F89; **navy:** #103447; **mint latar:** #E7F7F4; **surface:** putih; **garis:** #DCE8EB; **accent:** emas pucat #F5B958 (hanya untuk kategori).
- **Tipografi:** keluarga sans modern dengan fallback sistem, judul tebal, paragraf tidak terlalu lebar, rata kiri; tidak menggunakan huruf dekoratif.
- **Tata letak:** kontainer hingga 1240px, grid 2-4 kolom desktop, satu kolom mobile, sidebar menjadi konten vertikal pada mobile.
- **Komponen global:** pita status mockup, topbar Pemkab, identitas instansi, navbar sticky, breadcrumb, hero dalam, heading section, tombol utama/sekunder, card, tag, panel, footer, tombol peta situs.
- **Status UI:** default, hover, focus terlihat, aktif, kosong, verifikasi diperlukan; tidak memalsukan status "terkirim" untuk formulir.
- **Gambar:** foto dokumentasi resmi dan lambang daerah harus diunggah secara autentik; `object-fit: cover` dengan kontrol crop; teks alternatif deskriptif; simpan file asli dan turunan.
- **Aksesibilitas dan responsif:** target 320px-1920px; semua interaksi penting dapat dipakai tanpa hover; fokus keyboard; `prefers-reduced-motion`; tombol/chip sentuh yang lapang.
- **Konten bilingual:** bahasa Indonesia sebagai standar, bahasa daerah dapat hadir sebagai materi edukasi tambahan, bukan mengganti informasi resmi.

## E. Detail per halaman
Di bawah ini adalah spesifikasi yang harus dijaga ketika mockup dijadikan website produksi. Konten yang ditandai verifikasi tidak boleh ditayangkan sebelum disahkan.

| No | Halaman | Tujuan pengguna | Isi utama dan komponen | CTA, interaksi dan perhatian |
|---|---|---|---|---|
| 01 | **Beranda** | Menemukan jalan tercepat ke layanan | Hero tegas, akses cepat, layanan prioritas, edukasi, berita, kanal pengaduan | Cari Puskesmas, edukasi, pengaduan; metadata pembaruan |
| 02 | **Profil Dinas** | Mengenali tugas dan kewenangan OPD | Gambaran dinas, kedudukan, tugas/fungsi, arah pelayanan, visi-misi terbaru | Tautan organisasi, dokumen hukum, kontak |
| 03 | **Struktur Organisasi** | Mengetahui unit dan penanggung jawab | Bagan adaptif, profil pejabat resmi, tugas bidang, dokumen dasar hukum | Harus cocok dengan SOTK dan penetapan terbaru; hindari nama yang kedaluwarsa |
| 04 | **Katalog Layanan** | Menemukan layanan yang diperlukan | Kartu layanan, klasifikasi, ringkasan, kanal dan persyaratan | Filter kategori, link standar pelayanan |
| 05 | **Detail Layanan** | Memahami prosedur layanan | Persyaratan, sasaran, langkah, biaya bila berlaku, waktu, produk, pengaduan, sumber | Rujukan dan tanggal verifikasi; jangan membuat janji waktu palsu |
| 06 | **Direktori Puskesmas** | Mencari fasilitas primer | Pencarian nama, filter kecamatan, kartu fasilitas, alamat | Filter langsung; nama, alamat dan kontak wajib valid |
| 07 | **Profil Puskesmas** | Mengetahui layanan spesifik faskes | Foto bangunan, alamat, peta, layanan, jam, inovasi, kontak, akreditasi jika publik | Kontak ke faskes; data unit dikelola melalui penanggung jawab |
| 08 | **Indeks Edukasi** | Membaca topik kesehatan | Kategori keluarga/gizi/PTM/PHBS, pencarian, visual edukasi resmi | Filter topik, daftar artikel |
| 09 | **Detail Edukasi** | Memahami saran kesehatan umum | Ringkasan, isi sederhana, ilustrasi, daftar sumber, reviewer medis, tanggal tinjau | Tombol cari layanan; disclaimer bukan diagnosis |
| 10 | **Arsip Berita** | Melacak publikasi OPD | Pencarian, filter kategori, tanggal, foto unggulan, pagination | SEO dan arsip, tidak menghapus artikel lama tanpa redirect |
| 11 | **Detail Berita** | Membaca berita lengkap dan foto | Judul, tanggal, penulis, isi, galeri, alt text, sumber | Berita terkait, tautan sumber, metadata foto |
| 12 | **Galeri** | Menjelajah dokumentasi kegiatan | Album, tanggal, foto asli, kategori, atribut sumber | Filter album; hindari manipulasi identitas wajah |
| 13 | **Dashboard Data** | Memahami indikator publik | Kartu indikator, grafik agregat, kategori, waktu pembaruan | Tidak menampilkan rekam medis atau data individu |
| 14 | **Detail Indikator** | Memeriksa definisi dan sumber angka | Definisi, numerator, denominator, satuan, periode, wilayah, sumber dan caveat | Unduh data hanya jika disetujui dan aman |
| 15 | **Publikasi & Dokumen** | Mengunduh dokumen resmi | Tabel dokumen, kategori, tahun, nomor, tanggal, ukuran, versi, berkas | Pencarian dan filter; PDF harus terverifikasi dan dapat diakses |
| 16 | **PPID** | Mengetahui hak dan kelas informasi | DIP, berkala, setiap saat, serta-merta, prosedur dan kanal resmi | Permohonan informasi; tautan PPID utama |
| 17 | **Permohonan Informasi** | Memahami cara mengajukan | Alur, kelengkapan, form resmi, registrasi, jalur keberatan | Mockup tidak menyimpan data; produksi membutuhkan kanal PPID sah |
| 18 | **Pengaduan** | Menyampaikan aspirasi atau keluhan | SP4N-LAPOR!, kategori pengaduan/aspirasi/info, langkah menulis laporan | Tautan ke sistem resmi; jangan memproses rahasia medis publik |
| 19 | **Kontak** | Menghubungi dinas | Alamat kantor, peta, telepon, email dinas, jam layanan | Semua kontak harus diverifikasi; link yang dapat ditekan pada mobile |
| 20 | **Inovasi** | Mempelajari praktik baik kesehatan | Kartu inovasi, pengusul, masalah, solusi, dampak, bukti, replikasi | Bukti dampak terukur dan status implementasi |
| 21 | **FAQ** | Menemukan jawaban | Akordeon tanya jawab, kategori bantuan | Keyboard dan pembaca layar; sumber dan pemilik jawaban |
| 22 | **Pencarian** | Menemukan konten lintas kategori | Pencarian global, hasil, jenis konten, fallback tidak ditemukan | Indeks server-side ketika produksi |
| 23 | **Peta Situs** | Memahami seluruh navigasi | Katalog semua route, pintasan untuk peninjauan | Tautan lengkap, audit dead-link |
| 24 | **Kebijakan Privasi** | Memahami pemrosesan data | Tujuan, jenis data, dasar, hak, kontak, retensi, pihak terkait | Kebijakan final harus ditetapkan dan mutakhir |
| 25 | **Aksesibilitas** | Mendapat dukungan akses | Fitur akses, batasan yang diketahui, feedback hambatan | Audit manual dan otomatis; jangan mengklaim AA sebelum pengujian |
| 26 | **Survei Kepuasan** | Memberi evaluasi pelayanan | Ringkasan SKM, kanal survei, penggunaan masukan | Rujuk sistem SKM resmi, jangan menyimpan duplikat tanpa dasar |
| 27 | **Pengumuman Penting** | Mendapat info penting tepat waktu | Penerbit, urgensi, wilayah, waktu, instruksi, versi revisi | Mekanisme penyetujuan cepat; jangan tampilkan alert palsu |
| 28 | **404 / Error** | Pulih dari tautan rusak | Pesan jelas, cari, beranda, rekomendasi alternatif | 301 redirect dari URL lama dan pantau tautan rusak |

## F. Pengelolaan konten dan kewenangan
1. **Admin teknis**: operasi sistem, pembaruan, backup, monitoring dan keamanan, tidak otomatis memiliki kewenangan editorial.
2. **Redaktor OPD**: menyiapkan berita/foto, metadata dan alt text; mengajukan untuk tinjau.
3. **Validator substansi medis**: meninjau materi kesehatan, tanggal masa berlaku, risiko kesalahan informasi.
4. **Pengelola PPID**: mengesahkan dokumen publik, informasi dikecualikan dan kanal permohonan.
5. **Pengelola data**: mengesahkan dataset agregat, definisi indikator dan periode.
6. **Penerbit/approver**: menerbitkan konten yang telah disetujui.
7. **PIC Puskesmas**: memperbarui alamat, kontak, layanan, jadwal, inovasi, status dan dokumentasi unitnya.

Alur minimum: draft → review substansi → review foto, identitas dan hak publikasi → persetujuan → terbit → tinjau berkala → arsip / koreksi. Semua perubahan penting masuk audit log.

## G. Strategi migrasi dari WordPress lama
**Cakupan sesuai permintaan:** artikel/berita, halaman, foto terkait. Tidak perlu mengimpor database penuh WordPress lama.
1. Ekspor artikel, metadata judul/slug/tanggal/penulis/kategori, HTML bersih dan permalink lama.
2. Ekspor halaman statis (profil, visi-misi, fungsi, struktur, daftar fasilitas, dll.) beserta hierarki dan tautan internal.
3. Simpan seluruh foto terkait (featured image + galeri + gambar isi), file asli bila dapat diakses, ukuran, checksum, alt text dan relasi ke konten.
4. Bersihkan duplikasi thumbnail, gambar rusak dan tautan eksternal mati; jangan kehilangan foto asli.
5. Petakan judul, kategori, URL lama ke CPT/taksonomi sistem baru; aktifkan `301` pada URL lama yang berubah.
6. Jalankan review redaksi, izin publikasi wajah terutama anak/pasien, dan pemeriksaan informasi sensitif di foto, dokumen dan EXIF.
7. Publikasi di staging, lakukan content diff sebelum beralih ke domain resmi.

## H. Non-fungsional dan mutu produksi
- Keamanan: HTTPS, MFA admin, least-privilege, audit log, patch cadence, rate limiting, WAF sesuai risiko, backup dan restore test.
- SEO dan metadata: canonical, metadata OG, sitemap.xml, robots.txt yang tepat, structured data yang relevan tanpa klaim palsu, redirects.
- Performa: WebP/AVIF dan `srcset`, dimensi foto eksplisit, cache, CDN jika disetujui, optimasi font, JS bertahap, lazy loading di bawah fold.
- Aksesibilitas: evaluasi keyboard, pembaca layar, zoom 200-400%, kontras, focus, alt gambar, label formulir, error handling.
- Hukum dan pengawasan: koordinasi OPD dan Diskominfo terkait domain, penanggung jawab SPBE, data pribadi, PPID dan pengaduan.
- Pengukuran: completion rate pencarian Puskesmas, keberhasilan menemukan standar layanan, kualitas metadata, zero broken links kritikal, aksesibilitas dan Core Web Vitals lapangan.

## I. Fase implementasi
1. **Persetujuan arsitektur informasi dan UI kit:** validasi oleh Dinkes, PPID, Diskominfo, PIC Puskesmas.
2. **Migrasi arsip publik:** berita, halaman, foto asli, kaitan album dan redirect URL.
3. **Konten pelayanan berkualitas:** detail standar layanan, kontak faskes, berkas publik, edukasi yang direview medis.
4. **Implementasi CMS:** tipe konten khusus Puskesmas, edukasi, berita, dokumen, indikator; workflow approval.
5. **Integrasi yang disetujui:** SKM, SP4N, peta, data agregat; tidak perlu mengkloning fitur SATUSEHAT.
6. **UAT, aksesibilitas, keamanan, performa dan peluncuran:** staging, domain resmi, penanggung jawab, monitoring.

## J. Sumber dan catatan keakuratan
- Situs lama Dinkes Pinrang: https://dinkes.pinrangkab.go.id/ (struktur navigasi, berita, publikasi, daftar UPTD).
- SATUSEHAT Kemenkes: https://satusehat.kemkes.go.id/ (inspirasi desain visual dan penyajian informasi; bukan template identitas resmi).
- JDIH KemenPANRB: https://jdih.menpan.go.id/dokumen-hukum/peraturan-menteri-pendayagunaan-aparatur-negara-dan-reformasi-birokrasi-nomor-15-tahun-2014-tentang-411
- PerKI 1/2021: https://eppid.komisiinformasi.go.id/uploads/lampiran/22797PerKINo1Tahun2021.pdf
- WCAG: https://www.w3.org/TR/WCAG22/
- Core Web Vitals: https://web.dev/articles/vitals

Catatan: standar di atas adalah landasan rancangan dan target. Kesesuaian hukum, kinerja dan aksesibilitas perlu dievaluasi pada implementasi yang benar-benar dioperasikan.
