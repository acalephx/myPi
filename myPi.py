try:
    import RPi.GPIO as GPIO
    from time import sleep
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BCM)

channel_H = [17]
channel_L = [24]

GPIO.setup(channel_H, GPIO.OUT, initial=GPIO.HIGH)

GPIO.setup(channel_L, GPIO.OUT, initial=GPIO.LOW)

# myH = GPIO(17)
# myL = GPIO(24)

while True:
    sleep(3)
    GPIO.output(channel_L, True)
    sleep(3)
    GPIO.output(channel_L, False)

GPIO.cleanup([channel_H, channel_L])

