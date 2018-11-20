#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import tkinter.messagebox
import time

def showBrowser():
    # help(webdriver)
    # driver = webdriver.Ie()
    # driver = webdriver.Edge()

    # 创建chrome参数对象
    opt = webdriver.ChromeOptions()
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

def sendData_test(driver):
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

def sendData_wangyi(driver):
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


def runWebTask():
    driver = showBrowser()
    try:
        sendData_wangyi(driver)
    except (WebDriverException, NoSuchElementException, Exception) as e:
        print("error: ", e)
        tkinter.messagebox.showinfo( "error", e)
    finally:
        # time.sleep(10)
        # driver.close()
        pass

if __name__ == "__main__":
    runWebTask()
    