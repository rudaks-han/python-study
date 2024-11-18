from bs4 import BeautifulSoup

html = """
<p>   
    Hello    World!  
</p>
<p>Another text</p>
"""
soup = BeautifulSoup(html, "html.parser")
for string in soup.stripped_strings:
    print(repr(string))
