import os
import re

txt_path = r"c:\Users\manam\OneDrive\デスクトップ\佐藤美咲先生\小説_星屑_of_小夜曲_202602081601\囚われの白百合_愛執の枷.txt"
html_path = r"c:\Users\manam\OneDrive\デスクトップ\佐藤美咲先生\小説_星屑_of_小夜曲_202602081601\web\captive_lily.html"

with open(txt_path, 'r', encoding='utf-8') as f:
    text_content = f.read()

html_head = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>囚われの白百合、愛執の枷 - 星と花の小夜曲</title>
    <meta name="description" content="マツバ×イヨリの無理やり系ダークスイートなR18物語。">
    <link rel="stylesheet" href="style.css">
    <style>
        .work-info-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(189, 42, 78, 0.15);
            border: 1px solid rgba(189, 42, 78, 0.4);
            border-radius: 20px;
            padding: 4px 14px;
            font-size: 0.72rem;
            color: var(--text-dim);
            letter-spacing: 0.1rem;
            margin: 0 auto 1.5rem;
        }

        .novel-content p {
            line-height: 2.4;
            margin-bottom: 2rem;
            text-indent: 1em;
            min-height: 1em;
        }

        .chapter-break {
            text-align: center;
            margin: 4rem 0;
            color: #bd2a4e;
            letter-spacing: 1.5rem;
            font-size: 1.2rem;
            opacity: 0.6;
        }
    </style>
</head>
<body>
    <div class="background-overlay" style="background: linear-gradient(to bottom, rgba(10, 0, 20, 0.8), rgba(0, 0, 0, 0.95));"></div>
    <div class="noise"></div>
    <div class="magic-circle" style="opacity: 0.3;"></div>

    <header>
        <div class="subtitle">DARK MATSUIYO TALE (R-18)</div>
        <h1>囚われの白百合、愛執の枷</h1>
        <div class="subtitle-japanese">― 穏やかな微笑みと、逃げられない檻 ―</div>
        <nav class="nav-links">
            <a href="index.html">TOP</a>
            <a href="list.html">ARCHIVE</a>
        </nav>
    </header>

    <main>
        <article class="novel-container" style="max-width: 800px;">
            <div style="text-align:center; margin-bottom: 2rem;">
                <div class="work-info-badge">マツバ×イヨリ / ヤンデレ・ドス黒 / 無理やりR18 / 【真】全文掲載</div>
            </div>
            <div class="novel-content" id="content">
"""

lines = text_content.split('\n')
paragraphs_html = []
for line in lines:
    line = line.strip('\r')
    if '囚われの白百合、愛執の枷（完全版）' in line and len(paragraphs_html) == 0:
        continue # skip title
    if line.strip() in ['一', '二', '三', '四', '五', '六', '七', '八', '九']:
        paragraphs_html.append(f'                <div class="chapter-break">{line.strip()}</div>')
    elif line.strip() == '（了）' or line.strip() == '了' or line.strip() == '――了――':
        paragraphs_html.append(f'                <p style="text-align: right; color: var(--text-dim); font-size: 0.8rem; margin-top: 3rem;">了</p>')
    elif line.strip() == '' or line.strip('　') == '':
        continue
    else:
        # replace any specific text formatting if needed, but normally just p tag
        paragraphs_html.append(f'                <p>{line}</p>')

html_tail = """
            </div>
        </article>
        
        <div style="text-align: center; margin: 4rem 0;">
            <a href="list.html" style="color: var(--text-dim); text-decoration: none; font-size: 0.9rem;">← ARCHIVEに戻る</a>
        </div>
    </main>

    <footer>
        &copy; 2026 STELLAR CRADLE / STARRING MATSUBA &amp; IYORI.
    </footer>
</body>
</html>
"""

html_out = html_head + '\n'.join(paragraphs_html) + html_tail

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_out)

print("HTML compilation complete.")
