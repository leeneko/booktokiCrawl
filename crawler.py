#from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import os
import datetime


def proc(driver):
  '''
  # url
  url = "https://booktoki285.com/novel/222"
  chrome_options = Options()
  #chrome_options.add_argument('--headless')  # view On/Off
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')

  driver = webdriver.Chrome(options=chrome_options)
  driver.implicitly_wait(3)

  # 페이지로 이동합니다.
  driver.get(url)
  '''
  # 가져오려는 상세 문서 번호
  target_num = input('Detailed document number : ')
  # 해당 상세 문서로부터 몇개 가져올 것인지
  impr_count = input('number of detailed documents : ')

  print('########## PROCESSING (1/3) ##########')
  # item-subject 클래스인 a 태그를 모두 찾습니다.
  elements = driver.find_elements(By.CLASS_NAME, "item-subject")

  # 링크와 내용을 저장할 리스트를 만듭니다.
  my_list = []

  # 각 element에서 링크와 내용(유효성 검사)을 추출하여 리스트에 추가합니다.
  pattern_title = r'\b화산귀환-\d+화\b'
  pattern_no = r'\d+'
  for element in elements:
    link = element.get_attribute("href")
    text = re.findall(pattern_title, element.text)[0]
    no = int(re.findall(pattern_no, text)[0])
    my_list.append({"no": no, "link": link, "text": text})

  # list 정렬
  # lst.sort(key=lambda x: x["no"])  # no를 기준으로 오름차순 정렬
  # sorted(data, key=lambda x: x["no"])
  my_list.sort(key=lambda x: x["no"])

  # print('my_list : ', my_list[0])
  print('########## PROCESSING (2/3) ##########')
  # 저장할 폴더 생성
  folder_name = 'output'
  if not os.path.exists(folder_name):
    os.makedirs(folder_name)

  sub_list = []
  for item in my_list:
    if int(target_num) <= int(item["no"]) < int(target_num) + int(impr_count):
      sub_list.append(item)

  # 최대값, 최소값
  max_no = str(max(sub_list, key=lambda x: x["no"])["no"])
  # min_no = str(min(sub_list, key=lambda x: x['no'])['no'])

  # print('sub_list : ', sub_list[0])
  print('########## PROCESSING (3/3) ##########')
  for li in sub_list:
    link = li["link"]
    text = li["text"]
    driver.get(link)
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.TAG_NAME, "body")))
    soup = BeautifulSoup(driver.page_source, "html.parser")
    '''
    # 크롤링 도중 캡챠 발견 시 수동 인증 진행
    try:
      captcha_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "fcaptcha")))
      input('Please solve the captcha press enter to continue...')
    except:
      # 캡챠 폼이 나타나지 않을 경우, 그냥 지나감
      pass
    '''
    #content = soup.find("div", {"class": "content"}).get_text()
    content = soup.find_all('p')

    # 제목으로 된 텍스트 파일을 생성하고 내용을 저장합니다.
    file_name = f"{text}.txt"
    file_path = os.path.join(folder_name, file_name)

    print(str(li["no"]) + ' / ' + max_no + ', now time : ', datetime.datetime.now().strftime("%H:%M:%S"))
    with open(file_path, "w+", encoding="utf-8") as f:
      for p in content:
        # print(p.get_text() + '\n')
        f.write(p.get_text() + '\n')

  # Chrome 브라우저를 종료합니다.
  print('########## COMPLETE ##########')
  driver.quit()