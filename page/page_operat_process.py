from time import sleep

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class PageOperatProcess(BasePage):

    @staticmethod
    def purchase_file_manage(driver):
        """采购文件管理"""
        # driver.find_element(By.XPATH, '//div[text()=" 采购文件管理"]').click()
        driver.find_element(By.XPATH, "//div[contains(text(),'采购文件管理')]").click()
        sleep(2)

    @staticmethod
    def zb_file_manage(driver):
        """招标文件管理"""
        # driver.find_element(By.XPATH, '//div[text()=" 采购文件管理"]').click()
        driver.find_element(By.XPATH, "//div[contains(text(),'招标文件管理')]").click()
        sleep(2)

    @staticmethod
    def purchase_file_add(driver):
        """添加采购文件"""
        driver.find_element(By.XPATH, '//span[text()="添加采购文件"]').click()
        sleep(2)

    @staticmethod
    def zb_file_add(driver):
        """添加招标文件"""
        driver.find_element(By.XPATH, '//span[text()="添加招标文件"]').click()
        sleep(2)

    @staticmethod
    def purchase_notice(driver):
        """采购公告"""
        # driver.find_element(By.XPATH, '//div[text()=" 采购公告"]').click()
        driver.find_element(By.XPATH, "//div[contains(text(),'采购公告')]").click()
        sleep(2)

    @staticmethod
    def zb_notice(driver):
        """招标公告"""
        # driver.find_element(By.XPATH, '//div[text()=" 采购公告"]').click()
        driver.find_element(By.XPATH, "//div[contains(text(),'招标公告')]").click()
        sleep(2)

    @staticmethod
    def purchase_notice_invite(driver):
        """邀请公告"""
        # driver.find_element(By.XPATH, '//div[text()=" 邀请公告"]').click()
        driver.find_element(By.XPATH, "//div[contains(text(),'邀请公告')]").click()
        sleep(2)

    @staticmethod
    def purchase_notice_add(driver):
        """添加公告"""
        driver.find_element(By.XPATH, "//span[text()=' 添加公告 ']").click()
        sleep(2)

    @staticmethod
    def tender_invite_letter(driver):
        """投标邀请函"""
        # driver.find_element(By.XPATH, '//div[text()=" 投标邀请函"]').click()
        driver.find_element(By.XPATH, "//div[contains(text(),'投标邀请函')]").click()
        sleep(2)

    @staticmethod
    def add_tender_invite_letter(driver):
        """投标邀请函"""
        driver.find_element(By.XPATH, "//span[text()=' 添加投标邀请函 ']").click()
        sleep(2)

    @staticmethod
    def single_source(driver):
        """单一来源公示"""
        # driver.find_element(By.XPATH, '//div[text()=" 单一来源公示"]').click()
        driver.find_element(By.XPATH, "//div[contains(text(),'单一来源公示')]").click()
        sleep(2)

    @staticmethod
    def single_source_add(driver):
        """添加"""
        driver.find_element(By.XPATH, "//span[text()=' 添加 ']").click()
        sleep(2)

    def add_purchase_file(self,driver):
        """采购文件管理-添加采购文件"""
        self.purchase_file_manage(driver)
        self.purchase_file_add(driver)

    def add_zb_file(self,driver):
        """采购文件管理-添加招标文件"""
        self.zb_file_manage(driver)
        self.zb_file_add(driver)

    def add_purchase_notice(self,driver,kwargs):
        """采购公告-添加公告"""
        cg_type = kwargs['cg_type']
        if cg_type in ['公开招标','竞争性谈判','竞争性磋商','询价']:
            self.purchase_notice(driver)
        elif cg_type in ['邀请招标','单一来源采购']:
            self.purchase_notice_invite(driver)
        self.purchase_notice_add(driver)

    def add_gc_zb_notice(self,driver,kwargs):
        """工程-招标公告-添加公告"""
        cg_type = kwargs['cg_type']
        if cg_type in ['公开招标']:
            self.zb_notice(driver)
        elif cg_type in ['邀请招标']:
            self.purchase_notice_invite(driver)
        self.purchase_notice_add(driver)

    def add_invite_letter(self,driver):
        """投标邀请函-添加投标邀请函"""
        self.tender_invite_letter(driver)
        self.add_tender_invite_letter(driver)

    def add_single_source(self,driver):
        """单一来源公示-添加"""
        self.single_source(driver)
        self.single_source_add(driver)

