from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time


class GymReserve():
    def setup_method(self, service, vers):
        self.driver = webdriver.Chrome(service=service)
        self.vers = vers
        
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
            
            self.driver.find_element(By.XPATH, '//div[@class="modal-footer"]/input').click()

            self.driver.find_element(By.NAME, 'name').send_keys(self.vers["name"])
            self.driver.find_element(By.ID, 'rsvpif_email_id').send_keys(self.vers["email"])
            self.driver.find_element(By.ID, 'rsvpif_email_conf_id').send_keys(self.vers["email"])
            self.driver.find_element(By.NAME, 'other').send_keys(self.vers["no"])
            self.driver.find_element(By.NAME, 'other2').send_keys(self.vers["major"])
            self.driver.find_element(By.NAME, 'ans[186619]').send_keys(self.vers["major"])
            
            self.driver.find_element(By.NAME, 'do_rsv').click()
            script = "javascript: cmn.dispLoading();"
            self.driver.execute_script(script)


            self.driver.find_element(By.ID, 'ebtn_id').click()
            print("予約完了しました")

if __name__ == '__main__':
    chrome_driver_path = 'chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    service = Service(chrome_driver_path)

    #自身の情報を書き込む
    vers = {"name":"堂丸健吾", "email":"is0514se@ed.ritsumei.ac.jp", "no":"23530", "major":"情報理工学専攻"}
    
    reserve = GymReserve()
    reserve.setup_method(service, vers)
    inp = input("何日の予約をしますか？：")
    reserve.test_gymreserve(inp)
    
    time.sleep(5)
    reserve.teardown_method()
    
    