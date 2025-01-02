from old.login import Login
from common import tool
from gov import Gov


if __name__ == '__main__':
    # 1-公开招标 2-邀请招标 3-单一来源采购 4-竞争性谈判 5-竞争性磋商 6-询价
    bid_type = 5
    type_str = tool.get_bid_type(bid_type)
    time_date = tool.get_time()
    #唯一标识
    only = time_date['time_str']
    #项目编号
    cg_id = 'ZF-' + only
    #项目名称
    cg_name = 'ZF-竞争性磋商-20241218-1734491399'
    # cg_name = 'ZF-' + type_str + '-' + time_date['date_t'] + '-' + only
    #标段名称
    cg_bd_name = cg_name +'-标段1'
    #采购内容
    cg_nr = '水泥、钢筋、砂石、砖块'
    #邀请投标人
    tbr = ['tbr1','tbr2','tbr3']
    tbr_single = ['tbr1']
    #
    file = 'F:\上传文件\测试-招标文件.pdf'
    #项目信息
    gov_pro = {
        'cg_id': cg_id,
        'cg_name':cg_name,
        'cg_type':type_str,
        'cg_bd_name':cg_bd_name,
        'cg_nr':cg_nr,
        'type_str':type_str
    }
    #公告信息
    notice = {
        'start_date':time_date['data_5_min'],
        'end_date':time_date['data_20'],
        'cg_name':cg_name,
        'cg_bd_name': cg_bd_name,
        'tbr':tbr
    }

    gov = Gov()
    # 新增项目
    # login = Login()
    # driver = login.login_trade_zbr()
    # gov.add_project(driver,gov_pro)

    #新增项目审批
    login = Login()
    driver = login.login_trade_approve()
    gov.approve_pro(driver,gov_pro)

    # quit()
    # 新增采购文件
    login = Login()
    driver = login.login_trade_zbr()
    gov.enter_process(driver, gov_pro)
    gov.add_buy_file(driver,notice)
    gov.lowest_method(driver)
    gov.upload_file(driver,file)
    gov.data_packet(driver)

    # 采购文件审批
    login = Login()
    driver = login.login_trade_approve()
    gov.approve_pro(driver, gov_pro)

    # 登录招标人，进入操作流程
    login = Login()
    driver = login.login_trade_zbr()
    gov.enter_process(driver, gov_pro)
    if bid_type in [1,4,5,6]:
        #新增采购公告-开始字段
        gov.add_pro_notice(driver,notice)
        if bid_type == 1:
            #公开招标填写信息
            gov.add_pro_notice_public(driver,notice)
        elif bid_type in [4,5,6]:
            #谈判、磋商、询价填写信息
            gov.add_pro_notice_talk(driver,notice)
        #新增采购公告-结尾字段
        gov.add_pro_notice_end(driver)
    elif bid_type in [2,3]:
        if bid_type == 3:
            notice['tbr'] = tbr_single
            gov.single_source(driver,notice)
        gov.bid_invitation(driver, notice)
        gov.invitation_notice(driver, notice)

    #todo公告审核


