#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter                  # 导入 Tkinter 库
import tkinter.messagebox
from WebController import WebController
import random

import NFLog
import NFConfig

class Application():
    e_pwd = None
    e_user = None
    text_log = None
    text_num = None
    webController = None

    randomNumList = []

    def __init__(self):
        NFLog.registLogEvent(lambda logType, *args: 
            self.showLog(logType, *args))

    def show(self):
        root = tkinter.Tk()             # 创建窗口对象的背景色
        root.title("筛")
        root.wm_minsize(200,200)
        def on_closing():
            self.endWeb()
            root.destroy()
            # if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
            #     self.endWeb()
            #     root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)

        topFrame = tkinter.Frame(root)
        topFrame.grid(row=0)

        bottomFrame = tkinter.Frame(root)
        bottomFrame.grid(row=1)

        leftFrame = tkinter.Frame(topFrame)
        leftFrame.grid(row=0,column=0)

        rightFrame = tkinter.Frame(topFrame)
        rightFrame.grid(row=0,column=1)


        # leftFrame.pack()
        #第一行，用户名标签及输入框
        inputFrame = tkinter.Frame(leftFrame)
        inputFrame.pack()
        l_user = tkinter.Label(inputFrame, text = '用户名：')
        l_user.grid(row=0)
        # l_user.pack()
        self.e_usr = tkinter.Entry(inputFrame)
        self.e_usr.insert('end', NFConfig.default_usr)
        self.e_usr.grid(row=0,column=1)
        # self.e_usr.pack()

        #第二行，密码标签及输入框
        l_pwd = tkinter.Label(inputFrame,text='密码：')
        l_pwd.grid(row=1)
        # l_pwd.pack()
        self.e_pwd = tkinter.Entry(inputFrame)
        self.e_pwd['show']='*'
        self.e_pwd.insert('end', NFConfig.default_pwd)
        self.e_pwd.grid(row=1,column=1)
        # self.e_pwd.pack()

        btn = tkinter.Button(leftFrame, text ="生成一个随机数", command = lambda : self.createRandomNumList())
        btn.pack()

        btn = tkinter.Button(leftFrame, text ="清除随机数", command = lambda : self.clearRandomNumList())
        btn.pack()

        btn = tkinter.Button(leftFrame, text ="登录并提交", command = lambda : self.showWeb())
        btn.pack()

        btn = tkinter.Button(leftFrame, text ="showExtraInfo", command = lambda : self.webController.showExtraInfo())
        btn.pack()

        self.text_log = tkinter.Text(rightFrame, height=10)
        self.text_log.pack()
        
        self.text_num = tkinter.Text(bottomFrame, height=30)
        self.text_num.pack()

        self.showInfoToUi("start")


        root.mainloop()                 # 进入消息循环

    def createRandomNumList(self):
        # self.randomNumList.clear()
        numStr = "{0:0>4d}".format(random.randint(0,9999))
        self.randomNumList.append(numStr)
        print(numStr)
        
        # self.text_num
        self.text_num.insert(tkinter.END, numStr + '\n')
        # for item in self.randomNumList:
            
    def clearRandomNumList(self):
        self.randomNumList.clear()
        self.text_num.delete('0.0', tkinter.END)

    def showWeb(self):
        # tkinter.messagebox.showinfo( "Hello Python", "Hello Runoob")
        usr = self.e_usr.get()
        pwd = self.e_pwd.get()
        
        self.endWeb()
        self.webController = WebController()
        self.webController.startWebTask(usr, pwd, self.randomNumList)

    def endWeb(self):
        # pass
        if self.webController :
            self.webController.clear()
            self.webController = None

    def showLog(self, logType, *args):
        label = '[{0}]'.format(logType.name)
        logStr = label
        for item in args:
            logStr += " "
            logStr += "{0}".format(item)
        # self.text_log['text'] += logStr
        self.showInfoToUi(logStr)

    def showInfoToUi(self, logStr):
        self.text_log.insert(tkinter.END, logStr + '\n')
        self.text_log.yview_moveto(1)



if __name__ == "__main__":
    app = Application()
    app.show()