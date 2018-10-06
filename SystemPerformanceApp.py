'''
Created on Sep 15, 2018

@author: Sujay Joshi
'''
from time import sleep
from labs.module1 import SystemPerformanceAdaptor



sysPerfAdaptor = SystemPerformanceAdaptor.SystemPerformanceAdaptor()
sysPerfAdaptor.daemon = True

print("Starting system performance app daemon thread...")
sysPerfAdaptor.enableAdaptor=True
sysPerfAdaptor.start()
while (True):
    sleep(5)
    pass