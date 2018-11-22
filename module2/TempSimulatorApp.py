'''
Created on Sep 22, 2018

@author: Sujay Joshi
'''
    
    
from time import sleep
from labs.module2 import TempSensorEmulator

#here we are initilizing the temprature sensor emulaor to get the temprature
sysTempSensAdaptor = TempSensorEmulator.TempSensorEmulator()
sysTempSensAdaptor.daemon = True

print("Starting system performance app_daemon_thread...")
sysTempSensAdaptor.enableEmulator=True

sysTempSensAdaptor.start()
while (True):
    sleep(10)
    pass
