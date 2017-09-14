#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import threading
import time

class Add_event(wx.PyCommandEvent):
    def __init__ (self,eventType,id=-1):
        wx.PyCommandEvent.__init__(self,eventType,id)
        self.num=0

Add_EventType = wx.NewEventType()
EVT_Add = wx.PyEventBinder(Add_EventType,1)

class myTread(threading.Thread):
    def __init__(self,window):
        threading.Thread.__init__(self)
        self.window=window
        self.num=0
        self.start()
    def run(self):
        while(True):
            a=0
            for i in range(5):
                a=a+1
                time.sleep(1)
            self.num=a
            evn = Add_event(Add_EventType)
            evn.num=a
            wx.PostEvent(self.window,evn)
class Frame1(wx.Frame):
    def __init__ (self,parent,id=-1):
        wx.Frame.__init__(self,parent,id,title="test")
        self.Bind(EVT_Add,self.On_Time)
        self.thread1=myTread(self)
        self.timer = wx.Timer(self, id=-1)  # 创建定时器

        self.timer.Start(100)  # 设定时间间隔
        self.Show(True)

    def On_Time(self,evn):
        print "i=",self.thread1.num
app=wx.App()
fra1=Frame1(parent=None)
app.MainLoop()