# Importando as bibliotecas de terceiros
import json
import ogr

# Criando um ShapeFile e abrindo o ShapeFile criado anteriormente
driver = ogr.GetDriverByName('ESRI Shapefile')
shp_path = r'./1- GDAL/temperatura_maxmin_GIS.shp'
data_source = driver.Open(shp_path, 0)

# Cabeçario do GeoJson
fc = {
    'type': 'FeatureCollection',
    'features': []
    }

# Recuperando o layer do ShapeFile, percorrendo o layer e adicionando para o arrays de features no formato Json Object
lyr = data_source.GetLayer(0)
for feature in lyr:    
    fc['features'].append(feature.ExportToJson(as_object=True))

# Criando um arquivo Json e escrevendo o objeto adquirido
with open('./1- GDAL/temperatura_maxmin_GIS.json', 'w') as f:
    json.dump(fc, f)