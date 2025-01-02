from time import sleep

from selenium.webdriver.common.by import By



class PageUploadOtherFile:

    @staticmethod
    def next_step(driver):
        """下一步"""
        driver.find_element(By.XPATH, "//span[text()=' 下一步 ']").click()
        sleep(3)
