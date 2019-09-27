import folium


latitude = 33.593285
longtude = 130.35151
name = "福岡タワー"

map = folium.Map(location=[latitude, longtude], zoom_start=18)
folium.Marker(location=[latitude, longtude], popup=name).add_to(map)

map.save("post_list.html")
