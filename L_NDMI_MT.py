import ee
from ee_plugin import Map

#LANDSAT MULTITEMPORAL Normalised Difference Index

#rename bands
#Load image collections

L4 = ee.ImageCollection("LANDSAT/LT04/C01/T1_TOA").filterBounds(geometry)
L5 = ee.ImageCollection("LANDSAT/LT05/C01/T1_TOA").filterBounds(geometry)
L7 = ee.ImageCollection("LANDSAT/LE07/C01/T1_TOA").filterBounds(geometry)
L8 = ee.ImageCollection("LANDSAT/LC08/C01/T1_TOA").filterBounds(geometry)

#Collection 1 - Landsat 4 and 5
C1 = L5.merge(L4) \
.filterDate('1984-01-01', '1987-01-01') \
.sort('DATE_ACQUIRED') \
.filter(ee.Filter.lt('CLOUD_COVER', 10)) \
.select(['B4', 'B5']) \
.mean() \
.normalizedDifference(['B4', 'B5'])

#Collection 2 - Landsat 5 and 7
C2 = L7.merge(L5) \
.filterDate('1999-01-01', '2001-01-01') \
.sort('DATE_ACQUIRED') \
.filter(ee.Filter.lt('CLOUD_COVER', 10)) \
.select(['B4', 'B5']) \
.mean() \
.normalizedDifference(['B4', 'B5'])

#Collection 3 - Landsat 8
C3 = L8 \
.filterDate('2018-01-01', '2019-10-10') \
.sort('DATE_ACQUIRED') \
.filter(ee.Filter.lt('CLOUD_COVER',10)) \
.select(['B5', 'B6']) \
.mean() \
.normalizedDifference(['B5', 'B6'])

#Composite
NDWIchange = ee.Image.cat(C1, C2, C3)
NDWIchange2 = NDWIchange.multiply(1)

vizParams = {
  'min': -0.25,
  'max': 0.5
}
Map.addLayer(NDWIchange2, vizParams, 'NDWIchange')
Map