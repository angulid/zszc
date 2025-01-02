from common import tool
from create_pro_gc import CreateProGc

class GcRun:

    def __init__(self,gov_pro):
        self.cpg = CreateProGc()
        self.gov_pro = gov_pro
        self.pro_add = gov_pro['pro_add']
        self.pro_approve = gov_pro['pro_approve']
        self.file_add = gov_pro['file_add']
        self.file_approve = gov_pro['file_approve']
        self.notice_add = gov_pro['notice_add']
        self.notice_approve = gov_pro['notice_approve']
        self.pb_method = gov_pro['pb_method']

    def gc_pro(self):
        if self.pro_add == 'on':
            self.cpg.gc_create(self.gov_pro)
            self.cpg.approve(self.gov_pro)
            self.cpg.gc_pro_create(self.gov_pro)
        if self.pro_approve == 'on':
            self.cpg.approve(self.gov_pro)

        if self.file_add == 'on':
            if self.pb_method == '综合评分法':
                self.cpg.pro_add_buy_file_zonghe(self.gov_pro)
            elif self.pb_method == '最低评标价法':
                self.cpg.pro_add_buy_file_lowest_pingbiao(self.gov_pro)
            elif self.pb_method == '最低投标价法':
                self.cpg.pro_add_buy_file_lowest_toubiao_reject(self.gov_pro)
            else:
                print('没有这个评标办法')
        if self.file_approve == 'on':
            self.cpg.approve(self.gov_pro)

        if self.notice_add == 'on':
            self.cpg.add_notice(self.gov_pro)
        if self.notice_approve == 'on':
            self.cpg.approve(self.gov_pro)



