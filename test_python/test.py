from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

chrome_driver_path = 'chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('--headless')

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)

driver.implicitly_wait(10)

driver.get('https://www.library.chiyoda.tokyo.jp/')

text_box = driver.find_element(By.NAME, 'txt_word')
text_box.send_keys('Pythonプログラミング')

btn = driver.find_element(By.NAME, 'submit_btn_searchEasy')
btn.click()

oder = driver.find_element(By.ID, 'opt_oder')
oder_select = Select(oder)
oder_select.select_by_value('0')

btn_sort =driver.find_element(By.NAME, 'submit_btn_sort')
btn_sort.click()