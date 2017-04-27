import gopigo
import easygopigo
import time

# Connect the Ultrasonic Sensor to port A1

my_ultrasonic = easygopigo.UltraSonicSensor()

while True:
        
        print(my_ultrasonic.read())
        time.sleep(0.05)
