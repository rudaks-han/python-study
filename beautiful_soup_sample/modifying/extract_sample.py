from bs4 import BeautifulSoup

html = """
<div>
    <p>Hello</p>
    <p>World</p>
</div>
"""
soup = BeautifulSoup(html, "html.parser")
p_tag = soup.p.extract()  # 첫 번째 <p> 요소 제거
print(soup)
