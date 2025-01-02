from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    """
    各环境登录
    """
    def __init__(self):
        print('初始化')
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def login(self,url,username,password,role='招标人'):
        """登录方法封装"""
        print('交易系统登录')
        driver = self.driver
        self.driver.get(url)
        driver.find_element(By.NAME, 'username').send_keys(username)
        driver.find_element(By.NAME, 'password').send_keys(password)
        sleep(1)
        login_button = driver.find_element(By.XPATH,"//span[text()='立即登录']")
        login_button.click()
        if role == '招标人':
            print('招标人登录')
            login_role = driver.find_element(By.XPATH, "//*[text()='招标人登录']")
            print('登录账户：'+username)
            login_role.click()
        sleep(3)
        return driver

    def login_trade_sh_zbr(self):
        """沙河-招标人登录"""
        print('沙河交易系统登录 ------招标人')
        url = 'http://trade.jy-test.zszc.jianshicha.cn/'
        print('沙河测试环境')
        username = '招标人AAA'
        password = 'c123456.'
        driver = self.login(url,username,password)
        return driver

    def login_trade_sh_approve(self):
        """沙河-审批人登录"""
        print('沙河交易系统登录 ------审批人')
        role = '审批人'
        url = 'http://trade.jy-test.zszc.jianshicha.cn/'
        print('沙河测试环境')
        username = 'trade-audit'
        password = 'a123456.'
        driver = self.login(url, username, password,role)
        return driver

    def login_trade_zhuozhou_zbr(self):
        """涿州交易系统登录-招标人登录"""
        print('涿州交易系统登录 ------招标人')
        url = 'http://trade.zz-test.zszc.jianshicha.cn/#/login'
        print('涿州测试环境')
        role = '111'
        username = '招标人AAA'
        password = 'c123456.'
        driver = self.login(url,username,password,role)
        return driver

    def login_trade_zhuozhou_approve(self):
        """涿州交易系统登录-审批人登录"""
        print('涿州交易系统登录 ------审批人')
        role = '审批人'
        url = 'http://trade.zz-test.zszc.jianshicha.cn/#/login'
        print('涿州测试环境')
        username = '河北代清'
        password = 'a123456.'
        driver = self.login(url, username, password,role)
        return driver

    def login_trade_qy_zbr(self):
        """清苑交易系统登录-招标人登录"""
        print('清苑交易系统登录 ------招标人')
        url = 'http://trade.qy-test.zszc.jianshicha.cn/#/login'
        print('清苑交易系统登录')
        username = '测试专用企业'
        password = 'c123456.'
        driver = self.login(url,username,password)
        return driver

    def login_trade_qy_approve(self):
        """清苑交易系统登录-审批人登录"""
        print('沙河交易系统登录 ------审批人')
        role = '审批人'
        url = 'http://trade.qy-test.zszc.jianshicha.cn/#/login'
        print('清苑交易系统登录')
        username = 'trade-ceshi1'
        password = 'c123456.'
        driver = self.login(url, username, password,role)
        return driver