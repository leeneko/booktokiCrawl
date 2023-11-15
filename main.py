from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

while True:
  user_input = input('1. main / 2. viewer / 4. exit\n')
  if user_input == '1':
    # URL
    # url = "https://booktoki313.com/novel/222" # 화산귀환
    url = "https://booktoki314.com/novel/11881097"
    element = (By.CLASS_NAME, "item-subject")

    chrome_options = Options()
    # chrome_options.add_argument('--headless') # view On/Off
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)

    # direct page
    driver.get(url)
    driver.implicitly_wait(3)

    import crawler
    crawler.proc(driver)

  elif user_input == '2':
    import consoleViewer

    consoleViewer.view(input('input(e.g. - 12) : \n'))
    break
  elif user_input == '4':
    break
  else:
    print('not a valid input')
'''
    WebDriverWait(driver, 20).until(EC.url_to_be(url))  # 페이지 로딩한 뒤, url 일치 확인
    WebDriverWait(driver, 20).until(
      EC.presence_of_element_located(element))  # element가 나타날 때까지 기다림

    user_input = input('After Captcha Auth, 1. continued / 4. exit\n')
    if user_input == '1':
      import crawler
      crawler.proc(driver)
      break
    elif user_input == '4':
      break
  elif user_input == '2':
    import consoleViewer
    consoleViewer.view(input('input(e.g. - 12) : \n'))
    break
  elif user_input == '4':
    break
  else:
    print('not a valid input')
'''
