from bs4 import BeautifulSoup

# <table>
# <tr>
# <td>Cell 1</td>
# <td>Cell 2</td>
# </tr>
# </table>


html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test HTML</title>
</head>
<body>
    <header>
        <h1>헤더 메뉴</h1>
        <nav>
            <ul>
                <li><a href="/home">메뉴1</a></li>
                <li><a href="/about">메뉴2</a></li>
            </ul>
        </nav>
    </header>

    <section>
        <h2>Featured Articles</h2>
        <article>
            <h3>H3</h3>
            <p>p1</p>
            <a href="/articles/ai" class="read-more">Read more</a>
        </article>
    </section>

    <section>
        <h2>Our Team</h2>
        <div>
            <p><strong>John Doe</strong></p>
            <p>Position: CEO</p>
            <p>Bio: John has over 20 years of experience in technology leadership.</p>
        </div>
    </section>
    <footer>
        <p>&copy; 2024 Test Company. All rights reserved.</p>
        <img src="logo.png" alt="Test Company Logo">
    </footer>
</body>
</html>
"""

html = """
<div>
    <span>우리나라</span>
    <ul>
        <li>한국</li>
        <li>대한민국</li>
    </ul>
</div>
"""

# NEW_LINE = "__NEW_LINE__"
NEW_LINE = "\n"


def extract_text(html: str):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup.find_all(True):
        print(tag.name)
        if tag.name in ["p"]:
            # print("####### tag : " + str(tag).strip())
            if str(tag).strip() in ["<p><br/></p>", "<p><br></p>"]:
                # tag.replace_with("_______" + NEW_LINE + NEW_LINE)
                tag.insert_before("_______" + NEW_LINE + NEW_LINE)
                tag.unwrap()
            elif tag.parent is not None:
                tag.insert_before(NEW_LINE)
                tag.unwrap()
        elif tag.name in ["br"]:
            # if tag.parent is not None:
            tag.insert_before(NEW_LINE)
            tag.unwrap()
        elif tag.name in ["span"]:
            # texts = [span.get_text().strip() for span in tag.find_all("span")]
            # result = " ".join(texts)
            # tag.replace_with(result)
            tag.insert_before(tag.get_text() + " ")
            tag.extract()
        elif tag.name in ["head"]:
            tag.unwrap()
        elif tag.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            tag.insert_before(NEW_LINE + tag.get_text() + NEW_LINE)
            tag.extract()
        # <a> 태그를 [텍스트](URL) 형식으로 변환
        elif tag.name in ["a"] and tag.has_attr("href"):
            markdown_link = f"[{tag.get_text()}]({tag['href']})"
            tag.insert_before(markdown_link)
            tag.extract()  # <a> 태그 제거
        # <img> 태그를 ![alt](src) 형식으로 변환
        elif tag.name == "img" and tag.has_attr("src"):
            alt_text = tag.get("alt", "")  # alt 속성이 없으면 빈 문자열
            markdown_image = f"[unknown image]"
            tag.insert_before(markdown_image)  # 이미지 제거하도록 함.
            # tag.insert_before(markdown_image) # 이미지 제거하도록 함.
            tag.extract()
        # <ul> 태그를 처리
        elif tag.name == "ul":
            list_items = []
            for li in tag.find_all("li"):
                list_items.append(f"* {li.get_text(strip=True)}")
                li.extract()  # <li> 태그 제거
            tag.insert_before(NEW_LINE.join(list_items) + NEW_LINE)
            tag.extract()  # <ul> 태그 제거
        elif tag.name == "ol":
            list_items = []
            for index, li in enumerate(tag.find_all("li"), start=1):
                list_items.append(
                    f"{index}. {li.get_text(strip=True)}"
                )  # 숫자와 항목 형식으로 추가
                li.extract()  # <li> 태그 제거
            # <ol> 태그 제거 후 변환된 리스트를 추가
            tag.insert_before(NEW_LINE.join(list_items) + NEW_LINE)
            tag.extract()  # <ol> 태그 제거
        elif tag.name == "hr":
            tag.insert_before(NEW_LINE + "---" + NEW_LINE)
            tag.extract()
        elif tag.name == "blockquote":
            tag.insert_before(f" {tag.get_text()}\n")
            tag.extract()
        elif tag.name == "strong":
            tag.insert_before(f"**{tag.get_text()}**")
            tag.extract()
        elif tag.name == "em":
            tag.insert_before(f"*{tag.get_text()}*")
            tag.extract()
        elif tag.name == "pre":
            # <pre> 태그의 내용을 가져와서 마크다운 형식으로 변환
            code_content = tag.get_text(strip=False)  # 줄 바꿈 및 공백 유지
            markdown_code_block = f"```{NEW_LINE}{code_content}{NEW_LINE}```{NEW_LINE}"  # 마크다운 코드 블록 형식
            tag.insert_before(markdown_code_block)
            tag.extract()  # <pre> 태그 제거

    # return str(soup)
    return soup.get_text()


if __name__ == "__main__":
    result = extract_text(html)
    print("____ 결과 ____")
    print(result)
