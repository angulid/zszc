from time import sleep

from selenium.webdriver.common.by import By



class PageApprove:
    """
    审批页面
    """
    @staticmethod
    def approve_pro(driver, kwargs):
        """采购项目审批"""
        name = kwargs['cg_name']
        PageApprove.approve(driver,name)

    @staticmethod
    def approve(driver, name):
        """管理员审批通过"""
        # print("//*[@id='puilceTable']/form/div/div[4]/div[2]/table/tbody//span[contains(text(),'"+name+"')]/../../../*//span[text()=' 通过 ']")
        driver.find_element(By.XPATH,
                            "//*[@id='puilceTable']/form/div/div[4]/div[2]/table/tbody//span[contains(text(),'" + name + "')]/../../../*//span[text()=' 通过 ']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//div[@class='el-message-box']//span[contains(text(),'确定')]").click()
        sleep(4)
        driver.quit()