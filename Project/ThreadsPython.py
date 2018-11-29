import threading
import random
def worker():
    """thread worker function"""
    x = random.randint(0,100)
    for i in range(0,10000,1):
    	print ('Worker',str(x))
    
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()