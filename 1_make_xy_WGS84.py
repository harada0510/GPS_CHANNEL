# -*- coding: utf-8 -*-
import numpy as np

A_SEMIMAJOR_AXIS = 6378137.0;
F_FLATTENING = 1.0 / 298.257223563;
B_SEMIMINOR_AXIS = 6356752.3142;
# second eccentricity squared
ESQ_DASH = (A_SEMIMAJOR_AXIS**2 - B_SEMIMINOR_AXIS**2) / B_SEMIMINOR_AXIS**2;
# eccentricity squared
ESQ = 2 * F_FLATTENING - F_FLATTENING**2;    
 
 
def calculateNlat( lat ):
    return A_SEMIMAJOR_AXIS / np.sqrt( 1 - ( ESQ * np.sin( np.radians( lat ) )**2 ) );

def lla2ecef( lat, lon, alt ):
    # check for bad values
    if lat < -90 or lat > 90 or lon < -180 or lon > 180:
        return None
    N = calculateNlat( lat );
    x = (N + alt) * np.cos( np.radians( lat ) ) * np.cos( np.radians( lon ) );
    y = (N + alt) * np.cos( np.radians( lat ) ) * np.sin( np.radians( lon ) );
    z = ((N * (1 - ESQ)) + alt) * np.sin( np.radians( (lat) ) );
    return x, y, z
   

def ecef2lla( x, y, z ):
    lat = 0.0;
    lon = 0.0;
    alt = 0.0;
    # if it is one of the poles, no need to compute
    if x == 0 and y == 0:
        lon = 0.0;
        if z > 0:
            lat = 90;
            alt = z - B_SEMIMINOR_AXIS;
        else:
            lat = -90;
            alt = z + B_SEMIMINOR_AXIS;
        return lat, lon, alt

    p = np.sqrt( x**2 + y**2 );
    # parametric latitude of point p
    theta = np.arctan2( (z * A_SEMIMAJOR_AXIS), (p * B_SEMIMINOR_AXIS) );
    lat = np.rad2deg( np.arctan2( (z + (ESQ_DASH * B_SEMIMINOR_AXIS * \
        np.power( np.sin( theta ), 3 ))), (p - (ESQ * A_SEMIMAJOR_AXIS * \
        np.power( np.cos( theta ), 3 ))) ) );
    lon = np.rad2deg( np.arctan2( y, x ) );
    alt = (p / np.cos( np.radians( lat ) )) - calculateNlat( lat );
    return lat, lon, alt;

# for the test below
#lat, lon, alt = 36.31915174185337,  139.84288610607962, 0
#x,y,z = lla2ecef(lat, lon, alt)
#print x,y,z
#lat, lon, alt = ecef2lla(x,y,z)
#print lat,lon,alt


def rotate(x,y,deg):
	cos = np.cos(deg)
	sin = np.sin(deg)
	rot_x = (x * cos) - (y * sin)
	rot_y = (x * sin) + (y * cos)
	return rot_x, rot_y


#filename = raw_input('please enter the file name\n--->')
a = open('data/output.csv','r')
b = open('data/xy_WGS84.csv','w')
b.write('marker,x,y\n')
num = 0
for i in a:
    if num >= 1:
        LINE = i.rstrip().replace('"','').split(',')
        marker = LINE[0]
        lat    = float(LINE[1])
        lon    = float(LINE[2])
        alt    = 0.0
        x, y, Z   = lla2ecef(lat, lon, alt)
	deg = np.deg2rad(135) # edit here to change the degree
	rot_x, rot_y      = rotate(-x,y,deg)  # rotate the point for plotting with xy_offseted.csv
        b.write(marker+','+ str(rot_x) +','+ str(rot_y) +'\n')
	print marker, rot_x, rot_y
    num+=1
a.close()	
b.close()

