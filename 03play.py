# Prank 100% CPU Load

from threading import Thread

class MyThread(Thread):
	def __init__(self, name):
		thread.__init__(self)
		self.name = name

	def run(self):
		for i in range(1000000):
		msg = "%s is running: % \
		self.name
		print(msg)

def create_threads():
	for i in range(10000):
		name = "Thread #%s" % (i + 1)
		my_thread = MyThread(name)
		my_thread.start()

if __name__ == "__main__":
	create_threads()
