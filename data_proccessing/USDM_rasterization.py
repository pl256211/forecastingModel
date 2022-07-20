import geopandas, fiona
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from geocube.api.core import make_geocube
import os

mainDir = '/Volumes/AnikSchool/research_project/forecastingModel/dataDownloader/dataStorage/'

def produceOutGrid(file):
    x = geopandas.read_file(file)
    x['value'] = x['DM']



    out_grid = make_geocube(
        vector_data=x,
        measurements = ['value'],
        resolution=(-0.01, 0.01),
        fill=-9999
    )
    return out_grid
    
def rasterize(makeFile=False):
    years = os.listdir(mainDir + 'temp')
    years.remove('._.DS_Store')
    years.remove('.DS_Store')
    for i in years:
        files = os.listdir(mainDir + 'temp/' + i)
        for j in files:
            out_grid = produceOutGrid(mainDir + 'temp/' + i + '/' + j)
            '''x = geopandas.read_file(mainDir + 'temp/' + i + '/' + j)
            x['value'] = x['DM']


            print(x)

            out_grid = make_geocube(
                vector_data=x,
                measurements = ['value'],
                resolution=(-0.01, 0.01),
                fill=-9999
            )'''
            if not os.path.exists(mainDir + 'rasterized/' + i):
                os.mkdir(mainDir + 'rasterized/' + i)
            if makeFile == True:
                out_grid.rio.to_raster(mainDir + 'rasterized/' + i + j[:14] + '.tiff')
#print(os.listdir('/Volumes/AnikSchool/research_project/forecastingModel/dataDownloader/dataStorage/temp'))
#print(out_grid)
#print(out_grid.value)

#print(out_grid['value'])


#print(out_grid2)

#print(out_grid_norm)
def show(out_grid):
    fig = plt.figure(figsize=(17, 15))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    da_grib = xr.where(out_grid.value<-1999.0, np.nan, out_grid.value)

    da_grib.plot(levels = [0,1,2,3,4,5])


    ax.set_extent([-140, -50, 10, 60])
    ax.set_title("Rasterized with 0.01$^o$ Grids", fontsize=24)
    plt.show()

x = produceOutGrid('/Volumes/AnikSchool/research_project/forecastingModel/dataDownloader/dataStorage/temp/2018/USDM_20181113_M.zip')
show(x)





