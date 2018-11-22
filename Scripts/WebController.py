#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import tkinter.messagebox
import time

import NFLog
import NFConfig

class WebController():
    driver = None

    userName = None
    passWord = None
    numList = None

    def __init__(self):
        pass

    def createBrowser(self):
        # help(webdriver)
        # driver = webdriver.Ie()
        # driver = webdriver.Edge()

        # 创建chrome参数对象
        opt = webdriver.ChromeOptions()

        #修改日志级别
        # opt.add_argument('log-level=3')
        opt.add_argument('--no-sandbox')
        opt.add_argument('--disable-gpu')

        # # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
        # opt.set_headless()
        # opt.add_argument('headless')

        # 隐藏受到自动软件的控制提示
        opt.add_argument('disable-infobars')

        # # 创建chrome对象
        driver = webdriver.Chrome(options=opt)
        # driver = webdriver.Chrome()

        # driver.fullscreen_window()

        return driver

    def sendData_test(self, driver):
        driver.delete_all_cookies()
        driver.get('http://www.baidu.com/')
        # time.sleep(1)

        elem = driver.find_element_by_id("u1")
        elem = elem.find_element_by_name("tj_login")
        # elem = elem.find_element_by_xpath("//*[@id='u1']/a[@name='tj_login']")
        elem.click()
        print(elem)
        time.sleep(2)
        
        elem = driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn")
        elem.click()
        # elem = elem.find_element_by_name("tj_login")
        print(elem)
        elem = driver.find_element_by_id("TANGRAM__PSP_10__userName")
        elem.clear()
        elem.send_keys("")
        print(elem)
        elem = driver.find_element_by_id("TANGRAM__PSP_10__password")
        elem.send_keys("")
        print(elem)
        elem = driver.find_element_by_id("TANGRAM__PSP_10__submit")
        elem.click()
        print(elem)
        time.sleep(10)
        print("task over")
        
        driver.quit()
        
        # elem = driver.find_element_by_id("kw")
        # elem.send_keys("a123")
        # # # 提交表单
        # elem = driver.find_element_by_xpath("//*[@id='su']")
        # elem.click()

    def sendData_wangyi(self, driver):
        driver.delete_all_cookies()
        driver.get('http://caipiao.163.com/order/cqssc/')

        elem_wrap_star = driver.find_element_by_id("wrap_star1_fs")
        # driver.execute_script("arguments[0].setAttribute('rel', 'testaa1')", elem)

        print(elem_wrap_star)
        elem = elem_wrap_star.find_element_by_xpath(".//div[@class='ballarea clearfix']/div[@class='clearfix']/div[@class='redBallBox']/ul[@class='clearfix']")
        # driver.execute_script("arguments[0].setAttribute('rel', 'testaa2')", elem)
        # print(elem)
        btnList = []
        for num in range(0,10):
            btn = elem.find_element_by_xpath(".//li/a[@data-value='{0}']".format(num))
            btnList.append(btn)

        # driver.execute_script("arguments[0].setAttribute('rel', 'testaa3')", btnList[0])
        # print(btnList[0])

        okBtn = elem_wrap_star.find_element_by_xpath(".//div[@class='betbtnBox']/a[@class='betbtn disabled']")
        # okBtn = elem_wrap_star.find_element_by_xpath(".//div[@class='betbtnBox']/a[@class='betbtn']")

        time.sleep(1)

        btnList[0].click()
        btnList[3].click()
        btnList[5].click()
        okBtn.click()

        time.sleep(1)

        btnList[1].click()
        btnList[2].click()
        btnList[6].click()
        okBtn.click()

        
        # chain = ActionChains(driver)
        # chain.move_to_element(btnList[0])
        # chain.click(btnList[0])

        # driver.execute_async_script("arguments[0].click()", btnList[0])
        # driver.execute_script("arguments[0].click()", btnList[0])
        # btnList[0].click()


        print("click")

        # js = "alert(\"Hello World!\");"
        # driver.execute_async_script(js)

        # time.sleep(1000)

    def sendData_hy(self, driver):
        driver.delete_all_cookies()
        # driver.get('http://6895hy.us/')
        driver.get('http://sue.4lli.hy.0919999.net:891')
        # driver.get('http://sue.4lli.hy.0919999.net:891/Home/Main#$2')

        elem_username = driver.find_element_by_id("admin_username")
        elem_username.clear()
        elem_username.send_keys(self.usr)

        elem_password = driver.find_element_by_id("admin_password")
        elem_password.clear()
        elem_password.send_keys(self.pwd)

        elem_submit = driver.find_element_by_xpath("//body[@class='spb']/div[@class='contianer login-contianer']\
        /div[@class='login-area']/div[@class='login-form']/form/ul/li/input[@class='regsiter-btn']")
        elem_submit.click()
        
        NFLog.info("开始登录")

        # wait 同意协议
        try:
            WebDriverWait(driver,5,0.5).until(
                EC.presence_of_element_located((By.ID, 'Submit2')))
        except (Exception):
            NFLog.error("登录失败")
            # tkinter.messagebox.showinfo( "error", e)
            
            elem_tip = driver.find_element_by_id("tip")
            NFLog.info("错误信息:", elem_tip.text)
        else:
            elem_ok = driver.find_element_by_id("Submit2")
            elem_ok.click()
            NFLog.info("登录成功")
        finally:
            # time.sleep(10)
            # self.driver.close()
            pass
            
        # wait 指定页面
        WebDriverWait(driver,5,0.5).until(
            EC.presence_of_element_located((By.ID, 'TabMenuBox')))
        time.sleep(1)
        elem_tabMenuBox = driver.find_element_by_id("TabMenuBox")
        btn_txtImport = elem_tabMenuBox.find_element_by_xpath(".//li/a[@href='/BetPanel/FastTranslate/Index']")
        btn_txtImport.click()

        NFLog.info("进入指定页面")

        # 内容输入
        WebDriverWait(driver,5,0.5).until(
            EC.presence_of_element_located((By.ID, 'CleverTxt')))
        elem_CleverTxt = driver.find_element_by_id("CleverTxt")
        # driver.execute_script("return arguments[0].value='1234=1'", elem_CleverTxt)
        numStr = ""
        for item in self.numList:
            numStr += item + "=0.1\n"
        elem_CleverTxt.send_keys(numStr)
        textValue = driver.execute_script("return arguments[0].value", elem_CleverTxt)
        NFLog.info('提交数据:\n', textValue)

        # 提交
        self.elem_CleverTxt = elem_CleverTxt

        elem_Container = driver.find_element_by_id("Container")
        elem_inputW = elem_Container.find_element_by_xpath(".//div[@class='table-out']/form/table/tbody/tr/td[@class='inputW']")
        elem_submit = elem_inputW.find_element_by_xpath(".//button[@type='button']")
        # elem_reset = elem_inputW.find_element_by_xpath(".//button[@type='reset']")

        elem_submit.click()


        # # 切换frame
        # elem_IFRAME = driver.find_element_by_id("IFRAME")
        # frame_IFRAME = elem_IFRAME.find_element_by_xpath(".//iframe[@src='/InportTxt/Index']")
        # driver.switch_to.frame(frame_IFRAME)

        # elem_fileInput = driver.find_element_by_xpath(".//html/body/div[@class='table-out']/table[@class='tablecommon tablecommon1 break']\
        #     /tbody/tr[@class='t-left']/td/input[@type='file']")
        # self.elem_fileInput = elem_fileInput
        # NFLog.info("aa1", elem_fileInput.get_attribute("value"))
        # driver.execute_script(r"arguments[0].value='C:\Users\Administrator\Desktop\testa.txt'", elem_fileInput)
        # NFLog.info("aa2", elem_fileInput.get_attribute("value"))
        
    elem_CleverTxt = None
    def showExtraInfo(self):
        if self.driver:
            NFLog.info(self.elem_CleverTxt.get_attribute("value"))

    def clear(self):
        if self.driver:
            # self.driver.close()
            self.driver.quit()

    def startWebTask(self, usr, pwd, numList):
        NFLog.info("用户:", usr)
        self.usr = usr
        self.pwd = pwd
        self.numList = numList
        self.driver = self.createBrowser()
        try:
            self.sendData_hy(self.driver)
        except (NoSuchElementException) as e:
            NFLog.error(e.msg)
            tkinter.messagebox.showinfo( "error", e)
        except (WebDriverException) as e:
            NFLog.error(e.msg)
            tkinter.messagebox.showinfo( "error", e)
        except (Exception) as e:
            NFLog.error(e)
            tkinter.messagebox.showinfo( "error", e)
        finally:
            # time.sleep(10)
            # self.driver.close()
            pass

if __name__ == "__main__":
    webController = WebController()
    webController.startWebTask(NFConfig.default_usr, NFConfig.default_pwd, ["0000", "1111"])
    time.sleep(1000)
    