import multiprocessing

from person_detect import person_detect
from mask_check import mask_check
from exit_door import exit_door
import constant

def ana_kod(np,pd_queue,s_flag):
	print("a")
	num_people=0

	while(True):
#		print(not np.empty())
		if( not np.empty() ): # This checks whether there exists a people leaved	
			num_people=np.get()
			print(num_people)

		if(num_people<constant.CAPACITY):

			#Launch pd_process. It tries to detect whether there exists a human or not
			pd_process = multiprocessing.Process(target=person_detect , args=(pd_queue,))
			pd_process.start()
			human=pd_queue.get()

			if (human):
				s_flag.put(1)
				#Close person_detect.
				#pd_process.terminate()
				#Quit
#				break
		
		else:
			print("The capacity is full. Try later.")





if __name__ == '__main__':

	np       = multiprocessing.Queue()
	s_flag   = multiprocessing.Queue()
	pd_queue = multiprocessing.Queue()

	ana_process = multiprocessing.Process(target=ana_kod , args=(np,pd_queue,s_flag))
	#This is our main process

	exit_process = multiprocessing.Process(target=exit_door , args=(np,)) 
	#Counting the number of people lefting the building

	#Launches the mask process.
	mask_process = multiprocessing.Process(target=mask_check , args=(s_flag,))

	mask_process.start()
	ana_process.start()
	exit_process.start()