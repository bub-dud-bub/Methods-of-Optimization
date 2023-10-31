# -*- coding: cp1251 -*-
from ctypes import sizeof
from ctypes.wintypes import SIZE
import wx

class Window(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (500,500))
        self.BackgroundColour = "white"
        self.Size
        self.Show(True)
        
        self.lbl = wx.StaticText(self, wx.ID_ANY,"Подставьте значения в систему вида:", pos = (30,30))
        self.lbl = wx.StaticText(self, wx.ID_ANY,"A11 * X + A12 * Y + A13 * Z = F1", pos = (30,45))
        self.lbl = wx.StaticText(self, wx.ID_ANY,"A21 * X + A22 * Y + A23 * Z = F2", pos = (30,60))
        self.lbl = wx.StaticText(self, wx.ID_ANY,"A31 * X + A32 * Y + A33 * Z = F3", pos = (30,75))

        #Иксы
        self.lbl = wx.StaticText(self, wx.ID_ANY,"A11:", pos = (30,100))
        X1 = wx.TextCtrl(self, wx.ID_ANY,"4", pos = (55, 99))
        X1.SetSize((30,20))


        self.lbl = wx.StaticText(self, wx.ID_ANY,"A21:", pos = (30,125))
        X2 = wx.TextCtrl(self, wx.ID_ANY,"5", pos = (55, 124))
        X2.SetSize((30,20))

        self.lbl = wx.StaticText(self, wx.ID_ANY,"A31:", pos = (30,150))
        X3 = wx.TextCtrl(self, wx.ID_ANY,"3", pos = (55, 149))
        X3.SetSize((30,20))

        #Игреки
        self.lbl = wx.StaticText(self, wx.ID_ANY,"A12:", pos = (100,100))
        Y1 = wx.TextCtrl(self, wx.ID_ANY,"2", pos = (125, 99))
        Y1.SetSize((30,20))

        self.lbl = wx.StaticText(self, wx.ID_ANY,"A22:", pos = (100,125))
        Y2 = wx.TextCtrl(self, wx.ID_ANY,"3", pos = (125, 124))
        Y2.SetSize((30,20))

        self.lbl = wx.StaticText(self, wx.ID_ANY,"A32:", pos = (100,150))
        Y3 = wx.TextCtrl(self, wx.ID_ANY,"2", pos = (125, 149))
        Y3.SetSize((30,20))

        #Зеты
        self.lbl = wx.StaticText(self, wx.ID_ANY,"A13:", pos = (170,100))
        Z1 = wx.TextCtrl(self, wx.ID_ANY,"-1", pos = (195, 99))
        Z1.SetSize((30,20))

        self.lbl = wx.StaticText(self, wx.ID_ANY,"A23:", pos = (170,125))
        Z2 = wx.TextCtrl(self, wx.ID_ANY,"-2", pos = (195, 124))
        Z2.SetSize((30,20))

        self.lbl = wx.StaticText(self, wx.ID_ANY,"A33:", pos = (170,150))
        Z3 = wx.TextCtrl(self, wx.ID_ANY,"-3", pos = (195, 149))
        Z3.SetSize((30,20))

        #Эфы
        self.lbl = wx.StaticText(self, wx.ID_ANY,"F1:", pos = (240,100))
        F1 = wx.TextCtrl(self, wx.ID_ANY,"1", pos = (265, 99))
        F1.SetSize((30,20))

        self.lbl = wx.StaticText(self, wx.ID_ANY,"F2:", pos = (240,125))
        F2 = wx.TextCtrl(self, wx.ID_ANY,"2", pos = (265, 124))
        F2.SetSize((30,20))

        self.lbl = wx.StaticText(self, wx.ID_ANY,"F3:", pos = (240,150))
        F3 = wx.TextCtrl(self, wx.ID_ANY,"0", pos = (265, 149))
        F3.SetSize((30,20))

        X1,X2,X3,Y1,Y2,Y3,Z1,Z2,Z3,F1,F2,F3 = int(X1.Value),int(X2.Value),int(X3.Value),int(Y1.Value),int(Y2.Value),int(Y3.Value),int(Z1.Value),int(Z2.Value),int(Z3.Value),int(F1.Value),int(F2.Value),int(F3.Value)
        import count as ct
        X,Y,Z = ct.count(X1,X2,X3,Y1,Y2,Y3,Z1,Z2,Z3,F1,F2,F3)
        self.lbl = wx.StaticText(self, wx.ID_ANY,"Ответ:", pos = (30,200))
        self.lbl = wx.StaticText(self, wx.ID_ANY,"X:"+str(X), pos = (30,220))
        self.lbl = wx.StaticText(self, wx.ID_ANY,"Y:"+str(Y), pos = (30,240))
        self.lbl = wx.StaticText(self, wx.ID_ANY,"Z:"+str(Z), pos = (30,260))


app = wx.App()
wnd =Window(None, "Метод Гаусса")
app.MainLoop()