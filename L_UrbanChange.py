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
    .filterDate('1982-01-01', '1992-01-01') \
    .median()

image_02 = collection_filtered \
    .filterDate('1997-01-01', '2005-01-01') \
    .median()

image_03 = collection_filtered \
    .filterDate('2017-01-01', '2021-01-01') \
    .median()

rgb = ee.Image.cat(image_01, image_02, image_03)
rgb2 = rgb.multiply(-1)

vizParams = {'min': 400, 'max': 2500, 'gamma': [1], 'bands':["B3", "B3_1", "B3_2"]}
vizParams2 = {'min': -4200, 'max': -200, 'gamma': [0.4, 0.4, 0.4], 'bands':["B3", "B3_1", "B3_2"]}

Map.addLayer(rgb2, vizParams2)
Map

