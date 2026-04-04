$txtPath = "..\四月四日のこんぺいとう.txt"
$htmlPath = ".\yonigatsu_konpeito.html"

$lines = Get-Content $txtPath -Encoding UTF8
$paragraphs = @()
foreach ($line in $lines) {
    if ($line.Trim() -ne "") {
        $paragraphs += "<p>$($line)</p>"
    } else {
        $paragraphs += "<br>"
    }
}
$novelContent = $paragraphs -join "`r`n"

$htmlTemplate = @"
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>四月四日のこんぺいとう - ハーブティーと金平糖</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="background-overlay"></div>
    <div class="noise"></div>
    <div class="magic-circle"></div>

    <header>
        <div class="subtitle">ECHOES OF ECRUTEAK</div>
        <h1>ハーブティーと金平糖</h1>
        <div class="subtitle-japanese">― マツバ × イヨリ ―</div>
        <div class="subtitle">STARRING MATSUBA &amp; IYORI</div>
        <nav class="nav-links">
            <a href="index.html">Home</a>
            <a href="list.html">Archive</a>
            <a href="iyori_dic.html">Wiki</a>
        </nav>
        <div class="header-decoration"></div>
    </header>

    <main>
        <article class="novel-container">
            <h2 class="chapter-title">四月四日のこんぺいとう</h2>
            <div class="novel-content" id="content">
$novelContent
            </div>
            
            <div class="novel-navigation">
                <a href="list.html" class="nav-btn">Back to List</a>
                <a href="yonigatsu_konpeito_ecchi.html" class="nav-btn next-btn" style="border-color: #bd2a4e; color: #bd2a4e;">Next: 夜の部 (R-18)</a>
            </div>
        </article>
    </main>

    <footer>
        &copy; 2026 HERB TEA & KONPEITO / CREATED BY SATOH MISAKI.
    </footer>
</body>
</html>
"@

Set-Content -Path $htmlPath -Value $htmlTemplate -Encoding UTF8

$txtPath2 = "..\四月四日のこんぺいとう_夜の部.txt"
$htmlPath2 = ".\yonigatsu_konpeito_ecchi.html"

$lines2 = Get-Content $txtPath2 -Encoding UTF8
$paragraphs2 = @()
foreach ($line in $lines2) {
    if ($line.Trim() -ne "") {
        $paragraphs2 += "<p>$($line)</p>"
    } else {
        $paragraphs2 += "<br>"
    }
}
$novelContent2 = $paragraphs2 -join "`r`n"

$htmlTemplate2 = @"
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>四月四日のこんぺいとう 夜の部 - ハーブティーと金平糖</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="background-overlay"></div>
    <div class="noise"></div>
    <div class="magic-circle"></div>

    <header>
        <div class="subtitle">ECHOES OF ECRUTEAK (R-18)</div>
        <h1>ハーブティーと金平糖</h1>
        <div class="subtitle-japanese">― マツバ × イヨリ ―</div>
        <div class="subtitle" style="color: #bd2a4e;">ADULT ONLY CONTENTS</div>
        <nav class="nav-links">
            <a href="index.html">Home</a>
            <a href="list.html">Archive</a>
            <a href="iyori_dic.html">Wiki</a>
        </nav>
        <div class="header-decoration" style="background: linear-gradient(90deg, transparent, #bd2a4e, transparent);"></div>
    </header>

    <main>
        <article class="novel-container">
            <div class="warning-box" style="border: 1px solid #bd2a4e; padding: 1.5rem; margin-bottom: 3rem; text-align: center; border-radius: 15px; background: rgba(189, 42, 78, 0.05);">
                <p style="color: #bd2a4e; font-weight: bold; font-size: 1.1rem;">R-18 WARNING</p>
                <p style="font-size: 0.8rem; margin-top: 0.5rem;">この作品には成人向け描写が含まれます。18歳未満の方の閲覧は固く禁じます。</p>
            </div>

            <h2 class="chapter-title" style="color: #bd2a4e;">四月四日のこんぺいとう 夜の部</h2>
            <div class="novel-content" id="content">
$novelContent2
            </div>
            
            <div class="novel-navigation">
                <a href="yonigatsu_konpeito.html" class="nav-btn">Previous Page</a>
                <a href="list.html" class="nav-btn">Back to List</a>
            </div>
        </article>
    </main>

    <footer>
        &copy; 2026 HERB TEA & KONPEITO / CREATED BY SATOH MISAKI.
    </footer>
</body>
</html>
"@

Set-Content -Path $htmlPath2 -Value $htmlTemplate2 -Encoding UTF8

Write-Host "HTML conversion complete."
