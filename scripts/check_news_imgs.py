import os
from PIL import Image

imgs = [
    '03_FOTO/wp-content/uploads/2026/10/cbe0e611-4ec4-4b64-b3ca-7fce94ef85a7.jpeg',
    '03_FOTO/wp-content/uploads/2026/10/1bc6a3ea-2aef-49dd-891c-f1be7469aca3.jpeg',
    '03_FOTO/wp-content/uploads/2026/10/ea1473c4-840a-4595-b375-61e9c0030936.jpeg',
    '03_FOTO/wp-content/uploads/2026/04/669620247_3468968696591644_5507426269761402553_n-2.jpg'
]

for p in imgs:
    exists = os.path.exists(p)
    if exists:
        im = Image.open(p)
        print(f'{os.path.basename(p)}: Exists! Dimensi = {im.size}')
    else:
        print(f'{os.path.basename(p)}: NOT FOUND')

