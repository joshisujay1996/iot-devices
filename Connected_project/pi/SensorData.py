import os
from datetime import datetime
class SensorData():
    timeStamp= None
    name= 'TEMPERATURE READINGS'
    curValue= 0
    avgValue= 0
    minValue= 0
    maxValue= 0
    totValue= 0
    sampleCount = 0
    def __init__(self):
        self.timeStamp = str(datetime.now())

    #This function tracks every new temperature reading, calculates the average
    def addValue(self, newVal):

        #increase the sampleCount for every reading
        self.sampleCount += 1

        #adds the new temperature reading to the totalValue and notes the time of the reading
        self.totValue = self.totValue+newVal;
        self.timeStamp = str(datetime.now())
        self.curValue= newVal

        #tracks the minimum recorded temperature
        if(self.curValue < self.minValue):
            self.minValue = self.curValue

        #tracks the maximum recorded temperature
        if(self.curValue>self.maxValue):
            self.maxValue = self.curValue

        #calculate the average from all the readings
        if(self.totValue!=0 and self.sampleCount>0):
            self.avgValue = self.totValue/self.sampleCount

    #setters and getters

    def getAvgValue(self):
        return self.avgValue

    def getMaxValue(self):
        return self.maxValue

    def getMinValue(self):
        return self.minValue

    def getValue(self):
        return self.curValue

    def setName(self, name):
        self.name = name


    #function to re-format
    def __str__(self):
        customStr = \
            str(self.name + ':' + \
            os.linesep + '\tTime:     ' + self.timeStamp + \
            os.linesep + '\tCurrent: ' + str(self.curValue) + \
            os.linesep + '\tAverage: ' + str(self.avgValue) + \
            os.linesep + '\tSamples: ' + str(self.sampleCount) + \
            os.linesep + '\tMin:' + str(self.minValue) + \
            os.linesep + '\tMax:    ' + str(self.maxValue))

        return customStr
