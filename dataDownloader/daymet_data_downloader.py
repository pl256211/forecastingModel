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

def placeFileInDir(years, year, loc = 'hi'):
    numb = year
    bands = ['prcp_annttl_', 'tmin_annavg_', 'swe_annavg_', 'vp_annavg_', "tmax_annavg_"]
    for i in range(years):
        num = str(numb)
        for j in bands:
            directoryName = './dataStorage/raw/daymet/'
            url = 'https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1852/catalog.html?dataset=1852/daymet_v4_' + j + loc + '_' + num + '.nc'

            if not os.path.exists(directoryName):
                os.mkdir(directoryName)

            filename = download_file(url, directoryName)
            print(filename)
        numb -= 1

placeFileInDir(12, 2021)