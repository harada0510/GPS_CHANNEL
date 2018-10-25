# -*- coding: utf-8 -*-
import numpy as np


def rotate(x,y,deg):
	cos = np.cos(deg)
	sin = np.sin(deg)
	rot_x = (x * cos) - (y * sin)
	rot_y = (x * sin) + (y * cos)
	return rot_x, rot_y


a = open('data/xy_offseted.csv','r')
b = open('data/xy_rotated.csv','w')
b.write('marker,x_rotated,y_rotated\n')
num = 0
for i in a:
    if num >= 1:
        LINE = i.rstrip().replace('"','').split(',')
        marker = LINE[0]
        x    = float(LINE[1])
        y    = float(LINE[2])
	dis  = LINE[3]
	deg = np.deg2rad(90) # edit here to change the degree
	rot_x, rot_y      = rotate(x,-y,deg)  # rotate the point for plotting with xy_offseted.csv
        b.write(marker+','+ str(rot_x) +','+ str(rot_y) + ','+dis+'\n')
	print marker, rot_x, rot_y
    num+=1
a.close()	
b.close()



c = open('data/xy_WGS84_offseted.csv','r')
d = open('data/xy_WGS84_rotated.csv','w')
num = 0
for i in c:
    if num >= 1:
        LINE = i.rstrip().replace('"','').split(',')
        marker = LINE[0]
        x    = float(LINE[1])
        y    = float(LINE[2])
        dis  = LINE[3]
        deg = np.deg2rad(135) # edit here to change the degree
        rot_x, rot_y      = rotate(x,y,deg)  # rotate the point for plotting with xy_offseted.csv
        d.write(marker+','+ str(rot_x) +','+ str(rot_y) + ','+dis+'\n')
        print marker, rot_x, rot_y
    num+=1
c.close() 
d.close() 
