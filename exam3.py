"""
# 셀레니움 라이브러리로 사용
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome()
driver.implicitly_wait(3)
url = 'https://booktoki284.com/novel/222'
driver.get(url)

links = []
pattern = r'\b화산귀환-\d+화\b'
a_tags = driver.find_elements(By.CLASS_NAME, 'item-subject')
for a_tag in a_tags:
    link = {}
    link['text'] = a_tag.text
    # text = re.findall(pattern, a.text)
    link['href'] = re.findall(pattern, a_tag.get_attribute('href'))
    links.append(link)

for content in links:
    title = content['title']
    text = content['text']
    with open(title + '.txt', 'w', encoding='utf-8') as f:
        f.write(text)

driver.quit()
"""