import ee
import json
ee.Initialize()


def getData(dataSet, lastYear, neededValues, years): #(str, int, list, int)
    #import a collection of US State Coords
    states = ee.FeatureCollection("TIGER/2018/States")
    #import DAYMET weather Data
    snowPack = ee.ImageCollection(dataSet)#"NASA/ORNL/DAYMET_V4"
    #filter the US State Coords for California
    roi = states.filter(ee.Filter.eq('STATEFP', '06'))
    #the various bands
    bands = neededValues
    #bands = ['swe', 'prcp', 'tmax', 'tmin']



    for j in bands:
        #first year of the data
        startYear = lastYear
        for i in range(years):
            iDate = str(startYear) + '-01-01'
            fDate = str(startYear) + '-12-31'
            fileName = './dataStorage/' + j + '/rawCaliforniaWeatherData' + str(startYear) + '.json'
            #pull snow water equvilant data with a 13.65km x 13.65km resolution
            snowPackEqAPI = snowPack.select(j).filterDate(iDate, fDate)
            snowPackEq = snowPackEqAPI.getRegion(roi, 13650).getInfo()
            with open(fileName, 'w') as fileHandle:
                json.dump(snowPackEq, fileHandle)
            print(startYear)
            startYear -= 1
        
getData("NASA/ORNL/DAYMET_V4", 2020, ['swe', 'prcp', 'tmax', 'tmin'], 41)
getData("GRIDMET/DROUGHT", 2020, ['spi14d', 'eddi14d', 'spei14d', 'pdsi', 'z'], 40)


