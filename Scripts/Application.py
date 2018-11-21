#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter                  # 导入 Tkinter 库
import tkinter.messagebox
from WebController import WebController

import NFLog

class Application():
    root = None
    e_pwd = None
    e_user = None
    text_log = None
    webController = None
    def __init__(self):
        NFLog.registLogEvent(lambda logType, *args: 
            self.showLog(logType, *args))

    def show(self):
        self.root = tkinter.Tk()             # 创建窗口对象的背景色
        self.root.title("筛")
        self.root.wm_minsize(200,200)
        def on_closing():
            self.endWeb()
            self.root.destroy()
            # if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
            #     self.endWeb()
            #     self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)
        
        leftFrame = tkinter.Frame(self.root)
        leftFrame.grid(row=0,sticky=tkinter.E)
        # leftFrame.pack()
        #第一行，用户名标签及输入框
        l_user = tkinter.Label(leftFrame, text = '用户名：')
        l_user.grid(row=0,sticky=tkinter.W)
        # l_user.pack()
        self.e_usr = tkinter.Entry(leftFrame)
        self.e_usr.insert('end', "zbz679")
        self.e_usr.grid(row=0,column=1,sticky=tkinter.E)
        # self.e_usr.pack()

        #第二行，密码标签及输入框
        l_pwd = tkinter.Label(leftFrame,text='密码：')
        l_pwd.grid(row=1,sticky=tkinter.W)
        # l_pwd.pack()
        self.e_pwd = tkinter.Entry(leftFrame)
        self.e_pwd['show']='*'
        self.e_pwd.insert('end', "aaa12345")
        self.e_pwd.grid(row=1,column=1,sticky=tkinter.E)
        # self.e_pwd.pack()

        btn = tkinter.Button(leftFrame, text ="登录", command = lambda : self.showWeb())
        btn.grid(row=2,column=1,sticky=tkinter.E)
        # btn.pack()

        # content
        rightFrame = tkinter.Frame(self.root)
        rightFrame.grid(row=0,column=1,sticky=tkinter.E)
        # rightFrame.pack()
        self.text_log = tkinter.Text(rightFrame, height=10)
        self.text_log.pack()

        self.showInfoToUi("start")

        self.root.mainloop()                 # 进入消息循环

    def showWeb(self):
        # tkinter.messagebox.showinfo( "Hello Python", "Hello Runoob")
        usr = self.e_usr.get()
        pwd = self.e_pwd.get()
        
        self.endWeb()
        self.webController = WebController()
        self.webController.startWebTask(usr, pwd)

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
        self.text_log.insert('end', logStr + '\n')
        self.text_log.yview_moveto(1)



if __name__ == "__main__":
    app = Application()
    app.show()