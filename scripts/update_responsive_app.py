import re

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Update Hero stage side
    old_stage_side = '<div class="v4-stage-side" style="display:grid;grid-template-rows:1fr 1fr;gap:18px;">'
    new_stage_side = '<div class="v4-stage-side">'
    if old_stage_side in c:
        c = c.replace(old_stage_side, new_stage_side)
        print(f'[{path}] Updated v4-stage-side')
    else:
        print(f'[{path}] old_stage_side not found')

    # 2. Update v4-news-grid inline style
    old_news_grid = '<div class="v4-news-grid" style="grid-template-columns:1.2fr 1fr;gap:32px;">'
    new_news_grid = '<div class="v4-news-feature-grid">'
    if old_news_grid in c:
        c = c.replace(old_news_grid, new_news_grid)
        print(f'[{path}] Updated v4-news-feature-grid')
    else:
        print(f'[{path}] old_news_grid not found')

    # 3. Update side news panel inline style
    old_side_item = '<article class="panel" style="background:#ffffff;border:1px solid #dce8eb;border-radius:14px;padding:16px;display:grid;grid-template-columns:110px 1fr;gap:16px;align-items:center;">'
    new_side_item = '<article class="v4-side-news-item">'
    if old_side_item in c:
        c = c.replace(old_side_item, new_side_item)
        print(f'[{path}] Updated v4-side-news-item')
    else:
        print(f'[{path}] old_side_item not found')

    # 4. Update thumbnail container in side news
    old_side_thumb = '<div style="width:110px;height:85px;border-radius:10px;overflow:hidden;background:#e2e8f0;flex-shrink:0;">'
    new_side_thumb = '<div class="v4-side-news-thumb">'
    if old_side_thumb in c:
        c = c.replace(old_side_thumb, new_side_thumb)
        print(f'[{path}] Updated v4-side-news-thumb')
    else:
        print(f'[{path}] old_side_thumb not found')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

update_file('public/assets/app.v4.js')
update_file('public/assets/app.js')
