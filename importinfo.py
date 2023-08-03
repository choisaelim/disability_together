from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#from pandas.core.frame import DataFrame
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains

chrome_driver = "C:\\Users\\saelim\\Documents\\git\\disability_together\\chromedriver\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(chrome_driver, options=chrome_options)
# action = ActionChains(browser)



GANGNAM_URL = "http://gn.dfsc.or.kr/main/main.php?categoryid=04&menuid=01&groupid=00"
browser.get(GANGNAM_URL)
