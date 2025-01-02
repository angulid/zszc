from common import tool
from company.create_pro_comapny import CreateComPro

if __name__ == '__main__':
    bid_type = 1
    type_str = tool.get_bid_type(bid_type)
    time_date = tool.get_time()
    #唯一标识
    only = time_date['time_str']
    #项目编号
    cg_id = 'QY-' + only
    #项目名称
    # cg_name = 'QY-单一来源采购-20241220-1734678245'
    cg_name = 'QY-' + type_str + '-' + time_date['date_t'] + '-' + only
    #标段数量
    bid_num = 1
    #标段名称
    cg_bd_name = cg_name +'-标段'
    #采购内容
    cg_nr = '水泥、钢筋、砂石、砖块'
    #邀请投标人
    tbr = ['tbr1','tbr2','tbr3']
    tbr_single = ['tbr1']
    #
    file = 'F:\上传文件\测试-招标文件.pdf'
    jyzx = '河北省公共资源交易中心'
    bdhy = '工程类 / 规划 / 国民经济和社会发展规划 / 总体规划'
    zcr = '招标人AAA'
    #项目信息
    gov_pro = {
        'cg_id': cg_id,
        'cg_name':cg_name,
        'cg_type':type_str,
        'cg_bd_name':cg_bd_name,
        'cg_nr':cg_nr,
        'jyzx':jyzx,
        'bdhy':bdhy,
        'bid_num':bid_num,
        'file':file,
        'start_date': time_date['data_5_min'],
        'end_date': time_date['data_20'],
        'tbr': tbr,
        'tbr_single': tbr_single,
        'zcr': zcr
    }

    ccp = CreateComPro()
    ccp.pro_create(gov_pro)
    ccp.approve(gov_pro)

    ccp.pro_add_buy_file_zonghe(gov_pro)
    # ccp.pro_add_buy_file_lowest_pingbiao(gov_pro)
    # ccp.pro_add_buy_file_lowest_toubiao_reject(gov_pro)
    ccp.approve(gov_pro)

    ccp.add_notice(gov_pro)
    ccp.approve(gov_pro)
