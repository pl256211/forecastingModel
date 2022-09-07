import netCDF4 as nc
import os
import numpy as np
import numpy.ma as ma
from numpy import save
import xarray as xr
from USDM_rasterization import dataRasterization
from pyproj import Proj, transform
import matplotlib.pyplot as plt

filePath = '/Volumes/AnikSchool/research_project/forecastingModel/dataDownloader/dataStorage/raw/daymet/'




def xarrayProduction(dir):
    weatherData = dataRasterization('/Volumes/AnikSchool/research_project/forecastingModel/dataDownloader/dataStorage/')
    inProj = Proj('epsg:3857')
    outProj = Proj('epsg:4326')
   # for i in os.listdir(dir):
    x = xr.open_dataset(dir + '/daymet_v4_daily_hi_tmin_2020.nc')
    #print(x)
    #plt.figure(figsize=(17, 15))
    
    
    y = x.isel(time=1, nv = 0)
    
    '''for a in y:
        x1,y1 = y.x,y.y
        print(x1,y1)'''  
    print(y.coords['lat'].values)
    #print(y.dims)
    #print(type(y.tmin))
    weatherData.show2(y.tmin)

def mask(dir):
    for i in os.listdir(dir):
        ds = nc.Dataset(str(dir + i))
        band = i[19:-8]
        year = i[-7:-3]
        #print(year)
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

xarrayProduction(filePath)
#mask(filePath)
