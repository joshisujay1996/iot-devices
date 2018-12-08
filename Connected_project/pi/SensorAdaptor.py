from sense_hat import SenseHat
from time import sleep
import CoapClientApp
import senseme

#this class has a function whilch will be used in other class to call and run all the sensors and get values
class SensorAdaptor():
    def runme(self):
        while 1:
            temp = senseme.sensorFunction()
            #check if temp is greater than 25 , if so call teh client app to send data
            if(temp>25):
                CoapClientApp.startApp()
             #check if acclerometer reading , if so call teh client app to send data
            elif(senseme.intruderFunction()==1):
                CoapClientApp.startApp()
            else:
                sense.clear()
            break
