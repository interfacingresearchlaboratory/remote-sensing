import ee
from ee_plugin import Map

dataset = ee.Image('USGS/SRTMGL1_003') \
    .select('elevation')

nine = {'min': 000, 'max': 2000, 'palette':['Black', 'White'], 'opacity': 1};

Map.addLayer(dataset, nine, 'SRTM_30_0to100m01')