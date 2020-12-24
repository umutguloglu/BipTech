# Check the number of people leaved the building

from constant import mili,SEND_PERIOD

def exit_door(np):
	population=3
	while (True):
		timestamp=mili()
		while(True):
			if(mili()-timestamp>SEND_PERIOD):
				population+=1
				np.put(population)
				print(population)
				timestamp=mili()
			else:
				#In this part, we calculate whether a person leaved or not.	
				#------------------------------------------------------------------
				is_leaved=0 #The people is leaved
				#------------------------------------------------------------------
				if(is_leaved):
					population+=1




		