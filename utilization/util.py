## Reads files and returns an design load case object
## parses files commandlines etc
## verify inputs
## creates test objects
from ModelData.model import Sensor
from ModelData.model import DesingLoadCase
from ModelData.model import Point

import random

def createPseudoDesignLoadCase() -> DesingLoadCase:
    """
    creates a pseudo design load case object
    :return: Design load case object
    """
    sensorCollection = {"Tower": '1', "Yaw": '2', "FNx": '3', "FNy": '4', "FNz": '5'}
    sensorIdList = [int(key) for key in sensorCollection.values()]
    s1 = Sensor("Tower", "Kn", 0.3322,int(sensorCollection["Tower"]))
    s2 = Sensor("Yaw", "Ncm", 0.4411,int(sensorCollection["Yaw"]))
    s3 = Sensor("FNx", "Ncm", 0.1211,int(sensorCollection["FNx"]))
    s4 = Sensor("FNy", "Ncm", 0.5511,int(sensorCollection["FNy"]))
    s5 = Sensor("FNz", "Ncm", 0.6611,int(sensorCollection["FNz"]))
    sensors = [s1,s2,s3,s4,s5]

    dlc = DesingLoadCase()
    dlc.sensorIds = sensorIdList
    dlc.timeStep = 0.2346789025
    for ss in sensors:
        data = generateTimeSeries(dlc.timeStep)
        for keys1 in data.keys():
            pt = Point(ss,data[keys1],keys1)
            dlc.graph.append(pt)
    return dlc



def generateTimeSeries(timeStep)->dict:
    time = -timeStep
    data = dict()
    for i in range(1,100):
        time = time + timeStep
        val = random.uniform(1.01, 255.55)
        data[time] = val
    return data



