from sense_hat import SenseHat
import smtplib
from time import sleep

senseadpt= SenssorAdaptor.SensorAdaptor()
connectapp = CaopServerApp.CoapServerApp()
senseadpt.runme()
connectapp.ConnectApp

def sensorFunction():

        sense = SenseHat()
        sense.clear()

        temp= sense.get_temperature()
        print(type(temp))
        print(temp)
        temp1 = int(temp)
        print(temp1)

        return temp1

def intruderFunction():
    while True:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = abs(x)
        y = abs(y)
        z = abs(z)

        if x > 1 or y > 1 or z > 1:
            return 1
