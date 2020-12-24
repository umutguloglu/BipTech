# Check the mask

import multiprocessing
from constant import mili,TIME_LIMIT
from distance_check import distance_check

def mask_check(s_flag):

	flag=0
	is_suitable=1 ###### This will be changed during demo
	timestamp=mili()
	flag=s_flag.get()
	while (flag):
		#Here, the mask subsystem starts to check.

		if (is_suitable):
			print("Get close to the temperature sensor.")

			#Launches the distance process
			distance_process = multiprocessing.Process(target=distance_check)
			distance_process.start()
			break

		else:
			print("You cannot pass without wearing the mask properly.")
			if(mili()-timestamp>TIME_LIMIT):
				print("You did not wear the mask properly. You cannot pass.")
				break
			else:
				#Time limit is not exceeded. Continue to check the mask
				pass					


