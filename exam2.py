"""
# 페이지 리스트 파싱
import requests
from bs4 import BeautifulSoup

data = [{'text': 'Python', 'href': 'https://www.python.org/'},
        {'text': 'Google', 'href': 'https://www.google.com/'}]

for item in data:
    res = requests.get(item['href'])
    soup = BeautifulSoup(res.text, 'html.parser')
    content = soup.get_text()
    with open(f"{item['text']}.txt", "w", encoding="utf-8") as f:
        f.write(content)
"""