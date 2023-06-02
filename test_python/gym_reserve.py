from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class GymReserve():
    def setup_method(self, service):
        self.driver = webdriver.Chrome(service=service)
        self.vers = {}
        
    def teardown_method(self):
        self.driver.quit()
        
        
    def test_gymreserve(self, inp):
        self.driver.get("https://select-type.com/rsv/?id=KatPteH9vEg")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, "c_id").click()
        dropdown = self.driver.find_element(By.NAME, "c_id")
        dropdown.find_element(By.XPATH, "//option[. = 'BKCトレーニングルーム/BKC Gymnasium']").click()
        search = "2023-" + inp + "_td_cls"
        judge = self.driver.find_element(By.XPATH, value='//a[@id="{}"]/div[@class="cl-day-content"]/span'.format(search))
        if judge.text != "●":
            print("予約できないよ")
        else:
            self.driver.find_element(By.ID, search).click()
            choices = self.driver.find_elements(By.CLASS_NAME, 'res-label')
            choice_judges = self.driver.find_elements(By.XPATH, value='//a[@class="res-label"]')
            judge_i = []
            for choice_judge in choice_judges:
                if choice_judge.text == "×":
                    judge.append(0)
                else:
                    judge.append(1)
            choice_times = []
            for i, choice in enumerate(choices):
                choice_times.append(choice.text.split(" ")[0])
            print("現在予約可能な日時は以下の通りです")
            for i, time in enumerate(choice_times):
                print("{}:{}".format(i+1,time))
             
            i = input("どの時間帯を予約しますか：")
            print("{}の時間帯ですね、予約します".format(choices[int(i)-1].text.split(" ")[0]))
            choices[int(i)-1].click()
            self.driver.find_element(By.CLASS_NAME, 'btn-primary').click()
            print("予約完了しました")

if __name__ == '__main__':
    chrome_driver_path = 'chromedriver.exe'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    service = Service(chrome_driver_path)
    
    reserve = GymReserve()
    reserve.setup_method(service)
    inp = input("何曜日の予約をしますか？：")
    reserve.test_gymreserve(inp)
    
    time.sleep(2)
    reserve.teardown_method()
    
    