from time import sleep
from selenium.webdriver.common.by import By

from common import tool


class PageGcAdd:
    """
    政府采购项目编辑页
    """
    @staticmethod
    def level_province(driver):
        """省级"""
        driver.find_element(By.XPATH, '//span[text()="省级"]').click()
        sleep(1)

    @staticmethod
    def level_city(driver):
        """市级"""
        driver.find_element(By.XPATH, '//span[text()="市级"]').click()
        sleep(1)

    @staticmethod
    def dept_traffic(driver):
        """交通部门"""
        driver.find_element(By.XPATH, '//span[text()="交通部门"]').click()
        sleep(1)

    @staticmethod
    def dept_water(driver):
        """水利部门"""
        driver.find_element(By.XPATH, '//span[text()="水利部门"]').click()
        sleep(1)

    @staticmethod
    def dept_room(driver):
        """住建部门"""
        driver.find_element(By.XPATH, '//span[text()="住建部门"]').click()
        sleep(1)

    @staticmethod
    def dept_other(driver):
        """采其他部门"""
        driver.find_element(By.XPATH, '//span[text()="其他部门"]').click()
        sleep(1)

    @staticmethod
    def add_button(driver):
        """采其他部门"""
        driver.find_element(By.XPATH, '//button/span[text()="添加项目"]').click()
        sleep(1)

    def gc_add(self,driver,kwargs):
        self.level_city(driver)
        if kwargs['sxf'] == 1:
            self.dept_traffic(driver)
        self.add_button(driver)