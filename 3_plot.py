#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'

import csv
import sys
import codecs
from urlparse import urlparse #URL --> Domain
from time import sleep
from operator import itemgetter     #sort by factor
import numpy as np
import matplotlib.pyplot as plt
# ラベルを日本語対応にするのに必要
#font = {'family': 'AppleGothic'}
#plt.rc('font', **font)





#################### 平面直交座標系 #######################
a = open('data/xy_offseted.csv','r')
x_list  = []
y_list  = []
num = 0
for i in a:
	num = num+1
	if num >= 2:
		LINE = i.rstrip().split(',')
		marker = LINE[0]
		x      = float(LINE[1])
		y      = float(LINE[2])
		distance = LINE[3]

		x_list.append(x)
		y_list.append(y)

a.close()


################ WGS84座標系 ####################
b = open('data/xy_WGS84_offseted.csv','r')
x_wgs84_list = []
y_wgs84_list = []
num = 0
for i in b:
	num = num+1
	if num >= 2:
		LINE = i.rstrip().split(',')
		marker = LINE[0]
		x = float(LINE[1])
		y = float(LINE[2])
		distance = LINE[3]
		x_wgs84_list.append(x)
		y_wgs84_list.append(y)
b.close()





#print num_list
#num_list_per_5 = []
#rate_list_per_5= []
#for num in num_list:
#	if num % 5 == 0:
#		num_list_per_5.append(num)
#		rate_list_per_5.append(rate_list[num-1])
		


X = np.array(x_list)
Y = np.array(y_list)
X2 = np.array(x_wgs84_list)
Y2 = np.array(y_wgs84_list)
#Y2= np.array(count_list2)
#Y3= np.array(count_list3)
#Y = np.array(rate_list)
#X = np.array(num_list_per_5)
#Y = np.array(rate_list_per_5)
#Y2= np.array(rate_list_per_5_conf)
#Y3= np.array(rate_list_per_5_page)
plt.title('Plot of xy_offseted.csv',fontsize=18)
plt.xlabel('X[m]',fontsize=18)
plt.ylabel('Y[m]',fontsize=18)
plt.plot(X,Y,label = "xy_offseted.csv",marker='.',linewidth = 2.0,ms=10)
plt.plot(X2,Y2,label='xy_WGS84_offseted.csv',marker='.',linewidth = 2.0,ms=10)
#plt.plot(X,Y3,label=u'ページ数でランキング',marker='.',linewidth = 1.0,ms=10)
#plt.plot(X,Y,marker='.',linewidth = 6.0,ms=20)
#plt.plot(X,Y2,marker='.',linewidth = 4.0,ms=15)
#plt.plot(X,Y3,marker='.',linewidth = 2.0,ms=10)

#plt.plot(X,Y,marker='.')

#plt.plot(X,Y2,marker='.')
#plt.plot(X,Y3,marker='.')

#plt.ylim(0.0, 1.0)
#plt.xlim(0,90)
#plt.ylim(0,60)
#plt.legend(loc='lower right')
plt.legend() # 凡例を表示
plt.tick_params(labelsize=18)
plt.grid()
plt.savefig('data/plot.png',format = 'png', dpi=400)
#plt.plot(X,Y2,"r",label='confidence',marker='.')
plt.show()

