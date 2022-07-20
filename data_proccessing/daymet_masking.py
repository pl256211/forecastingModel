import netCDF4 as nc

filePath = '/Volumes/AnikSchool/research_project/forecastingModel/dataDownloader/dataStorage/raw/daymet/'
ds = nc.Dataset(str(filePath + "daymet_v4_daily_hi_prcp_2019.nc"))


tmax = ds['prcp'][:]