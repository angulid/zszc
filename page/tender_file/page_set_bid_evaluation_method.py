from time import sleep

from selenium.webdriver.common.by import By

from common import tool


class PageSetBidEvaluationMethod:

    @staticmethod
    def comprehensive(driver):
        """综合评标法"""
        driver.find_element(By.XPATH, "//span[contains(text(),'评标办法')]/../following-sibling::div//input").click()
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='综合评分法']").click()
        sleep(1)

    @staticmethod
    def step_quit(driver):
        """取消"""
        for i in range(5):
            try:
                bts = driver.find_elements(By.XPATH, "//button/span[text()='取消']")
                tool.locate(driver, bts[0])
                bts[0].click()
                sleep(1)
            except:
                pass

    @staticmethod
    def zhpg(driver):
        """综合评估法"""
        driver.find_element(By.XPATH, "//span[contains(text(),'评标办法')]/../following-sibling::div//input").click()
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='综合评估法']").click()
        sleep(1)

    @staticmethod
    def lowest_toubiao(driver):
        """最低投标价法"""
        driver.find_element(By.XPATH, "//span[contains(text(),'评标办法')]/../following-sibling::div//input").click()
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='最低投标价法']").click()
        sleep(1)

    @staticmethod
    def lowest_pingbiao(driver):
        """最低评标价法"""
        driver.find_element(By.XPATH, "//span[contains(text(),'评标办法')]/../following-sibling::div//input").click()
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='最低评标价法']").click()
        sleep(1)

    @staticmethod
    def reviewer(driver):
        """资格审查方-采购人代表"""
        driver.find_element(By.XPATH, "//span[text()=' 采购人代表 ']/preceding-sibling::span").click()

    @staticmethod
    def juror(driver):
        """资格审查方-评审委员会"""
        driver.find_element(By.XPATH, "//span[text()=' 采购人代表 ']/preceding-sibling::span").click()

    @staticmethod
    def add_bid_evaluation_step(driver):
        """添加评审步骤"""
        target = driver.find_element(By.XPATH, "//button//span[text()=' 添加评审步骤 ']")
        tool.locate(driver, target)
        target.click()
        sleep(1)

    @staticmethod
    def qualifications(driver):
        """资质评审"""
        driver.find_element(By.XPATH,
                            "//label[contains(text(),'评审步骤名称')]/following-sibling::div//input").send_keys(
            '资质评审')
        driver.find_element(By.XPATH,
                            "//span[contains(text(),'是否资格评审项')]/../following-sibling::div//span[text()='是']").click()
        target = driver.find_element(By.XPATH, "//button//span[text()='添加评审项']")
        tool.locate(driver, target)
        target.click()

        target = driver.find_element(By.XPATH, "//span[text()=' 评分原则 ']")
        tool.locate(driver, target)

        driver.find_element(By.XPATH, "//input[@placeholder='请输入评审项名称']").send_keys('资格评审项A')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请输入评审标准']").send_keys('评审标准：XXX')
        target = driver.find_element(By.XPATH, "//span[text()='保存']")
        tool.locate(driver, target)
        target.click()
        sleep(2)

    @staticmethod
    def qualifications_sxf(driver):
        """资质评审"""
        driver.find_element(By.XPATH,
                            "//label[contains(text(),'评审步骤名称')]/following-sibling::div//input").send_keys(
            '资质评审')
        driver.find_element(By.XPATH, "//input[@placeholder='请选择所属信封']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//span[text()='第一信封']").click()

        target = driver.find_element(By.XPATH, "//button//span[text()='添加评审项']")
        tool.locate(driver, target)
        target.click()

        target = driver.find_element(By.XPATH, "//span[text()=' 评分原则 ']")
        tool.locate(driver, target)

        driver.find_element(By.XPATH, "//input[@placeholder='请输入评审项名称']").send_keys('资格评审项A')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请输入评审标准']").send_keys('评审标准：XXX')
        target = driver.find_element(By.XPATH, "//span[text()='保存']")
        tool.locate(driver, target)
        target.click()
        sleep(2)

    @staticmethod
    def scored_step(driver):
        """打分式评审"""
        # 哥哥节点
        target = driver.find_element(By.XPATH,"//label[contains(text(),'评审步骤名称')]/following-sibling::div//input")
        tool.locate(driver,target)
        target.send_keys('打分步骤')
        driver.find_element(By.XPATH, "//span[contains(text(),'打分式评审')]/preceding-sibling::span").click()

    @staticmethod
    def scored_step_sxf(driver):
        """打分式评审"""
        # 哥哥节点
        target = driver.find_element(By.XPATH, "//label[contains(text(),'评审步骤名称')]/following-sibling::div//input")
        tool.locate(driver, target)
        target.send_keys('打分步骤')
        driver.find_element(By.XPATH, "//span[contains(text(),'打分式评审')]/preceding-sibling::span").click()
        sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='请选择所属信封']").click()
        sleep(1)
        driver.find_elements(By.XPATH, "//span[text()='第一信封']")[1].click()
        sleep(1)


    @staticmethod
    def is_blind(driver):
        """是否暗标"""
        driver.find_element(By.XPATH,
                            "//span[contains(text(),'是否暗标')]/../following-sibling::div//span[text()='是']").click()

    @staticmethod
    def add_review_item(driver):
        """添加评审项"""
        target = driver.find_element(By.XPATH, "//button//span[text()='添加评审项']")
        tool.locate(driver, target)
        target.click()
        driver.find_element(By.XPATH, "//input[@placeholder='请输入评审项名称']").send_keys('评审项A')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请输入评审标准']").send_keys('评审标准：AAA')

    @staticmethod
    def scored_40(driver):
        driver.find_element(By.XPATH, "//span[contains(text(),'标准分')]/../following-sibling::div//input").send_keys(
            '40')
        driver.find_element(By.XPATH, "//td[4]//input").send_keys('10')
        driver.find_element(By.XPATH, "//td[5]//input").send_keys('40')
        target = driver.find_element(By.XPATH, "//span[text()='保存']")
        tool.locate(driver, target)
        target.click()
        sleep(2)

    @staticmethod
    def scored_100(driver):
        """打分式评审-100分"""
        # 哥哥节点
        driver.find_element(By.XPATH, "//span[contains(text(),'标准分')]/../following-sibling::div//input").send_keys(
            '100')
        driver.find_element(By.XPATH, "//td[4]//input").send_keys('20')
        driver.find_element(By.XPATH, "//td[5]//input").send_keys('100')
        target = driver.find_element(By.XPATH, "//span[text()='保存']")
        tool.locate(driver, target)
        target.click()
        sleep(2)

    @staticmethod
    def business_scored(driver):
        """商务评分"""
        # driver.find_element(By.XPATH, "//button//span[text()=' 添加评审步骤 ']").click()
        driver.find_element(By.XPATH,
                            "//label[contains(text(),'评审步骤名称')]/following-sibling::div//input").send_keys(
            '商务打分')
        # 哥哥节点
        driver.find_element(By.XPATH, "//span[contains(text(),'价格得分评审')]/preceding-sibling::span").click()
        driver.find_element(By.XPATH,
                            "//span[contains(text(),'标准分')]/../following-sibling::div//input").send_keys('60')
        driver.find_element(By.XPATH,
                            "//span[contains(text(),'选择报价')]/../following-sibling::div//input[@placeholder='请选择']").click()
        driver.find_element(By.XPATH, "//li//span[text()='报价列']").click()

        target = driver.find_element(By.XPATH,
                                     "//span[contains(text(),'计算方式')]/../following-sibling::div//input[@placeholder='请选择']")
        tool.locate(driver, target)
        target.click()
        driver.find_element(By.XPATH, "//li//span[text()='系统计算']").click()

        driver.find_element(By.XPATH,
                            "//span[contains(text(),' 计算公式')]/../following-sibling::div//input[@placeholder='请选择']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='最低报价']").click()
        # driver.find_element(By.XPATH, "//li//span[text()='次低报价']").click()
        # driver.find_element(By.XPATH, "//li//span[text()='平均报价']").click()
        # driver.find_element(By.XPATH, "//li//span[text()='最高报价']").click()

        driver.find_element(By.XPATH,
                            "//span[contains(text(),'报价得分计算公式')]/../following-sibling::div//input[@placeholder='请选择']").click()
        driver.find_element(By.XPATH, "//li//span[text()='低价优先法']").click()
        sleep(1)

        target = driver.find_element(By.XPATH, "//span[text()='保存']")
        tool.locate(driver, target)
        target.click()
        sleep(2)

    @staticmethod
    def business_scored_sxf(driver):
        """商务评分"""
        # driver.find_element(By.XPATH, "//button//span[text()=' 添加评审步骤 ']").click()
        driver.find_element(By.XPATH,
                            "//label[contains(text(),'评审步骤名称')]/following-sibling::div//input").send_keys(
            '商务打分')
        # 哥哥节点
        driver.find_element(By.XPATH, "//span[contains(text(),'价格得分评审')]/preceding-sibling::span").click()
        driver.find_element(By.XPATH,
                            "//span[contains(text(),'标准分')]/../following-sibling::div//input").send_keys('60')
        driver.find_element(By.XPATH,
                            "//span[contains(text(),'选择报价')]/../following-sibling::div//input[@placeholder='请选择']").click()
        driver.find_element(By.XPATH, "//li//span[text()='报价列']").click()

        # target = driver.find_element(By.XPATH,
        #                              "//span[contains(text(),'计算方式')]/../following-sibling::div//input[@placeholder='请选择']")
        # tool.locate(driver, target)
        # target.click()
        # driver.find_element(By.XPATH, "//li//span[text()='系统计算']").click()

        # driver.find_element(By.XPATH,
        #                     "//span[contains(text(),' 计算公式')]/../following-sibling::div//input[@placeholder='请选择']").click()
        # sleep(1)
        # driver.find_element(By.XPATH, "//li//span[text()='合理平均报价']").click()
        # driver.find_element(By.XPATH, "//li//span[text()='次低报价']").click()
        # driver.find_element(By.XPATH, "//li//span[text()='平均报价']").click()
        # driver.find_element(By.XPATH, "//li//span[text()='最高报价']").click()

        # driver.find_element(By.XPATH,
        #                     "//span[contains(text(),'报价得分计算公式')]/../following-sibling::div//input[@placeholder='请选择']").click()
        # driver.find_element(By.XPATH, "//li//span[text()='偏差率计算法']").click()
        # sleep(1)

        target = driver.find_element(By.XPATH, "//span[text()='保存']")
        tool.locate(driver, target)
        target.click()
        sleep(2)

    @staticmethod
    def score_rule(driver):
        """评分原则"""
        driver.find_element(By.XPATH, "//span[text()='计算所有评委评分。']/../preceding-sibling::span/span").click()

    @staticmethod
    def is_reject(driver):
        """是否否决"""
        driver.find_element(By.XPATH,
                            "//span[contains(text(),'是否否决')]/../following-sibling::div//span[text()='否']").click()

    @staticmethod
    def next_step(driver):
        """下一步"""
        driver.find_element(By.XPATH, "//span[text()=' 下一步 ']").click()
        sleep(5)

    def set_bid_method_lowest_toubiao(self,driver):
        """最低投标价法"""
        self.lowest_toubiao(driver)
        self.add_bid_evaluation_step(driver)
        self.qualifications(driver)
        self.add_bid_evaluation_step(driver)
        self.scored_step(driver)
        self.is_blind(driver)
        self.add_review_item(driver)
        self.scored_100(driver)
        self.next_step(driver)

    def set_bid_method_lowest_toubiao_reject(self,driver):
        """最低投标价法-否决"""
        self.lowest_toubiao(driver)
        self.score_rule(driver)
        self.add_bid_evaluation_step(driver)
        self.qualifications(driver)
        self.add_bid_evaluation_step(driver)
        self.scored_step(driver)
        self.is_reject(driver)
        self.is_blind(driver)
        self.add_review_item(driver)
        self.scored_100(driver)
        # sleep(600)
        self.next_step(driver)

    def set_bid_method_lowest_pingbiao(self,driver):
        """最低评标价法"""
        self.lowest_pingbiao(driver)
        self.score_rule(driver)
        self.add_bid_evaluation_step(driver)
        self.qualifications(driver)
        self.add_bid_evaluation_step(driver)
        self.scored_step(driver)
        self.is_reject(driver)
        self.is_blind(driver)
        self.add_review_item(driver)
        self.scored_40(driver)
        self.add_bid_evaluation_step(driver)
        self.business_scored(driver)
        self.next_step(driver)

    def set_bid_method_comprehensive(self,driver):
        """综合评标法"""
        self.comprehensive(driver)
        self.add_bid_evaluation_step(driver)
        self.qualifications(driver)
        self.add_bid_evaluation_step(driver)
        self.scored_step(driver)
        self.is_blind(driver)
        self.add_review_item(driver)
        self.scored_40(driver)
        self.add_bid_evaluation_step(driver)
        self.business_scored(driver)
        self.next_step(driver)

    def set_bid_method_zhpg(self,driver):
        """综合评估法"""
        self.zhpg(driver)
        self.add_bid_evaluation_step(driver)
        self.qualifications(driver)
        self.add_bid_evaluation_step(driver)
        self.scored_step(driver)
        self.is_blind(driver)
        self.add_review_item(driver)
        self.scored_40(driver)
        self.add_bid_evaluation_step(driver)
        self.business_scored(driver)
        self.next_step(driver)

    def set_bid_method_comprehensive_sxf(self,driver):
        """综合评标法"""
        self.comprehensive(driver)
        self.step_quit(driver)
        self.add_bid_evaluation_step(driver)
        self.qualifications_sxf(driver)
        self.add_bid_evaluation_step(driver)
        self.scored_step_sxf(driver)
        self.is_blind(driver)
        self.add_review_item(driver)
        self.scored_40(driver)
        self.add_bid_evaluation_step(driver)
        self.business_scored_sxf(driver)
        self.next_step(driver)
