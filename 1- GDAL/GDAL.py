# Importando bibliotecas de terceiros
import gdal
import osgeo
import osgeo.ogr, osgeo.osr as ogr, osr
from osgeo import ogr 

# Importando bibliotecas nativas
import csv

# Criando ShapeFile e registrando o DATUM WGS84 - 4326
driver = ogr.GetDriverByName("ESRI Shapefile")
data_source = driver.CreateDataSource("./1- GDAL/temperatura_maxmin_GIS.shp")
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)

# Criação do layer nos parâmetros criados acima
layer = data_source.CreateLayer("main", srs, ogr.wkbPoint)

# Criação das propriedades que irão popular o layer
field_name = ogr.FieldDefn("city", ogr.OFTString)
field_name.SetWidth(32)
layer.CreateField(field_name)
field_maxmin = ogr.FieldDefn("max/min", ogr.OFTString)
field_maxmin.SetWidth(32)
layer.CreateField(field_maxmin)
layer.CreateField(ogr.FieldDefn("lat", ogr.OFTReal))
layer.CreateField(ogr.FieldDefn("long", ogr.OFTReal))
layer.CreateField(ogr.FieldDefn("temp", ogr.OFTReal))
field_plus = ogr.FieldDefn("plus", ogr.OFTString)
field_plus.SetWidth(32)
layer.CreateField(field_plus)

# Lendo o arquivo csv e populando o layer com sua propriedade correspondente
with open('./1- GDAL/temperatura_maxmin_GIS.csv', "r") as csv_toRead:
  csv_file = csv.DictReader(csv_toRead, delimiter=';',  fieldnames=['city', 'lat', 'long', 'temp', 'value'])
  for row in csv_file:
    feature = ogr.Feature(layer.GetLayerDefn())
    feature.SetField("city", row['city'])
    feature.SetField("max/min", row['value'])
    feature.SetField("lat", row['lat'])
    feature.SetField("long", row['long'])
    feature.SetField("temp", row['temp'])

    # PLUS: adicionando uma propriedade a mais conforme a temperatura    
    if int(feature.temp) <= 20:
      feature.SetField("plus", 'low')
    
    elif int(feature.temp) > 20 and int(feature.temp) <= 30:
      feature.SetField("plus", 'medium')

    elif int(feature.temp) > 30 and int(feature.temp) <= 40:
      feature.SetField("plus", 'high')
    
    elif int(feature.temp) > 40:
      feature.SetField("plus", 'extreme')

    # Criando o ponto geometrico no formato Well Know Text
    wkt = f"POINT({float(row['long'])} {float(row['lat'])})"
    point = ogr.CreateGeometryFromWkt(wkt)

    feature.SetGeometry(point)
    layer.CreateFeature(feature)
    feature = None
data_source = None