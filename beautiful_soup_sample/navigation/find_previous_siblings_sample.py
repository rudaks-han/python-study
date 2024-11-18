from bs4 import BeautifulSoup

html = """<div class="d1">
    <div class="d2">
        <span>메시지1</span>
        <span>메시지2</span>
        <p>메시지 p1</p>
        <p>메시지 p2</p>
        <p>메시지 p3</p>
    </div>
</div>
"""

soup = BeautifulSoup(html, "html.parser")
print(soup.p.find_previous_siblings())
