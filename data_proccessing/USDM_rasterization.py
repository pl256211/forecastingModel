import geopandas, fiona
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from geocube.api.core import make_geocube
import os
import json
from shapely.geometry import box

mainDir = '/Volumes/AnikSchool/research_project/forecastingModel/dataDownloader/dataStorage/'


US = geopandas.read_file(mainDir + 'gadm36_USA_shp/gadm36_USA_0.shp')
US['value'] = 0
print(US)
def printVector(v):
    
    out_grid = make_geocube(
        vector_data=v,
        measurements = ['value'],
        resolution=(-0.05, 0.05),
        fill=-9999
    )
    return out_grid

def produceOutGrid(file):
    x = geopandas.read_file(file)
    x['value'] = x['DM'] + 1
    print(x)
    newX = US.append(x)
    print(newX)


    out_grid = make_geocube(
        vector_data=newX,
        measurements = ['value'],
        resolution=(-0.05, 0.05),
        fill=-9999
        #geom=json.dumps(geom)
    )
    print(out_grid.dims)
    new = out_grid.to_array()
    new = new.to_numpy()
    mask = xr.where(out_grid.value<-1999.0, 0, 1)
    mask = mask.to_numpy()
    masked = np.append([mask], new, axis = 0)
    print(type(masked))
    print(masked.shape)
    print(masked)
    return out_grid, masked
    
def rasterize(makeFile=False):
    years = os.listdir(mainDir + 'temp')
    try:
        years.remove('._.DS_Store')
        years.remove('.DS_Store')
    except:
        pass
    for i in years:
        files = os.listdir(mainDir + 'temp/' + i)
        for j in files:
            out_grid = produceOutGrid(mainDir + 'temp/' + i + '/' + j)[1]
            if not os.path.exists(mainDir + 'rasterized/'):
                os.mkdir(mainDir + 'rasterized/' )
            if not os.path.exists(mainDir + 'rasterized/' + i):
                os.mkdir(mainDir + 'rasterized/' + i)
            if makeFile == True:
                np.save(mainDir + 'rasterized/' + i + '/' + j[:14] + '.npy',out_grid)

def show(out_grid):
    fig = plt.figure(figsize=(17, 15))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    da_grib = xr.where(out_grid.value<-1999.0, np.nan, out_grid.value)
    #print(type(da_grib))
    #print(da_grib)
    new = type(da_grib.to_numpy())
   

    #da_grib2 = xr.where(out_grid2.value<-1999.0, np.nan, out_grid2.value)
    
    #da_grib2.plot(levels = [0,1,2,3,4,5,6])
    da_grib.plot(levels = [0, 1, 2, 3, 4, 5, 6])


    ax.set_extent([-140, -50, 10, 60])
    ax.set_title("Rasterized with 0.01$^o$ Grids", fontsize=24)
    plt.show()

print(type(US))
x = produceOutGrid('/Volumes/AnikSchool/research_project/forecastingModel/dataDownloader/dataStorage/temp/2022/USDM_20220104_M.zip')[0]
rasterize(True)
show(x)





