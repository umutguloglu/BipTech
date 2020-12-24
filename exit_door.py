# Check the number of people leaved the building

from constant import mili,SEND_PERIOD
import time

def exit_door(np):
	population=3
	timestamp=0


#while(False):
	#In this part, we calculate whether a person leaved or not.
	#------------------------------------------------------------------
	is_leaved=1 #The people is leaved
	#------------------------------------------------------------------
	if(is_leaved):
		np.put(-1)
	while True:
		np.put(-1)
		time.sleep(10)
