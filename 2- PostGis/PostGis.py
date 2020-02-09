# Importando as bibliotecas de terceiros
import postgresql
import json

# Fazendo conexão com o banco local
db = postgresql.open(user = 'postgres', database = 'postgis_30_sample', port = 5432, password = 'postgres')

# Criando tabela conforme os campos do Json 
db.execute("""CREATE TABLE public.gis_test
              (
                  id serial NOT NULL,
                  city character varying,
                  maxmin character varying,
                  lat double precision,
                  long double precision,
                  temp double precision,
                  plus character varying,
                  CONSTRAINT gis_test_pkey PRIMARY KEY (id)
              ) """)

# Instanciando a query para realizar Insert
make_gis_table = db.prepare("INSERT INTO gis_test (city, maxmin, lat, long, temp, plus) VALUES ($1, $2, $3, $4, $5, $6)")

# Abrindo arquivo Json e realizando a leitura e transformando em dicionário
arq = open('./1- GDAL/temperatura_maxmin_GIS.json', 'r')
geojson = json.loads(arq.read())

# Executando as ações preparadas anteriormente
with db.xact():
# Percorrendo o array 'features' que contêm as informações de cada registro e inserindo na tabela.
  list(map(lambda feature: make_gis_table(f"{feature['properties']['city']}",
      f"{feature['properties']['max/min']}",
      feature['properties']['lat'],
      feature['properties']['long'],
      feature['properties']['temp'],
      f"{feature['properties']['plus']}"), geojson['features']))
   
#Inserção concluída - Primeira etapa

# Convertendo todos os pontos em uma única geometria de linha

# Construindo a query baseada em todas as coordenadas do Json
make_lineString = "SELECT ST_AsEWKT( ST_MakeLine( ARRAY[ "

# Criando pontos con cada Latitude e Longitude
for feature in geojson['features']:
  make_lineString += f"ST_MakePoint({feature['properties']['long']}, {feature['properties']['lat']}), "  

# Excluindo a última virgula
make_lineString = make_lineString[:-2]
make_lineString += " ] ));"

# Realizando a query
select = db.prepare(make_lineString)

# Mostrando resultado
for result in select:
  print(result)


# Segunda etapa concluída

### Utilizando GDAL para importação do arquivo e criação de tabela.
#Utilizando o GDAL em command line podemos fazer rapidamente a criação da tabela com os 'inserts' das informações com o comando:

 #   ogr2ogr -f "PostgreSQL" PG:"dbname=my_database user=postgres" "temperatura_maxmin_GIS.json" -nln destination_table -append