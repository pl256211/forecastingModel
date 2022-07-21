import netCDF4 as nc
import os
import numpy as np
import numpy.ma as ma
from numpy import save

filePath = '/Volumes/AnikSchool/research_project/forecastingModel/dataDownloader/dataStorage/raw/daymet/'
print(filePath[:-11])
def mask(dir):
    for i in os.listdir(dir):
        ds = nc.Dataset(str(dir + i))
        band = i[19:-8]
        #print(band)
        if not os.path.exists(filePath[:-11] + '/masked/'):
            os.mkdir(filePath[:-11] + '/masked/')
        if not os.path.exists(filePath[:-11] + '/masked/daymet/'):
            os.mkdir(filePath[:-11] + '/masked/daymet/')
        tmax = ds[band][:]
        save(filePath[:-11] + '/masked/daymet/' + i + '.npy',tmax)

mask(filePath)
