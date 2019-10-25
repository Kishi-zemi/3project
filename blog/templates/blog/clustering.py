import sqlite3
import pandas as pd
import folium
from folium.plugins import MarkerCluster
import pandas.io.sql as psql

dbname = 'h30_28.db'

conn = sqlite3.connect(dbname)
cur = conn.cursor()

map = folium.Map(
        location = [33.606785,130.418314],
        zoom_start=8
        )

mc = MarkerCluster()

def mapping(dataName,conn,iconColor):
    df = psql.read_sql(dataName,conn)
    df.duplicated()
    data_dict = df.to_dict(orient='list')
    latitude_list = data_dict['発生場所緯度']
    longitude_list = data_dict['発生場所経度']
    name_list = data_dict['発生場所番地']
    for i in range(len(latitude_list)): #for i in range(len(latitude_list)):
        mc.add_child(folium.Marker([latitude_list[i], longitude_list[i]],
            popup=name_list[i],
            icon=folium.Icon(color=iconColor)
        ))

mapping("SELECT * FROM sample WHERE 発生年 = 2018 AND ((甲_年齢 = '65～74歳') OR (甲_年齢 = '75歳以上'))", conn, 'red')
mapping("SELECT * FROM sample WHERE 発生年 = 2017 AND ((甲_年齢 = '65～74歳') OR (甲_年齢 = '75歳以上'))", conn, 'blue')
mapping("SELECT * FROM sample WHERE 発生年 = 2016 AND ((甲_年齢 = '65～74歳') OR (甲_年齢 = '75歳以上'))", conn, 'green')


map.add_child(mc)
map.save('clustered.html')

cur.close()
conn.close()
