from enum import Enum
from Abstraction.abstraction import testFunction;

## todo : sergerate properties into separate interfaces

class PointTypes(Enum):
    """
    Represents the point types in time series graph
    """
    Max = 1
    Min = 2
    Normal = 3

class Sensor:
    """
    Represensts a single sensor object
    """
    def __init__(self, name,unit,factor):
        self.Name = name
        self.Unit = unit
        self.factor = factor


class Point:
    """
    Represents a single point in multi sensor time series graph
    """
    def __init__(self,sensor,value,time,pointtype):
        self.Sensor = sensor
        self.Value = value
        self.Time = time
        self.PointType = pointtype


class DesingLoadCase:
    """
    Represents a single INT file which composes time series data of different sensors
    """
    def __init__(self,sensorIdList,timeStep,graph):
        self.SensorIds = sensorIdList
        self.TimeStep = timeStep
        self.Graph = graph;


###testing 1 - 2

GEN_s = Sensor(
    "XPressure",
    "N/cm2",
    0.323435)

maxPoint = Point(GEN_s,
                 234.213123,
                 2.34657,
                 PointTypes.Max)
print(maxPoint.Sensor.Name+ "(" +maxPoint.Sensor.Unit+")")
