# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 19:45:39 2020

@author: Sakshi Agarwal
"""

import queue
import threading
import time

q = queue.Queue()

def put_queue():
    print('Starting Producer Thread...')
    for i in range(100):
        q.put(i)
    print('element added..')
    

def get_queue():
    print('Starting Consumer Thread...')
    while not q.empty():
        print(threading.currentThread().getName() + ":" + str(q.get()))
        time.sleep(1)
    ##print('element fetched..')
    
p = threading.Thread(target = put_queue, name = 'producer')
c1 = threading.Thread(target = get_queue, name = 'consumer1')
c2 = threading.Thread(target = get_queue, name = 'consumer2')
c3 = threading.Thread(target = get_queue, name = 'consumer3')
p.start()
c1.start()
c2.start()
c3.start()


