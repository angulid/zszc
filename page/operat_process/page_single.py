from time import sleep

from selenium.webdriver.common.by import By

from common import tool


class PageSingle:
    """
    投标邀请函页面
    """
    @staticmethod
    def public_notice_name(driver,kwargs):
        target = driver.find_element(By.XPATH, "//input[@placeholder='请填写公告名称']")
        tool.locate(driver,target)
        target.send_keys(kwargs['cg_bd_name'] + '-公告')

    @staticmethod
    def purchaser_name(driver):
        driver.find_element(By.XPATH, "//input[@placeholder='请填写采购人名称']").send_keys('张XX')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写拟采购的货物或服务的说明']").send_keys('拟采购的货物或服务的说明')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写采用单一来源采购方式的原因及说明']").send_keys('采用单一来源采购方式的原因及说明')

    @staticmethod
    def purchaser_area(driver):
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写其他补充事宜']").send_keys('其他补充事宜')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写采购人地址']").send_keys('采购人地址')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写采购人联系方式']").send_keys('15766228511')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写财政部门名称']").send_keys('财政部门名称')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写财政部门地址']").send_keys('财政部门地址')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写财政部门联系方式']").send_keys('15766228512')

    @staticmethod
    def notice_start_end_time(driver,kwargs):
        driver.find_element(By.XPATH,
                            "//span[text()=' 公告发布时间 ']/../following-sibling::div//input[@placeholder='请选择日期时间']").send_keys(
            kwargs['start_date'])
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[3]//span[contains(text(),' 确定')]").click()
        driver.find_element(By.XPATH,
                            "//span[text()=' 公告结束时间（公示期限不得少于5个工作日） ']/../following-sibling::div//input[@placeholder='请选择日期时间']").send_keys(
            kwargs['end_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[4]//span[contains(text(),' 确定')]").click()

    @staticmethod
    def select_bid(driver):
        target = driver.find_element(By.XPATH,
                                     "//*[@id='puilceTable']/form/div/div[3]//span[@class='el-checkbox__input']")
        tool.locate(driver, target)
        target.click()

    @staticmethod
    def add_com(driver,kwargs):
        driver.find_element(By.XPATH, "//button//span[text()='添加企业']").click()
        # sleep(2)
        for t in kwargs['tbr_single']:
            driver.find_element(By.XPATH, "//input[@placeholder='请输入搜索名称']").send_keys(t)
            sleep(1)
            driver.find_element(By.XPATH, "//button//span[text()='查询']").click()
            sleep(1)
            driver.find_element(By.XPATH,
                                "//span[text()=' " + t + " ']/../../preceding-sibling::td//span[@class='el-checkbox__input']").click()

    @staticmethod
    def public_notice_content(driver):
        driver.switch_to.frame('selectedornoticeContent_ifr')
        driver.find_element(By.XPATH, "//body[@id='tinymce']/p").send_keys('公告内容:XXXXXXXXXXXXXXXXXXXXXX')
        driver.switch_to.default_content()

    @staticmethod
    def save(driver):
        """保存"""
        driver.find_element(By.XPATH, "//span[text()='保存']").click()
        sleep(3)

    @staticmethod
    def submit(driver):
        """提交"""
        driver.find_element(By.XPATH, "//span[text()='提交']").click()
        sleep(3)

    def add_single_source(self,driver,kwargs):
        self.select_bid(driver)
        self.add_com(driver,kwargs)
        self.public_notice_name(driver,kwargs)
        self.purchaser_name(driver)
        self.notice_start_end_time(driver,kwargs)
        self.purchaser_area(driver)
        # sleep(60)
        self.submit(driver)