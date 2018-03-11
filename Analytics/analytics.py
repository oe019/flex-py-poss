## contains analytical operations in design load case object
from utilization.util import createPseudoDesignLoadCase



dcase = createPseudoDesignLoadCase()



def getExtremum(dlc,sensorId,isMaximum=True):
    """
    gets the maximum value of a given sensor in the design load case time series
    :param dlc: Design load case object
    :param sensorId: sensor id of which the max value is desired
    :param isMaximum: default value True, determines the extremum type of the point
    :return: returns the Point object which has the maximum value for given sensor id
    """
    values = [val.value for val in dlc.graph if val.sensor.Id == sensorId]
    return max(values) if isMaximum == True else  min(values)


def getMaxWithCorrespondingValues(dlc,sensorId):
    max = getExtremum(dlc,sensorId,True)
    for senId in dlc.sensorIds:
        pass ## TODO Create RelativeExtremum model object and Extremum Type Enum (point, ExtremumType, CoValues->dict)

print(getExtremum(dcase,3,False))