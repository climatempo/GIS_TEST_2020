import gdal
import osgeo
import csv
import osgeo.ogr, osgeo.osr as ogr, osr #we will need some packages
from osgeo import ogr #and one more for the creation of a new field

driver = ogr.GetDriverByName("ESRI Shapefile")
data_source = driver.CreateDataSource("./1- GDAL/temperatura_maxmin_GIS.shp")
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)

layer = data_source.CreateLayer("main", srs, ogr.wkbPoint)

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

with open('./1- GDAL/temperatura_maxmin_GIS.csv', "r") as csv_toRead:
  csv_file = csv.DictReader(csv_toRead, delimiter=';',  fieldnames=['city', 'lat', 'long', 'temp', 'value'])
  for row in csv_file:

    feature = ogr.Feature(layer.GetLayerDefn())

    feature.SetField("city", row['city'])
    feature.SetField("max/min", row['value'])
    feature.SetField("lat", row['lat'])
    feature.SetField("long", row['long'])
    feature.SetField("temp", row['temp'])
    
    if int(feature.temp) <= 20:
      feature.SetField("plus", 'low')
    
    elif int(feature.temp) > 20 and int(feature.temp) <= 30:
      feature.SetField("plus", 'medium')

    elif int(feature.temp) > 30 and int(feature.temp) <= 40:
      feature.SetField("plus", 'high')
    
    elif int(feature.temp) > 40:
      feature.SetField("plus", 'extreme')

    wkt = f"POINT({float(row['long'])} {float(row['lat'])})"

    point = ogr.CreateGeometryFromWkt(wkt)

    feature.SetGeometry(point)
    layer.CreateFeature(feature)
    feature = None
data_source = None