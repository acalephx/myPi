from app.steering import Steering
import time

steering = Steering(18, 0, 180, 13, 0, 180, 90, 114)
# steering = Steering(17, 0, 180, 18, 0, 160, 90, 90)

steering.setup()

# steering.up()
# time.sleep(0.5)
# steering.down()
# time.sleep(0.5)
steering.specify(90, 180)
time.sleep(5)
# steering.left()
# steering.right()
steering.specify(90, 0)
time.sleep(0.5)
# steering.cleanup()
