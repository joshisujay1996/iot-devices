from sense_hat import SenseHat

sense = SenseHat()

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 1:
        file = open("/home/pi/Desktop/accvalue.txt","w")
        file.write("acc")
        file.close()
    else:
        sense.clear()
