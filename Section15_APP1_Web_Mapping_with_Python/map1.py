# IMPORTACIÓN DE BIBLIOTECAS Y PAQUETES
import folium
import pandas
import requests

# DECLARACION DE FUNCIONES Y RUTINAS
# Función: color_producer
# Descripción:  Retorna un color diferente según el valor de elevación
# Parámetros:   elevation - INTEGER:    Valor de elevación
# Retorno:      color - STRING:         Cadena de caracteres indicanto el color
def color_producer(elevation):
        if elevation < 1000:
                return 'green'
        elif 1000 <= elevation < 3000:
                return 'orange'
        else:
                return 'red'

# Creamos el dataframe desde el archivo con los datos
myData = pandas.read_csv("./Resources/Volcanoes.txt")
lat = list(myData["LAT"])
lon = list(myData["LON"])
elev = list(myData["ELEV"])
name = list(myData["NAME"])

# Creación de Mapa con punto de inicialización, nivel de zoom y tipo de cartografía
map = folium.Map(
    location=[38.58, -99.09],
    zoom_start=6,
    tiles="cartodb positron"
    )

# Añadimos objetos al mapa - MARKERS
#       Definimos la localizacion [latitud, longitud], el texto del popup que se muestra al pinchar sobre el Marker así como el estilo del mismo
#       FeatureGroup crea un grupo de características que despues podemos aplicar conjuntamente, en este caso para todos los Volcanes creamos una y para la capa de poblacion otra.
fg_volcanoes = folium.FeatureGroup(name='My Volcanoes')
fg_population = folium.FeatureGroup(name='Population')

# Categorizamos los colores de MARKERS segun la elevación
marker_elevation_color = 'green'

# Añadir los MARCADORES al mapa con las características elegidas.
for lt, ln, el, nm in zip(lat, lon, elev, name):
        fg_volcanoes.add_child(
                folium.CircleMarker(
                        location= [lt, ln],
                        radius= 6,
                        popup= str(el)+ " m.",
                        icon=folium.Icon(color= color_producer(el), icon_color= 'white'),
                        color = 'grey',
                        fill = True,
                        fillColor = color_producer(el),
                        fillOpacity = 0.5                         
                        ))
# Añadir el layer de población desde el GeoJSON
fg_population.add_child (folium.GeoJson (data = open("./Resources/world.json",'r', encoding='utf-8-sig').read(),
                            style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
                                                        else 'orange' if 10000000 <= x['properties']['POP2005'] < 50000000 
                                                        else 'red'}
                                                        ))

# Añadir la capa de marcadores al mapa
map.add_child(fg_volcanoes)
# Añadir la capa de poblacion al mapa
map.add_child(fg_population)
# Añadir control de LAYER
map.add_child(folium.LayerControl())
# Guardar el mapa en fichero HTML
map.save("Map1.html")