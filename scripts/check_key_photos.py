import os, glob

candidates = [
    'public/uploads/2026/05/WhatsApp-Image-2026-05-04-at-09.43.05.jpeg',
    'public/uploads/2020/11/wellcomedinkes.png',
    'public/uploads/2026/07/WhatsApp-Image-2026-07-20-at-11.09.24.jpeg',
    'public/uploads/2026/09/WhatsApp-Image-2026-09-28-at-08.09.04.jpeg',
    'public/uploads/2025/09/WhatsApp-Image-2025-09-15-at-09.39.21_c7feddcf-1.jpg',
    'public/uploads/2023/08/WhatsApp-Image-2023-08-03-at-14.46.33.jpeg',
    'public/uploads/2026/10/cbe0e611-4ec4-4b64-b3ca-7fce94ef85a7.jpeg',
    'public/uploads/2026/10/1bc6a3ea-2aef-49dd-891c-f1be7469aca3.jpeg',
    'public/uploads/2026/10/ea1473c4-840a-4595-b375-61e9c0030936.jpeg',
    'public/uploads/2026/01/38bc8607-83a1-401a-9444-eedb572aed42.jpeg'
]

for c in candidates:
    exists = os.path.exists(c)
    sz = os.path.getsize(c) if exists else 0
    print(f"File: {c} | Exists: {exists} | Size: {sz} bytes")
