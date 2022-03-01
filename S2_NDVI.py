import ee
from ee_plugin import Map

def maskS2clouds(image):
  qa = image.select('QA60')

  #Bits 10 and 11 are clouds and cirrus, respectively.
  cloudBitMask = 1 <<10 
  cirrusBitMask = 1 << 11

  #Both flags should be set to zero, indicatin clear conditions
  mask = qa.bitwiseAnd(cloudBitMask).eq(0) \
  .And(qa.bitwiseAnd(cirrusBitMask).eq(0))

  return image.updateMask(mask).divide(10000)

image = ee.ImageCollection('COPERNICUS/S2') \
.filterDate('2015-01-01','2021-12-31') \
.filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)) \
.map(maskS2clouds) \
.median()

# NDVI = '(nir-red)/(nir+red)'

ndvi = image.expression('(nir-red)/(nir+red)',{
  'nir':image.select('B8'),
  'red':image.select('B4')
}).rename('NDVI')

final_image = image.addBands(ndvi)

visualisation2 = {
  'min': 0.004,
  'max': 0.39,
  'bands':['NDVI'],
  'palette': ['f0ff10','ff5594','0bf532','02117e']
}

Map.addLayer(final_image, visualisation2, 'NDVI')
Map