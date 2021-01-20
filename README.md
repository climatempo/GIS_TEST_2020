<p align="center">
  <a href="http://www.climatempo.com.br">
      <img src="http://i.imgur.com/Q9lCAMF.png" alt="Climatempo" width="300px"/>
  </a>
</p>

___


## Processo de recrutamento

Olá candidato, pronto para participar do nosso processo de recrutamento **GIS**?

### Requisitos

**Bons conhecimentos em:**

- Python
- QGis
- PostGis
- Geoserver
- NetCDF
- Sistema de coordenadas

**Diferenciais:**

- Mapserver
- Geopandas

<br />

## Os Desafios

**Arquivos**

| Tipo   |Descrição                                                     |
| :------|:-------------------------------------------------------------|
| CSV    |Uma lista de temperaturas diarias por cidade (colunas lon/lat)|
| NetCDF |Contendo varios tempos (bandas) com um recorte AMS.           |

<br/>

**GDAL**

Conversão do arquivo csv de temperaturas mínima e máxima para arquivos shapefile.

Conversão dos arquivos shapefiles de temperatura em geojson.

	Plus: 
	Atualizar os arquivos shapefiles gerados com um atributo novo segundo as condições:
		Se for menor ou igual a 20 deve conter o valor 'low' no atributo;
		Se for maior que 20 e menor ou igual a 30, o valor deve ser 'medium';
		Se for maior que 30 e menor que 40, o valor deve ser 'high';
		Se for igual a 40 ou maior, o valor deve ser 'extreme'];
		
	Converter a unidade de temperatura do arquivo NetCDF de Kelvin para Celsius

<br/>

**PostGis**

Após converter os arquivos csv em geojson, importar para o postgres.

Manipulação do geojson, convertendo todos os pontos em uma única geometria de linha.

	Plus:
	Filtrar os dados de temperatura a partir dos polígonos (enviar a query SQL)
		[-56.468 -26.667 -42.500 -18.847] São Paulo 
		[-46.264 -24.429 -39.233 -19.155] Rio de Janeiro
		[-60.352 -18.775 -23.656 0.286]   Nordeste 

<br />

**Geoserver**

Em seu computador, deverá subir uma aplicacao geoserver em um servidor WEB para editar o projeto Geoserver disponibilizado em http://geoserver.org/release/stable/.

No projeto, cadastrar a camada utilizando o arquivo NETCDF.

Criar uma escala de cor (criada com CSS) e aplicar a camada (a escala deve ter intervalos de 10). Ex:

<br />

| Cor       |Valor|
| :---------|:-|
| Vermelho  |0 |
| Laranja   |10|
| Amarelo   |20|
| Verde     |30|
| Azul      |40|
| Roxo      |50|

<br />


	Plus:

	Criar uma camada dos estados do Brasil com os dados do IBGE.
	
	Criar um grupo de camadas que reúna a camada de estados SOBREPONDO a camada de temperatura previamente criada.

	Criar uma página simples com openlayers ou leaflet que consumirá essas camadas, contendo:
		Uma lista com os tempos pré definidos.
		Um mapa que exibe a camada criada.

	Obs:
		Ao trocar o tempo no lista (<select>) deverá exibir a camada com o tempo específico no mapa.

		A página deve ser criada na raiz do projeto do geoserver.



## ATENÇÃO ##

O processo do desafio deve ser:

1. Faça o fork do desafio.

2. Crie um **PROJECT.md** com a explicação de como devemos executar os comandos e queries utilizados para os desafios assim como o máximo de detalhes possivel do que foi feito.

3. O projeto **GEOSERVER EDITADO** deverá ser zipado e incluido no projeto.

4. Após concluir faça um pull request.

5. Envie um e-mail para diego.gomes@climatempo.com.br

___

Qualquer dúvida entre em contato com nossa equipe.

