from LabOptic import *
from draw_methods import *
import matplotlib.pyplot as plt
import numpy as np
import time
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
ximc_z = Ximc(2)
ximc_x = Ximc(0)
ximc_y = Ximc(1) #0 - x, 1 - z (вверх низ), 2 - y
ant = Antaus()
# ant.set_base_divider(222)
# ant.set_freq_time(5)
# ant.set_power_trim(50)

speed = 10
ximc_z.connect()
cord_z = ximc_z.get_position()
ximc_z.set_speed(speed)
ximc_y.connect()
cord_y = ximc_y.get_position()
ximc_y.set_speed(speed)
ximc_x.connect()
cord_x = ximc_x.get_position()
ximc_x.set_speed(speed)


x_min= 0 #mkm
y_min = 0 #mkm
z_min  = 0 #mkm
x_max = 60 #mkm
y_max = 60 #mkm
z_max = 150 #mkm
x_step = 10 #mkm
y_step = 10 #mkm
z_step = 15 #mkm
x_list = np.arange(int(cord_x[0]),(int(cord_x[0]))+(x_max+x_step), x_step)
y_list = np.arange(int(cord_y[0]),(int(cord_y[0]))+(y_max+y_step),y_step)
z_list = np.arange(int(cord_z[0]),(int(cord_z[0]))+(z_max+z_step),z_step)


print(x_list)
print(z_list)
print(y_list)
aq_time = [1, 2, 3, 4, 5, 6]
power = [50, 40, 30, 20, 10, 5]

arr_step=1

full_list = []
for y in y_list:
    for x in x_list[::arr_step]:
        full_list.append([x,y])
    arr_step*=1
full_list = np.array(full_list)

plt.plot(full_list[:,0], full_list[:,1],'-o')
plt.show()
k = 0
p = 0
t=0

arr_step = 1

for i in y_list:
        ant.set_power_trim(power[p])
        ximc_y.move(int(i), cord_y[1])
        # ximc_y.disconnect()
        time.sleep(y_step/speed +0.1)
        t = 0

        for j in x_list[1::arr_step]:
            ximc_x.move(int(j), cord_x[1])
            time.sleep(x_step/speed + 0.1)
            ant.schutter_open()
            time.sleep(aq_time[t])
            ant.schutter_close()
            t += 1
        ximc_x.move(cord_x[0], cord_x[1])
        time.sleep((x_max+x_step)/speed +0.1)
        k +=1
        arr_step*=1
        p +=1
ant.schutter_close()
print(k)
