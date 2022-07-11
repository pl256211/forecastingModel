import requests
import os

def download_file(url, directory):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url) as r:
        r.raise_for_status()
        with open(directory + local_filename, 'wb') as f:
            f.write(r.content)
    return local_filename

def placeFileInDir():
    
    bands = ['z.nc', 'spi14d.nc', 'pdsi.nc']
    
    for j in bands:
        directoryName = './dataStorage/raw/gridmet/'
        url = 'https://www.northwestknowledge.net/metdata/data/' + bands[j]

        if not os.path.exists(directoryName):
            os.mkdir(directoryName)

        filename = download_file(url, directoryName)
        print(filename)