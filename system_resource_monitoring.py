import psutil
import random
import threading

def display_cpu():
	global running

	running = True

	currentProcess = psutil.Process()

	# start loop 
	while running:
		print(currentProcess.cpu_percent(interval=1))

def start():
	global t
	#  create thread and start it 
	t = threading.Thread(target=display_cpu)
	t.start()

def stop():
	global running
	global t

	# use 'running' to stop loop in thread so thread will end
	running = False

	# wait fr thread's end
	t.join()

def hate_this():
	tab = []
	for i in range(1000000):
		tab.append(random.randint(1,100000))
	tab.sort()
	return tab

start()
try:
	result = hate_this()
finally: # stop therad even i press ctrl+c
	stop()

