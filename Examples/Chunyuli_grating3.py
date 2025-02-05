# from LabOptic import * #导入LabOptic配置
# from draw_methods import * #导入Drwa配置
# import time
# import numpy as np


# # Изменение параметров лазера #改变激光参数
# #antaus = Antaus()
# #antaus.set_base_divider(new_base_divider) #基础频率（177，222）
# #antaus.set_freq_time(new_freg_time) #除数，用来改变激光输出频率
# #antaus.set_power_trim(new_power) #输出功率百分比

# # Сдвинуть подвижку (Ximc) на 100
# ximc_y = Ximc(1)
# ximc_x = Ximc(0)
# ximc_z = Ximc(2) #0 - x, 1 - z (вверх низ), 2 - y


# ant = Antaus()
# ant.set_base_divider(222)
# ant.set_freq_time(400)
# ant.set_power_trim(29)

# #power = [1 + i for i in range(0, 6)]

# ximc_z.connect()
# ximc_y.connect()
# ximc_x.connect()

# #get current coordinate of each axis and set speed with "set_speed(n), where n -- the speed in um/s"

# speed_moving = 2500 #影响单位面积内的脉冲数

# cord_x = ximc_x.get_position()
# x_speed = 40
# ximc_x.set_speed(x_speed)
# cord_z = ximc_z.get_position()
# z_speed = speed_moving
# ximc_z.set_speed(z_speed)
# cord_y = ximc_y.get_position()
# ximc_y.set_speed(3000)

# x_step = 2 #mkm
# y_step = 5 #mkm
# z_step = 2 #mkm

# #scaning like a grating
# number_of_repeat = 750 #how many lines in the grating *2
# scanning_time = 1 #for 1 line scaning how many times

# x_min= 0 #mkm
# y_min = 0 #mkm
# z_min  = 0 #mkm
# x_max = x_step*number_of_repeat #mkm
# y_max = 1000 #mkm Real Z direction
# z_max = 3000 #mkm Real Y direction

# #step for each axis
# x_list = np.arange(int(cord_x[0]),(int(cord_x[0]))+(x_max+x_step),x_step) # np.arange (start, stop, step)
# z_list = np.arange(int(cord_z[0]),(int(cord_z[0]))+(z_max+z_step),z_max) #stop的值不包含在数组中
# y_list = np.arange(int(cord_y[0]),(int(cord_y[0]))+(y_max+y_step),y_max)
# # print(x_list) #作为提示
# # print(z_list) #作为提示
# # print(y_list)

# arr_step=1
# k = 0

# # y_move = 150 #make z diection move down X um
# # ximc_y.move(int(y_move+cord_y[0]), cord_y[0]) 
# # time.sleep(y_move/3000)


# # power = [45,46,47,48,49,50]

# t=1

# # while t <= number_of_repeat:

# #         for i in x_list[1:]:
# #             ant.set_power_trim(38)
# #             # ant.set_power_trim(power[k])
# #             ximc_x.move(int(i), cord_x[1]) 
# #             time.sleep(x_step/x_speed+1)

# #             st = 1
# #             while st <= scanning_time:
# #                   ximc_z.move(int(1), cord_z[0]) 
# #                   time.sleep(1.3)
# #                   ant.schutter_open() 
# #                   time.sleep((z_max)/speed_moving)   
# #                   ant.schutter_close()
# #                   ximc_z.move(cord_z[0], cord_z[1]) 
# #                   time.sleep((z_max/z_speed)+5.3)
# #                   print('__________________________',t,st)
# #                   st+=1
# #             t+=1
# #             # k+=1
# # ant.schutter_close()

# while t <= number_of_repeat:
#          ximc_x.move(int(cord_x[0]-x_step),cord_x[1])
#          time.sleep(x_step/x_speed +1)

#          ximc_z.move(cord_z[0]+z_max,cord_z[1])
#          time.sleep(1)
#          ant.schutter_open() 
#          time.sleep(z_max/z_speed+1)
#          ant.schutter_close()

#          ximc_x.move(int(cord_x[0]-2*x_step),cord_x[1])
#          time.sleep(x_step/x_speed)

#          ximc_z.move(cord_z[0],cord_z[1])
#          time.sleep(1)
#          ant.schutter_open() 
#          time.sleep(z_max/z_speed)
#          ant.schutter_close()
 
#          cord_x=ximc_x.get_position()
#          print('__________________________',t)
#          t +=1
# ant.schutter_close

                   
# # ximc_y.move(cord_y[0], cord_y[1]) 
# # time.sleep(y_move/3000)
# print('End program')

# _______________________________________________________________

from LabOptic import * #导入LabOptic配置
from draw_methods import * #导入Drwa配置
import time
import numpy as np


# Изменение параметров лазера #改变激光参数
#antaus = Antaus()
#antaus.set_base_divider(new_base_divider) #基础频率（177，222）
#antaus.set_freq_time(new_freg_time) #除数，用来改变激光输出频率
#antaus.set_power_trim(new_power) #输出功率百分比

# Сдвинуть подвижку (Ximc) на 100
ximc_z = Ximc(1)
ximc_x = Ximc(0)
ximc_y = Ximc(2) #0 - x, 1 - z (вверх низ), 2 - y


ant = Antaus()
ant.set_base_divider(222)
ant.set_freq_time(400)
ant.set_power_trim(40)

#power = [1 + i for i in range(0, 6)]

ximc_y.connect()
ximc_z.connect()
ximc_x.connect()

#get current coordinate of each axis and set speed with "set_speed(n), where n -- the speed in um/s"

speed_moving = 900 #影响单位面积内的脉冲数

cord_x = ximc_x.get_position()
x_speed = speed_moving
ximc_x.set_speed(x_speed)
cord_z = ximc_z.get_position()
z_speed = 20
ximc_z.set_speed(z_speed)
cord_y = ximc_y.get_position()
ximc_y.set_speed(1000)

x_step = 3 #mkm
y_step = 5 #mkm
z_step = 2.8 #mkm

#scaning like a grating
number_of_repeat = 5 #how many lines in the grating *2
scanning_time = 1 #for 1 line scaning how many times

x_min= 0 #mkm
y_min = 0 #mkm
z_min  = 0 #mkm
z_max = z_step*number_of_repeat #mkm
y_max = 1500 #mkm Real Z direction
x_max = 3500 #mkm Real Y direction

#step for each axis
x_list = np.arange(int(cord_x[0]),(int(cord_x[0]))+(x_max+x_step),x_max) # np.arange (start, stop, step)
z_list = np.arange(int(cord_z[0]),(int(cord_z[0]))+(z_max+z_step),z_step) #stop的值不包含在数组中
y_list = np.arange(int(cord_y[0]),(int(cord_y[0]))+(y_max+y_step),y_max)
# # print(x_list) #作为提示
# print(z_list) #作为提示
# print(y_list)

arr_step=1
k = 1

y_move = 170 #make z diection move down X um
# y_move = 102 #make z diection move down X um

ximc_y.move(int(y_move+cord_y[0]), cord_y[0]) 
time.sleep(1)


t=1

# while t <= number_of_repeat:
#         cord_z_c = ximc_z.get_position()
#         # for i in z_list[1:]:
#         ximc_z.move(cord_z_c[0]+z_step, cord_z[1]) 
#         time.sleep(z_step/z_speed+1)
#         st = 1
#         while st <= scanning_time:
#               # ximc_z.move(cord_z[0]+z_max,cord_z[1])
#               ximc_x.move(int(1), cord_x[0]) 
#               time.sleep(1.3)
#               ant.schutter_open() 
#               time.sleep((x_max)/speed_moving)   
#               ant.schutter_close()
#               ximc_x.move(cord_x[0], cord_x[1]) 
#               time.sleep((x_max/x_speed)+4.3)
#               print('__________________________',t,st)
#               st+=1
#               k+=1
#         t+=1
# ant.schutter_close()

#dobule side scanning__________________________________

while t <= number_of_repeat:
         ximc_z.move(int(cord_z[0]-z_step),cord_z[1])
         time.sleep(z_step/z_speed +1)

         ximc_x.move(cord_x[0]+x_max,cord_x[1])
         time.sleep(1)
         ant.schutter_open() 
         time.sleep(x_max/x_speed+1)
         ant.schutter_close()

         ximc_z.move(int(cord_z[0]-2*z_step),cord_z[1])
         time.sleep(z_step/z_speed)

         ximc_x.move(cord_x[0],cord_x[1])
         time.sleep(1)
         ant.schutter_open() 
         time.sleep(x_max/x_speed+1)
         ant.schutter_close()
 
         cord_z=ximc_z.get_position()
         print('__________________________',t)
         t +=1
ant.schutter_close

# while t <= number_of_repeat:
#          ximc_x.move(int(cord_x[0]-x_step),cord_x[1])
#          time.sleep(x_step/x_speed+1)

#          ximc_z.move(cord_z[0]+z_max,cord_z[1])
#          time.sleep(0.5)
#          ant.schutter_open() 
#          time.sleep(z_max/z_speed)
#          ant.schutter_close()

#          ximc_x.move(int(cord_x[0]-2*x_step),cord_x[1])
#          time.sleep(x_step/x_speed+1)

#          ximc_z.move(cord_z[0],cord_z[1])
#          time.sleep(0.5)
#          ant.schutter_open() 
#          time.sleep(z_max/z_speed)
#          ant.schutter_close()
 
#          cord_x=ximc_x.get_position()
#          print('__________________________',t)
#          t +=1
# ant.schutter_close

                   

ximc_y.move(cord_y[0], cord_y[1]) 
time.sleep(1)

print('End program')