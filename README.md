# forecastingModel
Find a relation between snowpack water value and droughts

# daymet_data_script
## Purpose 
to extract weather and drought data from google earth engine.
## How to Run
```
python ./dataDownloader/daymet_data_script.py
```
## Prerequsites
Google Earth Engine and JSON Modules

## Output
Produces Multiple JSON files containing weather and drought data for California
The file name will be in the format of "{band}/rawCaliforniaWeatherData{yyyy}.json". Band will tell the type of the data.

# USDM_data_extraction

## Purpose
To extract USDM drought data shapefiles and store them neatly in files

## Prerequsites
Requests

## How to Run
```
python ./dataDownloader/USDM_data_extraction.py

```

## Output
Produces multiple zip files with path "./dataDownloader/dataStorage/raw"
Produces multiple zip files with path "./dataDownloader/dataStorage/temp"
Produces multiple shp files with path "./dataDownloader/dataStorage/unzipped
