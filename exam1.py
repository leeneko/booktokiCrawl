"""
# 페이지 하나 파싱
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
headers = {"User-Agent" : ua.random}
url = "https://booktoki284.com/novel/222"
res = requests.get(url, headers=headers, verify=False)
html = res.text
soup = BeautifulSoup(html, "html.parser")
soup.prettify()
with open("output.html", "w", encoding="utf-8") as f:
    f.write(str(soup))
"""