# importing the requests module
import requests
#import the ability to change zip files
from zipfile import ZipFile
#import the ability to make changes to files
import os

def download_file(url, directory):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url) as r:
        r.raise_for_status()
        with open(directory + local_filename, 'wb') as f:
            f.write(r.content)
    return local_filename


def pullData(years, year):
    for i in range (years):
        url = 'https://droughtmonitor.unl.edu/data/shapefiles_m//' + str(year) + '_USDM_M.zip'

        # Downloading the file by sending the request to the URL
        #req = requests.get(url)
        
        # Split URL to get the file name
        #filename = url.split('/')[-1]
        #print(filename)
        
        directoryName = './dataStorage/raw/USDM/'

        if not os.path.exists(directoryName):
            os.mkdir(directoryName)

        filename = download_file(url, directoryName)
        print(filename)

        # Writing the file to the local file system
        #with open(directoryName + filename,'wb') as output_file:
         #   output_file.write(req.content)
        print('Downloading Completed')

        with ZipFile(directoryName + filename, 'r') as zip:
            zip.extractall('./dataStorage/temp/' + str(year))

        
        for path in os.listdir('./dataStorage/temp/' + str(year)):
            with ZipFile("./dataStorage/temp/" + str(year) + '/' + path, 'r') as zip:
                zip.extractall('./dataStorage/unzipped/' + str(year))
        year -=1

def removeEverythingButSHP(years, startYear):
    year = startYear
    for i in range(years):
        for path in os.listdir('./dataStorage/unzipped/' + str(year)):
            if path[-3:] != 'shp':
               os.remove('./dataStorage/unzipped/' + str(year) + '/' + path)
        year -= 1
pullData(10, 2022)
#removeEverythingButSHP(10, 2022)