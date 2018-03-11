from enum import Enum
from Abstraction.abstraction import testFunction;

## todo : sergerate properties into separate interfaces


class Sensor:
    """
    Represensts a single sensor object
    """
    def __init__(self, name=None,unit=None,factor=None):
        self.__name = name
        self.__unit = unit
        self.__factor = factor
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    @property
    def unit(self):
        return self.__unit
    @unit.setter
    def unit (self,value):
        self.__unit = value
    @property
    def factor(self):
        return self.__factor
    @factor.setter
    def factor (self,value):
        self.__factor = value





class Point:
    """
    Represents a single point in multi-sensor time series graph
    """
    def __init__(self,sensor=None,value=None,time=None):
        if(type(sensor) is not Sensor):
            raise ('type mismatch exception, sensor must be a sensor object')
        self.__sensor = sensor
        self.__value = value
        self.__time = time
    @property
    def sensor(self):
        return self.__sensor
    @sensor.setter
    def sensor(self,value):
        if (type(value) is not Sensor):
            raise ('type mismatch exception, sensor must be a sensor object')
        self.__sensor = value
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self,value):
        self.__value = value
    @property
    def time (self):
        return self.__time
    @time.setter
    def time(self,value):
        self.__time = value


class DesingLoadCase:
    """
    Represents a single INT file which composes time series data of different sensors
    """
    def __init__(self,sensorIdList,timeStep,graph):
        self.SensorIds = sensorIdList
        self.TimeStep = timeStep
        self.Graph = graph;










