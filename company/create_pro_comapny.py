from time import sleep

from base.page_approve import PageApprove
from page.page_pro_edit import PageProEdit
from page.operat_process.page_invite_edit import PageInviteEdit
from base.page_login import Login
from page.operat_process.page_notice import PageNotice
from page.operat_process.page_notice_invite import PageNoticeInvite
from page.page_operat_process import PageOperatProcess
from page.page_pro_manager import ProjectManager
from page.operat_process.page_single import PageSingle
from page.tender_file.page_bid_open_table import PageBidOpenTable
from page.tender_file.page_create_data_packet import PageCreateDataPacket
from page.tender_file.page_set_base_info import PageSetBaseInfo
from page.tender_file.page_set_bid_evaluation_method import PageSetBidEvaluationMethod
from page.tender_file.page_upload_bid_file import PageUploadBidFile
from page.tender_file.page_upload_other_file import PageUploadOtherFile

class CreateComPro:
    def __init__(self):
        self.pm = ProjectManager()
        self.ppe = PageProEdit()
        self.pa = PageApprove()
        self.pop = PageOperatProcess()
        self.psbi = PageSetBaseInfo()
        self.pbot = PageBidOpenTable()
        self.psbem = PageSetBidEvaluationMethod()
        self.pubf = PageUploadBidFile()
        self.puof = PageUploadOtherFile()
        self.pcdp = PageCreateDataPacket()
        self.pn = PageNotice()
        self.pni = PageNoticeInvite()
        self.pie = PageInviteEdit()
        self.ps = PageSingle()

    def login_zbr(self):
        """招标人登录"""
        login = Login()
        driver = login.login_trade_sh_zbr()
        return driver

    def login_approve(self):
        """审批人登录"""
        login = Login()
        driver = login.login_trade_sh_approve()
        return driver

    def pro_create(self,gov_pro):
        """项目新建"""
        driver = self.login_zbr()
        self.pm.enter_company_pro_page(driver)
        self.ppe.add_com_pro_submit(driver, gov_pro)

    def approve(self,gov_pro):
        """审批"""
        driver = self.login_approve()
        self.pa.approve_pro(driver, gov_pro)

    def pro_add_buy_file_zonghe(self,gov_pro):
        """采购文件-综合评分法"""
        driver = self.login_zbr()
        self.pm.enter_company_pro_process(driver, gov_pro)
        self.pop.add_purchase_file(driver)
        self.psbi.com_set_base_info(driver, gov_pro)
        self.pbot.set_bid_open_table(driver)
        self.psbem.set_bid_method_comprehensive(driver)
        self.pubf.upload_bid_file(driver, gov_pro)
        self.puof.next_step(driver)
        self.pcdp.data_packet(driver)
        sleep(5)

    def pro_add_buy_file_lowest_toubiao(self,gov_pro):
        """采购文件-最低投标价法"""
        driver = self.login_zbr()
        self.pm.enter_company_pro_process(driver, gov_pro)
        self.pop.add_purchase_file(driver)
        self.psbi.com_set_base_info(driver, gov_pro)
        self.pbot.set_bid_open_table(driver)
        self.psbem.set_bid_method_lowest_toubiao(driver)
        self.pubf.upload_bid_file(driver, gov_pro)
        self.puof.next_step(driver)
        self.pcdp.data_packet(driver)
        sleep(5)

    def pro_add_buy_file_lowest_toubiao_reject(self,gov_pro):
        """采购文件-最低投标价法"""
        driver = self.login_zbr()
        self.pm.enter_company_pro_process(driver, gov_pro)
        self.pop.add_purchase_file(driver)
        self.psbi.com_set_base_info(driver, gov_pro)
        self.pbot.set_bid_open_table(driver)
        self.psbem.set_bid_method_lowest_toubiao_reject(driver)
        self.pubf.upload_bid_file(driver, gov_pro)
        self.puof.next_step(driver)
        self.pcdp.data_packet(driver)
        sleep(5)

    def pro_add_buy_file_lowest_pingbiao(self,gov_pro):
        """采购文件-最低评标价法"""
        driver = self.login_zbr()
        self.pm.enter_company_pro_process(driver, gov_pro)
        self.pop.add_purchase_file(driver)
        self.psbi.com_set_base_info(driver, gov_pro)
        self.pbot.set_bid_open_table(driver)
        self.psbem.set_bid_method_lowest_pingbiao(driver)
        self.pubf.upload_bid_file(driver, gov_pro)
        self.puof.next_step(driver)
        self.pcdp.data_packet(driver)
        sleep(10)

    def add_invite_letter_test(self,gov_pro):
        """添加投标邀请函-测试"""
        driver = self.login_zbr()
        self.pm.enter_company_pro_process(driver, gov_pro)
        self.pop.add_invite_letter(driver)
        self.pie.add_letter(driver,gov_pro)

    def add_invite_letter(self,driver,gov_pro):
        """添加投标邀请函"""
        self.pop.add_invite_letter(driver)
        self.pie.add_letter(driver,gov_pro)

    def add_single_test(self,gov_pro):
        """添加单一来源公示-测试"""
        driver = self.login_zbr()
        self.pm.enter_company_pro_process(driver, gov_pro)
        self.pop.add_single_source(driver)
        self.ps.add_single_source(driver,gov_pro)

    def add_single(self,driver,gov_pro):
        """添加单一来源公示"""
        self.pop.add_single_source(driver)
        self.ps.add_single_source(driver,gov_pro)


    def add_notice(self,gov_pro):
        """新增采购公告"""
        driver = self.login_zbr()
        cg_type = gov_pro['cg_type']
        self.pm.enter_company_pro_process(driver, gov_pro)
        self.pop.add_purchase_notice(driver,gov_pro)
        if cg_type in ['公开招标']:
            self.pn.add_notice_submit(driver,gov_pro)
        elif cg_type in ['邀请招标','单一来源采购']:
            self.pni.add_notice_invite_save(driver,gov_pro)
            if cg_type in ['单一来源采购']:
                self.add_single(driver,gov_pro)
            self.add_invite_letter(driver, gov_pro)
        elif cg_type in ['竞争性谈判','竞争性磋商','询价']:
            self.pn.add_notice_submit_talks(driver,gov_pro)


