#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import tkinter.messagebox
import time

def showBrowser():
    # help(webdriver)
    # browser = webdriver.Ie()
    browser = webdriver.Edge()
    # browser = webdriver.Chrome()
    return browser

def sendData(browser):
    try:
        browser.get('http://www.baidu.com/')
        # time.sleep(1)

        elem = browser.find_element_by_id("u1")
        elem = elem.find_element_by_name("tj_login")
        # elem = elem.find_element_by_xpath("//*[@id='u1']/a[@name='tj_login']")
        elem.click()

        time.sleep(2)
        
        elem = browser.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn")
        elem.click()
        # elem = elem.find_element_by_name("tj_login")

        elem = browser.find_element_by_id("TANGRAM__PSP_10__userName")
        elem.send_keys("")

        elem = browser.find_element_by_id("TANGRAM__PSP_10__password")
        elem.send_keys("")

        elem = browser.find_element_by_id("TANGRAM__PSP_10__submit")
        elem.click()
        
        # elem = browser.find_element_by_id("kw")
        # elem.send_keys("a123")
        # # # 提交表单
        # elem = browser.find_element_by_xpath("//*[@id='su']")
        # elem.click()
    except (WebDriverException, NoSuchElementException, Exception) as e:
        tkinter.messagebox.showinfo( "error", e)
    finally:
        # time.sleep(10)
        # browser.close()
        pass



def runWebTask():
    browser = showBrowser()
    # browser.get('http://www.baidu.com/')
    sendData(browser)

if __name__ == "__main__":
    runWebTask()
    