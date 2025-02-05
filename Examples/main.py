from LabOptic import *
from draw_methods import *

# Включение лазера 
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
# ximc_z = Ximc(1)
# ximc_x = Ximc(0)
# ximc_y = Ximc(2) #0 - x, 1 - z (вверх низ), 2 - y
# ant = Antaus()
# ant.set_base_divider(222)
# ant.set_freq_time(20000)
# ant.set_power_trim(3)
# power = [1 + i for i in range(0, 6)]

# ximc_y.connect()
# ximc_z.connect()

# ximc_x.connect()


# #ximc_z.connect()
# cord_z = ximc_z.get_position()
# ximc_z.set_speed(2)
# # ximc_z.disconnect()
# # ximc_x.connect()
# cord_x = ximc_x.get_position()
# ximc_x.set_speed(2)
# # ximc_x.disconnect()
# # ximx_y.connect()
# cord_y = ximc_y.get_position()
# ximc_y.set_speed(2)
# # ximx_y.disconnect()

# x_min= 0 #mkm
# y_min = 0 #mkm
# z_min  = 0 #mkm
# x_max = 10 #mkm
# y_max = 10 #mkm
# z_max = 10 #mkm
# x_step = 1 #mkm
# y_step = 1 #mkm
# z_step = 1 #mkm
# x_list = np.arange(int(cord_x[0]),(int(cord_x[0]))+(x_max+x_step), x_step)
# z_list = np.arange(int(cord_z[0]),(int(cord_z[0]))+(z_max+z_step),z_step)
# y_list = np.arange(int(cord_y[0])+y_step,(int(cord_y[0]))+(y_max+y_step),y_step)
# print(x_list)
# print(z_list)
# print(y_list)

# # ximc_z.connect()
# # ximc_z.move(cord_z[0]+120, cord_z[1])
# # ximc_z.disconnect()


# arr_step=1
# k = 0
# for i in z_list:
#         # ximc_x.connect() 
#         # ant.schutter_open()   
#         # ximc_z.connect()
#         # ximc_z.move(int(i), cord_z[1])
#         # ximc_z.disconnect()
#         for j in x_list[::arr_step]: 
#             ximc_x.move(int(j), cord_x[1])
#             time.sleep(x_step/2)
#             ant.schutter_open()
#             time.sleep(0.5)
#             ant.schutter_close()
#         time.sleep(1)
#         # ant.schutter_close()
#         # ximc_x.move(cord_x[0], cord_x[1])
#         # ximc_x.disconnect()    
#         # ximx_y.connect()
#         ximc_z.move(int(i), cord_z[1])
#         # ximx_y.disconnect()
#         #ant.set_power_trim(power[k+1])
#         k +=1


#         arr_step*=-1
# ant.schutter_close()
array_of_circles_Pesa([10,10],4, 2, 20)

'''

# Line
ximc_x.connect()
coor = ximc_x.get_position()
k = 0
ant.schutter_open()
for i in range(1, len(power)):
    ximc_x.move(coor[0]+i*2,coor[1])
    ant.set_power_trim(power[k])
    time.sleep(0.25)
    k+=1
ant.schutter_close()
ximc_x.disconnect()
'''
# Пример использования метода из draw_methods
#antaus = Antaus()
#circle_Pesa(antaus, 10, 40, 40)'''