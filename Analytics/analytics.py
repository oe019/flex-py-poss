## contains analytical operations in design load case object
from ModelData.model import RelativeExtremum
from ModelData.model import PointTypes
from ModelData.model import Point
from ModelData.model import RelativeExtremum
from utilization.util import createPseudoDesignLoadCase



dcase = createPseudoDesignLoadCase()

listPoints = dcase.graph

def getExtremum(dlc,sensorId,isMaximum=True)->Point:
    """
    gets the maximum value of a given sensor in the design load case time series
    :param dlc: Design load case object
    :param sensorId: sensor id of which the max value is desired
    :param isMaximum: default value True, determines the extremum type of the point
    :return: returns the Point object which has the maximum value for given sensor id
    """
    values = [val.value for val in dlc.graph if val.sensor.Id == sensorId]
    mxval = max(values)
    pnts = [pnt for pnt in dlc.graph if int(pnt.sensor.Id) == int(sensorId) and pnt.value == mxval]
    ## TODO : handle multiple maximums
    return pnts[0]




def getMaxWithCorrespondingValues(dlc,sensorId)->RelativeExtremum:
    maxPt = getExtremum(dlc,sensorId,True)
    relvals = [pnt for pnt in dlc.graph if maxPt.time == pnt.time and pnt.sensor.Id != sensorId]
    return RelativeExtremum(PointTypes.Max,maxPt,relvals)

###test region

relEx = getMaxWithCorrespondingValues(dcase,2)

for asd in relEx.covals:
    print(relEx.pointType.name,'=',relEx.point.value,"timestamp:",relEx.point.time,":",relEx.point.sensor.name,"=>",asd.sensor.name,":", asd.time,"--",asd.value)






