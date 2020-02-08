import json
import ogr

driver = ogr.GetDriverByName('ESRI Shapefile')
shp_path = r'./1- GDAL/temperatura_maxmin_GIS.shp'
data_source = driver.Open(shp_path, 0)

fc = {
    'type': 'FeatureCollection',
    'features': []
    }

lyr = data_source.GetLayer(0)
for feature in lyr:    
    fc['features'].append(feature.ExportToJson(as_object=True))

with open('./1- GDAL/temperatura_maxmin_GIS.json', 'w') as f:
    json.dump(fc, f)