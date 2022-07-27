import netCDF4 as nc
import os
import numpy as np
import numpy.ma as ma
from numpy import save

filePath = '/Volumes/AnikSchool/research_project/forecastingModel/dataDownloader/dataStorage/raw/daymet/'
def mask(dir):
    for i in os.listdir(dir):
        ds = nc.Dataset(str(dir + i))
        band = i[19:-8]
        year = i[-7:-3]
        print(year)
        for j in range(len(ds[band])):
            if not os.path.exists(filePath[:-11] + 'masked/'):
                os.mkdir(filePath[:-11] + 'masked/')
            if not os.path.exists(filePath[:-11] + 'masked/daymet/'):
                os.mkdir(filePath[:-11] + 'masked/daymet/')
            if not os.path.exists(filePath[:-11] + 'masked/daymet/' + year + '/'):
                os.mkdir(filePath[:-11] + 'masked/daymet/' + year + '/')
            if not os.path.exists(filePath[:-11] + 'masked/daymet/' + year + '/' + i + '/'):
                os.mkdir(filePath[:-11] + 'masked/daymet/' + year + '/' + i + '/')
            tmax = ds[band][j][:]
            tmax = tmax.filled(-9999)
            mask = np.where(tmax<-1999.0, 0, 1)
            
            masked = np.append([mask], [tmax], axis = 0)
            np.save(filePath[:-11] + 'masked/daymet/' + year + '/' + i + '/'+  str(j) + '.npy',masked)

mask(filePath)
