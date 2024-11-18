from bs4 import BeautifulSoup

html = """<div>
<p>World</p>
</div>
"""

soup = BeautifulSoup(html, "html.parser")
new_tag = soup.new_tag("p")
new_tag.string = "Hello"
soup.p.insert_before(new_tag)
print(soup)
