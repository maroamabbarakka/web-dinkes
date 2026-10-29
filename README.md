# Portal Resmi Dinas Kesehatan Kabupaten Pinrang

Portal web resmi Dinas Kesehatan Kabupaten Pinrang, Sulawesi Selatan. Dibangun dengan rancangan UI/UX modern berstandar pemerintah (Komdigi & SatuSehat Inspired), didukung oleh **Firebase Web Platform (Hosting, Firestore, Storage)** serta integrasi data otentik hasil migrasi WordPress.

---

## 🌟 Fitur Utama

- **Desain Komdigi-Inspired (V4 Responsif):** 28 rute halaman responsif (desktop, tablet, mobile), bento grid layanan, panel data dark-navy berakuntabilitas tinggi, dan tipografi Plus Jakarta Sans.
- **Data Asli Lengkap:**
  - **349 Artikel Berita:** Termasuk peliputan kampanye GERMAS di 12 kecamatan, SPP-IRT, posbindu, serta galeri foto kegiatan resmi.
  - **19 UPTD Puskesmas:** Direktori terpadu 19 Puskesmas se-Kabupaten Pinrang dengan inovasi daerah (seperti *SAMAWA*, *Macenning*, *Gemas*) dan riwayat penghargaan.
  - **Dokumen Kinerja & Akuntabilitas:** Visi Misi, IKU, Renja, LKjIP, Standar Pelayanan Publik, dan kanal PPID.
- **Pencarian Cepat & Filter:** Mesin pencari instan untuk artikel, layanan, dan puskesmas.
- **Aksesibilitas WCAG 2.2 AA:** Tautan loncat ke konten utama (*skip link*), pengubah ukuran teks (*Aa font resizer*), dan mode kontras warna teruji.
- **Firebase Ready:** Terhubung langsung ke Cloud Firestore, Firebase Hosting, dan Firebase Storage.

---

## 📁 Struktur Direktori

```
├── public/                       # Direktori web statis siap deploy
│   ├── index.html                # Beranda portal (Bento & Hero Komdigi style)
│   ├── berita.html               # Indeks Berita & Paginasi
│   ├── berita-detail.html        # Laman Baca Artikel & Galeri
│   ├── puskesmas.html            # Direktori 19 Puskesmas
│   ├── puskesmas-detail.html     # Profil & Inovasi Puskesmas
│   ├── layanan.html              # Standar Pelayanan & SOP
│   ├── profil.html               # Profil Lembaga & Visi Misi
│   ├── organisasi.html           # Struktur Organisasi
│   ├── ppid.html                 # Keterbukaan Informasi Publik
│   ├── data.html                 # Panel Data & Indikator
│   ├── ... (28 halaman)
│   ├── assets/                   # CSS, JS Modular, Icon, dan Logo Resmi
│   │   ├── app.js                # Core Application Logic
│   │   ├── data-service.js       # Data Fetcher (Firestore + Local JSON Fallback)
│   │   ├── firebase-config.js    # Konfigurasi Firebase Modular SDK
│   │   ├── style.css, v3.css, v4.css
│   │   └── logo_pinrang_opt.png
│   └── data/                     # Dataset JSON terstruktur
│       ├── articles.json         # 349 artikel berita asli
│       ├── puskesmas.json        # 19 UPTD Puskesmas & inovasi
│       ├── pages.json            # Halaman kelembagaan
│       └── stats.json            # Indikator kinerja
├── scripts/                      # Skrip automasi & ekstraksi
│   ├── parse_backup.py           # Ekstraksi backup WordPress ke JSON
│   └── seed_firestore.mjs        # Sinkronisasi data ke Cloud Firestore
├── firebase.json                 # Konfigurasi Firebase Hosting & Cache
├── .firebaserc                   # Konfigurasi Project ID Firebase (dinkes-pinrang)
└── package.json
```

---

## 🚀 Panduan Penggunaan Lokal

### 1. Menjalankan Web Server Lokal
Jalankan perintah berikut di terminal:
```bash
python -m http.server 8085 --directory public
```
Buka peramban di: `http://localhost:8085`

### 2. Memperbarui / Mengekstrak Data dari Backup
Jika ada arsip berita baru dari folder cadangan:
```bash
python scripts/parse_backup.py
```

### 3. Mengunggah Data ke Cloud Firestore
```bash
npm install firebase
node scripts/seed_firestore.mjs
```

### 4. Deploy ke Firebase Hosting
```bash
firebase deploy --only hosting
```

---

## 🏛️ Identitas Resmi
- **Instansi:** Dinas Kesehatan Pemerintah Kabupaten Pinrang
- **Alamat:** Jl. Jenderal Sukawati, Pinrang, Sulawesi Selatan 91212
- **Kontak Aduan:** SP4N-LAPOR! & WhatsApp Official (+62 853-4217-2724)

