# Design System V3 — Pinrang Health Portal

## Identitas
Nama resmi tetap **Dinas Kesehatan Kabupaten Pinrang**. Gaya visual: modern, human-centered, komunikatif, tegas sebagai portal pemerintah. Inspirasi: kualitas hierarki, pola pelayanan publik, dan aksen biru/teal ala SATUSEHAT. Tidak memakai logo SATUSEHAT sebagai pengganti identitas instansi.

## Warna utama

| Peran | Kode | Penggunaan |
|---|---|---|
| Biru terang | `#1676F3` | Primary CTA, kartu direktori Puskesmas, ilustrasi layanan |
| Biru gelap | `#0756C1` | Hover, emphasis, kontrol |
| Teal kesehatan | `#078D90` | Identitas sekunder, edukasi promosi kesehatan |
| Navy | `#123A5B` | Judul, struktur kelembagaan |
| Mint | `#E8F9F5` | Layanan kesehatan |
| Lavender | `#F1EDFF` | Edukasi |
| Amber | `#FFF5E2` | Data/indikator |
| Cyan | `#E7F8FF` | Arsip dokumen/PPID |
| Coral | `#FFF0ED` | Pengaduan/partisipasi |

**Aturan penting:** warna bukan satu-satunya pembeda kategori. Seluruh kartu harus tetap memiliki teks, ikon, dan label yang terbaca. Tidak menggunakan warna merah untuk informasi rutin yang dapat diartikan sebagai bahaya.

## Tipografi dan ikon

- Plus Jakarta Sans, dengan fallback ke font sistem; font dari Google Fonts bila internet tersedia.
- Teks dasar 16px. Judul halaman desktop 34–48px, mobile 28–37px.
- Ikon SVG vektor dengan stroke yang konsisten; tidak menggantikan logo pemerintah.
- Kartu akses cepat desktop: ikon 40px dalam kotak 74px. Mobile 390px: ikon 34px dalam kotak 64px.
- Kartu memakai area klik menyeluruh, hover/focus state, padding besar, dan teks terstruktur.

## Penyusunan halaman

- Beranda: orientasi warga, pencarian, enam akses cepat, layanan, edukasi, berita, bantuan.
- Layanan/Puskesmas: ikon biru, pencarian dan filter, persyaratan, kontak, standar layanan.
- Edukasi: ungu/mint, tema berdasarkan kelompok sasaran dan topik kesehatan.
- Berita/galeri: dokumentasi otentik dan metadata; placeholder sementara bukan foto palsu.
- Data/PPID: biru-cyan, metadata sumber, tanggal pembaruan, akses informasi publik.
- Pengaduan: koral terbatas pada kartu, jangan dipakai sebagai indikator kegawatdaruratan.

## Mobile

Breakpoint utama 1040, 800, 640, 380px. Pada mobile, ilustrasi hero dekoratif disembunyikan, tombol utama lebih ringkas, pencarian diprioritaskan, dan kartu akses cepat menjadi dua kolom. Tata letak dapat berubah sesuai konten tanpa menentukan tinggi tetap yang memotong teks.

## Sebelum produksi

Pasang lambang daerah resmi, foto asli dan alt text, tanggal pembaruan, data Puskesmas terverifikasi, kebijakan PPID/privasi, pengujian kontras WCAG 2.2 AA, keyboard navigation, screen reader, Core Web Vitals pada perangkat nyata, peninjauan oleh Dinkes/Diskominfo.
