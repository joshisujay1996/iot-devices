from sense_hat import SenseHat
import smtplib
from time import sleep
from actuator import sendmail

#calling the sensoradaptor to sense the temprature and accelerometer reading
senseadpt= SenssorAdaptor.SensorAdaptor()
#calling the coap serverapp
connectapp = CaopServerApp.CoapServerApp()
#running the sensors
senseadpt.runme()
#connecting to the gateway
connectapp.ConnectApp
mailid = "joshi.suj@husky.nue.edu"
sendmail(mailid)

#this functionw will calculate the temprature
def sensorFunction():

        sense = SenseHat()
        sense.clear()

        temp= sense.get_temperature()
        print(type(temp))
        print(temp)
        temp1 = int(temp)
        print(temp1)
#returning temprature
        return temp1

# this function will sense  if there is any accleration in the pi
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
