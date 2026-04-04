import os

base_dir = r"c:\Users\manam\OneDrive\デスクトップ\佐藤美咲先生\小説_星屑_of_小夜曲_202602081601"
web_dir = os.path.join(base_dir, "web")

def convert(txt_filename, html_filename, is_r18):
    txt_path = os.path.join(base_dir, txt_filename)
    html_path = os.path.join(web_dir, html_filename)
    
    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    paragraphs = []
    for line in lines:
        line = line.strip('\n')
        if line.strip() != "":
            paragraphs.append(f"<p>{line}</p>")
        else:
            paragraphs.append("<br>")
            
    content = "\n".join(paragraphs)
    
    if is_r18:
        title = "四月四日のこんぺいとう 夜の部 - ハーブティーと金平糖"
        subtitle = "ECHOES OF ECRUTEAK (R-18)"
        warning_html = """
            <div class="warning-box" style="border: 1px solid #bd2a4e; padding: 1.5rem; margin-bottom: 3rem; text-align: center; border-radius: 15px; background: rgba(189, 42, 78, 0.05);">
                <p style="color: #bd2a4e; font-weight: bold; font-size: 1.1rem;">R-18 WARNING</p>
                <p style="font-size: 0.8rem; margin-top: 0.5rem;">この作品には成人向け描写が含まれます。18歳未満の方の閲覧は固く禁じます。</p>
            </div>
"""
        chapter_title = '<h2 class="chapter-title" style="color: #bd2a4e;">四月四日のこんぺいとう 夜の部</h2>'
        nav_html = """
            <div class="novel-navigation">
                <a href="yonigatsu_konpeito.html" class="nav-btn">Previous Page</a>
                <a href="list.html" class="nav-btn">Back to List</a>
            </div>
"""
        header_color = ' style="background: linear-gradient(90deg, transparent, #bd2a4e, transparent);"'
        adult_subtitle = '<div class="subtitle" style="color: #bd2a4e;">ADULT ONLY CONTENTS</div>'
    else:
        title = "四月四日のこんぺいとう - ハーブティーと金平糖"
        subtitle = "ECHOES OF ECRUTEAK"
        warning_html = ""
        chapter_title = '<h2 class="chapter-title">四月四日のこんぺいとう</h2>'
        nav_html = """
            <div class="novel-navigation">
                <a href="list.html" class="nav-btn">Back to List</a>
                <a href="yonigatsu_konpeito_ecchi.html" class="nav-btn next-btn" style="border-color: #bd2a4e; color: #bd2a4e;">Next: 夜の部 (R-18)</a>
            </div>
"""
        header_color = ''
        adult_subtitle = '<div class="subtitle">STARRING MATSUBA &amp; IYORI</div>'

    html_template = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="background-overlay"></div>
    <div class="noise"></div>
    <div class="magic-circle"></div>

    <header>
        <div class="subtitle">{subtitle}</div>
        <h1>ハーブティーと金平糖</h1>
        <div class="subtitle-japanese">― マツバ × イヨリ ―</div>
        {adult_subtitle}
        <nav class="nav-links">
            <a href="index.html">Home</a>
            <a href="list.html">Archive</a>
            <a href="iyori_dic.html">Wiki</a>
        </nav>
        <div class="header-decoration"{header_color}></div>
    </header>

    <main>
        <article class="novel-container">
{warning_html}
            {chapter_title}
            <div class="novel-content" id="content">
{content}
            </div>
{nav_html}
        </article>
    </main>

    <footer>
        &copy; 2026 HERB TEA & KONPEITO / CREATED BY SATOH MISAKI.
    </footer>
</body>
</html>
"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Generated {html_filename}")

convert("四月四日のこんぺいとう.txt", "yonigatsu_konpeito.html", False)
convert("四月四日のこんぺいとう_夜の部.txt", "yonigatsu_konpeito_ecchi.html", True)
