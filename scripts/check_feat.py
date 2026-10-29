import json

with open('public/data/articles.json', 'r', encoding='utf-8') as fp:
    articles = json.load(fp)

has_feat = [a for a in articles if a.get('featured_image')]
print(f'Total artikel: {len(articles)}')
print(f'Artikel yang punya featured_image: {len(has_feat)}')

for a in has_feat[:10]:
    print(f"ID {a['id']}: {a['title'][:50]} | Feat: {a['featured_image']}")
