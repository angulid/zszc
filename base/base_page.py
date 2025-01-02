from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    @staticmethod
    def driver_wait(driver,loc):
        locator = (By.XPATH, loc)
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))

    @staticmethod
    def driver_quit(driver):
        driver.quit()
