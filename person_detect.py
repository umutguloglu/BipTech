# Looks at HC-SR value to understand detection
from time import sleep
import multiprocessing

def person_detect(pd_queue):
#	while True:
	sleep(5)
	pd_queue.put(1)   # You will not send 0. Just 1.
