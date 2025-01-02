from time import sleep
from selenium.webdriver.common.by import By
from base.base_page import BasePage



class ProjectManager(BasePage):
    """
    项目管理页面
    """
    @staticmethod
    def project_manager(driver):
        """
        进入项目管理页
        """
        sleep(3)
        loc = "//span[text()='项目管理']"
        BasePage.driver_wait(driver,loc)
        pro_manager = driver.find_element(By.XPATH, loc)
        pro_manager.click()
        sleep(3)

    @staticmethod
    def gov_purchase(driver):
        """政府采购"""
        driver.find_element(By.XPATH, "//span[text()='政府采购']").click()
        sleep(1)

    @staticmethod
    def gov_purchase_pro(driver):
        """政府采购项目"""
        driver.find_element(By.XPATH, "//span[text()='政府采购项目']").click()
        sleep(1)

    @staticmethod
    def gov_purchase_add(driver):
        """新增政府采购项目"""
        driver.find_element(By.XPATH, "//*/span[text()=' 新增政府采购项目 ']").click()
        sleep(3)

    @staticmethod
    def company_purchase(driver):
        """企业采购"""
        driver.find_element(By.XPATH, "//span[text()='企业采购']").click()
        sleep(1)

    @staticmethod
    def company_purchase_pro(driver):
        """企业采购项目"""
        driver.find_element(By.XPATH, "//span[text()='企业采购项目']").click()
        sleep(1)

    @staticmethod
    def company_purchase_add(driver):
        """新增企业采购项目"""
        driver.find_element(By.XPATH, "//*/span[text()=' 新增企业采购项目 ']").click()
        sleep(3)

    @staticmethod
    def engineering(driver):
        """工程建设"""
        driver.find_element(By.XPATH, "//span[text()='工程建设']").click()
        sleep(1)

    @staticmethod
    def engineering_pro(driver):
        """工程建设项目"""
        driver.find_element(By.XPATH, "//span[text()='工程建设项目']").click()
        sleep(1)

    @staticmethod
    def engineering_pro_add(driver):
        """工程建设项目"""
        driver.find_element(By.XPATH, "//span[text()=' 新增工程建设项目 ']").click()
        sleep(1)

    @staticmethod
    def engineering_biz_pro(driver):
        """工程建设招标项目"""
        driver.find_element(By.XPATH, "//span[text()='工程建设招标项目']").click()
        sleep(1)

    @staticmethod
    def engineering_biz_pro_add(driver):
        """ 新增工程建设招标项目 """
        driver.find_element(By.XPATH, "//span[text()=' 新增工程建设招标项目 ']").click()
        sleep(1)

    @staticmethod
    def enter_process(driver, kwargs):
        """进入操作流程"""
        name = kwargs['cg_name']
        driver.find_element(By.XPATH,"//input[@placeholder='请填写项目名称']").send_keys(name)
        sleep(2)
        driver.find_element(By.XPATH,"//span[text()='搜索']").click()
        sleep(2)
        driver.find_element(By.XPATH,'//*[@id="puilceTable"]/form/div/div[4]//span[text()=" 进入操作流程 "]').click()
        sleep(3)

    @staticmethod
    def gc_enter_process(driver, kwargs):
        """进入操作流程"""
        name = kwargs['cg_name']
        driver.find_element(By.XPATH, "//input[@placeholder='请填写招标项目名称']").send_keys(name)
        sleep(2)
        driver.find_element(By.XPATH, "//span[text()='搜索']").click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="puilceTable"]/form/div/div[4]//span[text()=" 进入操作流程 "]').click()
        sleep(3)


    def enter_gov_pro_page(self,driver):
        """政府采购项目页"""
        self.project_manager(driver)
        self.gov_purchase(driver)
        self.gov_purchase_pro(driver)
        self.gov_purchase_add(driver)

    def enter_company_pro_page(self,driver):
        """企业采购项目页"""
        self.project_manager(driver)
        self.company_purchase(driver)
        self.company_purchase_pro(driver)
        self.company_purchase_add(driver)

    def enter_gov_pro_process(self,driver,kwargs):
        """进入政府项目操作流程"""
        self.project_manager(driver)
        self.gov_purchase(driver)
        self.gov_purchase_pro(driver)
        self.enter_process(driver,kwargs)

    def enter_company_pro_process(self,driver,kwargs):
        """进入企业项目操作流程"""
        self.project_manager(driver)
        self.company_purchase(driver)
        self.company_purchase_pro(driver)
        self.enter_process(driver,kwargs)

    def enter_engineering_pro(self,driver):
        """新增工程建设项目"""
        self.project_manager(driver)
        self.engineering(driver)
        self.engineering_pro(driver)
        self.engineering_pro_add(driver)

    def enter_engineering_biz_pro(self,driver):
        """新增工程建设招标项目"""
        self.project_manager(driver)
        self.engineering(driver)
        self.engineering_biz_pro(driver)
        self.engineering_biz_pro_add(driver)

    def enter_gc_pro_process(self,driver,kwargs):
        """进入工程项目操作流程"""
        self.project_manager(driver)
        self.engineering(driver)
        self.engineering_biz_pro(driver)
        self.gc_enter_process(driver,kwargs)






