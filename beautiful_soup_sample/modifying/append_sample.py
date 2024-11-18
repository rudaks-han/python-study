from bs4 import BeautifulSoup

html = """<div class="d1">
    <div class="d2">
        <span>메시지1</span>
        <span>메시지2</span>
    </div>
</div>
"""

soup = BeautifulSoup(html, "html.parser")
new_tag = soup.new_tag("span")
new_tag.string = "메시지3"
soup.span.append(new_tag)
print(soup)
