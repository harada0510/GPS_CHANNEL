#coding:utf-8
import math
import numpy as np

def convert(offset_x,offset_y,x,y,pre_X,pre_Y,distance):
	X = x - offset_x
	Y = y - offset_y
	#print X,Y,distance
	dif = math.sqrt((X-pre_X)**2 + (Y-pre_Y)**2)
	distance += dif
	#print X,Y,int(distance)
	return X,Y,distance


#filename = raw_input('please enter the input file name\n--->')
#filename2 = raw_input('please enter the output file name\n--->')
a = open('data/xy_WGS84.csv','r')
b = open('data/xy_WGS84_offseted.csv','w')
b.write('marker,x_offseted[m],y_offseted[m],distance[m]\n')
num = 0
offset_x = 0.0
offset_y = 0.0
pre_X    = 0.0
pre_Y    = 0.0
distance = 0.0
for i in a:
	if num >= 1:
		LINE = i.rstrip().replace('"','').split(',')
		marker = LINE[0]
		x    = float(LINE[1])
		y    = float(LINE[2])
		X,Y  = 0.0, 0.0
		if num==1:
			offset_x = x
			offset_y = y
		else:
			X, Y, distance   = convert(offset_x,offset_y,x,y,pre_X,pre_Y,distance)
		print marker,X,Y,int(distance)
		b.write(marker+','+str(X)+','+str(Y)+','+str(int(distance))+'\n')
		pre_X, pre_Y = X, Y
	num+=1
a.close()	
b.close()
