from time import sleep

from base.page_approve import PageApprove
from page.page_gc_add import PageGcAdd
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

class CreateProGc:
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
        self.pga = PageGcAdd()

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

    def gc_create(self, gov_pro):
        """工程项目新建"""
        driver = self.login_zbr()
        self.pm.enter_engineering_pro(driver)
        self.pga.gc_add(driver,gov_pro)
        self.ppe.add_gc_pro_submit(driver,gov_pro)

    def gc_pro_create(self, gov_pro):
        """工程项目新建"""
        driver = self.login_zbr()
        self.pm.enter_engineering_biz_pro(driver)
        if gov_pro['sxf'] == 1:
            self.ppe.add_gc_biz_sxf_submit(driver,gov_pro)
        else:
            self.ppe.add_gc_biz_submit(driver,gov_pro)


    def add_invite_letter(self,driver,gov_pro):
        """工程项目投标邀请函"""
        self.pop.add_invite_letter(driver)
        self.pie.add_letter(driver,gov_pro)

    def approve(self,gov_pro):
        """审批"""
        driver = self.login_approve()
        self.pa.approve_pro(driver, gov_pro)

    def pro_add_buy_file_zonghe(self,gov_pro):
        """招标文件-综合评分法"""
        driver = self.login_zbr()
        self.pm.enter_gc_pro_process(driver, gov_pro)
        self.pop.add_zb_file(driver)
        self.psbi.gc_set_base_info(driver, gov_pro)
        self.pbot.set_bid_open_table(driver,gov_pro['sxf'])
        if gov_pro['sxf'] == 1:
            self.psbem.set_bid_method_comprehensive_sxf(driver)
        else:
            self.psbem.set_bid_method_zhpg(driver)
        self.pubf.upload_bid_file(driver, gov_pro)
        self.puof.next_step(driver)
        self.pcdp.data_packet(driver)
        sleep(5)

    def add_notice(self,gov_pro):
        """新增采购文件"""
        Login()
        cg_type = gov_pro['cg_type']
        driver = self.login_zbr()
        self.pm.enter_gc_pro_process(driver, gov_pro)
        self.pop.add_gc_zb_notice(driver,gov_pro)
        if cg_type in ['公开招标']:
            self.pn.add_gc_zb_notice_submit(driver,gov_pro)
        elif cg_type in ['邀请招标']:
            self.pni.add_notice_invite_save(driver,gov_pro)
            self.add_invite_letter(driver, gov_pro)
