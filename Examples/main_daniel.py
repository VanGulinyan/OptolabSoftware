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
ximc_y = Ximc(1)
ximc_x = Ximc(0) #0 - x, 1 - z (вверх низ), 2 - y
ant = Antaus()
ant.set_base_divider(222)
ant.set_freq_time(20000)
ant.set_power_trim(1)


ximc_x.connect()
cord_x = ximc_x.get_position()
ximc_x.set_speed(1000)
ximc_x.disconnect()


ximc_y.connect()
cord_y = ximc_y.get_position()
ximc_y.set_speed(1000)
ximc_y.disconnect()



#ant.schutter_open()

cord_y1 = cord_y+3000
print(cord_y)

ximc_y.connect()
ximc_y.move(1, cord_y1)
ximc_y.disconnect()
      


#ant.schutter_close()
