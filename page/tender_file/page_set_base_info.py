from time import sleep

from selenium.webdriver.common.by import By

from common import tool
from common.tool import locate


class PageSetBaseInfo:

    @staticmethod
    def select_bid(driver):
        """选择标段"""
        driver.find_element(By.XPATH,
                            '//*[@id="puilceTable"]/form/div/div[3]//span[@class="el-checkbox__input"]').click()
        sleep(1)

    @staticmethod
    def set_deposit(driver, kwargs):
        """设置保证金"""
        target = driver.find_element(By.XPATH, "//span[text()=' 投标保证金 ']/../following-sibling::div//input")
        tool.locate(driver, target)
        target.send_keys('199')
        driver.find_element(By.XPATH,
                            "//span[text()=' 投标保证金 ']/../following-sibling::div//input[@placeholder='请选择']").click()
        sleep(1)

    @staticmethod
    def select_deposit(driver):
        """选择-保证金"""
        driver.find_element(By.XPATH, "//span[contains(text(),'保证金 ')]/preceding-sibling::span").click()
        sleep(1)

    @staticmethod
    def select_lg(driver):
        """选择-保函"""
        driver.find_element(By.XPATH, "//span[contains(text(),'保函 ')]/preceding-sibling::span").click()
        sleep(1)

    @staticmethod
    def paper_price(driver):
        """图纸押金"""
        driver.find_element(By.XPATH, "//span[text()=' 图纸押金(元) ']/../following-sibling::div//input").send_keys('18')
        sleep(1)

    @staticmethod
    def payments(driver):
        """填写缴费说明"""
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写缴费说明']").send_keys('请在线下缴费')

    @staticmethod
    def doubt_time(driver, kwargs):
        """质疑截止时间"""
        driver.find_element(By.XPATH, '//input[@placeholder="请选择日期时间"]').send_keys(
            kwargs['end_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, '//span[contains(text()," 确定")]').click()

    @staticmethod
    def use_ca(driver):
        """不选用CA"""
        target = driver.find_element(By.XPATH, '//label[@for="ifUseCa"]/..//span[text()="否"]')
        tool.locate(driver,target)
        target.click()

    @staticmethod
    def open_people(driver):
        """开标人数"""
        driver.find_element(By.XPATH,"//span[text()=' 开标时最少参与人数 ']/../following-sibling::div//input").send_keys('3')

    @staticmethod
    def tender_people(driver):
        """评标人数"""
        driver.find_element(By.XPATH, "//span[text()=' 评标时最少参与人数 ']/../following-sibling::div//input").send_keys('3')

    @staticmethod
    def two_room(driver):
        """开标室、评标室"""
        driver.find_element(By.XPATH, '//input[@placeholder="请填写开标室"]').send_keys('111')
        driver.find_element(By.XPATH, '//input[@placeholder="请填写评标室"]').send_keys('112')

    @staticmethod
    def tender_place(driver):
        """开标地点"""
        driver.find_element(By.XPATH,
                            "//span[text()=' 开标地点 ']/../following-sibling::div//input").send_keys('开标地点:102')

    @staticmethod
    def next_step(driver):
        """下一步"""
        driver.find_element(By.XPATH, "//span[text()=' 下一步 ']").click()
        sleep(5)

    def set_base_info(self,driver,kwargs):
        """基本信息设置-有CA"""
        self.select_bid(driver)
        self.set_deposit(driver,kwargs)
        self.select_deposit(driver)
        self.select_lg(driver)
        self.payments(driver)
        self.doubt_time(driver,kwargs)
        self.use_ca(driver)
        self.next_step(driver)

    def set_base_info_noca(self,driver,kwargs):
        """基本信息设置-没有CA"""
        self.select_bid(driver)
        self.set_deposit(driver,kwargs)
        self.select_deposit(driver)
        self.select_lg(driver)
        self.payments(driver)
        self.doubt_time(driver,kwargs)
        self.next_step(driver)

    def com_set_base_info(self,driver,kwargs):
        """企业采购-基本信息设置"""
        self.select_bid(driver)
        self.set_deposit(driver,kwargs)
        self.select_deposit(driver)
        self.select_lg(driver)
        self.payments(driver)
        # self.doubt_time(driver,kwargs)
        # self.use_ca(driver)
        self.open_people(driver)
        self.tender_people(driver)
        self.tender_place(driver)
        self.next_step(driver)

    def gc_set_base_info(self,driver,kwargs):
        """工程-基本信息设置-有CA"""
        self.select_bid(driver)
        self.set_deposit(driver,kwargs)
        self.select_deposit(driver)
        self.select_lg(driver)
        self.paper_price(driver)
        self.payments(driver)
        self.doubt_time(driver,kwargs)
        self.use_ca(driver)
        self.two_room(driver)
        self.next_step(driver)
