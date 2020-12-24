import multiprocessing

from person_detect import person_detect
from mask_check import mask_check
from exit_door import exit_door
import constant
import time

def ana_kod(np,pd_queue,s_flag):
	num_people=0
	in_the_mask=False
	while(True):
#		print(not np.empty())
#		print(num_people)     # Only for demo-test
		if( not np.empty() ): # This checks whether there exists a people leaved
			imp=np.get()
			if (imp==0) | (imp==1):			# Only happen when people is denied.
				in_the_mask=False
				mask_process.terminate()      # Kills the zombie process
				mask_process.join()
				time.sleep(2)
			num_people=num_people+imp
			print(num_people)

		if(not in_the_mask):
			if(num_people<constant.CAPACITY):
				print_flag=0
				#Launch pd_process. It tries to detect whether there exists a human or not
				pd_process = multiprocessing.Process(target=person_detect , args=(pd_queue,))
				pd_process.start()
				human=pd_queue.get()

				if (human):
					in_the_mask=True
					pd_process.terminate()
					pd_process.join()
					mask_process = multiprocessing.Process(target=mask_check , args=(np,))
					mask_process.start()
					#Close person_detect.
	#				pd_process.terminate()
	#				pd_process.join()
					#Quit
	#				break

			else:
				if(print_flag==0):
					in_the_mask=True
					print("The capacity is full. Try later.")
					print_flag=1





if __name__ == '__main__':

	np       = multiprocessing.Queue()
	s_flag   = multiprocessing.Queue()
	pd_queue = multiprocessing.Queue()

	ana_process = multiprocessing.Process(target=ana_kod , args=(np,pd_queue,s_flag,))
	#This is our main process

	exit_process = multiprocessing.Process(target=exit_door , args=(np,))
	#Counting the number of people lefting the building

	#Launches the mask process.
#	mask_process = multiprocessing.Process(target=mask_check , args=(s_flag,np,))

#	mask_process.start()
	ana_process.start()
	exit_process.start()
