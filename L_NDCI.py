import ee
from ee_plugin import Map

#LANDSAT Normalised Difference Vegetation Index

def renameBandsOLI(image):
    bands = ['B6','B5','B4', 'B3', 'B2']
    new_bands = ['B5','B4','B3', 'B2', 'B1']
    return image.select(bands).rename(new_bands)

#Load image collections
L4 = ee.ImageCollection("LANDSAT/LT04/C01/T1_SR")
L5 = ee.ImageCollection("LANDSAT/LT05/C01/T1_SR")
L7 = ee.ImageCollection("LANDSAT/LE07/C01/T1_SR")
L8 = ee.ImageCollection("LANDSAT/LC08/C01/T1_SR").map(renameBandsOLI)
collection = L4.merge(L5.merge(L7.merge(L8)))

collection_filtered = collection \
    .filterDate('1984-01-01', '2021-10-10') \
    .filter(ee.Filter.calendarRange(2,11,'month')) \
    .filter(ee.Filter.lt('CLOUD_COVER', 7)) \
    .select(['B5','B4'])

NDCI = collection_filtered \
.filterDate('2018-01-01', '2020-01-01') \
.mean() \
.normalizedDifference(['B5', 'B4'])

NDCI2 = NDCI.multiply(-1)

vizParams = {
  'min': -0.5,
  'max': 0.5,
  'palette': ["ffffff","aeaf75","000000"]
}

Map.addLayer(NDCI2, vizParams, 'NDCI')
Map