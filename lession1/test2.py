#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        button2=wx.Button(self,label="button2",pos=(100,150))
        button1 = wx.Button(self, label='Btn', pos=(100, 100))
        button2.Bind(wx.EVT_BUTTON, self.OnClicked)
        button1.Bind(wx.EVT_BUTTON, self.btnclk)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnClicked(self,e):
        print 'button2 clicked'
        e.Skip()

    def OnButtonClicked(self, e):
        print 'Panel received click event. propagated to Frame class'
        e.Skip()

    def btnclk(self, e):
        print "Button1 clicked"
        e.Skip()


class Example(wx.Frame):
    def __init__(self, parent):
        super(Example, self).__init__(parent)

        self.InitUI()

    def InitUI(self):
        mpnl = MyPanel(self)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

        self.SetTitle('Event propagation demo')
        self.Centre()
        self.Show(True)

    def OnButtonClicked(self, e):
        print 'click event received by frame class'



ex = wx.App()
Example(None)
ex.MainLoop()