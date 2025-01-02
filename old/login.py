from time import sleep
from xml.etree.ElementPath import xpath_tokenizer

from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    def __init__(self):
        print('初始化')
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def login_trade_zbr(self):
        print('进来了 ------login_trade_zbr')
        # 清苑
        # url = 'http://trade.qy-test.zszc.jianshicha.cn/#/login'
        # 沙河
        driver = self.driver
        url = 'http://trade.jy-test.zszc.jianshicha.cn/'
        self.driver.get(url)
        # time.sleep(5)
        # //*[@id="pane-pwd"]/div/form/div[1]/div/div[1]/input
        driver.find_element(By.NAME, 'username').send_keys('招标人AAA ')
        driver.find_element(By.NAME, 'password').send_keys('c123456.')
        sleep(2)
        login_button = driver.find_element(By.XPATH,
                                           '/html/body/div/div[1]/nav/div[2]/div/div[6]/div/div[2]/div[1]/div/form/div[4]/div/button')
        login_button.click()
        # sleep(100)
        login_role = driver.find_element(By.XPATH, "//*[text()='招标人登录']")
        login_role.click()
        return driver

    def login_trade_approve(self):
        print('进来了 ------login_trade_approve')
        driver = self.driver
        # 清苑
        # url = 'http://trade.qy-test.zszc.jianshicha.cn/#/login'
        # 沙河
        url = 'http://trade.jy-test.zszc.jianshicha.cn/'
        driver.get(url)
        # time.sleep(5)
        # //*[@id="pane-pwd"]/div/form/div[1]/div/div[1]/input
        driver.find_element(By.NAME, 'username').send_keys('trade-audit ')
        driver.find_element(By.NAME, 'password').send_keys('a123456.')
        sleep(2)
        login_button = driver.find_element(By.XPATH,
                                           '/html/body/div/div[1]/nav/div[2]/div/div[6]/div/div[2]/div[1]/div/form/div[4]/div/button')
        login_button.click()
        # sleep(100)
        # login_role = driver.find_element(By.XPATH, "//*[text()='招标人登录']")
        # login_role.click()
        return driver