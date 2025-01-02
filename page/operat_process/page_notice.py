from time import sleep

from selenium.webdriver.common.by import By

from common import tool


class PageNotice:
    """
    添加采购公告页面
    """

    @staticmethod
    def public_info(driver):
        """采购公告-公共填写字段
        开启地点、其他补充事项、采购人名称、采购人地址、采购人联系方式
        """
        target = driver.find_element(By.XPATH, "//input[@placeholder='请填写开启地点']")
        tool.locate(driver, target)
        target.send_keys('XXXX开启地点')

        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写其他补充事项']").send_keys('暂无其他补充事项')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写采购人名称']").send_keys('赵XX')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写采购人地址']").send_keys(
            '陕西省西安市雁塔区大慈恩寺')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写采购人联系方式']").send_keys('15788886666')

    @staticmethod
    def purchase_need(driver):
        """采购需求、合同履行期限、落实政府采购政策需满足的资格要求、本项目的特定资格要求"""
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写采购需求']").send_keys('XXXX采购需求')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写合同履行期限']").send_keys('1')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写落实政府采购政策需满足的资格要求']").send_keys('政府采购政策需满足的资格要求XXXX')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写本项目的特定资格要求']").send_keys(
            '本项目的特定资格要求XXX')

    @staticmethod
    def notice_name(driver,kwargs):
        """公告名称"""
        target = driver.find_element(By.XPATH, "//input[@placeholder='请填写公告名称']")
        tool.locate(driver,target)
        target.send_keys(kwargs['cg_bd_name'] + '-公告')

    @staticmethod
    def notice_start_end_time_1(driver,kwargs):
        """公告发布时间-公告结束时间"""
        driver.find_element(By.XPATH,
                            "//span[text()=' 公告发布时间-公告结束时间 ']/../following-sibling::div//input[@placeholder='开始时间']").send_keys(
            kwargs['start_date'])
        driver.find_element(By.XPATH,
                            "//span[text()=' 公告发布时间-公告结束时间 ']/../following-sibling::div//input[@placeholder='结束时间']").send_keys(
            kwargs['end_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[3]//span[contains(text(),' 确定')]").click()

    @staticmethod
    def notice_start_end_time_2(driver, kwargs):
        """公告发布/结束时间"""
        driver.find_element(By.XPATH,
                            "//span[text()=' 公告发布/结束时间 ']/../following-sibling::div//input[@placeholder='开始时间']").send_keys(
            kwargs['start_date'])
        driver.find_element(By.XPATH,
                            "//span[text()=' 公告发布/结束时间 ']/../following-sibling::div//input[@placeholder='结束时间']").send_keys(
            kwargs['end_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[2]//span[contains(text(),' 确定')]").click()

    @staticmethod
    def tender_file_get_time_1(driver,kwargs):
        """招标文件获取开始时间-招标文件获取截止时间"""
        driver.find_element(By.XPATH,
                            "//span[text()=' 招标文件获取开始时间-招标文件获取截止时间 ']/../following-sibling::div//input[@placeholder='开始时间']").send_keys(
            kwargs['start_date'])
        driver.find_element(By.XPATH,
                            "//span[text()=' 招标文件获取开始时间-招标文件获取截止时间 ']/../following-sibling::div//input[@placeholder='结束时间']").send_keys(
            kwargs['end_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[4]//span[contains(text(),' 确定')]").click()

    @staticmethod
    def tender_file_get_time_2(driver, kwargs):
        """招标文件获取开始时间、招标文件获取结束日期"""
        driver.find_element(By.XPATH,
                            "//span[text()=' 招标文件获取开始时间 ']/../following-sibling::div//input").send_keys(
            kwargs['start_date'])
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[3]//span[contains(text(),'确定')]").click()
        driver.find_element(By.XPATH,
                            "//span[text()=' 招标文件获取结束日期 ']/../following-sibling::div//input").send_keys(
            kwargs['end_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[4]//span[contains(text(),'确定')]").click()

    @staticmethod
    def gc_tender_file_get_time(driver, kwargs):
        """  资格预审文件（招标文件）获取开始日期 、  资格预审文件（招标文件）获取结束日期 """
        target = driver.find_element(By.XPATH,
                            "//span[text()=' 资格预审文件（招标文件）获取开始日期 ']/../following-sibling::div//input")
        tool.locate(driver,target)
        target.send_keys(kwargs['start_date'])
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[3]//span[contains(text(),'确定')]").click()
        driver.find_element(By.XPATH,
                            "//span[text()=' 资格预审文件（招标文件）获取结束日期 ']/../following-sibling::div//input").send_keys(
            kwargs['end_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[4]//span[contains(text(),'确定')]").click()

    @staticmethod
    def biz_price(driver):
        """ 标书售价（元）、 资料/图纸押金（元）  """
        driver.find_element(By.XPATH, "//input[@placeholder='请填写标书售价（元）']").send_keys('28')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写资料/图纸押金（元）']").send_keys('18')

    @staticmethod
    def open_time(driver,kwargs):
        """开标时间"""
        driver.find_element(By.XPATH,
                            "//span[text()=' 开标时间 ']/../following-sibling::div//input").send_keys(
            kwargs['end_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[9]//span[contains(text(),'确定')]").click()

    @staticmethod
    def gc_open_time(driver, kwargs):
        """ 投标文件（资格预审文件）递交截止时间 """
        driver.find_element(By.XPATH,
                            "//span[text()=' 投标文件（资格预审文件）递交截止时间 ']/../following-sibling::div//input").send_keys(
            kwargs['end_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[5]//span[contains(text(),'确定')]").click()

    @staticmethod
    def zb_info(driver):
        """ 招标代理机构 、 地址 、联系人、联系电话"""
        driver.find_element(By.XPATH, "//input[@placeholder='请填写招标代理机构']").send_keys('XX招标代理机构')
        driver.find_elements(By.XPATH, "//input[@placeholder='请填写地址']")[0].send_keys('招标人XX地址')
        driver.find_elements(By.XPATH, "//input[@placeholder='请填写地址']")[1].send_keys('招标代理机构XX地址')
        target = driver.find_elements(By.XPATH, "//input[@placeholder='请填写联系人']")[0]
        tool.locate(driver,target)
        target.send_keys('赵先生')
        driver.find_elements(By.XPATH, "//input[@placeholder='请填写联系人']")[1].send_keys('戴先生')
        driver.find_elements(By.XPATH, "//input[@placeholder='请填写电话']")[0].send_keys('15766228513')
        driver.find_elements(By.XPATH, "//input[@placeholder='请填写电话']")[1].send_keys('15766228514')

    @staticmethod
    def send_type(driver):
        """投标文件递交方法"""
        driver.find_element(By.XPATH, "//input[@placeholder='请选择投标文件递交方法']").send_keys('线上')
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='线上']").click()

    @staticmethod
    def get_type(driver):
        """招标文件获取方式"""
        driver.find_element(By.XPATH, "//input[@placeholder='请填写招标文件获取方式']").send_keys('官网获取')

    @staticmethod
    def select_host(driver,kwargs):
        driver.find_element(By.XPATH, "//input[@placeholder='请选择主持人姓名']").send_keys(kwargs['zcr'])
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='" + kwargs['zcr'] + "']").click()

    @staticmethod
    def select_bid(driver):
        """选择标段"""
        target = driver.find_element(By.XPATH,
                                     "//*[@id='puilceTable']/form/div/div[3]//span[@class='el-checkbox__input']")
        tool.locate(driver, target)
        target.click()

    @staticmethod
    def notice_publish(driver):
        driver.switch_to.frame('selectedornoticeContent_ifr')
        driver.find_element(By.XPATH, "//body[@id='tinymce']/p").send_keys('公告内容:XXXXXXXXXXXXXXXXXXXXXX')
        driver.switch_to.default_content()

    @staticmethod
    def day_time(driver):
        """上午开始时间、上午结束时间、下午开始时间、下午结束时间"""
        morning_start = driver.find_element(By.XPATH,
                                            "//span[text()=' 上午开始时间 ']/../following-sibling::div//input")
        tool.locate(driver,morning_start)
        morning_start.click()
        morning_start.clear()
        morning_start.send_keys('08:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[5]//button[text()='确定']").click()
        morning_end = driver.find_element(By.XPATH, "//span[text()=' 上午结束时间 ']/../following-sibling::div//input")
        morning_end.click()
        morning_end.clear()
        morning_end.send_keys('12:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[6]//button[text()='确定']").click()
        aft_start = driver.find_element(By.XPATH, "//span[text()=' 下午开始时间 ']/../following-sibling::div//input")
        aft_start.click()
        aft_start.clear()
        aft_start.send_keys('13:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[7]//button[text()='确定']").click()
        # 弟弟节点
        aft_start = driver.find_element(By.XPATH, "//span[text()=' 下午结束时间 ']/../following-sibling::div//input")
        aft_start.click()
        aft_start.clear()
        aft_start.send_keys('21:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[8]//button[text()='确定']").click()

    @staticmethod
    def send_end_time(driver,kwargs):
        """投标文件递交截止时间"""
        driver.find_element(By.XPATH,
                            "//span[text()=' 投标文件递交截止时间 ']/../following-sibling::div//input[@placeholder='请选择日期时间']").send_keys(
            kwargs['end_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//div[6]//span[contains(text(),' 确定')]").click()

    @staticmethod
    def doubt_phone(driver):
        """受理质疑电话"""
        driver.find_element(By.XPATH, "//input[@placeholder='请填写受理质疑电话']").send_keys('17866669999')

    @staticmethod
    def respond_area(driver):
        """响应文件提交地点"""
        driver.find_element(By.XPATH, "//input[@placeholder='请填写响应文件提交地点']").send_keys('响应地点')

    @staticmethod
    def jg_name(driver):
        """机关名称"""
        driver.find_element(By.XPATH, "//input[@placeholder='请填写审批、核准、备案机关名称']").send_keys('XXXX机关')

    @staticmethod
    def pw_id(driver):
        """批文名称及编号"""
        driver.find_element(By.XPATH, "//input[@placeholder='请填写批文名称及编号']").send_keys('113114115')

    @staticmethod
    def yz(driver):
        """业主"""
        driver.find_element(By.XPATH, "//input[@placeholder='请填写业主']").send_keys('夜XX')

    @staticmethod
    def notice_save(driver):
        """保存"""
        driver.find_element(By.XPATH, "//span[text()='保存']").click()
        sleep(5)

    @staticmethod
    def notice_submit(driver):
        """提交"""
        driver.find_element(By.XPATH, "//span[text()='提交']").click()
        sleep(5)


    def add_notice_save(self,driver,kwargs):
        """新增采购公告-保存"""
        self.select_host(driver,kwargs)
        self.notice_start_end_time_2(driver,kwargs)
        self.send_type(driver)
        self.select_bid(driver)
        self.notice_name(driver,kwargs)
        self.purchase_need(driver)
        self.tender_file_get_time_2(driver,kwargs)
        self.day_time(driver)
        self.get_type(driver)
        self.open_time(driver,kwargs)
        self.public_info(driver)
        self.notice_save(driver)

    def add_notice_submit(self, driver, kwargs):
        """新增采购公告-提交"""
        self.select_host(driver, kwargs)
        self.notice_start_end_time_2(driver, kwargs)
        self.send_type(driver)
        self.select_bid(driver)
        self.notice_name(driver, kwargs)
        self.purchase_need(driver)
        self.tender_file_get_time_2(driver, kwargs)
        self.day_time(driver)
        self.get_type(driver)
        self.open_time(driver, kwargs)
        self.public_info(driver)
        self.notice_submit(driver)

    def add_notice_submit_talks(self, driver, kwargs):
        """竞争性谈判-提交"""
        self.select_host(driver, kwargs)
        self.notice_start_end_time_2(driver, kwargs)
        self.send_type(driver)
        self.select_bid(driver)
        self.notice_name(driver, kwargs)
        self.purchase_need(driver)
        self.tender_file_get_time_2(driver, kwargs)
        self.day_time(driver)
        self.get_type(driver)
        self.respond_area(driver)
        self.open_time(driver, kwargs)
        self.public_info(driver)
        self.notice_submit(driver)

    def add_notice_invite_save(self,driver,kwargs):
        """新增邀请公告-保存"""
        self.select_bid(driver)
        self.notice_name(driver,kwargs)
        self.notice_start_end_time_2(driver,kwargs)
        self.tender_file_get_time_1(driver,kwargs)
        self.get_type(driver)
        self.send_type(driver)
        self.send_end_time(driver,kwargs)
        self.open_time(driver,kwargs)
        self.doubt_phone(driver)
        self.select_host(driver,kwargs)
        self.notice_publish(driver)
        self.notice_save(driver)

    def add_gc_zb_notice_submit(self,driver,kwargs):
        """工程-新增招标公告-保存"""
        self.select_host(driver, kwargs)
        self.notice_start_end_time_2(driver,kwargs)
        self.select_bid(driver)
        self.jg_name(driver)
        self.pw_id(driver)
        self.yz(driver)
        self.gc_tender_file_get_time(driver,kwargs)
        self.biz_price(driver)
        self.gc_open_time(driver,kwargs)
        self.zb_info(driver)
        self.notice_submit(driver)



