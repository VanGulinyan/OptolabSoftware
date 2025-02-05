import matplotlib.pyplot as plt
import numpy as np
from LabOptic import * 
from draw_methods import * 
import time

ximc_z = Ximc(1)  
ximc_x = Ximc(0)  
ximc_y = Ximc(2) #0 - x, 1 - z (вверх низ), 2 - y  
ant = Antaus()  
ant.set_power_trim(9)

speed_x = 7 
speed_y = 7
speed_z = 7

ximc_y.connect() 
ximc_z.connect() 
ximc_x.connect() 

cord_x = ximc_x.get_position()  
ximc_x.set_speed(speed_x)  
cord_z = ximc_z.get_position()  
ximc_z.set_speed(speed_z)  
cord_y = ximc_y.get_position()  
ximc_y.set_speed(speed_y)

n = 20 # n*pi - finish angle
theta = np.arange(0, n*np.pi, 0.1)
a = 1
b = 0.03

full_list = []


for dt in np.arange(0, 2*np.pi, np.pi/2.0):

    x = cord_x[0]+ a*np.cos(theta + dt)*np.exp(b*theta)
    z = cord_z[0]+ a*np.sin(theta + dt)*np.exp(b*theta)

full_list.append([x,z])
full_list = np.array(full_list)

# print(full_list[0][0][0])
ant.schutter_open()

for i in range(len(full_list[0][0])-1):
    ximc_z.move(int(full_list[0][1][i]), cord_z[1])
    ximc_x.move(int(full_list[0][0][i]), cord_x[1])
    time.sleep(np.sqrt((full_list[0][0][i] - full_list[0][0][i+1])  ** 2 + (full_list[0][1][i] - full_list[0][1][i+1]) ** 2)/speed_z)

ant.schutter_close()

# Preplot
# plt.figure(dpi=200, figsize=(8,6))
# plt.plot(full_list[:,0], full_list[:,1],'-o')
# plt.axis('equal') 
# plt.show()

