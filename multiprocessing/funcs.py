import numpy as np
import matplotlib.pyplot as plt
import time

def do_something(t=1):
    """ input sleep time in seconds"""
    print(f'Sleeping for {t} s...')
    time.sleep(t)
    print('Done sleeping!')