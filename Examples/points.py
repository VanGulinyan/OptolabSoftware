from LabOptic import *
from draw_methods import *
import time

#antaus = Antaus() 
#antaus.schutter_open() 
 
# Выключение лазера 
#antaus = Antaus() 
#antaus.schutter_close() 
 
# Изменение параметров лазера 
#antaus = Antaus() 
#antaus.set_base_divider(new_base_divider) 
#antaus.set_freq_time(new_freg_time) 
#antaus.set_power_trim(new_power) 
 
# Сдвинуть подвижку (Ximc) на 100 
ximc_z = Ximc(1) 
ximc_x = Ximc(0) 
ximc_y = Ximc(2) #0 - x, 1 - z (вверх низ), 2 - y 
ant = Antaus() 
# ant.set_base_divider(177) 
# ant.set_freq_time(1) 
# ant.set_power_trim(40) 

power = [1 + i for i in range(0,6)]
speed_x = 10
speed_y = 10
speed_z = 10
ximc_y.connect()
ximc_z.connect()
ximc_x.connect()
 
# ant.schutter_open() 
# time.sleep(4) 
# ant.schutter_close() 
# ximc_x.connect() 
# ximc_x.get_position() 
# ximc_x.move(20) 
# ximc_x.disconnect() 
# ximc_z.connect() 
cord_x = ximc_x.get_position() 
ximc_x.set_speed(speed_x) 
cord_z = ximc_z.get_position() 
ximc_z.set_speed(speed_z) 
# ximc_z.disconnect() 
# ximc_x.connect() 
# ximc_x.disconnect() 
# ximc_y.connect() 
# cord_y = ximc_y.get_position() 
# ximc_y.set_speed(10) 
# ximc_y.disconnect() 
 
x_min= 0 #mkm 
y_min = 0 #mkm 
z_min  = 0 #mkm 
x_max = 30 #mkm 
# y_max = 75 #mkm 
z_max = 30 #mkm 
x_step = 5 #mkm 
# y_step = 15 #mkm 
z_step = 5 #mkm 
x_list = np.arange(int(cord_x[0]),(int(cord_x[0]))+(x_max)+x_step, x_step) 
z_list = np.arange(int(cord_z[0]),(int(cord_z[0]))+(z_max)+ z_step,z_step) 
# y_list = np.arange(int(cord_y[0]),(int(cord_y[0]))+(y_max),y_step) 

print(x_list) 
print(z_list) 
# print(y_list) 

# aq_time = [6, 5, 4, 3, 2] 
# power = [70, 60, 50, 40, 30, 20] 
# arr_step=1 
# k = 0 
# p = 0 
# t=0 
 
 
# arr_step = 1 
# ximc_y.connect() 
# ximc_x.connect() 
 
# for i in y_list: 
#         ant.set_power_trim(power[p]) 
#         ximc_y.connect() 
#         ximc_y.move(int(i), cord_y[1]) 
#         ximc_y.disconnect() 
#         time.sleep(2) 
#         ximc_x.connect() 
#         t = 0 
#         for j in x_list[1::arr_step]: 
#             ximc_x.move(int(j), cord_x[1]) 
#             time.sleep(2) 
#             ant.schutter_open() 
#             time.sleep(aq_time[t]) 
#             ant.schutter_close() 
#             t += 1 
#             ximc_x.disconnect() 
#         k += 1 
#         arr_step*=1 
#         p += 1 
# ant.schutter_close() 
# print(k)

arr_step = 1 
k = 0

for i in z_list[1:]:
    ximc_z.move(int(i), cord_z[1])
    time.sleep(z_step/speed_z + 0.1)      #(расстояние между точкам / скорость) + 0.5сек
    for j in x_list[1::arr_step]:
        ximc_x.move(int(j), cord_x[1])
        time.sleep(x_step/speed_x+0.5)    #таймаут на перемещение
        ant.schutter_open()
        time.sleep(0.1)    #длительность открытого шаттера
        ant.schutter_close()
    ximc_x.move(cord_x[0], cord_x[1])
    
    time.sleep((x_max+x_step)/speed_x+0.1)
    
    k += 1
    arr_step*=1
ant.schutter_close()
print(k)