from bs4 import BeautifulSoup

html = """
<div class="d1">
    <div class="d2">
        <span>메시지1</span>
        <span>메시지2</span>
    </div>
</div>

<p>가나다</p>
"""

soup = BeautifulSoup(html, "html.parser")
soup.span.replace_with("새 메시지")
soup.p.replace_with("새 메시지")
print(soup)
