import time
from thing import PiThing

pi_thing = PiThing()


while True:
    pi_thing.set_ledr(True)
    time.sleep(0.5)
    pi_thing.set_ledr(False)
    time.sleep(0.5)
    pi_thing.set_ledv(False)
    time.sleep(0.5)
    pi_thing.set_ledv(True)
    time.sleep(0.5)