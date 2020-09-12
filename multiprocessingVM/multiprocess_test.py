import numpy as np
import matplotlib.pyplot as plt
import time
import os
import multiprocessing as mp


def do_something(t=1):
    """ input sleep time in seconds"""
    print(f'Sleeping for {t} s...')
    time.sleep(t)
    print('Done sleeping!')


# get number of cpu's
cpu = os.cpu_count()
# define process
p1 = mp.Process(target=do_something, args=[1])
p2 = mp.Process(target=do_something, args=[1])
p3 = mp.Process(target=do_something, args=[1])
# starting
p1.start()
p2.start()
p3.start()
# #join to actually run in parallel
p1.join()
p2.join()
p3.join()
