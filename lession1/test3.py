#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import time
class ClockWindow(wx.Window):
    def __init__(self, parent):
        wx.Window.__init__(self,parent)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer =wx.Timer(self)#创建定时器
        self.Bind(wx.EVT_TIMER,self.OnTimer,self.timer)# 绑定一个定时器事件
        self.timer.Start(1000)#设定时间间隔

    def Draw(self,dc):#绘制当前时间
        print "ontime"
        t = time.localtime(time.time())
        st = time.strftime("%I:%M:%S", t)
        w,h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th  = dc.GetTextExtent(st)
        dc.DrawText(st,(w-tw)/2, (h)/2- th/2)

    def OnTimer(self, evt):#显示时间事件处理函数
        dc = wx.BufferedDC(wx.ClientDC(self))
        self.Draw(dc)
    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        self.Draw(dc)
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="wx.Timer")
        ClockWindow(self)

app = wx.PySimpleApp()
frm = MyFrame()
frm.Show()
app.MainLoop()