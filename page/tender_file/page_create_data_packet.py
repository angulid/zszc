from time import sleep

from selenium.webdriver.common.by import By

from common import tool


class PageCreateDataPacket:

    @staticmethod
    def data_packet(driver):
        """生成数据包"""
        driver.find_element(By.XPATH, "//button//span[text()=' 生成数据包 ']").click()
        sleep(7)
        driver.find_element(By.XPATH, "//button//span[text()=' 提交 ']").click()
        sleep(10)
        driver.quit()
