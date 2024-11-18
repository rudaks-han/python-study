from bs4 import BeautifulSoup


html = """
<p style="font-family: "맑은 고딕"">a</p>
"""
soup = BeautifulSoup(html, "html.parser")
for tag in soup():
    tag.smooth()
    for attribute in ["class", "id", "name", "style"]:
        del tag[attribute]
print(html)
print(str(soup))
