from sense_hat import SenseHat
from time import sleep
import CoapClientApp
import senseme

class SensorAdaptor():
    def runme(self):
        while 1:
            temp = senseme.sensorFunction()
            if(temp>25):
                CoapClientApp.startApp()
            elif(senseme,intruderFunction()==1):
                CoapClientApp.startApp()
            else:
                sense.clear()
            break
