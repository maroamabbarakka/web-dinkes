with open('public/assets/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

interactive_code = """
// INTERAKTIVITAS MODAL GALERI & BACK TO TOP
window.currentAlbumIdx = 0;
window.currentSlideIdx = 0;

window.openAlbumModal = function(aIdx, pIdx) {
  window.currentAlbumIdx = aIdx;
  window.currentSlideIdx = pIdx;
  const albums = window.GALLERY_ALBUMS || [];
  const album = albums[aIdx];
  if (!album) return;

  const modal = document.getElementById('galleryModal');
  if (!modal) return;

  document.getElementById('modalAlbumCat').textContent = album.category;
  document.getElementById('modalAlbumTitle').textContent = album.title;
  window.updateModalSlide();
  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
};

window.closeAlbumModal = function() {
  const modal = document.getElementById('galleryModal');
  if (modal) modal.style.display = 'none';
  document.body.style.overflow = '';
};

window.updateModalSlide = function() {
  const albums = window.GALLERY_ALBUMS || [];
  const album = albums[window.currentAlbumIdx];
  if (!album) return;

  const photo = album.photos[window.currentSlideIdx];
  if (!photo) return;

  document.getElementById('modalCounter').textContent = `${window.currentSlideIdx + 1} / ${album.photos.length}`;
  const imgEl = document.getElementById('modalSlideImg');
  imgEl.src = photo.url;
  imgEl.alt = photo.caption;
  document.getElementById('modalSlideCaption').textContent = photo.caption;
  document.getElementById('modalFullBtn').href = photo.url;
};

window.nextAlbumSlide = function() {
  const albums = window.GALLERY_ALBUMS || [];
  const album = albums[window.currentAlbumIdx];
  if (!album) return;
  window.currentSlideIdx = (window.currentSlideIdx + 1) % album.photos.length;
  window.updateModalSlide();
};

window.prevAlbumSlide = function() {
  const albums = window.GALLERY_ALBUMS || [];
  const album = albums[window.currentAlbumIdx];
  if (!album) return;
  window.currentSlideIdx = (window.currentSlideIdx - 1 + album.photos.length) % album.photos.length;
  window.updateModalSlide();
};

// Pasang keyboard listener untuk galeri modal
document.addEventListener('keydown', (e) => {
  const modal = document.getElementById('galleryModal');
  if (modal && modal.style.display === 'flex') {
    if (e.key === 'Escape') window.closeAlbumModal();
    if (e.key === 'ArrowRight') window.nextAlbumSlide();
    if (e.key === 'ArrowLeft') window.prevAlbumSlide();
  }
});

function initBackToTop() {
  if (document.getElementById('backToTopBtn')) return;
  const btn = document.createElement('button');
  btn.id = 'backToTopBtn';
  btn.type = 'button';
  btn.setAttribute('aria-label', 'Kembali ke atas');
  btn.innerHTML = `<svg style="width:24px;height:24px;stroke:currentColor;fill:none;stroke-width:2.5;" viewBox="0 0 24 24"><path d="M12 19V5M5 12l7-7 7 7"/></svg>`;
  btn.style.cssText = 'position:fixed;bottom:28px;right:28px;width:50px;height:50px;border-radius:50%;background:linear-gradient(135deg,#087f89,#02a7b0);color:#ffffff;border:none;box-shadow:0 8px 24px rgba(8,127,137,0.45);cursor:pointer;z-index:9999;display:flex;align-items:center;justify-content:center;transition:all .3s cubic-bezier(.16,1,.3,1);opacity:0;visibility:hidden;transform:scale(0.8);';
  
  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  btn.addEventListener('mouseenter', () => {
    btn.style.transform = 'scale(1.1) translateY(-2px)';
    btn.style.boxShadow = '0 12px 28px rgba(8,127,137,0.55)';
  });
  btn.addEventListener('mouseleave', () => {
    btn.style.transform = 'scale(1)';
    btn.style.boxShadow = '0 8px 24px rgba(8,127,137,0.45)';
  });
  
  document.body.appendChild(btn);

  window.addEventListener('scroll', () => {
    if (window.scrollY > 350) {
      btn.style.opacity = '1';
      btn.style.visibility = 'visible';
      btn.style.transform = 'scale(1)';
    } else {
      btn.style.opacity = '0';
      btn.style.visibility = 'hidden';
      btn.style.transform = 'scale(0.8)';
    }
  });
}
"""

# Tambahkan sebelum (function() {
init_pos = code.find('// INTI EKSEKUSI')
if init_pos != -1:
    code = code[:init_pos] + interactive_code + "\n" + code[init_pos:]
    print("Kode interaktif berhasil disisipkan sebelum INTI EKSEKUSI.")
else:
    code = code + "\n" + interactive_code
    print("Kode interaktif ditambahkan di akhir file.")

# Panggil initBackToTop() di dalam attach()
code = code.replace("attach();", "attach(); initBackToTop();")
print("Panggilan initBackToTop() ditambahkan.")

with open('public/assets/app.js', 'w', encoding='utf-8') as f:
    f.write(code)
print("Berhasil menyimpan app.js.")

