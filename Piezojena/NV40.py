import os
import sys
import platform
import tempfile
import re
import serial
import matplotlib.pyplot as plt
import json
import antaus.antaus as ant


file_path = "conf.json"

def update_conf(object_name, name_of_data_change, new_value):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data_list = json.load(json_file)
    data_list[object_name][name_of_data_change] = new_value

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file)


class Pesa:
    number = None #x - 0, y - 1, z - 2
    com_port = 'COM8'  # Порт подключения. Узнать его можно: Диспетчер устройств -> Контроллеры USB
    cord = None   # Собственная координата
    ximc = None   # Объект класса Ximc, на которой стоит пеза. Важно: pesa.number=ximc.number

    def __init__(self, i):
        self.number = i
        self.cord = 0
        self.ximc = None

    def connect(self):
        with serial.Serial(port=self.com_port, baudrate=19200, xonxoff=True) as ser:
            command = 'setk,'+str(self.number)+',1\r'
            ser.write(command.encode()) 
            
    # step [um]
    def move(self, step):
        with serial.Serial(port=self.com_port, baudrate=19200, xonxoff=True) as ser:
            command = 'set,'+str(self.number)+','+str(step)+'\r'
            cord = 0
            cord = cord + step
            ser.write(command.encode())

    def disconnect(self):
        with serial.Serial(port=self.com_port, baudrate=19200, xonxoff=True) as ser:
            command = 'setk,'+str(self.number)+',0\r'
            ser.write(command.encode()) 

    def get_self_position(self):
        return self.cord

    def get_absolute_position(self):
        return self.cord+self.ximc.get_position()
