# Check whether the people passed

from constant import TIME_LIMIT
from time import perf_counter

def enterance_check(np):



	#------------------------------------------------------------------
	is_entered=1 #The people is entered
	#------------------------------------------------------------------
	timestamp=perf_counter()

	while (True):
		# Here, we calculate whether a person is entered or not
		if(is_entered):
			np.put(1)
			# Closing the door code. For temporarily, I used print.
			print("You passed. The door is closing.")
			break
		else:
			if(perf_counter()-timestamp>TIME_LIMIT):
				print("You did not pass. The door is closing")
				np.put(0)
				break
