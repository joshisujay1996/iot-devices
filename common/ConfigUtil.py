'''
Created on Sep 22, 2018

@author: Sujay Joshi
'''
import configparser
import os

DEFAULT_CONFIG_FILE = "../data/ConnectedDevicesConfig.props"


class ConfigUtil(object):
    configFile = DEFAULT_CONFIG_FILE
    configData = configparser.ConfigParser()
    
    def __init__(self, configFile = None):
    
        if(configFile!=None):
            self.configFile= configFile
            
    def loadConfig(self):
        if(os.path.exists(self.configFile)):
            self.configData.read(self.configFile)
            self.isLoaded = True
            
    def getConfig(self, forceReload = False):
        if(self.isLoaded==False or forceReload):
            self.loadConfig()
        return self.configData
    
    def getConfigFile(self):
        return self.configFile
    
    def getProperty(self, section, key, forceReload=False):
        return self.getConfig(forceReload).get(section,key)
    
    def isConfigDataLoaded(self):
        return self.isLoaded          