# -*- coding=utf-8 -*-
from pprint import pprint

from flask import Flask,render_template,request
import json

from common import tool
from company.company_run import CompanyRun
from gov.create_pro_gov import CreatePro
from gov.gov_run import GovRun

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template('index_1.html')

@app.route("/get_vlues",methods=['GET','POST'])
def get_vlues():
    args = request.form
    pro_type = args.get('pro_type')
    pro_name = args.get('pro_name')
    cg_type = args.get('cg_type')
    pb_method = args.get('pb_method')
    file = args.get('file')
    jyzx = args.get('jyzx')
    zcr = args.get('zcr')
    bdhy = args.get('bdhy')
    pro_add = args.get('pro_add')
    pro_approve = args.get('pro_approve')
    file_add = args.get('file_add')
    file_approve = args.get('file_approve')
    notice_add = args.get('notice_add')
    notice_approve = args.get('notice_approve')
    bid_num = int(args.get('bid_num'))
    tbr = ['tbr1', 'tbr2', 'tbr3']
    tbr_single = ['tbr1']

    time_date = tool.get_time()
    only = time_date['time_str']
    cg_id = only
    if pro_name == '':
        pro_name = pro_type +'-' + cg_type + '-' + time_date['date_t'] + '-' + only
    cg_bd_name = pro_name + '-标段'

    pro_info = {
        'cg_id': cg_id,
        'cg_name': pro_name,
        'cg_type': cg_type,
        'pb_method':pb_method,
        'cg_bd_name': cg_bd_name,
        'jyzx': jyzx,
        'bdhy': bdhy,
        'bid_num': bid_num,
        'file': file,
        'start_date': time_date['data_5_min'],
        'end_date': time_date['data_20'],
        'tbr': tbr,
        'tbr_single': tbr_single,
        'zcr': zcr,
        'pro_add':pro_add,
        'pro_approve': pro_approve,
        'file_add':file_add,
        'file_approve': file_approve,
        'notice_add':notice_add,
        'notice_approve': notice_approve
    }
    pprint(pro_info)
    if pro_type == '企业':
        cr = CompanyRun(pro_info)
        cr.com_pro()
    elif pro_type == '政府':
        gr = GovRun(pro_info)
        gr.govment_pro()
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)