import folium
import pandas as pd

data = pd.read_csv("stadium.csv", encoding="cp1252")
latitude = list(data['LAT'])
longitude = list(data['LON'])
name = list(data["NAME"])
capacity = list(data["capacity"])
website = list(data["website"])
picture = list(data['picture'])

f = folium.FeatureGroup("my map")
f.add_child(folium.GeoJson(data=(open("india_states.json",'r',encoding='utf-8-sig').read())))
for lt, ln, nm, cp, ws, pic in zip(latitude, longitude, name, capacity, website, picture):
                                   
    f.add_child(folium.Marker(location=[lt, ln],popup="&lt;b&gt;name: &lt;/b&gt;"+nm+ "&lt;br&gt; &lt;b&gt;capacity"
                                    ": &lt;/b&gt;"+str(cp)+""
                                    "&lt;br&gt;&lt;b&gt;wikipedia"
                                    "link: &lt;/b&gt;&lt;a href="+ws+"&gt;"
                            "click here&lt;/a&gt;"+"&lt;br&gt; &lt;img src="+pic+" "
                            "height=142 width=290&gt;",icon=folium.Icon(color="green")))
map = folium.Map(location=[21.1458,79.0082],zoom_start=5)
map.add_child(f)
map.save('map.html')