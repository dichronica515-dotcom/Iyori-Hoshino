import os

txt_path = r"c:\Users\manam\OneDrive\デスクトップ\佐藤美咲先生\小説_星屑_of_小夜曲_202602081601\今日のイヨリちゃんも、今日だけだから.txt"
html_path = r"c:\Users\manam\OneDrive\デスクトップ\佐藤美咲先生\小説_星屑_of_小夜曲_202602081601\web\today_iyori_only.html"

with open(txt_path, 'r', encoding='utf-8') as f:
    text_content = f.read()

html_head = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>今日のイヨリちゃんも、今日だけだから - 星と花の小夜曲</title>
    <meta name="description" content="『今日のチヒロは、今日だけなんです』の直後を描いた番外編。マツバ×イヨリの甘く官能的な夜の物語。">
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
    <div class="background-overlay" style="background: linear-gradient(to bottom, rgba(189, 42, 78, 0.1), rgba(0, 0, 0, 0.95));"></div>
    <div class="noise"></div>
    <div class="magic-circle"></div>

    <header>
        <div class="subtitle">STELLAR CRADLE #6 (R-18)</div>
        <h1>今日のイヨリちゃんも、今日だけだから</h1>
        <div class="subtitle-japanese">― まるごと愛して、骨ん中まで ―</div>
        <nav class="nav-links">
            <a href="index.html">TOP</a>
            <a href="child_rearing.html">SERIES</a>
            <a href="list.html">ARCHIVE</a>
        </nav>
    </header>

    <main>
        <article class="novel-container" style="max-width: 800px;">
            <div style="text-align:center; margin-bottom: 2rem;">
                <div class="work-info-badge">マツバ×イヨリ / 子育て番外編 / 甘々R18 / 【真】全文掲載</div>
            </div>
            <div class="novel-content" id="content">
"""

lines = text_content.split('\\n')
paragraphs_html = []
for line in lines:
    line = line.strip('\\r')
    if '今日のイヨリちゃんも、今日だけだから' == line.strip() and len(paragraphs_html) == 0:
        continue # skip title
    if line.strip() in ['一', '二', '三', '四', '五', '六', '七', '八', '九']:
        paragraphs_html.append(f'                <div class="chapter-break">{line.strip()}</div>')
    elif line.strip() == '了' or line.strip() == '――了――':
        paragraphs_html.append(f'                <p style="text-align: right; color: var(--text-dim); font-size: 0.8rem; margin-top: 3rem;">了</p>')
    elif line.strip() == '' or line.strip('　') == '':
        continue
    else:
        paragraphs_html.append(f'                <p>{line}</p>')

html_tail = """
            </div>
        </article>
        
        <div style="text-align: center; margin: 4rem 0;">
            <a href="child_rearing.html" style="color: var(--text-dim); text-decoration: none; font-size: 0.9rem;">← SERIESに戻る</a>
        </div>
    </main>

    <footer>
        &copy; 2026 STELLAR CRADLE / STARRING MATSUBA &amp; IYORI.
    </footer>
</body>
</html>
"""

html_out = html_head + '\\n'.join(paragraphs_html) + html_tail

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_out)

print("HTML compilation complete.")
