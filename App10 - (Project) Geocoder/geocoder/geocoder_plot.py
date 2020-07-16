import folium, requests, json
from folium import Popup
import pandas as pd
from geocoder_coordinates import lat_lon_message_error

api_key = '19e428b843c6cb57dd26080911d5f33d'
base_url = "http://api.openweathermap.org/data/2.5/weather?"
def create_map():
    df = pd.read_csv("./geocoder/addresses_updated.csv")
    first_lat = 0
    first_lon = 0
    for i in df.index:
        if str(df['latitude'][i]) != lat_lon_message_error() and str(df['longitude'][i]) != lat_lon_message_error():
            first_lat = df['latitude'][i]
            first_lon = df['longitude'][i]
            break
    m = folium.Map(location=[first_lat, first_lon], zoom_start=3, tiles='CartoDB positron')
    for i in df.index:
        if str(df['latitude'][i]) != lat_lon_message_error() and str(df['longitude'][i]) != lat_lon_message_error():
            lat = df.latitude[i]
            lon = df.longitude[i]
            complete_url = base_url + r"lat={}&lon={}&appid={}&units=metric".format(lat, lon, api_key)
            response = requests.get(complete_url)
            json = response.json()
            if json['cod'] == 200:
                temp = json['main']['temp']
                temp_min = json['main']['temp_min']
                temp_max = json['main']['temp_max']
            try:
                folium.Marker(location=[df.latitude[i],df.longitude[i]],
                popup=Popup(html=(r"<div style='color: black; font-size:14px;'><b>Temperatura</b><br> Atual: {} °C<br>Mínima: {} °C<br>Máxima {} °C</div>").format(temp,temp_min,temp_max), max_width=400),
                icon=folium.Icon(icon='cloud')
                ).add_to(m)
            except:
                pass
        else:
            continue

    m.save('./geocoder/templates/plot.html')