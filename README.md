***GIS_TEST_2020***:
Repositório com teste prático para a seleção de candidatos para a vaga de estagiário GIS.

ATENÇÃO:
Mande o link do seu pull request para diego.gomes@climatempo.com.br
  	
---
*** Teste ***:
Vamos disponibilizar 2 arquivos:
	CSV - Uma lista de temperaturas diarias por cidade (colunas long / lat)
	NetCDF - Que contenha varios tempos (pode ser humidade ou prec horario)

***DESAFIO***:

**GDAL**

Conversão do arquivo csv de temperaturas mínima e máxima para arquivos shapefile (enviar comandos)

Conversão dos arquivos shapefiles de temperatura em geojson (enviar comandos)

	Plus: 
	Atualizar os arquivos shapefiles gerados com um atributo novo segundo as condições:
		Se for menor ou igual a 20 deve conter o valor 'low' no atributo;
		Se for maior que 20 e menor ou igual a 30, o valor deve ser 'medium';
		Se for maior que 30 e menor que 40, o valor deve ser 'high';
		Se for igual a 40 ou maior, o valor deve ser 'extreme'];
		Obs: Deve-se enviar os comandos utilizados para reproduzirmos na Climatempo.
	Converter a unidade de temperatura do arquivo NetCDF de Kelvin para Celsius 
---
**PostGis**

Após converter os arquivos csv em geojson, importar para o postgres (enviar a query SQL)

Manipulação do geojson, convertendo todos os pontos em uma única geometria de linha (enviar a query SQL)

	Plus:
	Filtrar os dados de temperatura a partir dos polígonos (enviar a query SQL)
		[-56.468 -26.667 -42.500 -18.847] São Paulo 
		[-46.264 -24.429 -39.233 -19.155] Rio de Janeiro
		[-60.352 -18.775 -23.656 0.286]   Nordeste 
	
---
**Geoserver**

Em seu computador, deverá subir uma aplicacao geoserver em um servidor WEB para editar o projeto Geoserver (2.15.4) disponibilizado em http://geoserver.org/.

No projeto, cadastrar a camada utilizando o arquivo NETCDF.

Criar uma escala de cor e aplicar a camada (a escala deve ter intervalos de 10)

Ex:. 0 - azul escuro, 10 - azul claro, 20 - amarelo, 30 - laranja, 40 -vermelho.


	Plus:

	Criar uma camada dos estados do Brasil com os dados do IBGE.
	
	Criar um grupo de camadas que reúna a camada de estados SOBREPONDO a camada de temperatura previamente criada.

	Criar uma página simples com openlayers ou leaflet que consumirá essa camada, deve-se conter:
		Um select com os tempos pré definidos.
		Um mapa que exibe a camada criada.

	Obs:
		Ao trocar o tempo no select deverá exibir a camada com o tempo específico no mapa.

		A página deve ser criada na raiz do projeto do geoserver.



 <kbd>ATENÇÃO: O PROJETO **GEOSERVER EDITADO** DEVERÁ SER ZIPADO E ENVIADO JUNTO COM AS CONSULTAS E COMANDOS.</kbd>
