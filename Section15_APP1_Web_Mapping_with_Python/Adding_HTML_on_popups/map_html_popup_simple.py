import folium
import pandas

# Creamos el dataframe desde el archivo con los datos
myData = pandas.read_csv("../Resources/Volcanoes.txt")
lat = list(myData["LAT"])
lon = list(myData["LON"])
elev = (list(myData["ELEV"]))
name = list(myData["NAME"])

# Definimos el formato del texto mostrado en el PopUp mediante código HTML
html = '''<h4>Volcano information:</h4>
        Heigth: %s m.
        '''

map = folium.Map(
    location=[38.58, -99.09],
    zoom_start=6,
    tiles="cartodb positron"
    )

# Añadimos objetos al mapa - MARKERS
#       Definimos la localizacion [latitud, longitud], el texto del popup que se muestra al pinchar sobre el Marker así como el estilo del mismo
#       FeatureGroup crea un grupo de características que despues podemos aplicar conjuntamente.
fg = folium.FeatureGroup(name='My Volcanoes')

# Añadir los MARCADORES al mapa con las características elegidas.
for lt, ln, el, nm in zip(lat, lon, elev, name):
        iframe = folium.IFrame(
                html=html % str(el),
                width=200,
                height = 100
                )
        fg.add_child(
                folium.Marker(
                        location= [lt, ln],
                        popup= folium.Popup(iframe),
                        icon=folium.Icon(
                                color= 'green',
                                icon_color= 'white'
                                )))

map.add_child(fg)
map.save("Map_html_popup_simple.html")



