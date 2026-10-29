// Script seeding data ke Firestore menggunakan Firebase JS SDK
import { initializeApp } from "firebase/app";
import { getFirestore, doc, setDoc } from "firebase/firestore";
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.dirname(__dirname);

const firebaseConfig = {
  apiKey: "AIzaSyDK7sOlRHmc8WyJZsxQP032NYHtG9vcn-U",
  authDomain: "dinkes-pinrang.firebaseapp.com",
  projectId: "dinkes-pinrang",
  storageBucket: "dinkes-pinrang.firebasestorage.app",
  messagingSenderId: "281517642678",
  appId: "1:281517642678:web:a8b20c74bc8302fba5e717"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

async function seedData() {
  console.log("=== Memulai Sinkronisasi Data ke Cloud Firestore ===");

  // 1. Puskesmas
  const pkmData = JSON.parse(fs.readFileSync(path.join(ROOT, "public", "data", "puskesmas.json"), "utf8"));
  console.log(`Mengunggah ${pkmData.length} Puskesmas...`);
  for (const p of pkmData) {
    try {
      await setDoc(doc(db, "puskesmas", p.id), p);
      console.log(`  [Puskesmas] OK: ${p.name}`);
    } catch (err) {
      console.error(`  [Puskesmas] Error: ${p.name}`, err.message);
    }
  }

  // 2. Halaman
  const pagesData = JSON.parse(fs.readFileSync(path.join(ROOT, "public", "data", "pages.json"), "utf8"));
  console.log(`Mengunggah ${pagesData.length} Halaman Lembaga...`);
  for (const pg of pagesData) {
    try {
      await setDoc(doc(db, "pages", pg.slug), pg);
      console.log(`  [Halaman] OK: ${pg.title}`);
    } catch (err) {
      console.error(`  [Halaman] Error: ${pg.title}`, err.message);
    }
  }

  // 3. Stats
  const statsData = JSON.parse(fs.readFileSync(path.join(ROOT, "public", "data", "stats.json"), "utf8"));
  try {
    await setDoc(doc(db, "stats", "summary"), statsData);
    console.log("  [Stats] OK: Indikator ringkasan berhasil diunggah.");
  } catch (err) {
    console.error("  [Stats] Error:", err.message);
  }

  // 4. Artikel (Batch sample awal)
  const articlesData = JSON.parse(fs.readFileSync(path.join(ROOT, "public", "data", "articles.json"), "utf8"));
  console.log(`Mengunggah 20 artikel teratas (sample)...`);
  for (const art of articlesData.slice(0, 20)) {
    try {
      await setDoc(doc(db, "articles", String(art.id)), art);
      console.log(`  [Artikel] OK: ${art.title.slice(0, 40)}...`);
    } catch (err) {
      console.error(`  [Artikel] Error: ${art.id}`, err.message);
    }
  }

  console.log("=== Sinkronisasi Firestore Selesai! ===");
}

seedData().catch(console.error);

