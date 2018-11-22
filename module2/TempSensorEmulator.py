'''
Created on Sep 22, 2018

@author: Sujay Joshi
'''

from random import uniform
from time import sleep
import threading
from labs.common.SensorData import SensorData
from labs.module2.SmtpClientConnector import SmtpClientConnector

#This class is used to emulate the temprature of the device and we use this class in the test app to run it
class TempSensorEmulator(threading.Thread):
    enableEmulator = False
    prevTempSet = False
    isPrevTempSet = False
    curTemp = 0
    lowVal = 0
    highVal = 30
    rateInSec = 10
    alertDiff = 10    
    sensorData = SensorData()    
    connector = SmtpClientConnector()
    
    def __init__(self, rateInSec=10):
        super(TempSensorEmulator,self).__init__()
        if rateInSec > 10:
                self.rateInSec = rateInSec
                    
    def run(self):
        while True:
            if self.enableEmulator:                
                self.curTemp = uniform(float(self.lowVal),float(self.highVal))                
                self.sensorData.addValue(self.curTemp)                
                print('\n-------------------------')
                print('New sensor Readings:')
                print(' '+str(self.sensorData))                
                if self.isPrevTempSet == False:
                    print('testing')    
                    self.isPrevTempSet = True
                else:
                    print('testing')
                    
                    if ((abs(self.curTemp - self.sensorData.getAvgValue()))>=self.alertDiff):
                        print('\n Current temp exceeds average by > '+ str(self.alertDiff)+ '. Triggering alert...')
                        self.connector.publishMessage('Exceptional sensor Data  [test]', self.sensorData)
            sleep(self.rateInSec)                        
