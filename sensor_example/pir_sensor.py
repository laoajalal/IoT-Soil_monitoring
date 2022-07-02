from machine import Pin
import time
from machine import Timer

#config
motionDetected = 1
noMotionDetected = 0
hold_time_sec = 0.1

pir = Pin('P10',mode=Pin.IN)

led = Pin('P9', Pin.OUT, pull = Pin.PULL_DOWN)


chrono = Timer.Chrono()
chrono.start()

print("Starting Detection")
while True:
    if pir()==motionDetected:
        print(chrono.read(), "Motion Detected!")
        led.value(1)
    # print(pir())

    if pir()==noMotionDetected:
        print("No motion")
        led.value(0)

    time.sleep(hold_time_sec)
