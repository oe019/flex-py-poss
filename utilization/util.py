## Reads files and returns an design load case object
## parses files commandlines etc
## verify inputs
## creates test objects
from ModelData.model import Sensor
from ModelData.model import DesingLoadCase
from ModelData.model import Point

import random

def createPseudoDesignLoadCase():
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

    dlc = DesingLoadCase()
    dlc.sensorIds = sensorIdList
    for ia in range(0, 100):
        rnd = random.uniform(0.1, 299.3)
        time = rnd * ia
        value = rnd
        if (ia % 2 == 0):
            sns = s1
        if (ia % 3 == 0):
            sns = s2
        if (ia % 4 == 0):
            sns = s3
        if (ia % 5 == 0):
            sns = s4
        if (ia % 7 == 0):
            sns = s5
        pt = Point(sns, value, time)
        dlc.graph.append(pt)
    return dlc






