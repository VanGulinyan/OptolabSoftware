# from LabOptic import * 
# from draw_methods import * 
# import time
# import numpy as np
 
# ximc_z = Ximc(1)  
# ximc_x = Ximc(0)  
# ximc_y = Ximc(2) #0 - x, 1 - z (вверх низ), 2 - y  
# ant = Antaus()  
# #ant.set_base_divider(177)  
# # ant.set_freq_time(1)  
# # ant.set_power_trim(40)  
 
# # speed in um/s
# speed_x = 15
# speed_y = 3000
# speed_z = 15

# # initializing stages
# ximc_y.connect() 
# ximc_z.connect() 
# ximc_x.connect() 
  
# # setting speed and getting current coordinates
# cord_x = ximc_x.get_position()  
# ximc_x.set_speed(speed_x)  
# cord_z = ximc_z.get_position()  
# ximc_z.set_speed(speed_z)  
# cord_y = ximc_y.get_position()  
# ximc_y.set_speed(speed_y)  

# # generation of coordinates for array
# dot_number=9
# x_min= 0 #mkm  
# y_min = 0 #mkm  
# z_min  = 0 #mkm  
# x_max = dot_number*15 #mkm  
# y_max = 2000 #mkm  
# z_max = dot_number*15 #mkm  
# x_step = 15 #mkm  
# y_step = 15 #mkm  
# z_step = 15 #mkm  
# x_list = np.arange(int(cord_x[0]),(int(cord_x[0]))+(x_max)+x_step, x_step)  
# z_list = np.arange(int(cord_z[0]),(int(cord_z[0]))+(z_max)+ z_step,z_step)  
# y_list = np.arange(int(cord_y[0]),(int(cord_y[0]))+(y_max),y_step)  
 
# print(x_list)  
# print(z_list)  
# print(y_list)  
 
 
# arr_step = 1  
# p = 0
# k = 0

# # power = [18,19,20,21,22,23,25,26,27] 
# # power = [22,25,28,32,35,38,42,45,48]
# power = [34,38,42,46,50,54,58,62,66]
# #power = [95,90,85,80,78,75,73,70,65] 
# #power=[16,14,12,10,8,6,4,2,1]
# #power=[5,15,20,25]
# # in %, array length should be equal to the number of rows
# #power = [1,3,5,7,9,11,13,17,19,21] # in %, array length should be equal to the number of rows
# #aq_time = [1,2,3,4,5] # in seconds, array length should be equal to the number of columns
# #divider = [50000,40000,33333,28571,25000,22222,20000,18182,16667,13333] 
# # to change basic frequency to 4,5,6,7,8,9,10,11,12,15 in Hz
# divider = [50000,33333,25000,20000,13333,10000,8000,6667,5000] 

# y_move = 150
# ximc_y.move(int(y_move+cord_y[0]), cord_y[0]) 
# time.sleep((y_move/3000)+1)

# for i in z_list[1:]: 
#     t = 0
#     ant.set_power_trim(power[p]) # uncomment to change power in all lines
#     #ant.set_freq_time(divider[k]) # uncomment to frequency in all lines
#     ximc_z.move(int(i), cord_z[1]) 
#     time.sleep(z_step/speed_z + 0.5)      # (расстояние между точкам / скорость) + 0.5сек 
#     for j in x_list[1::arr_step]: 
#         ximc_x.move(int(j), cord_x[1])
#         ant.set_freq_time(divider[k]) #uncomment if u want to change freq every dot
#         k += 1 #uncomment if u want to change freq every dot
#         time.sleep(x_step/speed_x)    # таймаут на перемещение 
#         ant.schutter_open() 
#         time.sleep(1)    # длительность открытого шаттера 
#         # time.sleep(aq_time[t]) # uncomment to change aquisition time in each point
#         ant.schutter_close()
#         #t +=1 
#     ximc_x.move(cord_x[0], cord_x[1])
#     k = 0 #uncomment if you want to change freq every dot in a line 
    
#     time.sleep((x_max+x_step)/speed_x+0.1)  # таймаут на перемещение
    
#     p += 1
#     #k += 1
#     arr_step*=1 # change to -1 if snake-like array
# ant.schutter_close() 

# ximc_y.move(cord_y[0], cord_y[1]) 
# time.sleep((y_move/3000)+1)
# print('End program')

#____________________________________________________
#在更改坐标台后需要的代码

from LabOptic import * 
from draw_methods import * 
import time
import numpy as np
 
ximc_z = Ximc(1)  
ximc_x = Ximc(0)  
ximc_y = Ximc(2) #0 - x, 1 - z (вверх низ), 2 - y  
ant = Antaus()  
#ant.set_base_divider(177)  
# ant.set_freq_time(1)  
# ant.set_power_trim(40)  
 
# speed in um/s
speed_z = 15
speed_y = 15
speed_x = 15

# initializing stages
ximc_y.connect() 
ximc_z.connect() 
ximc_x.connect() 
  
# setting speed and getting current coordinates
cord_z = ximc_z.get_position()  
ximc_z.set_speed(speed_z)  
cord_x = ximc_x.get_position()  
ximc_x.set_speed(speed_x)  
cord_y = ximc_y.get_position()  
ximc_y.set_speed(speed_y)  

# generation of coordinates for array
dot_number=9
z_min= 0 #mkm  
y_min = 0 #mkm  
x_min  = 0 #mkm  
z_max = dot_number*10 #mkm  
y_max = dot_number*10 #mkm  
x_max = dot_number*10 #mkm  
z_step = 10 #mkm  
y_step = 10 #mkm  
x_step = 10 #mkm  
z_list = np.arange(int(cord_z[0]),(int(cord_z[0]))+(z_max)+z_step,z_step)  
x_list = np.arange(int(cord_x[0]),(int(cord_x[0]))+(x_max)+x_step,x_step)  
y_list = np.arange(int(cord_y[0]),(int(cord_y[0]))+(y_max)+y_step,y_step)  
 
# print(z_list)  
# print(x_list)  
# print(y_list)  
 
k=0 
arr_step = 1  

# power = [18,19,20,21,22,23,24,25,26,27] 
# power = [24,26,28,30,32,34,36,38,40]
# power = [13,14,15,16,17,18,19,20,21]
power = [30,31,32,33,34,35,36,37,38]
#power=[16,14,12,10,8,6,4,2,1]
#power=[5,15,20,25]
# power = [38,39,40,41,42,43,44,45,46] 
# in %, array length should be equal to the number of rows
# power = [1,3,5,7,9,11,13,17,19] # in %, array length should be equal to the number of rows
#aq_time = [1,2,3,4,5] # in seconds, array length should be equal to the number of columns
#divider = [50000,40000,33333,28571,25000,22222,20000,18182,16667,13333] 
# to change basic frequency to 4,5,6,7,8,9,10,11,12,15 in Hz
divider = [50000,33333,25000,20000,13333,10000,6667,5000,4000] 

y_move = -160
ximc_y.move(int(y_move+cord_y[0]), cord_y[0]) 
time.sleep((y_move/3000)+1)
p=0
for i in x_list[1:]: 
    t = 0
    ant.set_power_trim(power[p]) # uncomment to change power in all lines
    #ant.set_freq_time(divider[k]) # uncomment to frequency in all lines
    ximc_x.move(int(i), cord_x[1]) 
    time.sleep(x_step/speed_x + 0.5)      # (расстояние между точкам / скорость) + 0.5сек 
    for j in z_list[1::arr_step]: 
        ximc_z.move(int(j), cord_z[1])
        ant.set_freq_time(divider[k]) #uncomment if u want to change freq every dot
        k += 1 #uncomment if u want to change freq every dot
        time.sleep(z_step/speed_z)    # таймаут на перемещение 
        ant.schutter_open() 
        time.sleep(1)    # длительность открытого шаттера 
        # time.sleep(aq_time[t]) # uncomment to change aquisition time in each point
        ant.schutter_close()
        #t +=1 
    ximc_z.move(cord_z[0], cord_z[1])
    k = 0 #uncomment if you want to change freq every dot in a line 
    
    time.sleep((z_max+z_step)/speed_z+0.1)  # таймаут на перемещение
    
    p += 1
    #k += 1
    arr_step*=1 # change to -1 if snake-like array
ant.schutter_close() 

ximc_y.move(cord_y[0], cord_y[1]) 
time.sleep((y_move/3000)+1)
print('End program')


