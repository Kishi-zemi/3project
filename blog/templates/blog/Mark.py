import folium
from folium import IFrame
from folium.plugins import MarkerCluster

class MarkClass:

    def __init__(self,df,col,year):
        self.df = df
        self.col = col
        self.year = year
        self.map = folium.Map(
                    location = [33.606785,130.418314],
                    zoom_start=8
                    )

    def marker(self):
        self.__setmark()
        folium.LayerControl(collapsed=True).add_to(self.map)
        self.map.save(self.year+'.html')
        print("save finished!")

    def __setmark(self):

        data_dict = self.df.to_dict(orient='list')

        latitude_list = data_dict['発生場所緯度']
        longitude_list = data_dict['発生場所経度']
        name_list = data_dict['発生場所番地']
        year_list = data_dict['発生年']
        weather_list = data_dict['天候']
        party1_list = data_dict['甲_種別']
        party2_list = data_dict['乙_種別']
        time_list = data_dict['昼夜']
        injure_list = data_dict['事故内容']
        rename_list = []

        mc = MarkerCluster(control=False)
        self.map.add_child(mc)

        g1 = folium.plugins.FeatureGroupSubGroup(mc, "晴れ")
        self.map.add_child(g1)

        g2 = folium.plugins.FeatureGroupSubGroup(mc, "曇り")
        self.map.add_child(g2)

        g3 = folium.plugins.FeatureGroupSubGroup(mc, "雨")
        self.map.add_child(g3)

        g4 = folium.plugins.FeatureGroupSubGroup(mc, "雪")
        self.map.add_child(g4)

        g5 = folium.plugins.FeatureGroupSubGroup(mc, "霧")
        self.map.add_child(g5)

        g6 = folium.plugins.FeatureGroupSubGroup(mc, "豪雨")
        self.map.add_child(g6)

        g7 = folium.plugins.FeatureGroupSubGroup(mc, "大雪")
        self.map.add_child(g7)

        g8 = folium.plugins.FeatureGroupSubGroup(mc, "みぞれ")
        self.map.add_child(g8)


        for i in range(len(latitude_list)):
            if "福岡県" in name_list[i]:
                rename_list.append(name_list[i].lstrip("福岡県"))
            else:
                rename_list.append(name_list[i])

            tooltip = rename_list[i]

            url = "http://maps.google.com/maps?q=&layer=c&cbll=" + str(latitude_list[i]) + ","+ str(longitude_list[i]) + "&cbp=11,90,0,0,0"

            situation1 = self.__makeSituation(party1_list[i])
            situation2 = self.__makeSituation(party2_list[i])
            weather = self.__makeWeather(weather_list[i])
            time = self.__makeTime(time_list[i])
            ic = self.__makeIC(injure_list[i])

            html = """
            {{% raw %}}
                <a href="{url} "target="_blank">{name}</a></br>
                <img width="60" src="{{% static 'img/situation/left/{situation1}.jpg'%}}">
                <img width="60" src="{{% static 'img/situation/right/{situation2}.jpg'%}}">
                <img width="60" src="{{% static 'img/weather/{weather}.jpg'%}}">
                <img width="60" src="{{% static 'img/time/{time}.jpg'%}}">
                {{% endraw %}}
                """.format(url=url,name=tooltip,situation1=situation1,situation2=situation2,weather=weather,time=time)
            #iframe = folium.IFrame(html=html, width=100, height=300)
            popup = folium.Popup(html, max_width=2650)

            color = 'gray'
            if self.year == 'all':
                if year_list[i] == 2016:
                    color = 'blue'
                if year_list[i] == 2017:
                    color = 'red'
                if year_list[i] == 2018:
                    color = 'green'
            else:
                color = self.col

            if weather == "sun":
                self.__mark(latitude_list[i],longitude_list[i],tooltip,popup,color,g1)
            if weather == "cloud":
                self.__mark(latitude_list[i],longitude_list[i],tooltip,popup,color,g2)
            if weather == "rain":
                self.__mark(latitude_list[i],longitude_list[i],tooltip,popup,color,g3)
            if weather == "lightsnow":
                self.__mark(latitude_list[i],longitude_list[i],tooltip,popup,color,g4)
            if weather == "fog":
                self.__mark(latitude_list[i],longitude_list[i],tooltip,popup,color,g5)
            if weather == "heavyrain":
                self.__mark(latitude_list[i],longitude_list[i],tooltip,popup,color,g6)
            if weather == "heavysnow":
                self.__mark(latitude_list[i],longitude_list[i],tooltip,popup,color,g7)
            if weather == "sleet":
                self.__mark(latitude_list[i],longitude_list[i],tooltip,popup,color,g8)

        self.map.add_child(mc)


    def __mark(self,lat,lon,tooltip,popup,col,g):
        folium.Marker([lat,lon],
            popup=popup,
            icon=folium.Icon(color=col),
            tooltip=tooltip
            ).add_to(g)


    def __makeSituation(self,party):
        if party == "普通乗用（総重3.5t未満又は定員10人以下）" or party == "軽乗用" or party == "準中型乗用（総重3.5t-7.5t又は定員10人以下）":
            return "car"
        if party == "ミニカー" or party == "小型農耕作業用" or party == "小型特殊その他" or party == "軽車両その他":
            return "car"
        if party == "原付自転車" or party == "原付二種（５１-１２５）" or party == "軽二輪（１２６-２５０）" or party == "小型二輪（２５１-４００）":
            return "bike"
        if party == "小型二輪（７５１㏄以上）" or party == "小型二輪（４０１-７５０）":
            return "bike"
        if party == "自転車" or party == "駆動補助機付自転車":
            return "bicycle"
        if party == "軽貨物" or party == "大型貨物（総重11t又は最積6.5t以上）" or party == "普通貨物（総重3.5t未満又は最積2t未満）" or party == "中型貨物（総重7.5t-11t又は最積4.5-6.5t）":
            return "track"
        if party == "準中型貨物（総重3.5t-7.5t又は最積2t-4.5t）" or party == "大型特殊その他" or party == "大型農耕作業用":
            return "track"
        if party == "大型乗用（総重11t又は定員30人以上）" or party == "中型乗用（総重7.5t-11t又は定員11-29人）":
            return "bus"
        if "歩行者" in party:
            return "walker"
        if party == "相手なし":
            return "nobody"
        if party == "列車":
            return "train"
        if party == "対象外当事者":
            return "outofline"
        if party == "物件等":
            return "buildings"


    def __makeWeather(self,weather):
        if weather == "豪雨":
            return "heavyrain"
        if weather == "大雪":
            return "heavysnow"
        if "晴" in weather:
            return "sun"
        if "曇" in weather:
            return "cloud"
        if "雨" in weather:
            return "rain"
        if "霧" in weather:
            return "fog"
        if "雪" in weather:
            return "snow"
        if weather == "みぞれ":
            return "sleet"


    def __makeTime(self,time):
        if "昼" in time:
            return "noon"
        if "夜" in time:
            return "night"

    def __makeIC(self,injure):
        if injure == "死亡":
            return "fa-exclamation-triangle"
        else:
            return ""
