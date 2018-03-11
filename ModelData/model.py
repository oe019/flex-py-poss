
class Sensor:
    """
    Represensts a single sensor object
    """
    def __init__(self, name=None,unit=None,factor=None,id=None):
        self.__name = name
        self.__unit = unit
        self.__factor = factor
        self.__Id = id
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
    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self,value):
        self.__Id = value
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

#######Utilisation objects













