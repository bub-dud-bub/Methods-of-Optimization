# -*- coding: cp1251 -*-
import matplotlib.pyplot as plt
import wx
x1,y1 = 15,-19
x2,y2 = 76,89
c1,c2 = 2,1
#x1 = int(input("� �����:"))
#y1 = int(input("� �����:"))
#x2 = int(input("� �������:"))
#y2 = int(input("� �������:"))
#c1 = int(input("�������� �� �����:"))
#c2 = int(input("�������� �� ����:"))

mult = (x2-x1)/(y2-y1)
a = x1 + (0 - y1)*mult
qx = x2 - (x2 - a)/(c1/c2)
x = [x1, qx, x2]
y = [y1, 0, y2]
plt.plot(x,y, color='green', marker='o', markersize='4')

x = [0,100]
y = [0,0]
plt.plot(x,y, color='Blue')
plt.text(x1,y1, 'Boy (' + str(x1) + ',' + str(y1) + ')')
plt.text(qx+3,3, 'Q (' + str(qx) + ',' + str(0) + ')')
plt.text(x2,y2, 'Girl (' + str(x2) + ',' + str(y2) + ')')
plt.text(0,3, '����')
plt.text(0,-6, '�����')
plt.show()
