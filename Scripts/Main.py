#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter                  # 导入 Tkinter 库
import tkinter.messagebox
import WebTask

root = tkinter.Tk()             # 创建窗口对象的背景色
#                                 # 创建两个列表
# li     = ['C','python','php','html','SQL','java']
# movie  = ['CSS','jQuery','Bootstrap']
# listb  = tkinter.Listbox(root)          #  创建两个列表组件
# listb2 = tkinter.Listbox(root)
# for item in li:                 # 第一个小部件插入数据
#     listb.insert(0,item)
 
# for item in movie:              # 第二个小部件插入数据
#     listb2.insert(0,item)
 
# listb.pack()                    # 将小部件放置到主窗口中
# listb2.pack()

def showWeb():
    # tkinter.messagebox.showinfo( "Hello Python", "Hello Runoob")
    WebTask.runWebTask()
 
btn = tkinter.Button(root, text ="开始", command = showWeb)
btn.pack()

root.mainloop()                 # 进入消息循环

