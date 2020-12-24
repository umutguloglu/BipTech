import multiprocessing
import time

def spawn2(q,s):
	while(True):
		if(True):
			num=s.get()
			print(num)
			num=num+1
			s.put(num)
			time.sleep(5)
