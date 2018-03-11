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
    def __init__(self,sensor=Sensor(),value=None,time=None):
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
    def __init__(self,sensorIdList=list(),timeStep=None,graph=list()):
        if(type(sensorIdList) is not list):
            raise ('type mismatch exception, sensorIDs must be a list object')
        if (type(graph) is not list):
            raise ('type mismatch exception, graph must be a list object')
        self.__sensorIds = sensorIdList
        self.__timeStep = timeStep
        self.__graph = graph
    @property
    def sensorIds(self):
        return self.__sensorIds
    @sensorIds.setter
    def sensorIds(self,values):
        if type(values) is not list:
            raise ('type mismatch exception, sensorIDs must be a list object')
        self.__sensorIds = values
    @property
    def timeStep(self):
        return self.__timeStep
    @timeStep.setter
    def timeStep(self,val):
        self.__timeStep = val
    @property
    def graph(self):
        return self.__graph
    @graph.setter
    def graph(self,value):
        if(type(value)is not list):
            raise ('type mismatch exception, graph must be a list object')
        if(type(value[0]) is not Point):
            raise ('type mismatch exception, graph elements must be a Point object')
        self.__graph = value



s1 = Sensor("Tower",'KN',0.3334)
s2 = Sensor('Yaw','N/cm2',0.22333)

dlc = DesingLoadCase()
pt1 = Point(s1,23,3)
pt2 = Point(s2,13,5)
pt3 = Point(s1,54,2)
ls = [pt1,pt2,pt3]

dlc.graph.append(pt1)
dlc.graph.append(pt2)
dlc.graph.append(pt3)

print(dlc.graph[0].sensor.unit)














