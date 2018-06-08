
# Week 6 homework - What's The Weather Like


```python
#Three observable trends
Temperature does indeed increase as the the latitude gets closer to the equator which is lattitude 0.
There is not a strong coorleation between latitude and cloudiness.  
There is not a strong coorleation between latitude and wind speed.

```


```python
# Dependencies
from citipy import citipy
import openweathermapy.core as owm
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import seaborn
import pandas as pd
import numpy as np
import random
import requests


# Import api_key
from config import api_key
```


```python
# Create settings parameters to use with openweathermapy.core
#settings = {"units": "imperial", "APPID": api_key}
target_url = "http://api.openweathermap.org/data/2.5/weather?q="
units = "imperial"
#APPID = api_key
```


```python
# Sample Size - set to 520 when ready
sample_size = 520
```


```python
# start code to get random lat and lon
lat = {'min': -90, 'max': 90}
lng = {'min': -180, 'max': 180}

lat_values = np.arange(lat['min'], lat['max'], 0.01)
lng_values = np.arange(lng['min'], lng['max'], 0.01)
```


```python
# setup dataframe for the data
column_names = ('city_name', 'country_code', 'rand_lat', 'rand_lng', 'Latitude', 'Longitude','Temp (F)',
            'Humidity (%)','Cloudiness (%)','Wind Speed (mph)')
cities_df = pd.DataFrame(columns = column_names)
cities_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city_name</th>
      <th>country_code</th>
      <th>rand_lat</th>
      <th>rand_lng</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Temp (F)</th>
      <th>Humidity (%)</th>
      <th>Cloudiness (%)</th>
      <th>Wind Speed (mph)</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
record = 0
while len(cities_df) < sample_size:
    # Choose a random point within our lat-lng domain.
    rand_lat = random.choice(lat_values)
    rand_lng = random.choice(lng_values)
    # Call citipy's nearest_city() method to get a city object.
    city = citipy.nearest_city(rand_lat, rand_lng)
    city_name = city.city_name
    country_code = city.country_code
    # Call Open Weather Map API to obtain data and append it to df
    url = target_url + city_name + ',' + country_code + '&units=' + units + '&APPID=' + api_key
    weather_response = requests.get(url)
    weather_json = weather_response.json()
    if weather_json["cod"] == 200:
        print('City: %s. %s' % (weather_json['name'], url))
        latitude = weather_json["coord"]["lat"]
        longitude = weather_json["coord"]["lon"]
        temp = weather_json["main"]["temp"]
        humidity = weather_json["main"]["humidity"]
        cloud = weather_json["clouds"]["all"]
        wind = weather_json["wind"]["speed"]
        # Avoid repeating cities
        if city_name not in cities_df.city_name.values:
            print('Status code: %s. DF length is now: %d' % (str(weather_json["cod"]), len(cities_df)+1))
            # Append data to df columns
            cities_df.set_value(record, "city_name", city_name)
            cities_df.set_value(record, "country_code", country_code)
            cities_df.set_value(record, "rand_lat", rand_lat)
            cities_df.set_value(record, "rand_lng", rand_lng)
            cities_df.set_value(record, "Latitude", latitude)
            cities_df.set_value(record, "Longitude", longitude)
            cities_df.set_value(record, "Temp (F)", temp)
            cities_df.set_value(record, "Humidity (%)", humidity)
            cities_df.set_value(record, "Cloudiness (%)", cloud)
            cities_df.set_value(record, "Wind Speed (mph)", wind)


            record += 1
        

        else:
            pass
    else:
        pass
    
print(
"------------------------------\n"
"Finished     Finished   Finished\n"
)

```

    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 1
    

    C:\Users\cmaur\AppData\Local\Continuum\anaconda3\lib\site-packages\ipykernel_launcher.py:26: FutureWarning: set_value is deprecated and will be removed in a future release. Please use .at[] or .iat[] accessors instead
    C:\Users\cmaur\AppData\Local\Continuum\anaconda3\lib\site-packages\ipykernel_launcher.py:27: FutureWarning: set_value is deprecated and will be removed in a future release. Please use .at[] or .iat[] accessors instead
    C:\Users\cmaur\AppData\Local\Continuum\anaconda3\lib\site-packages\ipykernel_launcher.py:28: FutureWarning: set_value is deprecated and will be removed in a future release. Please use .at[] or .iat[] accessors instead
    C:\Users\cmaur\AppData\Local\Continuum\anaconda3\lib\site-packages\ipykernel_launcher.py:29: FutureWarning: set_value is deprecated and will be removed in a future release. Please use .at[] or .iat[] accessors instead
    C:\Users\cmaur\AppData\Local\Continuum\anaconda3\lib\site-packages\ipykernel_launcher.py:30: FutureWarning: set_value is deprecated and will be removed in a future release. Please use .at[] or .iat[] accessors instead
    C:\Users\cmaur\AppData\Local\Continuum\anaconda3\lib\site-packages\ipykernel_launcher.py:31: FutureWarning: set_value is deprecated and will be removed in a future release. Please use .at[] or .iat[] accessors instead
    C:\Users\cmaur\AppData\Local\Continuum\anaconda3\lib\site-packages\ipykernel_launcher.py:32: FutureWarning: set_value is deprecated and will be removed in a future release. Please use .at[] or .iat[] accessors instead
    C:\Users\cmaur\AppData\Local\Continuum\anaconda3\lib\site-packages\ipykernel_launcher.py:33: FutureWarning: set_value is deprecated and will be removed in a future release. Please use .at[] or .iat[] accessors instead
    C:\Users\cmaur\AppData\Local\Continuum\anaconda3\lib\site-packages\ipykernel_launcher.py:34: FutureWarning: set_value is deprecated and will be removed in a future release. Please use .at[] or .iat[] accessors instead
    C:\Users\cmaur\AppData\Local\Continuum\anaconda3\lib\site-packages\ipykernel_launcher.py:35: FutureWarning: set_value is deprecated and will be removed in a future release. Please use .at[] or .iat[] accessors instead
    

    City: Isangel. http://api.openweathermap.org/data/2.5/weather?q=isangel,vu&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 2
    City: Saint George. http://api.openweathermap.org/data/2.5/weather?q=saint george,bm&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 3
    City: Srednekolymsk. http://api.openweathermap.org/data/2.5/weather?q=srednekolymsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 4
    City: Ixtapa. http://api.openweathermap.org/data/2.5/weather?q=ixtapa,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 5
    City: Sobolevo. http://api.openweathermap.org/data/2.5/weather?q=sobolevo,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 6
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 7
    City: Stanovoye. http://api.openweathermap.org/data/2.5/weather?q=stanovoye,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 8
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 9
    City: Geraldton. http://api.openweathermap.org/data/2.5/weather?q=geraldton,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 10
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 11
    City: Bilma. http://api.openweathermap.org/data/2.5/weather?q=bilma,ne&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 12
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 13
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 14
    City: Gandajika. http://api.openweathermap.org/data/2.5/weather?q=gandajika,cd&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 15
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 16
    City: Drumheller. http://api.openweathermap.org/data/2.5/weather?q=drumheller,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 17
    City: Puerto Ayora. http://api.openweathermap.org/data/2.5/weather?q=puerto ayora,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 18
    City: Saint-Augustin. http://api.openweathermap.org/data/2.5/weather?q=saint-augustin,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 19
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 20
    City: Ust-Nera. http://api.openweathermap.org/data/2.5/weather?q=ust-nera,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 21
    City: Eldorado. http://api.openweathermap.org/data/2.5/weather?q=eldorado,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 22
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 23
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 24
    City: Camacha. http://api.openweathermap.org/data/2.5/weather?q=camacha,pt&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 25
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Murchison. http://api.openweathermap.org/data/2.5/weather?q=murchison,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 26
    City: Severo-Kurilsk. http://api.openweathermap.org/data/2.5/weather?q=severo-kurilsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 27
    City: Chastyye. http://api.openweathermap.org/data/2.5/weather?q=chastyye,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 28
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 29
    City: Te Anau. http://api.openweathermap.org/data/2.5/weather?q=te anau,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 30
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ostersund. http://api.openweathermap.org/data/2.5/weather?q=ostersund,se&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 31
    City: Uribia. http://api.openweathermap.org/data/2.5/weather?q=uribia,co&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 32
    City: Lamtah. http://api.openweathermap.org/data/2.5/weather?q=lamtah,tn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 33
    City: Abnub. http://api.openweathermap.org/data/2.5/weather?q=abnub,eg&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 34
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 35
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Butaritari. http://api.openweathermap.org/data/2.5/weather?q=butaritari,ki&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 36
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 37
    City: Hervey Bay. http://api.openweathermap.org/data/2.5/weather?q=hervey bay,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 38
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 39
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 40
    City: Leningradskiy. http://api.openweathermap.org/data/2.5/weather?q=leningradskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 41
    City: Mount Isa. http://api.openweathermap.org/data/2.5/weather?q=mount isa,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 42
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 43
    City: Wajima. http://api.openweathermap.org/data/2.5/weather?q=wajima,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 44
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 45
    City: Norman Wells. http://api.openweathermap.org/data/2.5/weather?q=norman wells,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 46
    City: Avarua. http://api.openweathermap.org/data/2.5/weather?q=avarua,ck&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 47
    City: Luderitz. http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 48
    City: Miyako. http://api.openweathermap.org/data/2.5/weather?q=miyako,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 49
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 50
    City: Darab. http://api.openweathermap.org/data/2.5/weather?q=darab,ir&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 51
    City: Lavrentiya. http://api.openweathermap.org/data/2.5/weather?q=lavrentiya,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 52
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 53
    City: Esperance. http://api.openweathermap.org/data/2.5/weather?q=esperance,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 54
    City: Marquette. http://api.openweathermap.org/data/2.5/weather?q=marquette,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 55
    City: New Norfolk. http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 56
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 57
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Arman. http://api.openweathermap.org/data/2.5/weather?q=arman,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 58
    City: Strezhevoy. http://api.openweathermap.org/data/2.5/weather?q=strezhevoy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 59
    City: New Norfolk. http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tiksi. http://api.openweathermap.org/data/2.5/weather?q=tiksi,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 60
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 61
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mangan. http://api.openweathermap.org/data/2.5/weather?q=mangan,in&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 62
    City: Provideniya. http://api.openweathermap.org/data/2.5/weather?q=provideniya,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 63
    City: Thompson. http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 64
    City: Luderitz. http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tucumcari. http://api.openweathermap.org/data/2.5/weather?q=tucumcari,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 65
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Iqaluit. http://api.openweathermap.org/data/2.5/weather?q=iqaluit,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 66
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 67
    City: Pevek. http://api.openweathermap.org/data/2.5/weather?q=pevek,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 68
    City: Lavrentiya. http://api.openweathermap.org/data/2.5/weather?q=lavrentiya,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hamilton. http://api.openweathermap.org/data/2.5/weather?q=hamilton,bm&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 69
    City: Buldana. http://api.openweathermap.org/data/2.5/weather?q=buldana,in&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 70
    City: Bethel. http://api.openweathermap.org/data/2.5/weather?q=bethel,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 71
    City: Khatanga. http://api.openweathermap.org/data/2.5/weather?q=khatanga,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 72
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kutahya. http://api.openweathermap.org/data/2.5/weather?q=kutahya,tr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 73
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 74
    City: Lorengau. http://api.openweathermap.org/data/2.5/weather?q=lorengau,pg&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 75
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Roald. http://api.openweathermap.org/data/2.5/weather?q=roald,no&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 76
    City: Sinnamary. http://api.openweathermap.org/data/2.5/weather?q=sinnamary,gf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 77
    City: Luganville. http://api.openweathermap.org/data/2.5/weather?q=luganville,vu&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 78
    City: Sharan. http://api.openweathermap.org/data/2.5/weather?q=sharan,af&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 79
    City: Puerto Ayora. http://api.openweathermap.org/data/2.5/weather?q=puerto ayora,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tuktoyaktuk. http://api.openweathermap.org/data/2.5/weather?q=tuktoyaktuk,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 80
    City: Staraya Mayna. http://api.openweathermap.org/data/2.5/weather?q=staraya mayna,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 81
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 82
    City: Adrar. http://api.openweathermap.org/data/2.5/weather?q=adrar,dz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 83
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 84
    City: Qaqortoq. http://api.openweathermap.org/data/2.5/weather?q=qaqortoq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 85
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Millinocket. http://api.openweathermap.org/data/2.5/weather?q=millinocket,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 86
    City: Kaeo. http://api.openweathermap.org/data/2.5/weather?q=kaeo,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 87
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Butaritari. http://api.openweathermap.org/data/2.5/weather?q=butaritari,ki&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Blair. http://api.openweathermap.org/data/2.5/weather?q=port blair,in&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 88
    City: Oktyabrskiy. http://api.openweathermap.org/data/2.5/weather?q=oktyabrskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 89
    City: Puerto Ayora. http://api.openweathermap.org/data/2.5/weather?q=puerto ayora,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Banyo. http://api.openweathermap.org/data/2.5/weather?q=banyo,cm&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 90
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kendari. http://api.openweathermap.org/data/2.5/weather?q=kendari,id&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 91
    City: Corovode. http://api.openweathermap.org/data/2.5/weather?q=corovode,al&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 92
    City: Pasni. http://api.openweathermap.org/data/2.5/weather?q=pasni,pk&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 93
    City: Kutum. http://api.openweathermap.org/data/2.5/weather?q=kutum,sd&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 94
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 95
    City: Abreus. http://api.openweathermap.org/data/2.5/weather?q=abreus,cu&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 96
    City: Atuona. http://api.openweathermap.org/data/2.5/weather?q=atuona,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 97
    City: Khatanga. http://api.openweathermap.org/data/2.5/weather?q=khatanga,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Chara. http://api.openweathermap.org/data/2.5/weather?q=chara,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 98
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mount Gambier. http://api.openweathermap.org/data/2.5/weather?q=mount gambier,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 99
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 100
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Thompson. http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Fukue. http://api.openweathermap.org/data/2.5/weather?q=fukue,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 101
    City: Barrow. http://api.openweathermap.org/data/2.5/weather?q=barrow,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 102
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 103
    City: Tuktoyaktuk. http://api.openweathermap.org/data/2.5/weather?q=tuktoyaktuk,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Puerto Ayora. http://api.openweathermap.org/data/2.5/weather?q=puerto ayora,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Skjervoy. http://api.openweathermap.org/data/2.5/weather?q=skjervoy,no&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 104
    City: Tadine. http://api.openweathermap.org/data/2.5/weather?q=tadine,nc&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 105
    City: Okha. http://api.openweathermap.org/data/2.5/weather?q=okha,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 106
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 107
    City: Peleduy. http://api.openweathermap.org/data/2.5/weather?q=peleduy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 108
    City: Atuona. http://api.openweathermap.org/data/2.5/weather?q=atuona,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mingguang. http://api.openweathermap.org/data/2.5/weather?q=mingguang,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 109
    City: Saskylakh. http://api.openweathermap.org/data/2.5/weather?q=saskylakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 110
    City: Sao Jose da Coroa Grande. http://api.openweathermap.org/data/2.5/weather?q=sao jose da coroa grande,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 111
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vila Nova de Milfontes. http://api.openweathermap.org/data/2.5/weather?q=vila nova de milfontes,pt&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 112
    City: Cabo San Lucas. http://api.openweathermap.org/data/2.5/weather?q=cabo san lucas,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 113
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 114
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Saint-Pierre. http://api.openweathermap.org/data/2.5/weather?q=saint-pierre,pm&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 115
    City: Patos. http://api.openweathermap.org/data/2.5/weather?q=patos,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 116
    City: Kapaa. http://api.openweathermap.org/data/2.5/weather?q=kapaa,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 117
    City: Upata. http://api.openweathermap.org/data/2.5/weather?q=upata,ve&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 118
    City: Rio Grande. http://api.openweathermap.org/data/2.5/weather?q=rio grande,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 119
    City: Saint George. http://api.openweathermap.org/data/2.5/weather?q=saint george,bm&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Srednekolymsk. http://api.openweathermap.org/data/2.5/weather?q=srednekolymsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Myitkyina. http://api.openweathermap.org/data/2.5/weather?q=myitkyina,mm&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 120
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Humberto de Campos. http://api.openweathermap.org/data/2.5/weather?q=humberto de campos,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 121
    City: Pomezia. http://api.openweathermap.org/data/2.5/weather?q=pomezia,it&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 122
    City: Thompson. http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Glendive. http://api.openweathermap.org/data/2.5/weather?q=glendive,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 123
    City: Hilo. http://api.openweathermap.org/data/2.5/weather?q=hilo,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 124
    City: Bay Roberts. http://api.openweathermap.org/data/2.5/weather?q=bay roberts,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 125
    City: Igrim. http://api.openweathermap.org/data/2.5/weather?q=igrim,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 126
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 127
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Sitka. http://api.openweathermap.org/data/2.5/weather?q=sitka,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 128
    City: Ulladulla. http://api.openweathermap.org/data/2.5/weather?q=ulladulla,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 129
    City: Pacifica. http://api.openweathermap.org/data/2.5/weather?q=pacifica,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 130
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Fairbanks. http://api.openweathermap.org/data/2.5/weather?q=fairbanks,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 131
    City: Chokurdakh. http://api.openweathermap.org/data/2.5/weather?q=chokurdakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 132
    City: Fukue. http://api.openweathermap.org/data/2.5/weather?q=fukue,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Agirish. http://api.openweathermap.org/data/2.5/weather?q=agirish,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 133
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lloydminster. http://api.openweathermap.org/data/2.5/weather?q=lloydminster,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 134
    City: Port Moresby. http://api.openweathermap.org/data/2.5/weather?q=port moresby,pg&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 135
    City: Nikolskoye. http://api.openweathermap.org/data/2.5/weather?q=nikolskoye,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 136
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kikwit. http://api.openweathermap.org/data/2.5/weather?q=kikwit,cd&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 137
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Sayat. http://api.openweathermap.org/data/2.5/weather?q=sayat,tm&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 138
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Atuona. http://api.openweathermap.org/data/2.5/weather?q=atuona,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Alice Springs. http://api.openweathermap.org/data/2.5/weather?q=alice springs,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 139
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Longyearbyen. http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 140
    City: Fereydun Kenar. http://api.openweathermap.org/data/2.5/weather?q=fereydun kenar,ir&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 141
    City: Lagoa Vermelha. http://api.openweathermap.org/data/2.5/weather?q=lagoa vermelha,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 142
    City: New Norfolk. http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Pleshanovo. http://api.openweathermap.org/data/2.5/weather?q=pleshanovo,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 143
    City: Bintulu. http://api.openweathermap.org/data/2.5/weather?q=bintulu,my&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 144
    City: Arak. http://api.openweathermap.org/data/2.5/weather?q=arak,ir&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 145
    City: Nikolskoye. http://api.openweathermap.org/data/2.5/weather?q=nikolskoye,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Chokurdakh. http://api.openweathermap.org/data/2.5/weather?q=chokurdakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kruisfontein. http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 146
    City: Katsuura. http://api.openweathermap.org/data/2.5/weather?q=katsuura,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 147
    City: Arkhangelsk. http://api.openweathermap.org/data/2.5/weather?q=arkhangelsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 148
    City: Avarua. http://api.openweathermap.org/data/2.5/weather?q=avarua,ck&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Zhigansk. http://api.openweathermap.org/data/2.5/weather?q=zhigansk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 149
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kununurra. http://api.openweathermap.org/data/2.5/weather?q=kununurra,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 150
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Sigli. http://api.openweathermap.org/data/2.5/weather?q=sigli,id&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 151
    City: Ejura. http://api.openweathermap.org/data/2.5/weather?q=ejura,gh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 152
    City: Khatanga. http://api.openweathermap.org/data/2.5/weather?q=khatanga,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bubaque. http://api.openweathermap.org/data/2.5/weather?q=bubaque,gw&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 153
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cayenne. http://api.openweathermap.org/data/2.5/weather?q=cayenne,gf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 154
    City: Atuona. http://api.openweathermap.org/data/2.5/weather?q=atuona,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Gamba. http://api.openweathermap.org/data/2.5/weather?q=gamba,ga&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 155
    City: Saskylakh. http://api.openweathermap.org/data/2.5/weather?q=saskylakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kodiak. http://api.openweathermap.org/data/2.5/weather?q=kodiak,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 156
    City: Almenara. http://api.openweathermap.org/data/2.5/weather?q=almenara,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 157
    City: Bruntal. http://api.openweathermap.org/data/2.5/weather?q=bruntal,cz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 158
    City: Zaranj. http://api.openweathermap.org/data/2.5/weather?q=zaranj,af&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 159
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Eureka. http://api.openweathermap.org/data/2.5/weather?q=eureka,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 160
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mbeya. http://api.openweathermap.org/data/2.5/weather?q=mbeya,tz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 161
    City: Hasaki. http://api.openweathermap.org/data/2.5/weather?q=hasaki,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 162
    City: Conceicao do Araguaia. http://api.openweathermap.org/data/2.5/weather?q=conceicao do araguaia,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 163
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Barrow. http://api.openweathermap.org/data/2.5/weather?q=barrow,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bukachacha. http://api.openweathermap.org/data/2.5/weather?q=bukachacha,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 164
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ozernovskiy. http://api.openweathermap.org/data/2.5/weather?q=ozernovskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 165
    City: Sao Filipe. http://api.openweathermap.org/data/2.5/weather?q=sao filipe,cv&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 166
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vokhma. http://api.openweathermap.org/data/2.5/weather?q=vokhma,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 167
    City: Pevek. http://api.openweathermap.org/data/2.5/weather?q=pevek,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Los Llanos de Aridane. http://api.openweathermap.org/data/2.5/weather?q=los llanos de aridane,es&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 168
    City: Qinggang. http://api.openweathermap.org/data/2.5/weather?q=qinggang,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 169
    City: Clyde River. http://api.openweathermap.org/data/2.5/weather?q=clyde river,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 170
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Maple Creek. http://api.openweathermap.org/data/2.5/weather?q=maple creek,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 171
    City: Kapchorwa. http://api.openweathermap.org/data/2.5/weather?q=kapchorwa,ug&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 172
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 173
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Sironj. http://api.openweathermap.org/data/2.5/weather?q=sironj,in&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 174
    City: Puerto Ayora. http://api.openweathermap.org/data/2.5/weather?q=puerto ayora,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kathu. http://api.openweathermap.org/data/2.5/weather?q=kathu,th&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 175
    City: Byron Bay. http://api.openweathermap.org/data/2.5/weather?q=byron bay,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 176
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Xique-Xique. http://api.openweathermap.org/data/2.5/weather?q=xique-xique,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 177
    City: Cocorit. http://api.openweathermap.org/data/2.5/weather?q=cocorit,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 178
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 179
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: New Norfolk. http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Carnarvon. http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 180
    City: Boa Vista. http://api.openweathermap.org/data/2.5/weather?q=boa vista,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 181
    City: Sechura. http://api.openweathermap.org/data/2.5/weather?q=sechura,pe&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 182
    City: Mariinsk. http://api.openweathermap.org/data/2.5/weather?q=mariinsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 183
    City: Date. http://api.openweathermap.org/data/2.5/weather?q=date,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 184
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tuktoyaktuk. http://api.openweathermap.org/data/2.5/weather?q=tuktoyaktuk,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hambantota. http://api.openweathermap.org/data/2.5/weather?q=hambantota,lk&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 185
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 186
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hasaki. http://api.openweathermap.org/data/2.5/weather?q=hasaki,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hirtshals. http://api.openweathermap.org/data/2.5/weather?q=hirtshals,dk&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 187
    City: Atuona. http://api.openweathermap.org/data/2.5/weather?q=atuona,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Clyde River. http://api.openweathermap.org/data/2.5/weather?q=clyde river,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Praya. http://api.openweathermap.org/data/2.5/weather?q=praya,id&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 188
    City: Cayenne. http://api.openweathermap.org/data/2.5/weather?q=cayenne,gf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Atuona. http://api.openweathermap.org/data/2.5/weather?q=atuona,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Povolzhskiy. http://api.openweathermap.org/data/2.5/weather?q=povolzhskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 189
    City: Puerto Ayora. http://api.openweathermap.org/data/2.5/weather?q=puerto ayora,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hamilton. http://api.openweathermap.org/data/2.5/weather?q=hamilton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Eston. http://api.openweathermap.org/data/2.5/weather?q=eston,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 190
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Seoul. http://api.openweathermap.org/data/2.5/weather?q=seoul,kr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 191
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: New Norfolk. http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kenai. http://api.openweathermap.org/data/2.5/weather?q=kenai,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 192
    City: Vardo. http://api.openweathermap.org/data/2.5/weather?q=vardo,no&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 193
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Talnakh. http://api.openweathermap.org/data/2.5/weather?q=talnakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 194
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Pochutla. http://api.openweathermap.org/data/2.5/weather?q=pochutla,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 195
    City: Nishihara. http://api.openweathermap.org/data/2.5/weather?q=nishihara,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 196
    City: Letterkenny. http://api.openweathermap.org/data/2.5/weather?q=letterkenny,ie&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 197
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Okha. http://api.openweathermap.org/data/2.5/weather?q=okha,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Turinsk. http://api.openweathermap.org/data/2.5/weather?q=turinsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 198
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Souillac. http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 199
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: New Norfolk. http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mogadishu. http://api.openweathermap.org/data/2.5/weather?q=mogadishu,so&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 200
    City: Hobyo. http://api.openweathermap.org/data/2.5/weather?q=hobyo,so&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 201
    City: Birjand. http://api.openweathermap.org/data/2.5/weather?q=birjand,ir&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 202
    City: Butaritari. http://api.openweathermap.org/data/2.5/weather?q=butaritari,ki&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kabompo. http://api.openweathermap.org/data/2.5/weather?q=kabompo,zm&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 203
    City: Leshukonskoye. http://api.openweathermap.org/data/2.5/weather?q=leshukonskoye,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 204
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mountain Home. http://api.openweathermap.org/data/2.5/weather?q=mountain home,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 205
    City: Hovd. http://api.openweathermap.org/data/2.5/weather?q=hovd,mn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 206
    City: San Cristobal. http://api.openweathermap.org/data/2.5/weather?q=san cristobal,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 207
    City: Mangrol. http://api.openweathermap.org/data/2.5/weather?q=mangrol,in&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 208
    City: Cayenne. http://api.openweathermap.org/data/2.5/weather?q=cayenne,gf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Teterow. http://api.openweathermap.org/data/2.5/weather?q=teterow,de&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 209
    City: Barrow. http://api.openweathermap.org/data/2.5/weather?q=barrow,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Luanda. http://api.openweathermap.org/data/2.5/weather?q=luanda,ao&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 210
    City: Belaya Gora. http://api.openweathermap.org/data/2.5/weather?q=belaya gora,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 211
    City: Tabou. http://api.openweathermap.org/data/2.5/weather?q=tabou,ci&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 212
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Pecos. http://api.openweathermap.org/data/2.5/weather?q=pecos,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 213
    City: Aykhal. http://api.openweathermap.org/data/2.5/weather?q=aykhal,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 214
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Megion. http://api.openweathermap.org/data/2.5/weather?q=megion,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 215
    City: Tonota. http://api.openweathermap.org/data/2.5/weather?q=tonota,bw&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 216
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Marsa Matruh. http://api.openweathermap.org/data/2.5/weather?q=marsa matruh,eg&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 217
    City: Saskylakh. http://api.openweathermap.org/data/2.5/weather?q=saskylakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Jaisalmer. http://api.openweathermap.org/data/2.5/weather?q=jaisalmer,in&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 218
    City: Loreto. http://api.openweathermap.org/data/2.5/weather?q=loreto,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 219
    City: Taoudenni. http://api.openweathermap.org/data/2.5/weather?q=taoudenni,ml&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 220
    City: Cherskiy. http://api.openweathermap.org/data/2.5/weather?q=cherskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 221
    City: Shemonaikha. http://api.openweathermap.org/data/2.5/weather?q=shemonaikha,kz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 222
    City: Clyde River. http://api.openweathermap.org/data/2.5/weather?q=clyde river,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Nikolskoye. http://api.openweathermap.org/data/2.5/weather?q=nikolskoye,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Villa Carlos Paz. http://api.openweathermap.org/data/2.5/weather?q=villa carlos paz,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 223
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rocha. http://api.openweathermap.org/data/2.5/weather?q=rocha,uy&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 224
    City: Guerrero Negro. http://api.openweathermap.org/data/2.5/weather?q=guerrero negro,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 225
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Macquarie. http://api.openweathermap.org/data/2.5/weather?q=port macquarie,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 226
    City: Norman Wells. http://api.openweathermap.org/data/2.5/weather?q=norman wells,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Boa Esperanca do Sul. http://api.openweathermap.org/data/2.5/weather?q=boa esperanca do sul,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 227
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tuktoyaktuk. http://api.openweathermap.org/data/2.5/weather?q=tuktoyaktuk,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Sitka. http://api.openweathermap.org/data/2.5/weather?q=sitka,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Fairbanks. http://api.openweathermap.org/data/2.5/weather?q=fairbanks,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mwense. http://api.openweathermap.org/data/2.5/weather?q=mwense,zm&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 228
    City: Luderitz. http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kangavar. http://api.openweathermap.org/data/2.5/weather?q=kangavar,ir&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 229
    City: Vao. http://api.openweathermap.org/data/2.5/weather?q=vao,nc&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 230
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hilo. http://api.openweathermap.org/data/2.5/weather?q=hilo,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Esperance. http://api.openweathermap.org/data/2.5/weather?q=esperance,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Faanui. http://api.openweathermap.org/data/2.5/weather?q=faanui,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 231
    City: Kapaa. http://api.openweathermap.org/data/2.5/weather?q=kapaa,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Burns Lake. http://api.openweathermap.org/data/2.5/weather?q=burns lake,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 232
    City: Ilulissat. http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 233
    City: Husavik. http://api.openweathermap.org/data/2.5/weather?q=husavik,is&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 234
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Carnarvon. http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Karratha. http://api.openweathermap.org/data/2.5/weather?q=karratha,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 235
    City: Ajdabiya. http://api.openweathermap.org/data/2.5/weather?q=ajdabiya,ly&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 236
    City: Nakhon Thai. http://api.openweathermap.org/data/2.5/weather?q=nakhon thai,th&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 237
    City: Labuhan. http://api.openweathermap.org/data/2.5/weather?q=labuhan,id&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 238
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Puerto Ayora. http://api.openweathermap.org/data/2.5/weather?q=puerto ayora,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Nyurba. http://api.openweathermap.org/data/2.5/weather?q=nyurba,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 239
    City: Guerrero Negro. http://api.openweathermap.org/data/2.5/weather?q=guerrero negro,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cayenne. http://api.openweathermap.org/data/2.5/weather?q=cayenne,gf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Sitka. http://api.openweathermap.org/data/2.5/weather?q=sitka,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hilo. http://api.openweathermap.org/data/2.5/weather?q=hilo,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cabo San Lucas. http://api.openweathermap.org/data/2.5/weather?q=cabo san lucas,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tuktoyaktuk. http://api.openweathermap.org/data/2.5/weather?q=tuktoyaktuk,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 240
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 241
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lorengau. http://api.openweathermap.org/data/2.5/weather?q=lorengau,pg&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Talnakh. http://api.openweathermap.org/data/2.5/weather?q=talnakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Moose Factory. http://api.openweathermap.org/data/2.5/weather?q=moose factory,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 242
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tual. http://api.openweathermap.org/data/2.5/weather?q=tual,id&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 243
    City: New Norfolk. http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Morristown. http://api.openweathermap.org/data/2.5/weather?q=morristown,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 244
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Beneditinos. http://api.openweathermap.org/data/2.5/weather?q=beneditinos,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 245
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Pyaozerskiy. http://api.openweathermap.org/data/2.5/weather?q=pyaozerskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 246
    City: Okhotsk. http://api.openweathermap.org/data/2.5/weather?q=okhotsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 247
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Villa del Rosario. http://api.openweathermap.org/data/2.5/weather?q=villa del rosario,ve&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 248
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Nikolskoye. http://api.openweathermap.org/data/2.5/weather?q=nikolskoye,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Atar. http://api.openweathermap.org/data/2.5/weather?q=atar,mr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 249
    City: Onega. http://api.openweathermap.org/data/2.5/weather?q=onega,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 250
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Nouadhibou. http://api.openweathermap.org/data/2.5/weather?q=nouadhibou,mr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 251
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Khatanga. http://api.openweathermap.org/data/2.5/weather?q=khatanga,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Sao Filipe. http://api.openweathermap.org/data/2.5/weather?q=sao filipe,cv&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Manono. http://api.openweathermap.org/data/2.5/weather?q=manono,cd&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 252
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Xining. http://api.openweathermap.org/data/2.5/weather?q=xining,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 253
    City: Komsomolskiy. http://api.openweathermap.org/data/2.5/weather?q=komsomolskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 254
    City: Yinchuan. http://api.openweathermap.org/data/2.5/weather?q=yinchuan,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 255
    City: San Juan Bautista. http://api.openweathermap.org/data/2.5/weather?q=san juan bautista,py&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 256
    City: Bethel. http://api.openweathermap.org/data/2.5/weather?q=bethel,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Butaritari. http://api.openweathermap.org/data/2.5/weather?q=butaritari,ki&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mitsamiouli. http://api.openweathermap.org/data/2.5/weather?q=mitsamiouli,km&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 257
    City: Ilulissat. http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Whitehorse. http://api.openweathermap.org/data/2.5/weather?q=whitehorse,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 258
    City: Itarema. http://api.openweathermap.org/data/2.5/weather?q=itarema,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 259
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hilo. http://api.openweathermap.org/data/2.5/weather?q=hilo,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Barrow. http://api.openweathermap.org/data/2.5/weather?q=barrow,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Dalvik. http://api.openweathermap.org/data/2.5/weather?q=dalvik,is&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 260
    City: Rio Cuarto. http://api.openweathermap.org/data/2.5/weather?q=rio cuarto,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 261
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Uyskoye. http://api.openweathermap.org/data/2.5/weather?q=uyskoye,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 262
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Timbiqui. http://api.openweathermap.org/data/2.5/weather?q=timbiqui,co&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 263
    City: Clyde River. http://api.openweathermap.org/data/2.5/weather?q=clyde river,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Okhotsk. http://api.openweathermap.org/data/2.5/weather?q=okhotsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Poum. http://api.openweathermap.org/data/2.5/weather?q=poum,nc&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 264
    City: Basoko. http://api.openweathermap.org/data/2.5/weather?q=basoko,cd&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 265
    City: Katsuura. http://api.openweathermap.org/data/2.5/weather?q=katsuura,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Geraldton. http://api.openweathermap.org/data/2.5/weather?q=geraldton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hilo. http://api.openweathermap.org/data/2.5/weather?q=hilo,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: New Norfolk. http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Atar. http://api.openweathermap.org/data/2.5/weather?q=atar,mr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Riberalta. http://api.openweathermap.org/data/2.5/weather?q=riberalta,bo&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 266
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Carnarvon. http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Salalah. http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Athabasca. http://api.openweathermap.org/data/2.5/weather?q=athabasca,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 267
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Atar. http://api.openweathermap.org/data/2.5/weather?q=atar,mr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Santa Rosa. http://api.openweathermap.org/data/2.5/weather?q=santa rosa,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 268
    City: Luderitz. http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: New Norfolk. http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Diamantino. http://api.openweathermap.org/data/2.5/weather?q=diamantino,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 269
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Chicama. http://api.openweathermap.org/data/2.5/weather?q=chicama,pe&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 270
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Fairbanks. http://api.openweathermap.org/data/2.5/weather?q=fairbanks,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Haradok. http://api.openweathermap.org/data/2.5/weather?q=haradok,by&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 271
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Dunedin. http://api.openweathermap.org/data/2.5/weather?q=dunedin,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 272
    City: De Land. http://api.openweathermap.org/data/2.5/weather?q=de land,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 273
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Barrow. http://api.openweathermap.org/data/2.5/weather?q=barrow,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lima. http://api.openweathermap.org/data/2.5/weather?q=lima,pe&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 274
    City: New Norfolk. http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Butaritari. http://api.openweathermap.org/data/2.5/weather?q=butaritari,ki&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bathsheba. http://api.openweathermap.org/data/2.5/weather?q=bathsheba,bb&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 275
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Thompson. http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tiksi. http://api.openweathermap.org/data/2.5/weather?q=tiksi,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Caranavi. http://api.openweathermap.org/data/2.5/weather?q=caranavi,bo&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 276
    City: Severo-Kurilsk. http://api.openweathermap.org/data/2.5/weather?q=severo-kurilsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Aswan. http://api.openweathermap.org/data/2.5/weather?q=aswan,eg&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 277
    City: Atuona. http://api.openweathermap.org/data/2.5/weather?q=atuona,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kapaa. http://api.openweathermap.org/data/2.5/weather?q=kapaa,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Comodoro Rivadavia. http://api.openweathermap.org/data/2.5/weather?q=comodoro rivadavia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 278
    City: Semporna. http://api.openweathermap.org/data/2.5/weather?q=semporna,my&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 279
    City: Touros. http://api.openweathermap.org/data/2.5/weather?q=touros,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 280
    City: North Bend. http://api.openweathermap.org/data/2.5/weather?q=north bend,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 281
    City: Klaksvik. http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 282
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kiunga. http://api.openweathermap.org/data/2.5/weather?q=kiunga,pg&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 283
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Butaritari. http://api.openweathermap.org/data/2.5/weather?q=butaritari,ki&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kodiak. http://api.openweathermap.org/data/2.5/weather?q=kodiak,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lethem. http://api.openweathermap.org/data/2.5/weather?q=lethem,gy&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 284
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vostok. http://api.openweathermap.org/data/2.5/weather?q=vostok,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 285
    City: Alice Springs. http://api.openweathermap.org/data/2.5/weather?q=alice springs,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bow Island. http://api.openweathermap.org/data/2.5/weather?q=bow island,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 286
    City: San Cristobal. http://api.openweathermap.org/data/2.5/weather?q=san cristobal,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Fort Nelson. http://api.openweathermap.org/data/2.5/weather?q=fort nelson,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 287
    City: Platteville. http://api.openweathermap.org/data/2.5/weather?q=platteville,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 288
    City: Port Hardy. http://api.openweathermap.org/data/2.5/weather?q=port hardy,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 289
    City: Kailahun. http://api.openweathermap.org/data/2.5/weather?q=kailahun,sl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 290
    City: Aklavik. http://api.openweathermap.org/data/2.5/weather?q=aklavik,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 291
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hofn. http://api.openweathermap.org/data/2.5/weather?q=hofn,is&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 292
    City: Saint Albans. http://api.openweathermap.org/data/2.5/weather?q=saint albans,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 293
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Butaritari. http://api.openweathermap.org/data/2.5/weather?q=butaritari,ki&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Broome. http://api.openweathermap.org/data/2.5/weather?q=broome,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 294
    City: Boden. http://api.openweathermap.org/data/2.5/weather?q=boden,se&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 295
    City: Alfredo Chaves. http://api.openweathermap.org/data/2.5/weather?q=alfredo chaves,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 296
    City: Provideniya. http://api.openweathermap.org/data/2.5/weather?q=provideniya,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Luanda. http://api.openweathermap.org/data/2.5/weather?q=luanda,ao&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hilo. http://api.openweathermap.org/data/2.5/weather?q=hilo,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Barrow. http://api.openweathermap.org/data/2.5/weather?q=barrow,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Puerto Escondido. http://api.openweathermap.org/data/2.5/weather?q=puerto escondido,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 297
    City: Lewistown. http://api.openweathermap.org/data/2.5/weather?q=lewistown,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 298
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ostrovnoy. http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 299
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Falam. http://api.openweathermap.org/data/2.5/weather?q=falam,mm&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 300
    City: Talnakh. http://api.openweathermap.org/data/2.5/weather?q=talnakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cockburn Town. http://api.openweathermap.org/data/2.5/weather?q=cockburn town,tc&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 301
    City: Kedgwick. http://api.openweathermap.org/data/2.5/weather?q=kedgwick,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 302
    City: Touros. http://api.openweathermap.org/data/2.5/weather?q=touros,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Weymouth. http://api.openweathermap.org/data/2.5/weather?q=weymouth,gb&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 303
    City: Nikolskoye. http://api.openweathermap.org/data/2.5/weather?q=nikolskoye,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vernon. http://api.openweathermap.org/data/2.5/weather?q=vernon,fr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 304
    City: Aykhal. http://api.openweathermap.org/data/2.5/weather?q=aykhal,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kigoma. http://api.openweathermap.org/data/2.5/weather?q=kigoma,tz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 305
    City: Lapeer. http://api.openweathermap.org/data/2.5/weather?q=lapeer,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 306
    City: Nome. http://api.openweathermap.org/data/2.5/weather?q=nome,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 307
    City: Somerset. http://api.openweathermap.org/data/2.5/weather?q=somerset,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 308
    City: Oksfjord. http://api.openweathermap.org/data/2.5/weather?q=oksfjord,no&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 309
    City: Omboue. http://api.openweathermap.org/data/2.5/weather?q=omboue,ga&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 310
    City: Waipawa. http://api.openweathermap.org/data/2.5/weather?q=waipawa,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 311
    City: Khatanga. http://api.openweathermap.org/data/2.5/weather?q=khatanga,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Perivolion. http://api.openweathermap.org/data/2.5/weather?q=perivolion,gr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 312
    City: Tuatapere. http://api.openweathermap.org/data/2.5/weather?q=tuatapere,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 313
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Poya. http://api.openweathermap.org/data/2.5/weather?q=poya,nc&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 314
    City: Butaritari. http://api.openweathermap.org/data/2.5/weather?q=butaritari,ki&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Lincoln. http://api.openweathermap.org/data/2.5/weather?q=port lincoln,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 315
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Khatanga. http://api.openweathermap.org/data/2.5/weather?q=khatanga,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Severo-Kurilsk. http://api.openweathermap.org/data/2.5/weather?q=severo-kurilsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kaspiyskiy. http://api.openweathermap.org/data/2.5/weather?q=kaspiyskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 316
    City: San Policarpo. http://api.openweathermap.org/data/2.5/weather?q=san policarpo,ph&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 317
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Augusta. http://api.openweathermap.org/data/2.5/weather?q=port augusta,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 318
    City: Kaitangata. http://api.openweathermap.org/data/2.5/weather?q=kaitangata,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 319
    City: Laurel. http://api.openweathermap.org/data/2.5/weather?q=laurel,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 320
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Geraldton. http://api.openweathermap.org/data/2.5/weather?q=geraldton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Baie-Comeau. http://api.openweathermap.org/data/2.5/weather?q=baie-comeau,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 321
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kaitangata. http://api.openweathermap.org/data/2.5/weather?q=kaitangata,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: San Patricio. http://api.openweathermap.org/data/2.5/weather?q=san patricio,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 322
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rafai. http://api.openweathermap.org/data/2.5/weather?q=rafai,cf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 323
    City: Wolnzach. http://api.openweathermap.org/data/2.5/weather?q=wolnzach,de&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 324
    City: Atuona. http://api.openweathermap.org/data/2.5/weather?q=atuona,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Korla. http://api.openweathermap.org/data/2.5/weather?q=korla,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 325
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 326
    City: Saba. http://api.openweathermap.org/data/2.5/weather?q=saba,hn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 327
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ixtapa. http://api.openweathermap.org/data/2.5/weather?q=ixtapa,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Khatanga. http://api.openweathermap.org/data/2.5/weather?q=khatanga,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mbandaka. http://api.openweathermap.org/data/2.5/weather?q=mbandaka,cd&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 328
    City: Kruisfontein. http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yoichi. http://api.openweathermap.org/data/2.5/weather?q=yoichi,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 329
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kapaa. http://api.openweathermap.org/data/2.5/weather?q=kapaa,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tiksi. http://api.openweathermap.org/data/2.5/weather?q=tiksi,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 330
    City: Havre-Saint-Pierre. http://api.openweathermap.org/data/2.5/weather?q=havre-saint-pierre,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 331
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vysokogornyy. http://api.openweathermap.org/data/2.5/weather?q=vysokogornyy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 332
    City: Chicama. http://api.openweathermap.org/data/2.5/weather?q=chicama,pe&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Poum. http://api.openweathermap.org/data/2.5/weather?q=poum,nc&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tettnang. http://api.openweathermap.org/data/2.5/weather?q=tettnang,de&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 333
    City: Tarko-Sale. http://api.openweathermap.org/data/2.5/weather?q=tarko-sale,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 334
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Guerrero Negro. http://api.openweathermap.org/data/2.5/weather?q=guerrero negro,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ebolowa. http://api.openweathermap.org/data/2.5/weather?q=ebolowa,cm&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 335
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Clyde River. http://api.openweathermap.org/data/2.5/weather?q=clyde river,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Shangrao. http://api.openweathermap.org/data/2.5/weather?q=shangrao,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 336
    City: Kahului. http://api.openweathermap.org/data/2.5/weather?q=kahului,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 337
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kalabo. http://api.openweathermap.org/data/2.5/weather?q=kalabo,zm&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 338
    City: Alofi. http://api.openweathermap.org/data/2.5/weather?q=alofi,nu&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 339
    City: Oussouye. http://api.openweathermap.org/data/2.5/weather?q=oussouye,sn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 340
    City: Nouadhibou. http://api.openweathermap.org/data/2.5/weather?q=nouadhibou,mr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Sisimiut. http://api.openweathermap.org/data/2.5/weather?q=sisimiut,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 341
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Walvis Bay. http://api.openweathermap.org/data/2.5/weather?q=walvis bay,na&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 342
    City: Chernyshevskiy. http://api.openweathermap.org/data/2.5/weather?q=chernyshevskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 343
    City: Khorramshahr. http://api.openweathermap.org/data/2.5/weather?q=khorramshahr,ir&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 344
    City: Krasnoshchekovo. http://api.openweathermap.org/data/2.5/weather?q=krasnoshchekovo,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 345
    City: Baykit. http://api.openweathermap.org/data/2.5/weather?q=baykit,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 346
    City: Geraldton. http://api.openweathermap.org/data/2.5/weather?q=geraldton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yerbogachen. http://api.openweathermap.org/data/2.5/weather?q=yerbogachen,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 347
    City: Sinjar. http://api.openweathermap.org/data/2.5/weather?q=sinjar,iq&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 348
    City: Pangai. http://api.openweathermap.org/data/2.5/weather?q=pangai,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 349
    City: Barrow. http://api.openweathermap.org/data/2.5/weather?q=barrow,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hilo. http://api.openweathermap.org/data/2.5/weather?q=hilo,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Pangnirtung. http://api.openweathermap.org/data/2.5/weather?q=pangnirtung,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 350
    City: Kaspiyskiy. http://api.openweathermap.org/data/2.5/weather?q=kaspiyskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kahului. http://api.openweathermap.org/data/2.5/weather?q=kahului,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Antalaha. http://api.openweathermap.org/data/2.5/weather?q=antalaha,mg&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 351
    City: Kindia. http://api.openweathermap.org/data/2.5/weather?q=kindia,gn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 352
    City: Karratha. http://api.openweathermap.org/data/2.5/weather?q=karratha,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kashi. http://api.openweathermap.org/data/2.5/weather?q=kashi,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 353
    City: Atikokan. http://api.openweathermap.org/data/2.5/weather?q=atikokan,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 354
    City: Sao Filipe. http://api.openweathermap.org/data/2.5/weather?q=sao filipe,cv&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Guiratinga. http://api.openweathermap.org/data/2.5/weather?q=guiratinga,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 355
    City: Kenai. http://api.openweathermap.org/data/2.5/weather?q=kenai,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lorengau. http://api.openweathermap.org/data/2.5/weather?q=lorengau,pg&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Macquarie. http://api.openweathermap.org/data/2.5/weather?q=port macquarie,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Pratapgarh. http://api.openweathermap.org/data/2.5/weather?q=pratapgarh,in&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 356
    City: Geraldton. http://api.openweathermap.org/data/2.5/weather?q=geraldton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hualmay. http://api.openweathermap.org/data/2.5/weather?q=hualmay,pe&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 357
    City: Dumai. http://api.openweathermap.org/data/2.5/weather?q=dumai,id&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 358
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: North Bend. http://api.openweathermap.org/data/2.5/weather?q=north bend,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Korla. http://api.openweathermap.org/data/2.5/weather?q=korla,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cuamba. http://api.openweathermap.org/data/2.5/weather?q=cuamba,mz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 359
    City: Mahebourg. http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Padang. http://api.openweathermap.org/data/2.5/weather?q=padang,id&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 360
    City: Katsuura. http://api.openweathermap.org/data/2.5/weather?q=katsuura,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Touros. http://api.openweathermap.org/data/2.5/weather?q=touros,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Harper. http://api.openweathermap.org/data/2.5/weather?q=harper,lr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 361
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Dongsheng. http://api.openweathermap.org/data/2.5/weather?q=dongsheng,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 362
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Muros. http://api.openweathermap.org/data/2.5/weather?q=muros,es&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 363
    City: Korla. http://api.openweathermap.org/data/2.5/weather?q=korla,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ahipara. http://api.openweathermap.org/data/2.5/weather?q=ahipara,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 364
    City: Adrar. http://api.openweathermap.org/data/2.5/weather?q=adrar,dz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tahoua. http://api.openweathermap.org/data/2.5/weather?q=tahoua,ne&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 365
    City: Sazonovo. http://api.openweathermap.org/data/2.5/weather?q=sazonovo,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 366
    City: Bethel. http://api.openweathermap.org/data/2.5/weather?q=bethel,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hammerfest. http://api.openweathermap.org/data/2.5/weather?q=hammerfest,no&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 367
    City: Cherskiy. http://api.openweathermap.org/data/2.5/weather?q=cherskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Sobolevo. http://api.openweathermap.org/data/2.5/weather?q=sobolevo,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Saint-Augustin. http://api.openweathermap.org/data/2.5/weather?q=saint-augustin,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Moyale. http://api.openweathermap.org/data/2.5/weather?q=moyale,et&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 368
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Glendive. http://api.openweathermap.org/data/2.5/weather?q=glendive,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Swindon. http://api.openweathermap.org/data/2.5/weather?q=swindon,gb&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 369
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Razdolinsk. http://api.openweathermap.org/data/2.5/weather?q=razdolinsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 370
    City: Carnarvon. http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ilulissat. http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Butaritari. http://api.openweathermap.org/data/2.5/weather?q=butaritari,ki&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Coquimbo. http://api.openweathermap.org/data/2.5/weather?q=coquimbo,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 371
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: San Juan. http://api.openweathermap.org/data/2.5/weather?q=san juan,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 372
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Naron. http://api.openweathermap.org/data/2.5/weather?q=naron,es&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 373
    City: Uvira. http://api.openweathermap.org/data/2.5/weather?q=uvira,cd&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 374
    City: Kungurtug. http://api.openweathermap.org/data/2.5/weather?q=kungurtug,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 375
    City: Guerrero Negro. http://api.openweathermap.org/data/2.5/weather?q=guerrero negro,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Thompson. http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bhadrachalam. http://api.openweathermap.org/data/2.5/weather?q=bhadrachalam,in&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 376
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Sharjah. http://api.openweathermap.org/data/2.5/weather?q=sharjah,ae&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 377
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: College. http://api.openweathermap.org/data/2.5/weather?q=college,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 378
    City: Bethel. http://api.openweathermap.org/data/2.5/weather?q=bethel,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Iquique. http://api.openweathermap.org/data/2.5/weather?q=iquique,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 379
    City: Boa Vista. http://api.openweathermap.org/data/2.5/weather?q=boa vista,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mount Gambier. http://api.openweathermap.org/data/2.5/weather?q=mount gambier,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kavieng. http://api.openweathermap.org/data/2.5/weather?q=kavieng,pg&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 380
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Butaritari. http://api.openweathermap.org/data/2.5/weather?q=butaritari,ki&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Upernavik. http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mayo. http://api.openweathermap.org/data/2.5/weather?q=mayo,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 381
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Talnakh. http://api.openweathermap.org/data/2.5/weather?q=talnakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Karpogory. http://api.openweathermap.org/data/2.5/weather?q=karpogory,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 382
    City: Victor Harbor. http://api.openweathermap.org/data/2.5/weather?q=victor harbor,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 383
    City: Barrow. http://api.openweathermap.org/data/2.5/weather?q=barrow,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Provideniya. http://api.openweathermap.org/data/2.5/weather?q=provideniya,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Coquimbo. http://api.openweathermap.org/data/2.5/weather?q=coquimbo,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kapaa. http://api.openweathermap.org/data/2.5/weather?q=kapaa,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Muncar. http://api.openweathermap.org/data/2.5/weather?q=muncar,id&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 384
    City: Brynmawr. http://api.openweathermap.org/data/2.5/weather?q=brynmawr,gb&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 385
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Geraldton. http://api.openweathermap.org/data/2.5/weather?q=geraldton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Elizabeth. http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Nortelandia. http://api.openweathermap.org/data/2.5/weather?q=nortelandia,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 386
    City: Puerto Ayora. http://api.openweathermap.org/data/2.5/weather?q=puerto ayora,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Morros. http://api.openweathermap.org/data/2.5/weather?q=morros,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 387
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kanye. http://api.openweathermap.org/data/2.5/weather?q=kanye,bw&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 388
    City: Kantemirovka. http://api.openweathermap.org/data/2.5/weather?q=kantemirovka,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 389
    City: Margate. http://api.openweathermap.org/data/2.5/weather?q=margate,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 390
    City: Tiksi. http://api.openweathermap.org/data/2.5/weather?q=tiksi,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Sinnamary. http://api.openweathermap.org/data/2.5/weather?q=sinnamary,gf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kapaa. http://api.openweathermap.org/data/2.5/weather?q=kapaa,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mount Isa. http://api.openweathermap.org/data/2.5/weather?q=mount isa,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Talnakh. http://api.openweathermap.org/data/2.5/weather?q=talnakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lorengau. http://api.openweathermap.org/data/2.5/weather?q=lorengau,pg&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cap Malheureux. http://api.openweathermap.org/data/2.5/weather?q=cap malheureux,mu&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 391
    City: Esperance. http://api.openweathermap.org/data/2.5/weather?q=esperance,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Xichang. http://api.openweathermap.org/data/2.5/weather?q=xichang,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 392
    City: Ejura. http://api.openweathermap.org/data/2.5/weather?q=ejura,gh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Seminole. http://api.openweathermap.org/data/2.5/weather?q=seminole,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 393
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Linxia. http://api.openweathermap.org/data/2.5/weather?q=linxia,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 394
    City: Chake Chake. http://api.openweathermap.org/data/2.5/weather?q=chake chake,tz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 395
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Gharghoda. http://api.openweathermap.org/data/2.5/weather?q=gharghoda,in&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 396
    City: Cherskiy. http://api.openweathermap.org/data/2.5/weather?q=cherskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Saskylakh. http://api.openweathermap.org/data/2.5/weather?q=saskylakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ponta do Sol. http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Barrow. http://api.openweathermap.org/data/2.5/weather?q=barrow,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tuatapere. http://api.openweathermap.org/data/2.5/weather?q=tuatapere,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Beringovskiy. http://api.openweathermap.org/data/2.5/weather?q=beringovskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 397
    City: Vestmanna. http://api.openweathermap.org/data/2.5/weather?q=vestmanna,fo&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 398
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Lincoln. http://api.openweathermap.org/data/2.5/weather?q=port lincoln,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Severo-Kurilsk. http://api.openweathermap.org/data/2.5/weather?q=severo-kurilsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Santa Teresa. http://api.openweathermap.org/data/2.5/weather?q=santa teresa,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 399
    City: Broome. http://api.openweathermap.org/data/2.5/weather?q=broome,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Nemuro. http://api.openweathermap.org/data/2.5/weather?q=nemuro,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 400
    City: Butaritari. http://api.openweathermap.org/data/2.5/weather?q=butaritari,ki&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Saskylakh. http://api.openweathermap.org/data/2.5/weather?q=saskylakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Thompson. http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Sur. http://api.openweathermap.org/data/2.5/weather?q=sur,om&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 401
    City: New Norfolk. http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Prince Rupert. http://api.openweathermap.org/data/2.5/weather?q=prince rupert,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 402
    City: Tuktoyaktuk. http://api.openweathermap.org/data/2.5/weather?q=tuktoyaktuk,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Norman Wells. http://api.openweathermap.org/data/2.5/weather?q=norman wells,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vila Franca do Campo. http://api.openweathermap.org/data/2.5/weather?q=vila franca do campo,pt&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 403
    City: Manokwari. http://api.openweathermap.org/data/2.5/weather?q=manokwari,id&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 404
    City: Chokurdakh. http://api.openweathermap.org/data/2.5/weather?q=chokurdakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Changchun. http://api.openweathermap.org/data/2.5/weather?q=changchun,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 405
    City: Port Alfred. http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Stokmarknes. http://api.openweathermap.org/data/2.5/weather?q=stokmarknes,no&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 406
    City: Mabaruma. http://api.openweathermap.org/data/2.5/weather?q=mabaruma,gy&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 407
    City: Liverpool. http://api.openweathermap.org/data/2.5/weather?q=liverpool,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 408
    City: Kavieng. http://api.openweathermap.org/data/2.5/weather?q=kavieng,pg&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Husavik. http://api.openweathermap.org/data/2.5/weather?q=husavik,is&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ponta Delgada. http://api.openweathermap.org/data/2.5/weather?q=ponta delgada,pt&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 409
    City: Carnarvon. http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tuktoyaktuk. http://api.openweathermap.org/data/2.5/weather?q=tuktoyaktuk,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Thompson. http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kapaa. http://api.openweathermap.org/data/2.5/weather?q=kapaa,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Morro Bay. http://api.openweathermap.org/data/2.5/weather?q=morro bay,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 410
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ganzhou. http://api.openweathermap.org/data/2.5/weather?q=ganzhou,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 411
    City: Faanui. http://api.openweathermap.org/data/2.5/weather?q=faanui,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Avarua. http://api.openweathermap.org/data/2.5/weather?q=avarua,ck&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Puerto Ayora. http://api.openweathermap.org/data/2.5/weather?q=puerto ayora,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: San Patricio. http://api.openweathermap.org/data/2.5/weather?q=san patricio,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Fillan. http://api.openweathermap.org/data/2.5/weather?q=fillan,no&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 412
    City: Lahr. http://api.openweathermap.org/data/2.5/weather?q=lahr,de&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 413
    City: Faaborg. http://api.openweathermap.org/data/2.5/weather?q=faaborg,dk&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 414
    City: Alofi. http://api.openweathermap.org/data/2.5/weather?q=alofi,nu&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kapaa. http://api.openweathermap.org/data/2.5/weather?q=kapaa,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Nikolskoye. http://api.openweathermap.org/data/2.5/weather?q=nikolskoye,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Taft. http://api.openweathermap.org/data/2.5/weather?q=taft,ir&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 415
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bilma. http://api.openweathermap.org/data/2.5/weather?q=bilma,ne&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Neftcala. http://api.openweathermap.org/data/2.5/weather?q=neftcala,az&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 416
    City: Atuona. http://api.openweathermap.org/data/2.5/weather?q=atuona,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Sitka. http://api.openweathermap.org/data/2.5/weather?q=sitka,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Avarua. http://api.openweathermap.org/data/2.5/weather?q=avarua,ck&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kalabo. http://api.openweathermap.org/data/2.5/weather?q=kalabo,zm&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Skelleftea. http://api.openweathermap.org/data/2.5/weather?q=skelleftea,se&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 417
    City: Okhotsk. http://api.openweathermap.org/data/2.5/weather?q=okhotsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Geraldton. http://api.openweathermap.org/data/2.5/weather?q=geraldton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Chokurdakh. http://api.openweathermap.org/data/2.5/weather?q=chokurdakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Beringovskiy. http://api.openweathermap.org/data/2.5/weather?q=beringovskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Progreso. http://api.openweathermap.org/data/2.5/weather?q=progreso,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 418
    City: Qaqortoq. http://api.openweathermap.org/data/2.5/weather?q=qaqortoq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Barrow. http://api.openweathermap.org/data/2.5/weather?q=barrow,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Faanui. http://api.openweathermap.org/data/2.5/weather?q=faanui,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Abu Dhabi. http://api.openweathermap.org/data/2.5/weather?q=abu dhabi,ae&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 419
    City: Tateyama. http://api.openweathermap.org/data/2.5/weather?q=tateyama,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 420
    City: Minsk. http://api.openweathermap.org/data/2.5/weather?q=minsk,by&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 421
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Talnakh. http://api.openweathermap.org/data/2.5/weather?q=talnakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Srednekolymsk. http://api.openweathermap.org/data/2.5/weather?q=srednekolymsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Pimenta Bueno. http://api.openweathermap.org/data/2.5/weather?q=pimenta bueno,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 422
    City: Srednekolymsk. http://api.openweathermap.org/data/2.5/weather?q=srednekolymsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Berlevag. http://api.openweathermap.org/data/2.5/weather?q=berlevag,no&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 423
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Scarborough. http://api.openweathermap.org/data/2.5/weather?q=scarborough,tt&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 424
    City: Bethel. http://api.openweathermap.org/data/2.5/weather?q=bethel,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Khandyga. http://api.openweathermap.org/data/2.5/weather?q=khandyga,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 425
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Navoloki. http://api.openweathermap.org/data/2.5/weather?q=navoloki,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 426
    City: Ribeira Grande. http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cherskiy. http://api.openweathermap.org/data/2.5/weather?q=cherskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Praia da Vitoria. http://api.openweathermap.org/data/2.5/weather?q=praia da vitoria,pt&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 427
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Narsaq. http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 428
    City: Abha. http://api.openweathermap.org/data/2.5/weather?q=abha,sa&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 429
    City: Jevargi. http://api.openweathermap.org/data/2.5/weather?q=jevargi,in&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 430
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Dudinka. http://api.openweathermap.org/data/2.5/weather?q=dudinka,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 431
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bambous Virieux. http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ugoofaaru. http://api.openweathermap.org/data/2.5/weather?q=ugoofaaru,mv&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 432
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kapaa. http://api.openweathermap.org/data/2.5/weather?q=kapaa,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Siemiatycze. http://api.openweathermap.org/data/2.5/weather?q=siemiatycze,pl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 433
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cherskiy. http://api.openweathermap.org/data/2.5/weather?q=cherskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yuryuzan. http://api.openweathermap.org/data/2.5/weather?q=yuryuzan,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 434
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bartica. http://api.openweathermap.org/data/2.5/weather?q=bartica,gy&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 435
    City: Pyapon. http://api.openweathermap.org/data/2.5/weather?q=pyapon,mm&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 436
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lorengau. http://api.openweathermap.org/data/2.5/weather?q=lorengau,pg&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kodiak. http://api.openweathermap.org/data/2.5/weather?q=kodiak,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Turukhansk. http://api.openweathermap.org/data/2.5/weather?q=turukhansk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 437
    City: Hasaki. http://api.openweathermap.org/data/2.5/weather?q=hasaki,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hilo. http://api.openweathermap.org/data/2.5/weather?q=hilo,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mehamn. http://api.openweathermap.org/data/2.5/weather?q=mehamn,no&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 438
    City: Pevek. http://api.openweathermap.org/data/2.5/weather?q=pevek,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Atar. http://api.openweathermap.org/data/2.5/weather?q=atar,mr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kitami. http://api.openweathermap.org/data/2.5/weather?q=kitami,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 439
    City: Vila Franca do Campo. http://api.openweathermap.org/data/2.5/weather?q=vila franca do campo,pt&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Butaritari. http://api.openweathermap.org/data/2.5/weather?q=butaritari,ki&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Avarua. http://api.openweathermap.org/data/2.5/weather?q=avarua,ck&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Esperance. http://api.openweathermap.org/data/2.5/weather?q=esperance,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cetraro. http://api.openweathermap.org/data/2.5/weather?q=cetraro,it&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 440
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Chimbote. http://api.openweathermap.org/data/2.5/weather?q=chimbote,pe&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 441
    City: Emerald. http://api.openweathermap.org/data/2.5/weather?q=emerald,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 442
    City: Banda Aceh. http://api.openweathermap.org/data/2.5/weather?q=banda aceh,id&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 443
    City: Apac. http://api.openweathermap.org/data/2.5/weather?q=apac,ug&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 444
    City: Atuona. http://api.openweathermap.org/data/2.5/weather?q=atuona,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Talnakh. http://api.openweathermap.org/data/2.5/weather?q=talnakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vao. http://api.openweathermap.org/data/2.5/weather?q=vao,nc&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: East London. http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Avarua. http://api.openweathermap.org/data/2.5/weather?q=avarua,ck&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kota Belud. http://api.openweathermap.org/data/2.5/weather?q=kota belud,my&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 445
    City: Chifeng. http://api.openweathermap.org/data/2.5/weather?q=chifeng,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 446
    City: Adrar. http://api.openweathermap.org/data/2.5/weather?q=adrar,dz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Nyurba. http://api.openweathermap.org/data/2.5/weather?q=nyurba,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lodja. http://api.openweathermap.org/data/2.5/weather?q=lodja,cd&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 447
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Grindavik. http://api.openweathermap.org/data/2.5/weather?q=grindavik,is&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 448
    City: Mar del Plata. http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tezu. http://api.openweathermap.org/data/2.5/weather?q=tezu,in&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 449
    City: Ust-Kan. http://api.openweathermap.org/data/2.5/weather?q=ust-kan,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 450
    City: Sao Joao da Barra. http://api.openweathermap.org/data/2.5/weather?q=sao joao da barra,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 451
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Victoria. http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Careiro da Varzea. http://api.openweathermap.org/data/2.5/weather?q=careiro da varzea,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 452
    City: Hilo. http://api.openweathermap.org/data/2.5/weather?q=hilo,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Esperance. http://api.openweathermap.org/data/2.5/weather?q=esperance,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Muros. http://api.openweathermap.org/data/2.5/weather?q=muros,es&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Olean. http://api.openweathermap.org/data/2.5/weather?q=olean,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 453
    City: Puerto Ayora. http://api.openweathermap.org/data/2.5/weather?q=puerto ayora,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Saldanha. http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Guarapuava. http://api.openweathermap.org/data/2.5/weather?q=guarapuava,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 454
    City: Thompson. http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Saint-Philippe. http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Dubbo. http://api.openweathermap.org/data/2.5/weather?q=dubbo,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 455
    City: Thompson. http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: New Norfolk. http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kassala. http://api.openweathermap.org/data/2.5/weather?q=kassala,sd&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 456
    City: Marovoay. http://api.openweathermap.org/data/2.5/weather?q=marovoay,mg&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 457
    City: Kiunga. http://api.openweathermap.org/data/2.5/weather?q=kiunga,pg&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Nagai. http://api.openweathermap.org/data/2.5/weather?q=nagai,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 458
    City: Kaitangata. http://api.openweathermap.org/data/2.5/weather?q=kaitangata,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tuktoyaktuk. http://api.openweathermap.org/data/2.5/weather?q=tuktoyaktuk,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kapaa. http://api.openweathermap.org/data/2.5/weather?q=kapaa,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kitimat. http://api.openweathermap.org/data/2.5/weather?q=kitimat,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 459
    City: Oriximina. http://api.openweathermap.org/data/2.5/weather?q=oriximina,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 460
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Erzincan. http://api.openweathermap.org/data/2.5/weather?q=erzincan,tr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 461
    City: Kharan. http://api.openweathermap.org/data/2.5/weather?q=kharan,pk&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 462
    City: Vardo. http://api.openweathermap.org/data/2.5/weather?q=vardo,no&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Manavalakurichi. http://api.openweathermap.org/data/2.5/weather?q=manavalakurichi,in&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 463
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Puerto Ayora. http://api.openweathermap.org/data/2.5/weather?q=puerto ayora,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Pathanamthitta. http://api.openweathermap.org/data/2.5/weather?q=pathanamthitta,in&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 464
    City: Jutai. http://api.openweathermap.org/data/2.5/weather?q=jutai,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 465
    City: Guerrero Negro. http://api.openweathermap.org/data/2.5/weather?q=guerrero negro,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Klaksvik. http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Buchanan. http://api.openweathermap.org/data/2.5/weather?q=buchanan,lr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 466
    City: Havre-Saint-Pierre. http://api.openweathermap.org/data/2.5/weather?q=havre-saint-pierre,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Saskylakh. http://api.openweathermap.org/data/2.5/weather?q=saskylakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Saskylakh. http://api.openweathermap.org/data/2.5/weather?q=saskylakh,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Chuy. http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Semey. http://api.openweathermap.org/data/2.5/weather?q=semey,kz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 467
    City: Vestmannaeyjar. http://api.openweathermap.org/data/2.5/weather?q=vestmannaeyjar,is&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 468
    City: Mahina. http://api.openweathermap.org/data/2.5/weather?q=mahina,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 469
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ladovskaya Balka. http://api.openweathermap.org/data/2.5/weather?q=ladovskaya balka,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 470
    City: Gaya. http://api.openweathermap.org/data/2.5/weather?q=gaya,ne&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 471
    City: Khatanga. http://api.openweathermap.org/data/2.5/weather?q=khatanga,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tekirdag. http://api.openweathermap.org/data/2.5/weather?q=tekirdag,tr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 472
    City: Erenhot. http://api.openweathermap.org/data/2.5/weather?q=erenhot,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 473
    City: Cherskiy. http://api.openweathermap.org/data/2.5/weather?q=cherskiy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Nikolskoye. http://api.openweathermap.org/data/2.5/weather?q=nikolskoye,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Pevek. http://api.openweathermap.org/data/2.5/weather?q=pevek,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Meadow Lake. http://api.openweathermap.org/data/2.5/weather?q=meadow lake,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 474
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kupang. http://api.openweathermap.org/data/2.5/weather?q=kupang,id&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 475
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: San Cristobal. http://api.openweathermap.org/data/2.5/weather?q=san cristobal,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Atuona. http://api.openweathermap.org/data/2.5/weather?q=atuona,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Thompson. http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Alyangula. http://api.openweathermap.org/data/2.5/weather?q=alyangula,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 476
    City: Port-Gentil. http://api.openweathermap.org/data/2.5/weather?q=port-gentil,ga&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 477
    City: Jining. http://api.openweathermap.org/data/2.5/weather?q=jining,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 478
    City: Yellowknife. http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Busselton. http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Uray. http://api.openweathermap.org/data/2.5/weather?q=uray,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 479
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: New Norfolk. http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ashcroft. http://api.openweathermap.org/data/2.5/weather?q=ashcroft,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 480
    City: Sao Filipe. http://api.openweathermap.org/data/2.5/weather?q=sao filipe,cv&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Salekhard. http://api.openweathermap.org/data/2.5/weather?q=salekhard,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 481
    City: Marawi. http://api.openweathermap.org/data/2.5/weather?q=marawi,sd&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 482
    City: San Cristobal. http://api.openweathermap.org/data/2.5/weather?q=san cristobal,ve&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Fougamou. http://api.openweathermap.org/data/2.5/weather?q=fougamou,ga&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 483
    City: Hobart. http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lufilufi. http://api.openweathermap.org/data/2.5/weather?q=lufilufi,ws&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 484
    City: Lagoa. http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 485
    City: New Norfolk. http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tigil. http://api.openweathermap.org/data/2.5/weather?q=tigil,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 486
    City: Jalu. http://api.openweathermap.org/data/2.5/weather?q=jalu,ly&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 487
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hilo. http://api.openweathermap.org/data/2.5/weather?q=hilo,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hervey Bay. http://api.openweathermap.org/data/2.5/weather?q=hervey bay,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lesozavodsk. http://api.openweathermap.org/data/2.5/weather?q=lesozavodsk,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 488
    City: Burgeo. http://api.openweathermap.org/data/2.5/weather?q=burgeo,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 489
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Thompson. http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cape Town. http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mehamn. http://api.openweathermap.org/data/2.5/weather?q=mehamn,no&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Korla. http://api.openweathermap.org/data/2.5/weather?q=korla,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Uige. http://api.openweathermap.org/data/2.5/weather?q=uige,ao&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 490
    City: Maningrida. http://api.openweathermap.org/data/2.5/weather?q=maningrida,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 491
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Atuona. http://api.openweathermap.org/data/2.5/weather?q=atuona,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Port Shepstone. http://api.openweathermap.org/data/2.5/weather?q=port shepstone,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 492
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lokosovo. http://api.openweathermap.org/data/2.5/weather?q=lokosovo,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 493
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: New Norfolk. http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hayvoron. http://api.openweathermap.org/data/2.5/weather?q=hayvoron,ua&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 494
    City: Georgetown. http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Arraial do Cabo. http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Jamestown. http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Enterprise. http://api.openweathermap.org/data/2.5/weather?q=enterprise,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 495
    City: Torbay. http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kodiak. http://api.openweathermap.org/data/2.5/weather?q=kodiak,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Phuket. http://api.openweathermap.org/data/2.5/weather?q=phuket,th&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 496
    City: Yemelyanovo. http://api.openweathermap.org/data/2.5/weather?q=yemelyanovo,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 497
    City: Constitucion. http://api.openweathermap.org/data/2.5/weather?q=constitucion,mx&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 498
    City: Deoria. http://api.openweathermap.org/data/2.5/weather?q=deoria,in&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 499
    City: Trelleborg. http://api.openweathermap.org/data/2.5/weather?q=trelleborg,se&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 500
    City: Almaznyy. http://api.openweathermap.org/data/2.5/weather?q=almaznyy,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 501
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Shenjiamen. http://api.openweathermap.org/data/2.5/weather?q=shenjiamen,cn&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 502
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tautira. http://api.openweathermap.org/data/2.5/weather?q=tautira,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 503
    City: Dingle. http://api.openweathermap.org/data/2.5/weather?q=dingle,ie&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 504
    City: Buchanan. http://api.openweathermap.org/data/2.5/weather?q=buchanan,lr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Meulaboh. http://api.openweathermap.org/data/2.5/weather?q=meulaboh,id&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 505
    City: Nemuro. http://api.openweathermap.org/data/2.5/weather?q=nemuro,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Ushuaia. http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hithadhoo. http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Puerto Ayora. http://api.openweathermap.org/data/2.5/weather?q=puerto ayora,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bathsheba. http://api.openweathermap.org/data/2.5/weather?q=bathsheba,bb&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Conceicao do Araguaia. http://api.openweathermap.org/data/2.5/weather?q=conceicao do araguaia,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tasiilaq. http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Thompson. http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lompoc. http://api.openweathermap.org/data/2.5/weather?q=lompoc,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 506
    City: Kapaa. http://api.openweathermap.org/data/2.5/weather?q=kapaa,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Dikson. http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lewistown. http://api.openweathermap.org/data/2.5/weather?q=lewistown,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Yuzha. http://api.openweathermap.org/data/2.5/weather?q=yuzha,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 507
    City: Kudahuvadhoo. http://api.openweathermap.org/data/2.5/weather?q=kudahuvadhoo,mv&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 508
    City: Seoul. http://api.openweathermap.org/data/2.5/weather?q=seoul,kr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Sumenep. http://api.openweathermap.org/data/2.5/weather?q=sumenep,id&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 509
    City: Tuktoyaktuk. http://api.openweathermap.org/data/2.5/weather?q=tuktoyaktuk,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Punta Arenas. http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Aripuana. http://api.openweathermap.org/data/2.5/weather?q=aripuana,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 510
    City: Tiksi. http://api.openweathermap.org/data/2.5/weather?q=tiksi,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Kapaa. http://api.openweathermap.org/data/2.5/weather?q=kapaa,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Puerto Ayora. http://api.openweathermap.org/data/2.5/weather?q=puerto ayora,ec&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Cidreira. http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Albany. http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bredasdorp. http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lebu. http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Karratha. http://api.openweathermap.org/data/2.5/weather?q=karratha,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Brae. http://api.openweathermap.org/data/2.5/weather?q=brae,gb&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 511
    City: Nanortalik. http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Marsaxlokk. http://api.openweathermap.org/data/2.5/weather?q=marsaxlokk,mt&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 512
    City: Esperance. http://api.openweathermap.org/data/2.5/weather?q=esperance,au&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Palmer. http://api.openweathermap.org/data/2.5/weather?q=palmer,us&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 513
    City: San Rafael. http://api.openweathermap.org/data/2.5/weather?q=san rafael,ar&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 514
    City: Pevek. http://api.openweathermap.org/data/2.5/weather?q=pevek,ru&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Lardos. http://api.openweathermap.org/data/2.5/weather?q=lardos,gr&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 515
    City: Cockburn Town. http://api.openweathermap.org/data/2.5/weather?q=cockburn town,bs&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hermanus. http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Tuktoyaktuk. http://api.openweathermap.org/data/2.5/weather?q=tuktoyaktuk,ca&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Castro. http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Vaini. http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Bluff. http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Belmonte. http://api.openweathermap.org/data/2.5/weather?q=belmonte,br&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 516
    City: Setermoen. http://api.openweathermap.org/data/2.5/weather?q=setermoen,no&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 517
    City: Santa Marta. http://api.openweathermap.org/data/2.5/weather?q=santa marta,co&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 518
    City: Qaanaaq. http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Hasaki. http://api.openweathermap.org/data/2.5/weather?q=hasaki,jp&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Rikitea. http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    City: Mao. http://api.openweathermap.org/data/2.5/weather?q=mao,td&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 519
    City: Coihaique. http://api.openweathermap.org/data/2.5/weather?q=coihaique,cl&units=imperial&APPID=25bc90a1196e6f153eece0bc0b0fc9eb
    Status code: 200. DF length is now: 520
    ------------------------------
    Finished     Finished   Finished
    
    


```python
# view data
cities_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city_name</th>
      <th>country_code</th>
      <th>rand_lat</th>
      <th>rand_lng</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Temp (F)</th>
      <th>Humidity (%)</th>
      <th>Cloudiness (%)</th>
      <th>Wind Speed (mph)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>arraial do cabo</td>
      <td>br</td>
      <td>-32.18</td>
      <td>-29.75</td>
      <td>-22.97</td>
      <td>-42.02</td>
      <td>72.52</td>
      <td>88</td>
      <td>75</td>
      <td>5.82</td>
    </tr>
    <tr>
      <th>1</th>
      <td>isangel</td>
      <td>vu</td>
      <td>-20.11</td>
      <td>178.55</td>
      <td>-19.55</td>
      <td>169.27</td>
      <td>70.38</td>
      <td>100</td>
      <td>92</td>
      <td>19.93</td>
    </tr>
    <tr>
      <th>2</th>
      <td>saint george</td>
      <td>bm</td>
      <td>29.39</td>
      <td>-54.13</td>
      <td>32.38</td>
      <td>-64.68</td>
      <td>80.6</td>
      <td>78</td>
      <td>75</td>
      <td>12.75</td>
    </tr>
    <tr>
      <th>3</th>
      <td>srednekolymsk</td>
      <td>ru</td>
      <td>66.03</td>
      <td>153.04</td>
      <td>67.46</td>
      <td>153.71</td>
      <td>49.77</td>
      <td>72</td>
      <td>88</td>
      <td>3.27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ixtapa</td>
      <td>mx</td>
      <td>9.56</td>
      <td>-104.7</td>
      <td>20.71</td>
      <td>-105.21</td>
      <td>87.8</td>
      <td>70</td>
      <td>90</td>
      <td>14.99</td>
    </tr>
  </tbody>
</table>
</div>




```python
# save to csv file
cities_df.to_csv("weatherpy_results.csv", encoding="utf-8", index=False)
```

# Scatter Plots


```python
# Scatter plot - Temperature (F) vs. Latitude
plt.scatter(cities_df["Latitude"],cities_df["Temp (F)"], alpha = 0.5)
plt.xlabel("City Latitude")
plt.ylabel("Temperature (F)")
# Move title up with the "y" option
plt.title("City Latitude vs Temperature (F)",y=1.05)
plt.savefig("Lat_vs_TempF.png")

plt.show()
```


![png](output_11_0.png)



```python
# Scatter plot - Humidity (%) vs. Latitude
plt.scatter(cities_df["Latitude"],cities_df["Humidity (%)"], alpha = 0.5)
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")
# Move title up with the "y" option
plt.title("City Latitude vs Humidity (%)",y=1.05)
plt.savefig("Lat_vs_Humidity.png")

plt.show()
```


![png](output_12_0.png)



```python
# Scatter plot - Cloudiness (%) vs. Latitude
plt.scatter(cities_df["Latitude"],cities_df["Cloudiness (%)"], alpha = 0.5)
plt.xlabel("Latitude")
plt.ylabel("Cloudiness (%)")
# Move title up with the "y" option
plt.title("City Latitude vs Cloudiness (%)",y=1.05)
plt.savefig("Lat_vs_Cloud.png")

plt.show()
```


![png](output_13_0.png)



```python
# Scatter plot - Wind Speed (mph) vs. Latitude
plt.scatter(cities_df["Latitude"],cities_df["Wind Speed (mph)"], alpha = 0.5)
plt.xlabel("Latitude")
plt.ylabel("Wind Speed (mph)")
# Move title up with the "y" option
plt.title("City Latitude vs Wind Speed (mph)",y=1.05)
plt.savefig("Lat_vs_Wind.png")

plt.show()
```


![png](output_14_0.png)



```python
# Scatter plot - Longtitude vs. Latitude
plt.scatter(cities_df["Latitude"],cities_df["Longitude"], alpha = 0.5)
plt.xlabel("Latitude")
plt.ylabel("Longitude")
# Move title up with the "y" option
plt.title("City Latitude vs Longitude",y=1.05)
plt.savefig("LatvsLong.png")

plt.show()
```


![png](output_15_0.png)


#END
