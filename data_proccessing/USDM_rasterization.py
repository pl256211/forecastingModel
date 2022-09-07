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




class dataRasterization:

    def __init__(self, dir):
        self.dir = dir
        self.US = geopandas.read_file(self.dir + 'gadm36_USA_shp/gadm36_USA_0.shp')
        self.US['value'] = 0



    def printVector(self, v):
        
        out_grid = make_geocube(
            vector_data=v,
            measurements = ['value'],
            resolution=(-0.05, 0.05),
            fill=-9999
        )
        return out_grid

    def produceOutGrid(self, file):
        x = geopandas.read_file(file)
        x['value'] = x['DM'] + 1
        #print(x)
        newX = self.US.append(x)
        #print(newX)


        out_grid = make_geocube(
            vector_data=newX,
            measurements = ['value'],
            resolution=(-0.05, 0.05),
            fill=-9999
            #geom=json.dumps(geom)
        )
        #print(out_grid.dims)
        new = out_grid.to_array()
        new = new.to_numpy()
        mask = xr.where(out_grid.value<-1999.0, 0, 1)
        mask = mask.to_numpy()
        masked = np.append([mask], new, axis = 0)
        #print(type(masked))
        #print(masked.shape)
        #print(masked)
        return out_grid, masked
        
    def rasterize(self, makeFile=False):
        years = os.listdir(self.dir + 'temp')
        try:
            years.remove('._.DS_Store')
            years.remove('.DS_Store')
        except:
            pass
        
        for i in years:
            files = os.listdir(self.dir + 'temp/' + i)
            for j in files:
                out_grid = self.produceOutGrid(self.dir + 'temp/' + i + '/' + j)[1]
                '''print(out_grid.shape)
                for i in range(len(out_grid[0])):
                    for j in range(len(out_grid[0,i])):
                        if out_grid[0,i,j] != 0.0:
                            print(out_grid[1,i,j])
                            print(i)
                            print(j)'''
                if not os.path.exists(self.dir + 'rasterized/'):
                    os.mkdir(self.dir + 'rasterized/' )
                if not os.path.exists(self.dir + 'rasterized/' + i):
                    os.mkdir(self.dir + 'rasterized/' + i)
                if makeFile == True:
                    pass
                    #np.save(self.dir + 'rasterized/' + i + '/' + j[:14] + '.npy',out_grid)

    def show(self, out_grid, value):
        fig = plt.figure(figsize=(17, 15))
        ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
        da_grib = xr.where(value<-1999.0, np.nan, value)
        #print(type(da_grib))
        #print(da_grib)
        
        #new = type(da_grib.to_numpy())
    

        #da_grib2 = xr.where(out_grid2.value<-1999.0, np.nan, out_grid2.value)
        
        #da_grib2.plot(levels = [0,1,2,3,4,5,6])
        da_grib.plot(levels = [0, 1, 2, 3, 4, 5, 6])


        ax.set_extent([-180, 180, -90, 90])
        ax.set_title("Rasterized with 0.01$^o$ Grids", fontsize=24)
        plt.show()

    def show2(self, out_grid):
        plt.figure(figsize=(17, 15))
        ax = plt.axes(projection=ccrs.PlateCarree())
        #ax = plt.axes(projection=ccrs.LambertConformal())
        #ax.set_global()
        ax.set_extent([-165,-150,16,25])
        out_grid.plot.pcolormesh(ax=ax, transform = ccrs.PlateCarree(), x='lon', y ='lat', add_colorbar=False)
        #out_grid.plot.pcolormesh(ax=ax, transform = ccrs.LambertConformal(), x='x', y ='y', add_colorbar=False)
        ax.coastlines()
        plt.show()

#print(type(US))
droughtData = dataRasterization(mainDir)
x = droughtData.produceOutGrid('/Volumes/AnikSchool/research_project/forecastingModel/dataDownloader/dataStorage/temp/2022/USDM_20220104_M.zip')[0]
#print(x.dims)
#print(type(x))
#print(x)
#droughtData.rasterize(False)
#droughtData.show(x, x.value)
#droughtData.(x.value)





