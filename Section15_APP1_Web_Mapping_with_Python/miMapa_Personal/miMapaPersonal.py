# IMPORTACION DE BIBLIOTECAS Y PAQUETES
import pandas as pd
import json
import folium
import string

# Crear mapa
map = folium.Map(
    location = [40.437925, -3.7619364],
    zoom_start = 6,
    tiles = 'cartodb positron'
    )

# Importamos los datos y abrimos el archivo
with open ('./resources/sitios_guardados.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

# Normalizamos los datos y le damos un formato de tabla
misDatos = pd.json_normalize(data['features'])
#     Eliminamos los datos INCONGRUENTES: coordenadas = [0.0]
misDatos = misDatos[misDatos["geometry.coordinates"].apply(lambda x: x != [0, 0])]
#     Eliminamos aquellos que no tienen nombre
misDatos = misDatos[misDatos["properties.location.name"].notna()]

#     Eliminamos los duplicados si existen
#misDatos = misDatos.drop_duplicates()


# Extraemos los datos de latitud y longitud desde el archivo
longitud = list(misDatos['geometry.coordinates'].apply (lambda x: x[0]))
latitud = list(misDatos['geometry.coordinates'].apply (lambda x: x[1]))
nombre = list(misDatos['properties.location.name'])

# Formato de los datos mostrados en el PopUP del mapa
html = '''<h4>%s</h4>'''


# Crear y caracterizar la capa de SITIOS GUARDADOS a los MARCADORES
fg_saved = folium.FeatureGroup(name = 'Mis Sitios Guardados')

for lat, lon, nm in zip(latitud, longitud, nombre):
    iframe = folium.IFrame(html %str(nm).title(), width=150, height=100)
    fg_saved.add_child (
        folium.CircleMarker (
            location = [lat, lon],
            radius = 6,
            popup = folium.Popup(iframe),
            icon = folium.Icon(color = 'darkgreen', icon_color = 'white'),
            color = 'gray',
            fill = True,
            fillColor = 'orange',
            fillOpacity = 0.5
            ))

# Añadir la capa de SITIOS GUARDADOS
map.add_child(fg_saved)
# Añadir el control de capas al mapa
map.add_child(folium.LayerControl())
# Guardar el mapa en un fichero HTML
map.save ("miMapa.html")