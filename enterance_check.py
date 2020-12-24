# Check whether the people passed

from constant import mili,TIME_LIMIT

def enterance_check(np):

	# Here, we calculate whether a person is entered or not

	#------------------------------------------------------------------
	is_entered=1 #The people is entered
	#------------------------------------------------------------------
	timestamp=mili()

	while (True):
		if(is_entered):
			np.put(1)
			# Closing the door code. For temporarily, I used print.
			print("You passed. The door is closing.")
			break
		else:
			if(mili()-timestamp>TIME_LIMIT):
				print("You did not pass. The door is closing")
				np.put(0)
				break
