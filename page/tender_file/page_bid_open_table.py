from time import sleep

from selenium.webdriver.common.by import By

from common import tool


class PageBidOpenTable:

    @staticmethod
    def list_add_quote(driver):
        """输入报价列"""
        driver.find_element(By.XPATH, '//tr[1]//input[@placeholder="请输入名称"]').send_keys('报价列')

        driver.find_element(By.XPATH, "//tr[1]//td[4]//input[@placeholder='请选择']").click()
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]//span[text()='报价']").click()

        driver.find_element(By.XPATH, "//tr[1]//td[3]//input[@placeholder='请选择']").click()
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]//span[text()='数字含小数']").click()
        sleep(1)

    @staticmethod
    def list_add_work_date(driver):
        """新增工期列"""
        driver.find_element(By.XPATH, "//span[text()=' 添加 ']").click()
        driver.find_element(By.XPATH, '//tr[2]//input[@placeholder="请输入名称"]').send_keys('工期列')

        driver.find_element(By.XPATH, "//tr[2]//td[4]//input[@placeholder='请选择']").click()
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[1]//span[text()='工期']").click()

        driver.find_element(By.XPATH, "//tr[2]//td[3]//input[@placeholder='请选择']").click()
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[1]//span[text()='任意格式文本']").click()
        sleep(1)

    @staticmethod
    def list_add_work_date_sxf(driver):
        """新增工期列"""
        driver.find_elements(By.XPATH, "//input[@placeholder='请选择']")[3].click()
        sleep(1)
        driver.find_elements(By.XPATH, "//span[text()='第二信封']")[1].click()

        driver.find_elements(By.XPATH, "//input[@placeholder='请选择']")[6].click()
        sleep(1)
        driver.find_elements(By.XPATH, "//span[text()='第一信封']")[1].click()

    @staticmethod
    def next_step(driver):
        """"""
        driver.find_element(By.XPATH, "//span[text()=' 下一步 ']").click()
        sleep(5)

    def set_bid_open_table(self,driver,sxf=0):
        self.list_add_quote(driver)
        self.list_add_work_date(driver)
        if sxf == 1:
            self.list_add_work_date_sxf(driver)
        self.next_step(driver)