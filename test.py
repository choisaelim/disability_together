import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#환경변수

#며칠 전 글까지 볼건지
DAY_BEFORE = 14 #나중에 1일로 변경
YYYYMMDD_FORMAT = '%Y-%m-%d'
MMDD_FORMAT = '%m-%d'

#언제까지 크롤링할지 날짜 확인
import datetime

until = datetime.datetime.now() - datetime.timedelta(DAY_BEFORE)


chrome_driver = "C:\\Users\\saelim\\Documents\\git\\disability_together\\chromedriver\\chromedriver.exe"

chrome_options = Options()

# browser = webdriver.Chrome(chrome_driver, options=chrome_options)
# GANGNAM_URL = "http://gn.dfsc.or.kr/main/main.php?categoryid=04&menuid=01&groupid=00"
# browser.get(GANGNAM_URL)

# lines = browser.find_elements(By.CSS_SELECTOR, '#contents_area > table > tbody > tr')
# print(len(lines))
print(until.strftime(YYYYMMDD_FORMAT))
# browser.close()