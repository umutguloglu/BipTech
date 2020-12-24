# Check whether the people passed

from constant import mili,TIME_LIMIT

def enterance_check(np):

	# Here, we calculate whether a person is entered or not

	#------------------------------------------------------------------
	is_entered=1 #The people is entered
	#------------------------------------------------------------------
	timestamp=mili()

	while (True):

		if( not np.empty() ): # This checks whether there exists a people leaved
			num_people=np.get()

		if(is_entered):
			num_people=num_people+1
			np.put(num_people)
			# Closing the door code. For temporarily, I used print.
			print("You passed. The door is closing.")	
		else:
			if(mili()-timestamp>TIME_LIMIT):
				np.put(num_people)
				print("You did not pass. The door is closing")
