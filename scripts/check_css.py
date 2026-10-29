with open('public/assets/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f'Total baris style.css: {len(lines)}')
# Cek beberapa class
content = ''.join(lines)
for c in ['v4-executive', 'profile-card', 'kadis', 'pagination', 'badge', 'modal', 'card-grid']:
    print(f'Class {c} in style.css:', c in content)

