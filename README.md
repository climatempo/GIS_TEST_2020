## Arthur Barbero



Para a realização deste teste, utilizei dos seguintes recursos:

#### Requisitos:
- Python 3.6 (https://www.python.org/)
- PostgreSQL 10.11 (https://www.postgresql.org/download/windows/)
- PostGIS 3.0.0
- GDAL - Windows Binaries - GISInternals Support Site (http://www.gisinternals.com) - gdal-300-1911-core
- Extensão GDAL para Python -  GISInternals Support Site (http://www.gisinternals.com) - GDAL-3.0.2.py3.6
- Geoserver 2.15.4 - Web Archive (http://geoserver.org/release/maintain/)
- Xampp - Tomcat Server Control - (https://www.apachefriends.org/pt_br/download.html)

#### Python external Libraries:
 - GDAL (https://pypi.org/project/GDAL/)
 - py-postgresql (https://pypi.org/project/py-postgresql/)
  
  
### Testes

**GDAL**

Para concluir a primeira etapa do teste, criei o programa em python ``GDAL.py`` que cria o ShapeFile e insere com as informações obtidas do ``.csv``, nesta etapa também, adicionei o atributo novo contido na etapa Plus, no final de sua compilação ele criará os arquivos ShapeFiles com o mesmo nome do ``.csv``.

Na conversão dos arquivos ShapeFiles para GeoJson, criei o programa em python ``GeoJson.py`` que lê o arquivo recém criado ``.shp`` e cria uma 'String' adcionando as features contidas no layer do ShapeFile para depois realizar a escrita de um novo arquivo, de mesmo nome com extensão ``.json``, utilizando a biblioteca ``json`` nativa do Python.

----

**PostGis**

A segunda etapa do teste realizei de duas maneiras. De primeiro caso, apliquei os comandos contidos na aplicação GDAL acessando o banco e importando o ``Json`` diretamente para uma nova tabela no PostgreSQL em um database local, porém, o teste solicitava as querys executadas, então por via das dúvidas, criei um programa em Python, ``PostGis.py``, que realiza todas as querys de forma automatizada, sem que eu tenha que acessar campo por campo em varios ``inserts``, ao iniciar o programa, primeiramente ele utiliza-ra da biblioteca ``py-postgresql`` para criar a conexão com o banco local, depois irá criar uma tabela com as colunas exatas para o arquivo ``Json``, em seguida iteramos o array de features que existem dentro do GeoJson a fim de selecionar os valores para concluir os ``inserts``.
Neste mesmo programa, depois de importar e inserir em uma tabela, ele imprime na tela a geometria em linha ``LineString`` utilizando uma query construida da mesma maneira, iterando sobre o array de features e pegando os pontos de 'long' e 'lat' com o comando ``ST_MakePoint`` e depois utilizando o comando ``ST_MakeLine`` e imprimindo com o formato dado pelo comando ``ST_AsEWKT``.

Nesta etapa não consegui realizar o 'Plus' pois não consegui formar poligonos com os arrays entregues, ou realmente não compreendi o enunciado, porém, gostaria muito de poder ter o conhecimento de como formar eles ou qual o formato entregue. Nesses 4 dias de teste pensei que a lógica por traz de apresentar as temperaturas que intersectassem nestes polígonos seria utilizando dos comandos:

>SELECT temp FROM tabela t WHERE ST_Intersects(geometria, ST_MakePoint(t.long, t.lat))

Porém, ainda assim não realizei esta parte. Se possível gostaria de saber ao final desta seleção quais seriam as respostas destes testes Plus.

----
**GeoServer**

Na terceira etapa, foi a que tive menos contato em minha experiência, então me contive em realizar apenas o solicitado.
No diretório ``3- Geoserver`` encontra-se o arquivo zipado do GeoServer que editei nesta etapa, mas se por via das dúvidas a camada criada apresentar algum erro, tomei a liberdade de exportar a camada em formato PNG que se encontra na pasta. 
A importação do arquivo ``NetCDF`` foi realizada sem problemas e a escala de cores foi realizada como estilização de camada no formato ``SLD``. Os valores de escalonamento escolhidos foram ``270, 280, 290, 300, 310`` trazendo maiores tons de amarelo e laranja ao mapa.

Em vista do tempo não realizei o teste Plus deste. Porém possuo conhecimentos em manipular a biblioteca do OpenLayers em nivel de Front-End, tanto em Vue.JS e React.JS.

----
**Gostaria de agradecer pela oportunidade de participar do teste, aprendi muito nestes 4 dias, já valeu a pena, tomo a liberdade de encaminhar novamente meu currículo pelo repositório.**

Estou a disposição para quaisquer dúvidas!

------


>***GIS_TEST_2020***:
>
>Repositório com teste prático para a seleção de candidatos para a vaga de estagiário GIS.
>
>ATENÇÃO:
>Mande o link do seu pull request para diego.gomes@climatempo.com.br
>  	
>---
>*** Teste ***:
>Vamos disponibilizar 2 arquivos:
>	CSV - Uma lista de temperaturas diarias por cidade (colunas long / lat)
>	NetCDF - Que contenha varios tempos (pode ser humidade ou prec horario)
>
>***DESAFIO***:
>
>**GDAL**
>
>Conversão do arquivo csv de temperaturas mínima e máxima para arquivos shapefile (enviar comandos)
>
>Conversão dos arquivos shapefiles de temperatura em geojson (enviar comandos)
>
>	Plus: 
>	Atualizar os arquivos shapefiles gerados com um atributo novo segundo as condições:
>		Se for menor ou igual a 20 deve conter o valor 'low' no atributo;
>		Se for maior que 20 e menor ou igual a 30, o valor deve ser 'medium';
>		Se for maior que 30 e menor que 40, o valor deve ser 'high';
>		Se for igual a 40 ou maior, o valor deve ser 'extreme'];
>		Obs: Deve-se enviar os comandos utilizados para reproduzirmos na Climatempo.
>	Converter a unidade de temperatura do arquivo NetCDF de Kelvin para Celsius 
>---
>**PostGis**
>
>Após converter os arquivos csv em geojson, importar para o postgres (enviar a query SQL)
>
>Manipulação do geojson, convertendo todos os pontos em uma única geometria de linha (enviar a query SQL)
>
>	Plus:
>	Filtrar os dados de temperatura a partir dos polígonos (enviar a query SQL)
>		[-56.468 -26.667 -42.500 -18.847] São Paulo 
>		[-46.264 -24.429 -39.233 -19.155] Rio de Janeiro
>		[-60.352 -18.775 -23.656 0.286]   Nordeste 
>	
>---
>**Geoserver**
>
>Em seu computador, deverá subir uma aplicacao geoserver em um servidor WEB para editar o projeto Geoserver (2.15.4) disponibilizado em >http://geoserver.org/.
>
>No projeto, cadastrar a camada utilizando o arquivo NETCDF.
>
>Criar uma escala de cor e aplicar a camada (a escala deve ter intervalos de 10)
>
>Ex:. 0 - azul escuro, 10 - azul claro, 20 - amarelo, 30 - laranja, 40 -vermelho.
>
>
>	Plus:
>
>	Criar uma camada dos estados do Brasil com os dados do IBGE.
>	
>	Criar um grupo de camadas que reúna a camada de estados SOBREPONDO a camada de temperatura previamente criada.
>
>	Criar uma página simples com openlayers ou leaflet que consumirá essa camada, deve-se conter:
>		Um select com os tempos pré definidos.
>		Um mapa que exibe a camada criada.
>
>	Obs:
>		Ao trocar o tempo no select deverá exibir a camada com o tempo específico no mapa.
>
>		A página deve ser criada na raiz do projeto do geoserver.
>
>
>
><kbd>ATENÇÃO: O PROJETO **GEOSERVER EDITADO** DEVERÁ SER ZIPADO E ENVIADO JUNTO COM AS CONSULTAS E COMANDOS.</kbd>
>
