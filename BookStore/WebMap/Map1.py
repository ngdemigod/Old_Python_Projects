import pandas
import folium

data = pandas.read_csv("/Users/austin.saleh/Dropbox/Courses/Python/Projects/WebMap/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """<h4>Volcano Information<h4>
Name: %s <br>
Height: %s m
"""
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

us_map = folium.Map(location=[33.74, -84.38], zoom_start=6,tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el, na in zip(lat,lon,elev,name):
    iframe = folium.IFrame(html=html % (na,el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup=folium.Popup(iframe),
    fill_color= color_producer(el), color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
 style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

us_map.add_child(fgv)
us_map.add_child(fgp)
us_map.add_child(folium.LayerControl())

us_map.save("Map1.html")