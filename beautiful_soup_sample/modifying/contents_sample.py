from bs4 import BeautifulSoup

html = """<div class="d1">
    <div class="d2">
        <span>메시지1</span>
        <span>메시지2</span>
    </div>
</div>"""

soup = BeautifulSoup(html, "html.parser")
print(soup.div.contents)
