# Check the distance

import multiprocessing
from constant import TEMP_LIMIT,DISTANCE_MIN,DISTANCE_MAX
from enterance_check import enterance_check
import time

def distance_check(np):

	while (True):
		#Here, the distance is measured.
		#------------------------------------------------------------------
		dist=4 ###### This will be changed during demo
		#------------------------------------------------------------------

		if (dist<DISTANCE_MIN):
			print("Move away from the temperature sensor.")

		elif (dist>DISTANCE_MAX):
			print("Get close to the temperature sensor.")

		else:
			#Here, the temperature is measured.
			#------------------------------------------------------------------
			temp=37 ###### This will be changed during demo
			#------------------------------------------------------------------

			if(temp>=TEMP_LIMIT): #Fewer case

				print("You have fewer. You cannot pass.")
				np.put(0)
				break

			else: #Temperature is fine

				# Opening the door code. For temporarily, I used print.
				print("You are OK. The door is opening.")

				# Launches isEntered_process. It makes sure that the people entered.
				isEntered_process = multiprocessing.Process(target=enterance_check, args=(np,))
				isEntered_process.start()
				isEntered_process.join()
				break
