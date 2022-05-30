import ee
from ee_plugin import Map

#rename L8 bands in order to create one seamless composite with L5
def renameBandsOLI(image):
    bands = ['B4', 'B3', 'B2']
    new_bands = ['B3', 'B2', 'B1']
    return image.select(bands).rename(new_bands)

#Load image collections
L4 = ee.ImageCollection("LANDSAT/LT04/C01/T1_SR")
L5 = ee.ImageCollection("LANDSAT/LT05/C01/T1_SR")
L7 = ee.ImageCollection("LANDSAT/LE07/C01/T1_SR")
L8 = ee.ImageCollection("LANDSAT/LC08/C01/T1_SR").map(renameBandsOLI)
collection = L4.merge(L5.merge(L7.merge(L8)))

collection_filtered = collection \
    .filter(ee.Filter.calendarRange(2,11,'month')) \
    .filter(ee.Filter.lt('CLOUD_COVER', 7)) \
    .select(['B3','B2','B1'])

image_01 = collection_filtered \
    .filterDate('2010-01-01', '2020-01-01') \
    .median()

vizParams = {'min': -10, 'max': 4000}

Map.addLayer(image_01, vizParams)
Map