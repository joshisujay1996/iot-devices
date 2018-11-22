'''
Created on Oct 13, 2018

@author: Sujay Joshi
'''
from labs.common.ActuatorData import ActuatorData
from RPI import GPIO
#this is used to generate temprature values
class TempActuatorEmulator():   

    def __init__(self):
        
        self.thisActuatorData = ActuatorData()
        self.thisActuatorData.setValue(20)
        self.thisActuatorData.setCommand('IDEAL')
     
    def processMessage(self, actuatorData):
        
        
        if(self.thisActuatorData!=actuatorData):
        
            if (actuatorData.getCommand() == 'INCREASE'):           
                print('Increasing temperature')
                GPIO.set_rotation(actuatorData.getValue())
            #GPIO stands for general purpose input output
            #we set rotation and get values
            elif (actuatorData.getCommand() == 'DECREASE'):
                print('Decreasing temperature')
                GPIO.set_rotation(actuatorData.getValue())        
            else:
                print('maintaining the ideal temperature')
                GPIO.set_rotation(actuatorData.getValue())
                
            self.thisActuatorData = actuatorData
        
