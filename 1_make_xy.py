#coding:utf-8
import math
import numpy as np
import pyproj

def convert(lat, lon):
	EPSG4612 = pyproj.Proj("+init=EPSG:4612")
	EPSG2451 = pyproj.Proj("+init=EPSG:2451")
	y,x = pyproj.transform(EPSG4612, EPSG2451, lon,lat)
	print x,y
	return x,y


#filename = raw_input('please enter the file name\n--->')
a = open('data/output.csv','r')
b = open('data/xy.csv','w')
b.write('marker,x,y\n')
num = 0
for i in a:
	if num >= 1:
		LINE = i.rstrip().replace('"','').split(',')
		marker = LINE[0]
		lat    = float(LINE[1])
		lon    = float(LINE[2])
		x, y   = convert(lat, lon)
		b.write(marker+','+ str(x) +','+ str(y) +'\n')
	num+=1
a.close()	
b.close()
