import time
import datetime
from selenium.webdriver.common.by import By

def locate(driver,target):
    driver.execute_script("arguments[0].scrollIntoView();",target)

def get_time():
    # time_now = time.strftime('%Y-%m-%d %H:%M:%S')
    year = int(time.strftime('%Y'))
    month = int(time.strftime('%m'))
    day = int(time.strftime('%d'))
    hour = int(time.strftime('%H'))
    minute = int(time.strftime('%M'))
    second = int(time.strftime('%S'))
    date_t = time.strftime('%Y%m%d')
    date_today = datetime.date(year,month,day)
    date_now = datetime.time(hour, minute, second)
    data_tomorrow = date_today + datetime.timedelta(days=1)
    data_20 = date_today + datetime.timedelta(days=40)
    data_5_min = (datetime.datetime.now() + datetime.timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")
    data_10_min = (datetime.datetime.now() + datetime.timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")
    time_date = {
        'date_today':str(date_today),
        'date_now':str(date_now),
        'data_tomorrow':str(data_tomorrow),
        'data_20':str(data_20),
        'data_5_min':str(data_5_min),
        'data_10_min':str(data_10_min),
        'time_str':str(int(time.time())),
        'date_t':date_t
    }
    return time_date

def get_bid_type(bid_type):
    type_str = ''
    if bid_type == 1:
        type_str = '公开招标'
    elif bid_type == 2:
        type_str = '邀请招标'
    elif bid_type == 3:
        type_str = '单一来源采购'
    elif bid_type == 4:
        type_str = '竞争性谈判'
    elif bid_type == 5:
        type_str = '竞争性磋商'
    elif bid_type == 6:
        type_str = '询价'
    return type_str

def find_element(driver,loc,find_type='XPATH'):
    if find_type == 'NAME':
        el = driver.find_element(By.NAME, loc)
    else:
        el = driver.find_element(By.XPATH, loc)
    return el

# t = get_time()
# print(t)