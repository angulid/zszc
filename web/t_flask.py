# -*- coding=utf-8 -*-
from pprint import pprint

from flask import Flask,render_template,request
import json

from common import tool
from company.company_run import CompanyRun

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/get_vlues",methods=['GET','POST'])
def get_vlues():
    args = request.form
    pro_type = args.get('pro_type')
    pro_name = args.get('pro_name')
    cg_type = args.get('cg_type')
    file = args.get('file')
    jyzx = args.get('jyzx')
    zcr = args.get('zcr')
    bdhy = args.get('bdhy')
    bid_num = int(args.get('bid_num'))
    tbr = ['tbr1', 'tbr2', 'tbr3']
    tbr_single = ['tbr1']

    time_date = tool.get_time()
    only = time_date['time_str']
    cg_id = only
    if pro_name == '':
        cg_name = pro_type +'-' + cg_type + '-' + time_date['date_t'] + '-' + only
    cg_bd_name = cg_name + '-标段'

    pro_info = {
        'cg_id': cg_id,
        'cg_name': cg_name,
        'cg_type': cg_type,
        'cg_bd_name': cg_bd_name,
        'jyzx': jyzx,
        'bdhy': bdhy,
        'bid_num': bid_num,
        'file': file,
        'start_date': time_date['data_5_min'],
        'end_date': time_date['data_20'],
        'tbr': tbr,
        'tbr_single': tbr_single,
        'zcr': zcr
    }

    if pro_type == '企业':
        cr = CompanyRun(pro_info)
        cr.com_zh()
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)