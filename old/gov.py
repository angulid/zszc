
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common import tool
from selenium.webdriver.common.by import By
from time import sleep

class Gov:
    @staticmethod
    def add_project(webdriver, kwargs):
        """新增政府采购项目"""
        print('进这个add_project')
        # print(kwargs)
        driver = webdriver
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[3]/div[1]/span[3]').click()
        # todo 登录后，如何切换至招标人角色，默认为招标人，点击会报错
        # driver.find_element(By.XPATH,"//*[text()='招标人']")
        locator = (By.XPATH, "//span[text()='项目管理']")
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
        driver.find_element(By.XPATH, "//span[text()='项目管理']").click()
        sleep(5)
        driver.find_element(By.XPATH, "//span[text()='政府采购']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//span[text()='政府采购项目']").click()
        sleep(3)
        driver.find_element(By.XPATH, "//*/span[text()=' 新增政府采购项目 ']").click()
        driver.find_element(By.XPATH,"//input[@placeholder='请填写采购办备案编号']").send_keys(kwargs['cg_id'])
        driver.find_element(By.XPATH,"//input[@placeholder='请填写采购项目名称']").send_keys(kwargs['cg_name'])
        sleep(1)
        driver.find_element(By.XPATH,"//input[@placeholder='请选择项目所属地区']").click()
        sleep(1)
        driver.find_element(By.XPATH,"//li//span[text()='河北省']").click()
        sleep(1)
        driver.find_element(By.XPATH,"//li//span[text()='石家庄市']").click()
        sleep(1)
        driver.find_element(By.XPATH,"//li//span[text()='长安区']").click()
        # driver.find_element(By.XPATH,"//span[text()='河北省 / 石家庄市 / 长安区']").click()
        # driver.find_element(By.XPATH,"//input[@placeholder='请选择交易中心']").send_keys('河北清苑阳光招采交易中心')
        driver.find_element(By.XPATH,"//input[@placeholder='请选择交易中心']").click()
        sleep(1)
        driver.find_element(By.XPATH,"//span[text()='河北省公共资源交易中心']").click()
        # driver.find_element(By.XPATH,"//input[@placeholder='请选择价款形式']").send_keys('金额')
        driver.find_element(By.XPATH,"//input[@placeholder='请选择价款形式']").click()
        # sleep(1)
        driver.find_element(By.XPATH,"//*/span[text()='金额']").click()
        driver.find_element(By.XPATH,"//input[@placeholder='请填写预算金额']").send_keys('150')
        driver.find_element(By.XPATH,"//input[@placeholder='请选择预算金额单位']").click()
        # sleep(1)
        driver.find_element(By.XPATH,"//*/span[text()='万元']").click()
        driver.find_element(By.XPATH,"//input[@placeholder='请选择项目所属行业']").send_keys('农、林、牧、渔业 / 农业')
        sleep(1)
        driver.find_element(By.XPATH,"//*/span[text()='农、林、牧、渔业 / 农业']").click()
        driver.find_element(By.XPATH,"//span[text()=' 集中采购 ']").click()
        driver.find_element(By.XPATH,"//span[text()=' 服务 ']").click()
        driver.find_element(By.XPATH,"//span[text()=' 采购单位 ']").click()

        # todo:拉动滚动条到指定位置
        # js = "var q=document.documentElement.scrollTop=10000"
        # driver.execute_script(js)
        target = driver.find_element(By.XPATH,"//input[@placeholder='请选择预算部门单位性质']")
        tool.locate(driver,target)
        # driver.execute_script("arguments[0].scrollIntoView();", target)

        driver.find_element(By.XPATH,"//input[@placeholder='请选择预算部门单位性质']").click()
        driver.find_element(By.XPATH,"//*//span[text()='国家机关']").click()

        driver.find_element(By.XPATH,"//input[@placeholder='请选择采购方式']").click()
        sleep(1)
        driver.find_element(By.XPATH,"//*/span[text()='"+kwargs['type_str']+"']").click()

        driver.find_element(By.XPATH,"//textarea[@placeholder='请填写采购内容']").send_keys(kwargs['cg_nr'])
        driver.find_element(By.XPATH,"//input[@placeholder='请填写采购人联系人']").send_keys('李XX')
        driver.find_element(By.XPATH,"//input[@placeholder='请填写联系人手机号码']").send_keys('14855559999')

        driver.find_element(By.XPATH,"//*/span[text()='选择']").click()
        driver.find_element(By.XPATH,'//*[@id="puilceTable"]/form/div/div[4]/div[2]/table/tbody/tr[1]/td[4]/div/div/span/button').click()

        # todo:拉动滚动条到指定位置
        # js = "var q=document.documentElement.scrollTop=10000"
        # driver.execute_script(js)
        target = driver.find_element(By.XPATH,"//span[text()='保存']")
        # driver.execute_script("arguments[0].scrollIntoView();", target)
        tool.locate(driver, target)

        driver.find_element(By.XPATH,"//*/span[text()=' 创建标段 ']").click()
        driver.find_element(By.XPATH,"//input[@placeholder='请填写标段（包）名称']").send_keys(kwargs['cg_bd_name'])
        driver.find_element(By.XPATH,"//textarea[@placeholder='请填写标段（包）描述']").send_keys(kwargs['cg_bd_name']+'的描述')
        driver.find_element(By.XPATH,"//input[@placeholder='请选择标段（包）分类']").send_keys('工程类 / 规划 / 国民经济和社会发展规划 / 总体规划')
        sleep(2)
        driver.find_element(By.XPATH,"//*/span[text()='工程类 / 规划 / 国民经济和社会发展规划 / 总体规划']").click()
        driver.find_element(By.XPATH,"//input[@placeholder='请填写投资概算（万元/人民币）']").send_keys('110')
        driver.find_element(By.XPATH,"//textarea[@placeholder='请填写投标人资格条件']").send_keys('资格条件A')

        # 创建标段-提交
        driver.find_element(By.XPATH,'//div[@id="customForm"]/div/button[2]/span[text()="提交"]').click()
        sleep(3)

        # 项目信息：保存/提交
        # driver.find_element(By.XPATH,"//span[text()='保存']").click()
        driver.find_element(By.XPATH,"//span[text()='提交']").click()

        time.sleep(5)
        driver.quit()


    @staticmethod
    def approve_pro(webdriver, kwargs):
        """管理员审批通过"""
        driver = webdriver
        name = kwargs['cg_name']
        # name = 'ZF-邀请招标-20241119-1731984338'
        driver.find_element(By.XPATH,"//*[@id='puilceTable']/form/div/div[4]/div[2]/table/tbody//span[contains(text(),'"+name+"')]/../../../*//span[text()=' 通过 ']").click()
        sleep(1)
        # driver.find_element(By.XPATH,"//span[contains(text(),'取消')]").click()
        driver.find_element(By.XPATH,"//div[@class='el-message-box']//span[contains(text(),'确定')]").click()
        sleep(4)
        driver.quit()

    @staticmethod
    def enter_process(webdriver, kwargs):
        """进入操作流程"""
        print('进入操作流程enter_process')
        driver = webdriver
        name = kwargs['cg_name']
        # 上边还有个地方需要修改，审核
        # name = 'ZF-邀请招标-20241119-1731984338'
        sleep(5)
        # todo 登录后，如何切换至招标人角色，默认为招标人，点击会报错
        # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[3]/div[1]/span[3]').click()
        # driver.find_element(By.XPATH,"//*[text()='招标人']")
        locator = (By.XPATH, "//span[text()='项目管理']")
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
        driver.find_element(By.XPATH, "//span[text()='项目管理']").click()
        sleep(2)
        driver.find_element(By.XPATH, "//span[text()='政府采购']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//span[text()='政府采购项目']").click()
        sleep(3)
        driver.find_element(By.XPATH,"//input[@placeholder='请填写项目名称']").send_keys(name)
        sleep(2)
        driver.find_element(By.XPATH,"//span[text()='搜索']").click()
        sleep(2)
        driver.find_element(By.XPATH,'//*[@id="puilceTable"]/form/div/div[4]//span[text()=" 进入操作流程 "]').click()

    @staticmethod
    def add_buy_file(webdriver,kwargs):
        """新增采购文件"""
        driver = webdriver
        sleep(3)
        driver.find_element(By.XPATH,'//div[text()=" 采购文件管理"]').click()
        sleep(2)
        driver.find_element(By.XPATH,'//span[text()="添加采购文件"]').click()
        driver.find_element(By.XPATH,
                            '//*[@id="puilceTable"]/form/div/div[3]//span[@class="el-checkbox__input"]').click()
        target = driver.find_element(By.XPATH, "//textarea[@placeholder='请填写缴费说明']")
        tool.locate(driver, target)
        target.send_keys('请在线下缴费')
        driver.find_element(By.XPATH, '//input[@placeholder="请选择日期时间"]').send_keys(kwargs['end_date']+' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, '//span[contains(text()," 确定")]').click()
        driver.find_element(By.XPATH, '//label[@for="ifUseCa"]/..//span[text()="否"]').click()
        driver.find_element(By.XPATH, "//span[text()=' 下一步 ']").click()
        sleep(5)

        driver.find_element(By.XPATH, '//input[@placeholder="请输入名称"]').send_keys('报价列')
        driver.find_element(By.XPATH, "//td[3]//input[@placeholder='请选择']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='数字含小数']").click()

        driver.find_element(By.XPATH, "//td[4]//input[@placeholder='请选择']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='报价']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//span[text()=' 下一步 ']").click()
        sleep(5)

    @staticmethod
    def lowest_method(webdriver):
        """最低评分方法"""
        driver = webdriver
        driver.find_element(By.XPATH, "//span[contains(text(),'评标办法')]/../following-sibling::div//input").click()
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='最低投标价法']").click()
        sleep(1)

        target = driver.find_element(By.XPATH, "//button//span[text()=' 添加评审步骤 ']")
        # driver.execute_script("arguments[0].scrollIntoView();", target)
        tool.locate(driver, target)
        target.click()

        driver.find_element(By.XPATH, "//label[contains(text(),'评审步骤名称')]/following-sibling::div//input").send_keys('资质评审')
        driver.find_element(By.XPATH, "//span[contains(text(),'是否资格评审项')]/../following-sibling::div//span[text()='是']").click()
        driver.find_element(By.XPATH, "//button//span[text()='添加评审项']").click()

        target = driver.find_element(By.XPATH, "//span[text()=' 评分原则 ']")
        # driver.execute_script("arguments[0].scrollIntoView();", target)
        tool.locate(driver, target)

        driver.find_element(By.XPATH, "//input[@placeholder='请输入评审项名称']").send_keys('资格评审项A')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请输入评审标准']").send_keys('评审标准：XXX')
        # driver.execute_script("arguments[0].scrollIntoView();", target)
        tool.locate(driver, target)
        driver.find_element(By.XPATH, "//span[text()='保存']").click()
        sleep(2)

        driver.find_element(By.XPATH, "//button//span[text()=' 添加评审步骤 ']").click()
        driver.find_element(By.XPATH,
                            "//label[contains(text(),'评审步骤名称')]/following-sibling::div//input").send_keys(
            '打分步骤')
        #哥哥节点
        driver.find_element(By.XPATH,"//span[contains(text(),'打分式评审')]/preceding-sibling::span").click()
        driver.find_element(By.XPATH,
                            "//span[contains(text(),'标准分')]/../following-sibling::div//input").send_keys('100')
        driver.find_element(By.XPATH, "//span[contains(text(),'是否暗标')]/../following-sibling::div//span[text()='是']").click()
        driver.find_element(By.XPATH, "//button//span[text()='添加评审项']").click()
        # driver.execute_script("arguments[0].scrollIntoView();", target)
        tool.locate(driver, target)
        driver.find_element(By.XPATH, "//input[@placeholder='请输入评审项名称']").send_keys('打分评审项A')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请输入评审标准']").send_keys('评审标准：AAA')
        driver.find_element(By.XPATH, "//td[4]//input").send_keys('20')
        driver.find_element(By.XPATH, "//td[5]//input").send_keys('100')
        # driver.execute_script("arguments[0].scrollIntoView();", target)
        tool.locate(driver, target)
        driver.find_element(By.XPATH, "//span[text()='保存']").click()
        sleep(2)
        driver.find_element(By.XPATH, "//span[text()=' 下一步 ']").click()
        sleep(5)

    @staticmethod
    def upload_file(webdriver,file):
        """上传采购文件"""
        driver = webdriver
        driver.find_element(By.XPATH, "//input[@type='file']").send_keys(file)
        sleep(5)
        driver.find_element(By.XPATH, "//span[text()=' 下一步 ']").click()
        sleep(3)
        driver.find_element(By.XPATH, "//span[text()=' 下一步 ']").click()
        sleep(3)

    @staticmethod
    def data_packet(webdriver):
        """生成数据包"""
        driver = webdriver
        driver.find_element(By.XPATH,"//button//span[text()=' 生成数据包 ']").click()
        sleep(7)
        driver.find_element(By.XPATH, "//button//span[text()=' 提交 ']").click()
        sleep(10)
        driver.quit()

    @staticmethod
    def add_pro_notice(webdriver, kwargs):
        """新增采购公告"""
        driver = webdriver
        name = kwargs['cg_bd_name']
        sleep(3)
        driver.find_element(By.XPATH, '//div[text()=" 采购公告"]').click()
        sleep(2)
        driver.find_element(By.XPATH, "//span[text()=' 添加公告 ']").click()
        sleep(5)
        driver.find_element(By.XPATH,"//input[@placeholder='请选择主持人姓名']").send_keys('招标人AAA')
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='招标人AAA']").click()
        driver.find_element(By.XPATH, '//input[@placeholder="开始时间"]').send_keys(kwargs['start_date']+' 00:00:00')
        driver.find_element(By.XPATH, '//input[@placeholder="结束时间"]').send_keys(kwargs['end_date']+' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, '//span[contains(text()," 确定")]').click()
        driver.find_element(By.XPATH, "//input[@placeholder='请选择投标文件递交方法']").send_keys('线上')
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='线上']").click()
        driver.find_element(By.XPATH, "//*[@id='puilceTable']/form/div/div[3]//span[@class='el-checkbox__input']").click()

        target = driver.find_element(By.XPATH, "//input[@placeholder='请填写公告名称']")
        tool.locate(driver,target)
        target.send_keys(name+'-公告')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写采购需求']").send_keys('XXXX采购需求')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写合同履行期限']").send_keys('1')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写落实政府采购政策需满足的资格要求']").send_keys('政府采购政策需满足的资格要求XXXX')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写本项目的特定资格要求']").send_keys(
            '本项目的特定资格要求XXX')
        target = driver.find_element(By.XPATH, "//span[text()=' 招标文件获取开始时间 ']")
        tool.locate(driver,target)

    @staticmethod
    def add_pro_notice_end(webdriver):
        """采购公告-公共填写字段"""
        driver = webdriver
        sleep(1)
        target = driver.find_element(By.XPATH, "//input[@placeholder='请填写开启地点']")
        tool.locate(driver,target)
        target.send_keys('XXXX开启地点')

        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写其他补充事项']").send_keys('暂无其他补充事项')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写采购人名称']").send_keys('赵XX')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写采购人地址']").send_keys('陕西省西安市雁塔区大慈恩寺')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写采购人联系方式']").send_keys('15788886666')
        driver.find_element(By.XPATH,"//span[text()='保存']").click()
        sleep(5)

    @staticmethod
    def  add_pro_notice_public(webdriver, kwargs):
        """采购公告-公共招标"""
        driver = webdriver
        # sleep(3)
        driver.find_element(By.XPATH,
                            "//span[text()=' 招标文件获取开始时间 ']/../following-sibling::div//input").send_keys(
            kwargs['start_date']+' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[3]//span[contains(text(),'确定')]").click()
        driver.find_element(By.XPATH,
                            "//span[text()=' 招标文件获取结束日期 ']/../following-sibling::div//input").send_keys(
            kwargs['end_date']+' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[4]//span[contains(text(),'确定')]").click()
        morning_start = driver.find_element(By.XPATH,"//span[text()=' 上午开始时间 ']/../following-sibling::div//input")
        morning_start.click()
        morning_start.clear()
        morning_start.send_keys('08:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[5]//button[text()='确定']").click()
        morning_end = driver.find_element(By.XPATH,"//span[text()=' 上午结束时间 ']/../following-sibling::div//input")
        morning_end.click()
        morning_end.clear()
        morning_end.send_keys('12:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[6]//button[text()='确定']").click()
        aft_start = driver.find_element(By.XPATH,"//span[text()=' 下午开始时间 ']/../following-sibling::div//input")
        aft_start.click()
        aft_start.clear()
        aft_start.send_keys('13:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[7]//button[text()='确定']").click()
        #弟弟节点
        aft_start = driver.find_element(By.XPATH,"//span[text()=' 下午结束时间 ']/../following-sibling::div//input")
        aft_start.click()
        aft_start.clear()
        aft_start.send_keys('21:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[8]//button[text()='确定']").click()

        driver.find_element(By.XPATH, "//input[@placeholder='请填写招标文件获取方式']").send_keys('官网获取')

        driver.find_element(By.XPATH,
                            "//span[text()=' 开标时间 ']/../following-sibling::div//input").send_keys(
            kwargs['end_date']+' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[9]//span[contains(text(),'确定')]").click()

    @staticmethod
    def add_pro_notice_talk(webdriver, kwargs):
        """采购公告-竞争性谈判、磋商、询价"""
        driver = webdriver
        # sleep(3)
        driver.find_element(By.XPATH,
                            "//span[text()=' 招标文件获取开始时间 ']/../following-sibling::div//input").send_keys(
            kwargs['start_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[3]//span[contains(text(),'确定')]").click()
        driver.find_element(By.XPATH,
                            "//span[text()=' 招标文件获取结束日期 ']/../following-sibling::div//input").send_keys(
            kwargs['end_date']+' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[4]//span[contains(text(),'确定')]").click()
        morning_start = driver.find_element(By.XPATH,
                                            "//span[text()=' 上午开始时间 ']/../following-sibling::div//input")
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
        driver.find_element(By.XPATH, "//input[@placeholder='请填写招标文件获取方式']").send_keys('官网获取')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写响应文件提交地点']").send_keys('提交地点：XXX')
        driver.find_element(By.XPATH,
                            "//span[text()=' 开标时间 ']/../following-sibling::div//input").send_keys(
            kwargs['end_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//body/div[9]//span[contains(text(),'确定')]").click()

    @staticmethod
    def bid_invitation(webdriver, kwargs):
        """邀请招标-投标邀请函"""
        driver = webdriver
        sleep(3)
        driver.find_element(By.XPATH, '//div[text()=" 投标邀请函"]').click()
        sleep(2)
        driver.find_element(By.XPATH, "//span[text()=' 添加投标邀请函 ']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//*[@id='puilceTable']/form/div/div[4]//span[text()=' 选择 ']").click()
        for t in kwargs['tbr']:
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
        # 招标文件获取/截止时间
        target = driver.find_element(By.XPATH, "//span[text()=' 招标文件获取/截止时间 ']")
        tool.locate(driver,target)
        driver.find_element(By.XPATH, '//input[@placeholder="开始时间"]').send_keys(kwargs['start_date']+' 00:00:00')
        driver.find_element(By.XPATH, '//input[@placeholder="结束时间"]').send_keys(kwargs['end_date']+' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, '//span[contains(text()," 确定")]').click()
        driver.find_element(By.XPATH, "//input[@placeholder='请填写招标联系人']").send_keys('雷先生')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写招标联系电话']").send_keys('15722223333')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写内容']").send_keys('邀请内容：XXXX')
        driver.find_element(By.XPATH,"//span[text()='提交']").click()
        sleep(3)
        driver.find_element(By.XPATH, "//*[@id='puilceTable']/form/div/div[4]/div[2]//span[text()=' 发布 ']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(),' 确定')]").click()
        sleep(5)

    @staticmethod
    def invitation_notice(webdriver, kwargs):
        """邀请公告"""
        driver = webdriver
        name = kwargs['cg_bd_name']
        sleep(3)
        driver.find_element(By.XPATH, '//div[text()=" 邀请公告"]').click()
        sleep(2)
        driver.find_element(By.XPATH, "//span[text()=' 添加公告 ']").click()
        sleep(2)
        driver.find_element(By.XPATH, "//*[@id='puilceTable']/form/div/div[3]//span[@class='el-checkbox__input']").click()
        target = driver.find_element(By.XPATH, "//input[@placeholder='请填写公告名称']")
        tool.locate(driver,target)
        target.send_keys(name+'-公告')

        driver.find_element(By.XPATH, "//span[text()=' 公告发布/结束时间 ']/../following-sibling::div//input[@placeholder='开始时间']").send_keys(kwargs['start_date']+' 00:00:00')
        driver.find_element(By.XPATH, "//span[text()=' 公告发布/结束时间 ']/../following-sibling::div//input[@placeholder='结束时间']").send_keys(kwargs['end_date']+' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[4]//span[contains(text(),' 确定')]").click()

        driver.find_element(By.XPATH, "//span[text()=' 招标文件获取/截止时间 ']/../following-sibling::div//input[@placeholder='开始时间']").send_keys(kwargs['start_date']+' 00:00:00')
        driver.find_element(By.XPATH, "//span[text()=' 招标文件获取/截止时间 ']/../following-sibling::div//input[@placeholder='结束时间']").send_keys(kwargs['end_date']+' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[5]//span[contains(text(),' 确定')]").click()
        driver.find_element(By.XPATH, "//input[@placeholder='请选择招标文件获取方法']").send_keys('线上')
        sleep(1)
        driver.find_element(By.XPATH,"//*[@id='customForm']/form/div/span[16]//span[text()='线上']").click()
        driver.find_element(By.XPATH, "//input[@placeholder='请选择投标文件递交方法']").send_keys('线上')
        sleep(1)
        driver.find_element(By.XPATH,"//*[@id='customForm']/form/div/span[17]//span[text()='线上']").click()
        driver.find_element(By.XPATH,
                            "//span[text()=' 投标文件递交截止时间 ']/../following-sibling::div//input[@placeholder='请选择日期时间']").send_keys(
            kwargs['end_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//div[6]//span[contains(text(),' 确定')]").click()

        driver.find_element(By.XPATH,
                            "//span[text()=' 开标时间 ']/../following-sibling::div//input[@placeholder='请选择日期时间']").send_keys(
            kwargs['end_date'] + ' 08:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//div[7]//span[contains(text(),' 确定')]").click()
        driver.find_element(By.XPATH, "//input[@placeholder='请填写受理质疑电话']").send_keys('17866669999')
        driver.find_element(By.XPATH,"//input[@placeholder='请选择主持人姓名']").send_keys('招标人AAA')
        sleep(1)
        driver.find_element(By.XPATH, "//li//span[text()='招标人AAA']").click()
        # 富文本
        driver.switch_to.frame('selectedornoticeContent_ifr')
        driver.find_element(By.XPATH, "//body[@id='tinymce']/p").send_keys('公告内容:XXXXXXXXXXXXXXXXXXXXXX')
        driver.switch_to.default_content()
        target = driver.find_element(By.XPATH, "//span[text()='保存']")
        # target = driver.find_element(By.XPATH, "//span[text()='提交']")
        tool.locate(driver,target)
        target.click()
        sleep(5)
        driver.quit()

    @staticmethod
    def single_source(webdriver,kwargs):
        """单一来源公示"""
        driver = webdriver
        name = kwargs['cg_bd_name']
        sleep(3)
        driver.find_element(By.XPATH, '//div[text()=" 单一来源公示"]').click()
        sleep(1)
        driver.find_element(By.XPATH, "//span[text()=' 添加 ']").click()
        sleep(1)
        driver.find_element(By.XPATH,
                            "//*[@id='puilceTable']/form/div/div[3]//span[@class='el-checkbox__input']").click()
        driver.find_element(By.XPATH, "//button//span[text()='添加企业']").click()
        # sleep(2)
        for t in kwargs['tbr']:
            driver.find_element(By.XPATH, "//input[@placeholder='请输入搜索名称']").send_keys(t)
            sleep(1)
            driver.find_element(By.XPATH, "//button//span[text()='查询']").click()
            sleep(1)
            driver.find_element(By.XPATH,
                                "//span[text()=' " + t + " ']/../../preceding-sibling::td//span[@class='el-checkbox__input']").click()
        target = driver.find_element(By.XPATH,"//input[@placeholder='请填写公告名称']")
        tool.locate(driver,target)
        target.send_keys(name+'-公示')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写采购人名称']").send_keys('刘某')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写拟采购的货物或服务的说明']").send_keys('拟采购的服务说明：XXXX')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写采用单一来源采购方式的原因及说明']").send_keys('原因及说明：XXXX')
        driver.find_element(By.XPATH,
                            "//span[text()=' 公告发布时间 ']/../following-sibling::div//input[@placeholder='请选择日期时间']").send_keys(
            kwargs['start_date'] + ' 08:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//div[3]//span[contains(text(),' 确定')]").click()

        driver.find_element(By.XPATH,
                            "//span[contains(text(),'公告结束时间')]/../following-sibling::div//input[@placeholder='请选择日期时间']").send_keys(
            kwargs['end_date'] + ' 08:00:00')
        sleep(1)
        driver.find_element(By.XPATH, "//div[4]//span[contains(text(),' 确定')]").click()
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写其他补充事宜']").send_keys(
            '补充事宜：XXXX')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写采购人地址']").send_keys('西藏自治区拉萨市区西北的玛布日山')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写采购人联系方式']").send_keys('15866664444')
        target = driver.find_element(By.XPATH, "//input[@placeholder='请填写财政部门名称']")
        tool.locate(driver,target)
        target.send_keys('XX财政部门')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写财政部门地址']").send_keys('河北省石家庄市桥西区泰华街48号')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写财政部门联系方式']").send_keys('15866665555')
        # driver.find_element(By.XPATH, "//span[text()='保存']").click()
        driver.find_element(By.XPATH, "//span[text()='提交']").click()
        sleep(3)

    @staticmethod
    def bid_invitation_single(webdriver, kwargs):
        """单一来源采购-投标邀请函"""
        driver = webdriver
        tbr = ['tbr1']
        sleep(3)
        driver.find_element(By.XPATH, '//div[text()=" 投标邀请函"]').click()
        sleep(1)
        driver.find_element(By.XPATH, "//span[text()=' 添加投标邀请函 ']").click()
        driver.find_element(By.XPATH, "//*[@id='puilceTable']/form/div/div[4]//span[text()=' 选择 ']").click()
        for t in tbr:
            sleep(1)
            driver.find_element(By.XPATH, "//button//span[text()='添加企业']").click()
            sleep(1)
            qy_name = driver.find_element(By.XPATH, "//input[@placeholder='请输入企业名称']")
            qy_name.clear()
            qy_name.send_keys(t)
            driver.find_element(By.XPATH, "//button//span[text()='查询']").click()
            sleep(1)
            driver.find_element(By.XPATH,
                                "//span[text()=' " + t + " ']/../../preceding-sibling::td//span[@class='el-checkbox__input']").click()
            driver.find_element(By.XPATH, "//button//span[text()='确定']").click()
        # 招标文件获取/截止时间
        target = driver.find_element(By.XPATH, "//span[text()=' 招标文件获取/截止时间 ']")
        tool.locate(driver, target)
        driver.find_element(By.XPATH, '//input[@placeholder="开始时间"]').send_keys(kwargs['start_date'] + ' 00:00:00')
        driver.find_element(By.XPATH, '//input[@placeholder="结束时间"]').send_keys(kwargs['end_date'] + ' 00:00:00')
        sleep(1)
        driver.find_element(By.XPATH, '//span[contains(text()," 确定")]').click()
        driver.find_element(By.XPATH, "//input[@placeholder='请填写招标联系人']").send_keys('雷先生')
        driver.find_element(By.XPATH, "//input[@placeholder='请填写招标联系电话']").send_keys('15722223333')
        driver.find_element(By.XPATH, "//textarea[@placeholder='请填写内容']").send_keys('邀请内容：XXXX')
        driver.find_element(By.XPATH, "//span[text()='提交']").click()
        sleep(3)
        driver.find_element(By.XPATH, "//*[@id='puilceTable']/form/div/div[4]/div[2]//span[text()=' 发布 ']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(),' 确定')]").click()
        sleep(5)
