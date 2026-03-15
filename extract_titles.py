import os
import re

directory = r'C:\Users\manam\OneDrive\デスクトップ\佐藤美咲先生\小説_星屑_of_小夜曲_202602081601\web'
exclude_files = ['index.html', 'list.html', 'character.html', 'iyori_dic.html', 'funya_world.html', 'funya_kingdom.html', 'funya_world_new.html', 'hoshi_no_shirabe.html', 'observer_log.html', 'gakuen_lovcom_portal.html']

results = []

for filename in os.listdir(directory):
    if filename.endswith('.html') and filename not in exclude_files:
        path = os.path.join(directory, filename)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            title_match = re.search(r'<title>(.*?)</title>', content)
            h1_match = re.search(r'<h1>(.*?)</h1>', content)
            
            title = title_match.group(1).replace(' - 金平糖とハーブティー', '').replace(' | MATSUBA & IYORI Portal', '').strip() if title_match else filename
            # Some titles might have extra info, let's clean it.
            
            # Check for R18 keywords or categories
            category = 'general'
            if 'R-18' in content or 'r18' in filename or 'pink' in filename or 'sexual' in filename or 'biyaku' in filename:
                category = 'r18'
            
            results.append({
                'filename': filename,
                'title': title,
                'category': category
            })

# Sort by filename or title
results.sort(key=lambda x: x['title'])

for res in results:
    print(f"[{res['category']}] {res['title']} ({res['filename']})")
