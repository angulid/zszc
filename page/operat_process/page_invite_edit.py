from time import sleep

from selenium.webdriver.common.by import By

from common import tool


class PageInviteEdit:
    """
    投标邀请函页面
    """
    @staticmethod
    def select_bid(driver):
        driver.find_element(By.XPATH, "//*[@id='puilceTable']/form/div/div[4]//span[text()=' 选择 ']").click()

    @staticmethod
    def add_tbr(driver,kwargs):
        if kwargs['cg_type'] in ['单一来源采购']:
            tbr = kwargs['tbr_single']
        else:
            tbr = kwargs['tbr']
        for t in tbr:
            sleep(1)
            driver.find_element(By.XPATH, "//button//span[text()='添加企业']").click()
            sleep(1)
            qy_name = driver.find_element(By.XPATH, "//input[@placeholder='请输入企业名称']")
            qy_name.clear()
            qy_name.send_keys(t)
            driver.find_element(By.XPATH, "//button//span[text()='查询']").click()
            sleep(1)
            driver.find_element(By.XPATH, "//span[text()=' "+t+" ']/../../preceding-sibling::td//span[@class='el-checkbox__input']").click()
            driver.find_element(By.XPATH, "//button//span[text()='确定']").click()


    @staticmethod
    def tender_file_get_time(driver,kwargs):
        target = driver.find_element(By.XPATH, "//span[text()=' 招标文件获取/截止时间 ']")
        tool.locate(driver, target)
        driver.find_element(By.XPATH, '//input[@placeholder="开始时间"]').send_keys(kwargs['start_date'])
        driver.find_element(By.XPATH, '//input[@placeholder="结束时间"]').send_keys(kwargs['end_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, '//span[contains(text()," 确定")]').click()

    @staticmethod
    def contact_info(driver):
        driver.find_element(By.XPATH, "//input[@placeholder='请填写招标联系人']").send_keys('雷先生')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写招标联系电话']").send_keys('15722223333')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写内容']").send_keys('邀请内容：XXXX')

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

    @staticmethod
    def publish(driver):
        driver.find_element(By.XPATH, "//*[@id='puilceTable']/form/div/div[4]/div[2]//span[text()=' 发布 ']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(),' 确定')]").click()
        sleep(4)


    def add_letter(self,driver,kwargs):
        self.select_bid(driver)
        self.add_tbr(driver,kwargs)
        self.tender_file_get_time(driver,kwargs)
        self.contact_info(driver)
        self.submit(driver)
        self.publish(driver)

