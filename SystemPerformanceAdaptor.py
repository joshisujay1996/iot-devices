'''
Created on Sep 15, 2018

@author: Sujay Joshi
'''
import psutil,threading
from time import sleep
class SystemPerformanceAdaptor(threading.Thread):
    enableAdaptor=False
    rateInsec=5

    def __init__(self, rateInsec=5):
        super(SystemPerformanceAdaptor,self).__init__()
    
        if rateInsec> 0:
            self.rateInsec =rateInsec
            
    def run(self):
        while True:
            if self.enableAdaptor:
                print('\n--------------------')
                print('New system performance readings:')
                print(' ' + str(psutil.cpu_stats()))
                print(' ' + str(psutil.virtual_memory()))
        
            sleep(self.rateInsec)
