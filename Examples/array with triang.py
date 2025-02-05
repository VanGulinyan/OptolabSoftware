from LabOptic import * 
from draw_methods import * 
import time
import numpy as np

# XIMC connection
# DO NOT CHANGE!
ximc_y = Ximc(1)  
ximc_x = Ximc(0)  
ximc_z = Ximc(2) #0 - x, 1 - z (вверх низ), 2 - y  

# Antaus setup
# base_divider = 222 # from 177 to 222
#freq = 10  # freq you need, min 4 Hz
#main_power = 14 # power in %

ant = Antaus()
# # ant.set_base_divider(base_divider)  
# ant.set_freq_time(44.4 * 10 ** 6 / 222 / freq)  
# ant.set_power_trim(main_power)  
 
# speed in um/s
speed_y = 10 
speed_z = 60 
speed_x = 10 

# initializing stages
ximc_z.connect() 
ximc_y.connect() 
ximc_x.connect() 
  
# setting speed and getting current coordinates
cord_x = ximc_x.get_position()  
ximc_x.set_speed(speed_x)  
cord_z = ximc_z.get_position()  
ximc_z.set_speed(speed_z)  
cord_y = ximc_y.get_position()  
ximc_y.set_speed(speed_y)  

# generation of coordinates for array
x_min= 0 #mkm  
y_min = 0 #mkm  
z_min  = 0 #mkm  
x_max = 30 #mkm  
y_max = 30 #mkm  
z_max = 30 #mkm  
x_step = 5 #mkm  
y_step = 5 #mkm  
z_step = 5 #mkm  
x_list = np.arange(int(cord_x[0]),(int(cord_x[0]))+(x_max)+x_step, x_step)  
z_list = np.arange(int(cord_z[0]),(int(cord_z[0]))+(z_max)+ z_step,z_step)  
y_list = np.arange(int(cord_y[0]),(int(cord_y[0]))+(y_max),y_step)  
 
print(x_list)  
print(z_list)  
print(y_list)  
 
# aq_time = [6, 5, 4, 3, 2]  
# power = [70, 60, 50, 40, 30, 20]  
arr_step=1  
k = 0  
p = 0  
t=0  
 
arr_step = 1  
p = 0

def fitPLaneLTSQ(XYZ):
    # Fits a plane to a point cloud,
    # Where Z = aX + bY + c        ----Eqn #1
    # Rearanging Eqn1: aX + bY -Z +c =0
    # Gives normal (a,b,-1)
    # Normal = (a,b,-1)
    XYZ=np.array(XYZ)
    [rows,cols] = XYZ.shape
    G = np.ones((rows,3))
    G[:,0] = XYZ[:,0]  #X
    G[:,1] = XYZ[:,1]  #Y
    Z = XYZ[:,2]
    (a,b,c),resid,rank,s = np.linalg.lstsq(G,Z)
    return (a, b, c)

#calibrate калибровка по текущему положению стола
# calibr_xyz = [] #задаем, если уже калибровали
# def calibrate(calibr_xyz):
#     if calibr_xyz==[]:
#         print("Калибровка: введите что-то чтобы добавить точку, 0 чтобы закончить")
#         s=input()
#         while s!='0':
#             #вводим текущие координаты стола, предварительно настраиваимся по точкам
#             x, y, z = (ximc_x.get_position(), ximc_y.get_position(), ximc_z.get_position()) #задаем в формате (steps, microsteps) ?????
#             cord_xyz = (x[0], z[0], y[0]) #пока steps
#             calibr_xyz.append(cord_xyz)
#             s=input()
#     #a, b, c = fitPLaneLTSQ(xyz)
#     return fitPLaneLTSQ(calibr_xyz)
# # a, b, c = calibrate(calibr_xyz)
# a, b, c = (-7.784114226138603e-14, -5.040412531798211e-14, 6757.000000000366)
# print(a, b, c)
# print("---------------------------------------------------------")

# z_i=a*x_i+b*y_i+c #=z_fromXY(x_i, y_i)

power = [1,2,3,4,5] # in %, array length should be equal to the number of rows
aq_time = [1,2,3,4,5] # in seconds, array length should be equal to the number of columns

for i in z_list[1:]: 
    t = 0
    # ant.set_power_trim(power[p]) # uncomment to change power in all lines
    ximc_z.move(int(i), cord_z[1]) 
    time.sleep(z_step/speed_z + 0.1)      # (расстояние между точкам / скорость) + 0.1 сек 
    for j in x_list[1::arr_step]: 
        ximc_x.move(int(j), cord_x[1]) 
        # ximc_y.move(int(a*j+b*i+c), cord_y[1])
        time.sleep(x_step/speed_x + 0.1)    # таймаут на перемещение 
        
        ant.schutter_open()
        time.sleep(0.12)    # длительность открытого шаттера 
        # time.sleep(aq_time[t]) # uncomment to change aquisition time in each point
        ant.schutter_close()
        t +=1 
    ximc_x.move(cord_x[0], cord_x[1]) 
    
    time.sleep((x_max+x_step)/speed_x+0.1)  # таймаут на перемещение
    
    p += 1 
    arr_step*=1 # change to -1 if snake-like array
# ant.schutter_close() 
