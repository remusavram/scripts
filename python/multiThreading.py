'''
Created on Dec 1, 2014

@author: remusav
'''


from Queue import Queue
from threading import Thread
from time import sleep

class Worker(Thread):
    """Thread executing tasks from a given tasks queue"""
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try: func(*args, **kargs)
            except Exception, e: print e
            self.tasks.task_done()

class ThreadPool:
    """Pool of threads consuming tasks from a queue"""
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads): Worker(self.tasks)
    
    def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))
    
    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()

def task(i):
    print i
    sleep(1)

# 1) Init a Thread pool with the desired number of threads
pool = ThreadPool(40)

for i in range(100):
    # 2) Add the task to the queue
    pool.add_task(task, i)

# 3) Wait for completion
pool.wait_completion()