import ee
from ee_plugin import Map

# Load the Sentinel-1 ImageCollection.
sentinel1 = ee.ImageCollection('COPERNICUS/S1_GRD')

# Filter by metadata properties.
vh = sentinel1 \
  .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH')) \
  .filter(ee.Filter.eq('instrumentMode', 'IW')) \
  .filterDate("2015-01-01","2022-01-01")

# Filter to get images from different look angles.
vhAscending = vh.filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING'))
vhDescending = vh.filter(ee.Filter.eq('orbitProperties_pass', 'DESCENDING'))

# Create a composite from means at different polarizations and look angles.
vhMaxA = vhAscending.select('VH').max();#.focal_median()
vhMaxD = vhDescending.select('VH').max();#.focal_median()

# Map composite over the Channel
Map.addLayer(vhMaxA, {'min': -15, 'max': 0}, 'VH ASC max',0)
Map.addLayer(vhMaxD, {'min': -30, 'max': 0}, 'VH DES max')
Map