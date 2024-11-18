from bs4 import BeautifulSoup

html = """<div class="d1">
    <div class="d2">
        <span>메시지1</span>
        <span>메시지2</span>
    </div>
</div>
"""

soup = BeautifulSoup(html, "html.parser")
new_tag1 = soup.new_tag("p")
new_tag1.string = "First"
new_tag2 = soup.new_tag("p")
new_tag2.string = "Second"
soup.span.extend([new_tag1, new_tag2])

print(soup)
