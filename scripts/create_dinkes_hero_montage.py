from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

def create_hero_montage():
    width, height = 640, 560
    # Canvas transparan
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    
    # 1. Background Badge Lingkaran Radial / Card
    bg_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw_bg = ImageDraw.Draw(bg_layer)
    
    # Lingkaran aksen toska lembut di belakang
    draw_bg.ellipse([100, 40, 560, 500], fill=(230, 247, 245, 230), outline=(187, 247, 208, 180), width=3)
    draw_bg.ellipse([70, 20, 590, 540], outline=(8, 127, 137, 40), width=1)
    
    # 2. Gambar Gedung Kantor Dinkes sebagai backdrop melengkung
    try:
        kantor = Image.open("public/assets/kantor_dinkes_pinrang.jpg").convert("RGBA")
        kantor_w, kantor_h = 380, 260
        kantor = kantor.resize((kantor_w, kantor_h), Image.Resampling.LANCZOS)
        
        # Mask rounded corner untuk foto kantor
        mask_kantor = Image.new("L", (kantor_w, kantor_h), 0)
        draw_mask = ImageDraw.Draw(mask_kantor)
        draw_mask.rounded_rectangle([0, 0, kantor_w, kantor_h], radius=24, fill=255)
        
        # Tempel kantor di belakang kiri-tengah
        canvas.paste(bg_layer, (0, 0), bg_layer)
        canvas.paste(kantor, (130, 80), mask_kantor)
        
        # Overlay gradien tipis di foto kantor
        overlay = Image.new("RGBA", (kantor_w, kantor_h), (8, 127, 137, 70))
        canvas.paste(overlay, (130, 80), mask_kantor)
    except Exception as e:
        print("Kantor error:", e)

    # 3. Foto Kepala Dinas di depan
    try:
        kadis = Image.open("public/assets/kadis_ramli_yunus.png").convert("RGBA")
        # Resize proporsional
        k_w = 340
        k_h = int(kadis.height * (k_w / kadis.width))
        kadis = kadis.resize((k_w, k_h), Image.Resampling.LANCZOS)
        
        # Potong jika terlalu panjang
        if k_h > 460:
            kadis = kadis.crop((0, 0, k_w, 460))
            k_h = 460
            
        # Drop shadow untuk foto kadis
        shadow = Image.new("RGBA", (k_w + 30, k_h + 30), (0, 0, 0, 0))
        draw_s = ImageDraw.Draw(shadow)
        # Buat siluet gelap
        alpha = kadis.split()[3]
        shadow.paste((16, 52, 71, 90), (15, 15), mask=alpha)
        shadow = shadow.filter(ImageFilter.GaussianBlur(10))
        
        # Tempel shadow lalu kadis
        canvas.paste(shadow, (190, 75), shadow)
        canvas.paste(kadis, (205, 90), kadis)
    except Exception as e:
        print("Kadis error:", e)

    # 4. Pita / Banner "DINAS KESEHATAN KABUPATEN PINRANG" di bagian bawah
    banner_w, banner_h = 440, 68
    banner_x, banner_y = (width - banner_w) // 2, height - 80
    
    # Shadow banner
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle([banner_x - 4, banner_y - 2, banner_x + banner_w + 4, banner_y + banner_h + 8], radius=20, fill=(16, 52, 71, 60))
    
    # Body banner biru navy pekat dengan border toska
    draw.rounded_rectangle([banner_x, banner_y, banner_x + banner_w, banner_y + banner_h], radius=18, fill=(16, 52, 71, 245), outline=(10, 163, 152, 230), width=3)
    
    # Tambahkan teks banner
    try:
        font_main = ImageFont.truetype("arialbd.ttf", 17)
        font_sub = ImageFont.truetype("arial.ttf", 12)
    except:
        font_main = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        
    text1 = "DINAS KESEHATAN"
    text2 = "KABUPATEN PINRANG"
    
    # Posisi teks di tengah banner
    draw.text((banner_x + 120, banner_y + 14), text1, fill=(255, 255, 255), font=font_main)
    draw.text((banner_x + 120, banner_y + 38), text2, fill=(94, 234, 212), font=font_sub)
    
    # Tempel Logo Pinrang kecil di kiri banner
    try:
        logo_pinrang = Image.open("public/assets/logo_pinrang_opt.png").convert("RGBA")
        logo_pinrang = logo_pinrang.resize((48, 48), Image.Resampling.LANCZOS)
        canvas.paste(logo_pinrang, (banner_x + 16, banner_y + 10), logo_pinrang)
    except Exception as e:
        print("Logo error:", e)

    # Tempel Logo Kemenkes kecil di samping logo pinrang
    try:
        logo_kemenkes = Image.open("public/assets/kemenkes.jpg").convert("RGBA")
        logo_kemenkes = logo_kemenkes.resize((44, 44), Image.Resampling.LANCZOS)
        canvas.paste(logo_kemenkes, (banner_x + 68, banner_y + 12), logo_kemenkes)
    except Exception as e:
        print("Logo Kemenkes error:", e)

    out_path = "public/assets/hero_illustration_dinkes.png"
    canvas.save(out_path, "PNG")
    print(f"Berhasil membuat {out_path} ({os.path.getsize(out_path)} bytes)")

create_hero_montage()

