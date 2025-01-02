from time import sleep

from selenium.webdriver import ActionChains as action
from selenium.webdriver.common.by import By

from common import tool
from base.base_page import BasePage


class PageProEdit(BasePage):

    """项目信息编辑页"""
    @staticmethod
    def pro_id(driver,kwargs):
        """采购计划编号、采购项目名称"""
        driver.find_element(By.XPATH, "//input[@placeholder='请填写采购办备案编号']").send_keys(kwargs['cg_id'])
        driver.find_element(By.XPATH, "//input[@placeholder='请填写采购项目名称']").send_keys(kwargs['cg_name'])

    @staticmethod
    def pro_name(driver, kwargs):
        """项目名称"""
        driver.find_element(By.XPATH, "//input[@placeholder='请填写项目名称']").send_keys(kwargs['cg_name'])

    @staticmethod
    def base_info_area(driver):
        """项目所属地区"""
        driver.find_element(By.XPATH, "//input[@placeholder='请选择项目所属地区']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='河北省']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='石家庄市']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='长安区']").click()

    @staticmethod
    def base_info_trading_center(driver,kwargs):
        """
        交易中心
        """
        driver.find_element(By.XPATH, "//input[@placeholder='请选择交易中心']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//span[text()='"+kwargs['jyzx']+"']").click()

    @staticmethod
    def base_info_price_type(driver):
        """
        价款形式
        """
        driver.find_element(By.XPATH, "//input[@placeholder='请选择价款形式']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//*/span[text()='金额']").click()

    @staticmethod
    def base_info_price(driver):
        """预算金额、预算金额单位"""
        driver.find_element(By.XPATH, "//input[@placeholder='请填写预算金额']").send_keys('300')
        driver.find_element(By.XPATH, "//input[@placeholder='请选择预算金额单位']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//*/span[text()='万元']").click()

    @staticmethod
    def base_info_price_gc(driver):
        """工程：预算金额、预算金额单位"""
        driver.find_element(By.XPATH, "//input[@placeholder='请填写预算金额（人民币）']").send_keys('300')
        driver.find_element(By.XPATH, "//input[@placeholder='请选择预算金额单位']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//*/span[text()='万元']").click()

    @staticmethod
    def base_info_sector(driver):
        """项目所属行业"""
        driver.find_element(By.XPATH, "//input[@placeholder='请选择项目所属行业']").send_keys('农、林、牧、渔业 / 农业')
        sleep(1)
        driver.find_element(By.XPATH, "//*/span[text()='农、林、牧、渔业 / 农业']").click()

    @staticmethod
    def base_info_sector_gc(driver):
        """工程：项目所属行业"""
        driver.find_element(By.XPATH, "//input[@placeholder='请选择项目行业']").send_keys('农、林、牧、渔业 / 农业')
        sleep(1)
        driver.find_element(By.XPATH, "//*/span[text()='农、林、牧、渔业 / 农业']").click()

    @staticmethod
    def gc_pro_sort(driver):
        """工程：招标项目分类"""
        driver.find_element(By.XPATH, "//input[@placeholder='请选择招标项目分类']").send_keys('工程类 / 规划')
        sleep(1)
        driver.find_element(By.XPATH, "//*/span[text()='工程类 / 规划']").click()

    @staticmethod
    def pro_sector_type(driver):
        """行业类型"""
        driver.find_element(By.XPATH, "//input[@placeholder='请选择行业类型']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//*/span[text()='市政']").click()

    @staticmethod
    def base_info_organization_mode(driver):
        """交易组织形式"""
        driver.find_element(By.XPATH, "//span[text()=' 分散采购 ']").click()

    @staticmethod
    def base_info_pro_type(driver):
        """采购项目类型"""
        driver.find_element(By.XPATH, "//span[text()=' 服务 ']").click()

    @staticmethod
    def base_info_organization_type(driver):
        """预算部门单位性质"""
        driver.find_element(By.XPATH, "//span[text()=' 采购单位 ']").click()
        target = driver.find_element(By.XPATH, "//input[@placeholder='请选择预算部门单位性质']")
        tool.locate(driver, target)

        driver.find_element(By.XPATH, "//input[@placeholder='请选择预算部门单位性质']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//*//span[text()='国家机关']").click()


    @staticmethod
    def base_info_purchase_info(driver,kwargs):
        """采购方式、采购内容、采购人联系人、 联系人手机号码"""
        target = driver.find_element(By.XPATH, "//input[@placeholder='请选择采购方式']")
        tool.locate(driver,target)
        target.click()
        sleep(1)
        driver.find_element(By.XPATH, "//*/span[text()='" + kwargs['cg_type'] + "']").click()
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写采购内容']").send_keys('采购内容XXXXX')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写采购人联系人']").send_keys('李XX')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写联系人手机号码']").send_keys('14855559999')

    @staticmethod
    def gc_purchase_info(driver, kwargs):
        """招标方式"""
        cg_type = kwargs['cg_type']
        if cg_type == '邀请招标':
            driver.find_element(By.XPATH, "//span[text()=' 邀请招标 ']/preceding-sibling::span/span").click()
        else:
            pass

    @staticmethod
    def base_info_monitor(driver):
        """项目监督人信息"""
        driver.find_element(By.XPATH, "//*/span[text()='选择']").click()
        driver.find_element(By.XPATH,
                            '//*[@id="puilceTable"]/form/div/div[4]/div[2]/table/tbody/tr[1]/td[4]/div/div/span/button').click()

    @staticmethod
    def gc_monitor(driver):
        """gc-项目监督人信息"""
        driver.find_element(By.XPATH, "//*[@id='customForm']/form/div/span[23]//span[text()='选择']").click()
        driver.find_element(By.XPATH,
                            '//*[@id="puilceTable"]/form/div/div[4]/div[2]/table/tbody/tr[1]/td[4]/div/div/span/button').click()

    @staticmethod
    def pro_monitor_dept(driver):
        """监督部门"""
        target = driver.find_element(By.XPATH, "//input[@placeholder='请选择监督部门']")
        tool.locate(driver,target)
        target.send_keys('发展改革委')
        sleep(1)
        driver.find_element(By.XPATH, "//*//span[text()='发展改革委']").click()
        # action(driver).click(target)

    @staticmethod
    def base_info_subject_property(driver):
        """投资主体性质"""
        driver.find_element(By.XPATH, "//*/span[text()=' 财政支付 ']").click()

    @staticmethod
    def pro_address(driver):
        """项目地址"""
        driver.find_element(By.XPATH, "//input[@placeholder='请填写项目地址']").send_keys('项目地址XXX')

    @staticmethod
    def pro_legal_person(driver):
        """项目法定代表人"""
        driver.find_element(By.XPATH, "//input[@placeholder='请填写项目法定代表人']").send_keys('法XX')

    @staticmethod
    def pro_size(driver):
        """项目规模"""
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写项目规模']").send_keys('项目规模:SSS')

    @staticmethod
    def pro_funds_source(driver):
        """资金来源-出资比例"""
        driver.find_element(By.XPATH,"//span[text()='政府 ']/preceding-sibling::span/span").click()

    @staticmethod
    def tender_willing(driver):
        """自愿招标"""
        ele = driver.find_element(By.XPATH, "//span[text()=' 自愿招标 ']/preceding-sibling::span/span")
        action(driver).click(on_element=ele).perform()
        sleep(1)

    @staticmethod
    def tender_legally(driver):
        """依法招标"""
        ele = driver.find_element(By.XPATH, "//span[text()=' 依法招标 ']/preceding-sibling::span/span")
        action(driver).click(on_element=ele).perform()
        sleep(1)

    # @staticmethod
    # def pro_director(driver):
    #     """招标人项目负责人"""
    #     driver.find_element(By.XPATH, "//input[@placeholder='请填写招标人项目负责人']").send_keys('付XX')

    @staticmethod
    def pro_director(driver):
        """招标人项目负责人"""
        driver.find_element(By.XPATH, "//input[@placeholder='请填写招标人项目负责人']").send_keys('付XX')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写负责人联系电话']").send_keys('15788889999')

    @staticmethod
    def pro_range(driver):
        """招标内容与范围及招标方案说明"""
        target = driver.find_element(By.XPATH, "//textarea[@placeholder='请填写 招标内容与范围及招标方案说明']")
        tool.locate(driver,target)
        target.send_keys('招标内容与范围及招标方案说明')

    @staticmethod
    def plan_time(driver,kwargs):
        """交通-计划开工时间、交通-计划交工时间、交通-项目类别、交通-技术等级、交通-项目里程（公里）、 交通-工程预算（万元）"""
        driver.find_element(By.XPATH,
                            "//span[text()=' 交通-计划开工时间 ']/../following-sibling::div//input").send_keys(
            kwargs['start_date'])
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[5]//span[contains(text(),'确定')]").click()
        driver.find_element(By.XPATH,
                            "//span[text()=' 交通-计划交工时间 ']/../following-sibling::div//input").send_keys(
            kwargs['end_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[6]//span[contains(text(),'确定')]").click()
        driver.find_element(By.XPATH, "//input[@placeholder='请选择交通-项目类别']").click()
        sleep(1)
        driver.find_elements(By.XPATH, "//span[text()='公路']")[1].click()
        driver.find_element(By.XPATH, "//input[@placeholder='请选择交通-技术等级']").click()
        sleep(1)
        driver.find_elements(By.XPATH, "//span[text()='高速公路']")[0].click()
        driver.find_element(By.XPATH, "//input[@placeholder='请填写交通-项目里程（公里）']").send_keys('3000')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写交通-工程预算（万元）']").send_keys('288')

    @staticmethod
    def team_member(driver):
        """招标小组成员"""
        driver.find_element(By.XPATH,"//span[text()='添加成员']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='请填写姓名']").send_keys('组二林')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写手机号']").send_keys('15766228513')
        driver.find_element(By.XPATH, "//input[@placeholder='请选择职称']").click()
        sleep(1)
        driver.find_elements(By.XPATH,"//span[text()='教授']")[1].click()
        driver.find_element(By.XPATH, "//input[@placeholder='请选择职称等级']").click()
        sleep(1)
        driver.find_elements(By.XPATH, "//span[text()='中级']")[1].click()
        driver.find_element(By.XPATH, "//*[@id='puilceTable']/form/div/div[3]//span[@class='el-switch__core']").click()
        sleep(1)

    @staticmethod
    def approve_dept(driver):
        """审核单位"""
        driver.find_element(By.XPATH, "//input[@placeholder='请选择审核单位']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//span[text()='交通']").click()
        driver.find_element(By.XPATH, "//input[@placeholder='请先选择审核单位']").send_keys('XXXX审核部门')

    @staticmethod
    def base_info_save(driver):
        """保存"""
        target = driver.find_element(By.XPATH, "//span[text()='保存']")
        tool.locate(driver, target)
        driver.find_element(By.XPATH,"//span[text()='保存']").click()
        sleep(2)

    @staticmethod
    def base_info_submit(driver):
        """提交"""
        target = driver.find_element(By.XPATH, "//span[text()='保存']")
        tool.locate(driver, target)
        driver.find_element(By.XPATH, "//span[text()='提交']").click()
        sleep(3)


    @staticmethod
    def create_bid(driver,kwargs):
        """
        创建标段
        :param webdriver:driver
        :param kwargs: bid_num-标段数量，cg_bd_name-标段名称
        :return:
        """
        for n in range(kwargs['bid_num']):
            cg_bd_name = kwargs['cg_bd_name'] + str(n+1)
            driver.find_element(By.XPATH, "//*/span[text()=' 创建标段 ']").click()
            bid_name = driver.find_element(By.XPATH, "//input[@placeholder='请填写标段（包）名称']")
            bid_name.clear()
            bid_name.send_keys(cg_bd_name)
            driver.find_element(By.XPATH, "//textarea[@placeholder='请填写标段（包）描述']").send_keys(
                kwargs['cg_bd_name'] + '的描述')
            driver.find_element(By.XPATH, "//input[@placeholder='请选择标段（包）分类']").send_keys(kwargs['bdhy'])
            sleep(2)
            driver.find_element(By.XPATH, "//*/span[text()='" + kwargs['bdhy'] + "']").click()
            driver.find_element(By.XPATH, "//input[@placeholder='请填写投资概算（万元/人民币）']").send_keys('10')
            driver.find_element(By.XPATH, "//textarea[@placeholder='请填写投标人资格条件']").send_keys('资格条件A')

            driver.find_element(By.XPATH, '//div[@id="customForm"]/div/button[2]/span[text()="提交"]').click()
            sleep(3)

    @staticmethod
    def select_pro(driver):
        """选择工程项目"""
        driver.find_element(By.XPATH, "//*[@id='customForm']/form/div/span[2]//span[text()='选择']").click()
        sleep(2)

    @staticmethod
    def query_gc_pro(driver,kwargs):
        """查询指定工程项目"""
        cg_name = kwargs['cg_name']
        driver.find_element(By.XPATH, "//input[@placeholder='请输入项目名称']").send_keys(cg_name)
        driver.find_element(By.XPATH, "//button//span[text()='查询']").click()
        sleep(1)
        driver.find_element(By.XPATH,
                            "//*[@id='puilceTable']/form/div/div[4]/div[2]/table/tbody/tr//span[text()=' "+cg_name+" ']/../../..//span[text()=' 选择 ']").click()
        # driver.find_element(By.XPATH, "//button//span[text()='确定']").click()

    def add_gov_pro_input_info(self,driver,kwargs):
        self.pro_id(driver, kwargs)
        self.base_info_area(driver)
        self.base_info_trading_center(driver,kwargs)
        self.base_info_price_type(driver)
        self.base_info_price(driver)
        self.base_info_sector(driver)
        self.base_info_organization_mode(driver)
        self.base_info_pro_type(driver)
        self.base_info_organization_type(driver)
        self.base_info_purchase_info(driver, kwargs)
        self.base_info_monitor(driver)
        self.create_bid(driver, kwargs)

    def add_gov_pro_save(self,driver,kwargs):
        self.add_gov_pro_input_info(driver,kwargs)
        self.base_info_save(driver)
        self.driver_quit(driver)

    def add_gov_pro_submit(self,driver,kwargs):
        self.add_gov_pro_input_info(driver,kwargs)
        self.base_info_submit(driver)
        self.driver_quit(driver)

    def add_com_pro_input_info(self,driver,kwargs):
        self.pro_id(driver, kwargs)
        self.base_info_area(driver)
        self.base_info_price(driver)
        self.base_info_sector(driver)
        self.base_info_organization_mode(driver)
        self.base_info_pro_type(driver)
        self.base_info_subject_property(driver)
        self.base_info_purchase_info(driver, kwargs)
        self.base_info_monitor(driver)
        self.create_bid(driver, kwargs)

    def add_com_pro_save(self,driver,kwargs):
        self.add_com_pro_input_info(driver,kwargs)
        self.base_info_save(driver)
        self.driver_quit(driver)

    def add_com_pro_submit(self,driver,kwargs):
        self.add_com_pro_input_info(driver,kwargs)
        self.base_info_submit(driver)
        self.driver_quit(driver)

    def add_gc_pro(self,driver,kwargs):
        self.pro_name(driver,kwargs)
        self.base_info_area(driver)
        self.base_info_price_gc(driver)
        self.pro_address(driver)
        self.pro_legal_person(driver)
        self.base_info_sector_gc(driver)
        self.pro_sector_type(driver)
        self.pro_monitor_dept(driver)
        self.tender_willing(driver)
        self.pro_size(driver)
        self.pro_funds_source(driver)
        self.pro_director(driver)

    def add_gc_biz_pro(self,driver,kwargs):
        self.select_pro(driver)
        self.query_gc_pro(driver,kwargs)
        self.base_info_trading_center(driver,kwargs)
        self.gc_pro_sort(driver)
        self.gc_purchase_info(driver,kwargs)
        self.pro_range(driver)
        self.team_member(driver)
        self.gc_monitor(driver)
        self.approve_dept(driver)
        self.create_bid(driver,kwargs)

    def add_gc_biz_pro_sxf(self,driver,kwargs):
        self.select_pro(driver)
        self.query_gc_pro(driver,kwargs)
        self.base_info_trading_center(driver,kwargs)
        self.gc_pro_sort(driver)
        self.gc_purchase_info(driver,kwargs)
        self.pro_range(driver)
        self.plan_time(driver,kwargs)
        self.team_member(driver)
        self.gc_monitor(driver)
        self.approve_dept(driver)
        self.create_bid(driver,kwargs)

    def add_gc_pro_save(self,driver,kwargs):
        self.add_gc_pro(driver,kwargs)
        self.base_info_save(driver)
        self.driver_quit(driver)

    def add_gc_pro_submit(self,driver,kwargs):
        self.add_gc_pro(driver,kwargs)
        self.base_info_submit(driver)
        self.driver_quit(driver)

    def add_gc_biz_submit(self,driver,kwargs):
        self.add_gc_biz_pro(driver,kwargs)
        self.base_info_submit(driver)
        self.driver_quit(driver)

    def add_gc_biz_sxf_submit(self,driver,kwargs):
        self.add_gc_biz_pro_sxf(driver,kwargs)
        self.base_info_submit(driver)
        self.driver_quit(driver)




