from time import sleep

from selenium.webdriver.common.by import By


class PageUploadBidFile:

    @staticmethod
    def upload_file(driver, file):
        """上传采购文件"""
        driver.find_element(By.XPATH, "//input[@type='file']").send_keys(file)
        sleep(5)

    @staticmethod
    def next_step(driver):
        """下一步"""
        driver.find_element(By.XPATH, "//span[text()=' 下一步 ']").click()
        sleep(3)

    def upload_bid_file(self,driver,kwargs):
        self.upload_file(driver,kwargs['file'])
        self.next_step(driver)