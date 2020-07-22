import sys
print('start')
import math

 

command_time = 0                        #反应时间
tolerance = 7                           #公差(标)
target_lat = 28.6602696                 #纬度
target_lng = 115.8430531                #经度



h=0                                     #高度
g=9.79                                  #加速度
i=0                                     #两点的距离(初始为零)
s=0                                     #gps计算的两点距离
fall_dist = 0                           #水瓶下落的水平距离
execute_dist = 0                        #反应时间走过的距离


def gps_distance(lat1, lon1, lat2, lon2):           #两点的经纬度
	radius_of_earth = 6371393                       #地球半径

#radians将x(角度)转成弧度
#sqrt 开方
#atan2返回y/x的正切
#asin返回x的反正弦
	from math import radians, cos, sin, sqrt, atan2,asin  
    #经纬度转换为弧度        
	lat1 = radians(lat1)
	lat2 = radians(lat2)
	lon1 = radians(lon1)
	lon2 = radians(lon2)               
	dLat = lat2 - lat1
	dLon = lon2 - lon1                                      #两点分别在东西方向和南北方向的弧度差

	a = sin(0.5*dLat)**2 + sin(0.5*dLon)**2 * cos(lat1) * cos(lat2)
       
	c = 2.0 * atan2(sqrt(a), sqrt(1.0-a))                    #两点间的弧度(角度)
	return radius_of_earth * c                               #返回两点的距离
    
while True:
    s=gps_distance(target_lat, target_lng, cs.lat, cs.lng )                                                    
    h = math.fabs(cs.alt)
    fall_dist = math.sqrt((2*(h)*(cs.groundspeed*cs.groundspeed))/g)    #水瓶水平运动路程
    execute_dist = (command_time/1000)*cs.groundspeed                   #反应时间运动路程
    s1 = fall_dist + execute_dist                                       #投水时到靶标的距离
    if(s!=i):                                                           #是否在靶标的正上方
        print"miss=",s-i                                                #打印相差多少
        print"alt:",cs.alt                                              #打印高度
        print"distance_threw",s-s1                                      #打印到投水点的距离
        print("---------------------")
    i=s  
    if(s-s1 <= tolerance):                                              #在误差范围内
        if(s-s1 < 0):                                                   #错过投水点
            Script.SendRC(5,1100,True)                                  #舵机(通道，1100~1900)，投水
            print"tune up the tolerance"                                #有点偏差
            break
            
        Script.Sleep(((s-s1)/(cs.groundspeed))*1000)                    #舵机休眠(毫秒)
        Script.SendRC(5,1100,True)
        print"bottle has been thrown successfully"
        break
    