from LabOptic import * #导入LabOptic配置
from draw_methods import * #导入Drwa配置

# Включение лазера 
#antaus = Antaus()
#antaus.schutter_open() #打开激光

# Выключение лазера
#antaus = Antaus()
#antaus.schutter_close() #关闭激光

# Изменение параметров лазера #改变激光参数
# antaus = Antaus()
#antaus.set_base_divider(new_base_divider) #基础频率（177，222）
#antaus.set_freq_time(new_freg_time) #除数，用来改变激光输出频率
#antaus.set_power_trim(new_power) #输出功率百分比

# Сдвинуть подвижку (Ximc) на 100
ximc_z = Ximc(1)
ximc_x = Ximc(0)
ximc_y = Ximc(2) #0 - x, 1 - z (вверх низ), 2 - y
ant = Antaus()
ant.set_base_divider(222)
ant.set_freq_time(2000)
ant.set_power_trim(5)
#power = [1 + i for i in range(0, 6)]

ximc_y.connect()
ximc_z.connect()
ximc_x.connect()

#get current coordinate of each axis and set speed with "set_speed(n), where n -- the speed in um/s"

speed_moving = 100 #影响单位面积内的脉冲数

cord_x = ximc_x.get_position()
x_speed = 40
ximc_x.set_speed(x_speed)
cord_z = ximc_z.get_position()
z_speed = speed_moving
ximc_z.set_speed(z_speed)
cord_y = ximc_y.get_position()
ximc_y.set_speed(3000)

#sizes of working area
number_of_lines = 4
x_step = 10 #mkm
y_step = 5 #mkm
z_step = 10 #mkm

x_min= 0 #mkm
y_min = 0 #mkm
z_min  = 0 #mkm
x_max = x_step*number_of_lines #mkm
y_max = 230 #mkm
z_max = 200 #mkm
# x_max = 30 #mkm
# y_max = 30 #mkm
# z_max = 30 #mkm

#step for each axis
x_list = np.arange(int(cord_x[0]),(int(cord_x[0]))+(x_max+x_step),x_step) # np.arange (start, stop, step)
z_list = np.arange(int(cord_z[0]),(int(cord_z[0]))+(z_max+z_step),z_max) #stop的值不包含在数组中
y_list = np.arange(int(cord_y[0]),(int(cord_y[0]))+(y_max+y_step),y_max)
print(x_list) #作为提示
print(z_list) #作为提示
print(y_list)

#power = [30,29,28,27,26,25,24,23,22,21]
#power = [21,21,20,20,19,19,18,18]
power = [12,12,12,12]

arr_step=1
k = 0

y_move = 150
ximc_y.move(int(y_move+cord_y[0]), cord_y[0]) 
# ximc.dis
# scanning area like grating
time.sleep(y_move/3000)

for i in x_list[1:]:
        ant.set_power_trim(power[k])
        ximc_x.move(int(i), cord_x[1]) 
        time.sleep(x_step/x_speed+1)
        ant.schutter_open() #激光打开
        ximc_z.move(int(1), cord_z[0]) #坐标台移动
        time.sleep(z_max/z_speed)   
        #comment line below if you want to make snake-like movement
        ant.schutter_close() #激光关闭,uncomment for 1 time scaning
        ximc_z.move(cord_z[0], cord_z[1]) #坐标台移动
        time.sleep(z_max/z_speed)
        k +=1 ##k取下一个值

        #if you wamt to make it move like a snake, change arr_step to *=-1
        arr_step*=1
ant.schutter_close() 

ximc_y.move(cord_y[0], cord_y[1]) 
time.sleep(y_move/3000)
print('End program')
