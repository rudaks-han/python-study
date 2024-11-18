import re

from bs4 import BeautifulSoup

html = """<div>
  Hello
  <p>World</p>
  <p><!-- some comment -->Text</p>
  <p>More <b>Text</b></p>
</div>
"""


soup = BeautifulSoup(html, "html.parser")
soup.smooth()

print(soup)
