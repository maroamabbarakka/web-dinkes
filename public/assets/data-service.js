// Data Service untuk Portal Dinkes Pinrang
// Menghubungkan Firebase Firestore dengan fallback ke arsip lokal terindeks

let cachedArticles = null;
let cachedPuskesmas = null;
let cachedPages = null;
let cachedStats = null;

// Fungsi helper untuk memperbaiki URL foto dari WordPress lama ke aset lokal
export function resolveImageUrl(url) {
  if (!url) return 'assets/puskesmas.png';
  let cleanUrl = url;
  if (cleanUrl.includes('dinkes.pinrangkab.go.id/wp-content/uploads/')) {
    cleanUrl = cleanUrl.replace('https://dinkes.pinrangkab.go.id/wp-content/uploads/', 'uploads/');
  }
  // Normalisasi dimensi thumbnail WordPress (-1024x768 dsb) ke berkas master asli
  cleanUrl = cleanUrl.replace(/-\d+x\d+(\.[a-zA-Z0-9]+)$/i, '$1');
  return cleanUrl;
}

// Mengambil seluruh artikel
export async function getArticles() {
  if (cachedArticles) return cachedArticles;
  try {
    const res = await fetch('data/articles.json');
    if (!res.ok) throw new Error('Gagal memuat articles.json');
    const data = await res.json();
    cachedArticles = data.map(item => ({
      ...item,
      featured_image: resolveImageUrl(item.featured_image),
      gallery_images: (item.gallery_images || []).map(resolveImageUrl)
    }));
    return cachedArticles;
  } catch (err) {
    console.warn('Gagal memuat artikel:', err);
    return [];
  }
}

// Mengambil artikel berdasarkan ID atau slug
export async function getArticleById(idOrSlug) {
  const articles = await getArticles();
  const cleanId = String(idOrSlug).replace(/^p-/, '');
  return articles.find(a => String(a.id) === cleanId || a.slug === idOrSlug) || null;
}

// Mengambil seluruh Puskesmas
export async function getPuskesmasList() {
  if (cachedPuskesmas) return cachedPuskesmas;
  try {
    const res = await fetch('data/puskesmas.json');
    if (!res.ok) throw new Error('Gagal memuat puskesmas.json');
    cachedPuskesmas = await res.json();
    return cachedPuskesmas;
  } catch (err) {
    console.warn('Gagal memuat Puskesmas:', err);
    return [];
  }
}

// Mengambil Puskesmas berdasarkan ID atau Slug
export async function getPuskesmasById(idOrSlug) {
  const list = await getPuskesmasList();
  return list.find(p => p.id === idOrSlug || p.slug === idOrSlug || String(p.no) === String(idOrSlug)) || null;
}

// Mengambil halaman kelembagaan
export async function getPages() {
  if (cachedPages) return cachedPages;
  try {
    const res = await fetch('data/pages.json');
    if (!res.ok) throw new Error('Gagal memuat pages.json');
    cachedPages = await res.json();
    return cachedPages;
  } catch (err) {
    return [];
  }
}

export async function getPageBySlug(slug) {
  const pages = await getPages();
  return pages.find(p => p.slug === slug) || null;
}

// Mengambil statistik
export async function getStats() {
  if (cachedStats) return cachedStats;
  try {
    const res = await fetch('data/stats.json');
    if (!res.ok) throw new Error('Gagal memuat stats.json');
    cachedStats = await res.json();
    return cachedStats;
  } catch (err) {
    return null;
  }
}

// Pencarian lintas konten
export async function searchAll(query) {
  if (!query || !query.trim()) return { articles: [], puskesmas: [] };
  const q = query.toLowerCase().trim();
  const articles = await getArticles();
  const puskesmas = await getPuskesmasList();

  const matchedArticles = articles.filter(a => 
    a.title.toLowerCase().includes(q) || 
    (a.excerpt && a.excerpt.toLowerCase().includes(q)) ||
    (a.category && a.category.toLowerCase().includes(q))
  ).slice(0, 15);

  const matchedPuskesmas = puskesmas.filter(p => 
    p.name.toLowerCase().includes(q) || 
    p.kecamatan.toLowerCase().includes(q) || 
    p.address.toLowerCase().includes(q) ||
    p.innovations.some(i => i.toLowerCase().includes(q))
  );

  return { articles: matchedArticles, puskesmas: matchedPuskesmas };
}
