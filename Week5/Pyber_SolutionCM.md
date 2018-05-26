
# Pyber


```python
# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
```


```python
# Read in data
city_data = pd.read_csv("instructions/pyber/raw_data/city_data.csv")
ride_data = pd.read_csv("instructions/pyber/raw_data/ride_data.csv")
#city_data.head()
ride_data.head()
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
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South Roy</td>
      <td>2016-01-02 18:42:34</td>
      <td>17.49</td>
      <td>4036272335942</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wiseborough</td>
      <td>2016-01-21 17:35:29</td>
      <td>44.18</td>
      <td>3645042422587</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spencertown</td>
      <td>2016-07-31 14:53:22</td>
      <td>6.87</td>
      <td>2242596575892</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nguyenbury</td>
      <td>2016-07-09 04:42:44</td>
      <td>6.28</td>
      <td>1543057793673</td>
    </tr>
  </tbody>
</table>
</div>




```python
pyber_data1 = pd.merge(ride_data, city_data, on="city", how="left")
pyber_data1.head()
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
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South Roy</td>
      <td>2016-01-02 18:42:34</td>
      <td>17.49</td>
      <td>4036272335942</td>
      <td>35</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wiseborough</td>
      <td>2016-01-21 17:35:29</td>
      <td>44.18</td>
      <td>3645042422587</td>
      <td>55</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spencertown</td>
      <td>2016-07-31 14:53:22</td>
      <td>6.87</td>
      <td>2242596575892</td>
      <td>68</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nguyenbury</td>
      <td>2016-07-09 04:42:44</td>
      <td>6.28</td>
      <td>1543057793673</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Set new index
pyber_data = pyber_data1.set_index("city")
pyber_data.head()
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
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Sarabury</th>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>South Roy</th>
      <td>2016-01-02 18:42:34</td>
      <td>17.49</td>
      <td>4036272335942</td>
      <td>35</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>Wiseborough</th>
      <td>2016-01-21 17:35:29</td>
      <td>44.18</td>
      <td>3645042422587</td>
      <td>55</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>Spencertown</th>
      <td>2016-07-31 14:53:22</td>
      <td>6.87</td>
      <td>2242596575892</td>
      <td>68</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>Nguyenbury</th>
      <td>2016-07-09 04:42:44</td>
      <td>6.28</td>
      <td>1543057793673</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Rural filter
rural_pyber_data = pyber_data[pyber_data['type'] == "Rural"]
rural_pyber_data.head()

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
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Horneland</th>
      <td>2016-07-19 10:07:33</td>
      <td>12.63</td>
      <td>8214498891817</td>
      <td>8</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>Kinghaven</th>
      <td>2016-05-18 23:28:12</td>
      <td>20.53</td>
      <td>6432117120069</td>
      <td>3</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>New Johnbury</th>
      <td>2016-04-21 08:30:25</td>
      <td>56.60</td>
      <td>9002881309143</td>
      <td>6</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>South Joseph</th>
      <td>2016-02-17 01:41:29</td>
      <td>57.52</td>
      <td>7365786843443</td>
      <td>3</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>Kennethburgh</th>
      <td>2016-10-19 13:13:17</td>
      <td>24.43</td>
      <td>2728236352387</td>
      <td>3</td>
      <td>Rural</td>
    </tr>
  </tbody>
</table>
</div>




```python
#rural data items for bubble chart
rural_avg_fare = rural_pyber_data.groupby(["city"]).mean()["fare"].rename("Average Fare by City")
rural_tot_rides = rural_pyber_data.groupby(["city"]).count()["ride_id"].rename("Total Number of Rides")
rural_tot_drivers = rural_pyber_data.groupby(["city"]).mean()["driver_count"].rename("Total Drivers by City")
rural_avg_fare
rural_tot_rides
rural_tot_drivers

```




    city
    East Leslie              9.0
    East Stephen             6.0
    East Troybury            3.0
    Erikport                 3.0
    Hernandezshire          10.0
    Horneland                8.0
    Jacksonfort              6.0
    Kennethburgh             3.0
    Kinghaven                3.0
    Manuelchester            7.0
    Matthewside              4.0
    New Johnbury             6.0
    North Whitney           10.0
    Shelbyhaven              9.0
    South Elizabethmouth     3.0
    South Joseph             3.0
    Stevensport              6.0
    West Kevintown           5.0
    Name: Total Drivers by City, dtype: float64




```python
#Urban filter
urban_pyber_data = pyber_data[pyber_data['type'] == "Urban"]
urban_pyber_data.head()
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
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Sarabury</th>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>South Roy</th>
      <td>2016-01-02 18:42:34</td>
      <td>17.49</td>
      <td>4036272335942</td>
      <td>35</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>Wiseborough</th>
      <td>2016-01-21 17:35:29</td>
      <td>44.18</td>
      <td>3645042422587</td>
      <td>55</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>Spencertown</th>
      <td>2016-07-31 14:53:22</td>
      <td>6.87</td>
      <td>2242596575892</td>
      <td>68</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>Nguyenbury</th>
      <td>2016-07-09 04:42:44</td>
      <td>6.28</td>
      <td>1543057793673</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
#urban data items for bubble chart
urban_avg_fare = urban_pyber_data.groupby(["city"]).mean()["fare"].rename("Average Fare by City")
urban_tot_rides = urban_pyber_data.groupby(["city"]).count()["ride_id"].rename("Total Number of Rides")
urban_tot_drivers = urban_pyber_data.groupby(["city"]).mean()["driver_count"].rename("Total Drivers by City")
#urban_avg_fare
#urban_tot_rides
#urban_tot_drivers
```


```python
#Suburban filter
suburban_pyber_data = pyber_data[pyber_data['type'] == "Suburban"]
suburban_pyber_data.head()
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
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Port James</th>
      <td>2016-12-04 06:16:36</td>
      <td>15.77</td>
      <td>2259499336994</td>
      <td>15</td>
      <td>Suburban</td>
    </tr>
    <tr>
      <th>Port James</th>
      <td>2016-12-04 06:16:36</td>
      <td>15.77</td>
      <td>2259499336994</td>
      <td>3</td>
      <td>Suburban</td>
    </tr>
    <tr>
      <th>New Samanthaside</th>
      <td>2016-06-05 14:36:58</td>
      <td>39.38</td>
      <td>3647873452658</td>
      <td>16</td>
      <td>Suburban</td>
    </tr>
    <tr>
      <th>Port Alexandria</th>
      <td>2016-07-29 09:30:09</td>
      <td>24.86</td>
      <td>2962960319234</td>
      <td>27</td>
      <td>Suburban</td>
    </tr>
    <tr>
      <th>Lake Brenda</th>
      <td>2016-08-26 03:07:30</td>
      <td>20.97</td>
      <td>5231983896020</td>
      <td>24</td>
      <td>Suburban</td>
    </tr>
  </tbody>
</table>
</div>




```python
#suburban data items for bubble chart
suburban_avg_fare = suburban_pyber_data.groupby(["city"]).mean()["fare"].rename("Average Fare by City")
suburban_tot_rides = suburban_pyber_data.groupby(["city"]).count()["ride_id"].rename("Total Number of Rides")
suburban_tot_drivers = suburban_pyber_data.groupby(["city"]).mean()["driver_count"].rename("Total Drivers by City")
#suburban_avg_fare
suburban_tot_rides
suburban_tot_drivers
```




    city
    Anitamouth              16.0
    Campbellport            26.0
    Carrollbury              4.0
    Clarkstad               21.0
    Conwaymouth             18.0
    East Cherylfurt          9.0
    East Jenniferchester    22.0
    Floresberg               7.0
    Jasonfort               25.0
    Jeffreyton               8.0
    Johnland                13.0
    Kyleton                 12.0
    Lake Brenda             24.0
    Martinmouth              5.0
    New Brandonborough       9.0
    New Cindyborough        20.0
    New Jessicamouth        22.0
    New Lynn                20.0
    New Michelleberg         9.0
    New Samanthaside        16.0
    North Tara              14.0
    North Tracyfort         18.0
    Paulfort                13.0
    Port Alexandria         27.0
    Port Guytown            26.0
    Port James               9.0
    Port Jose               11.0
    Port Michelleview       16.0
    Rodriguezview           10.0
    Sarahview               18.0
    South Gracechester      19.0
    South Jennifer           6.0
    South Shannonborough     9.0
    Thomastown               1.0
    Tiffanyton              21.0
    Webstertown             26.0
    West Evan                4.0
    West Pamelaborough      27.0
    West Paulport            5.0
    West Tony               17.0
    Williamchester          26.0
    Name: Total Drivers by City, dtype: float64



# bubble chart - Pyber Bubble Chart


```python
#bubble chart - Pyber Bubble Chart


#colors "gold", "lightskyblue", "lightcoral"
plt.scatter(urban_tot_rides,urban_avg_fare,s=5*urban_tot_drivers,color="lightskyblue",edgecolors="black",label="urban",alpha=0.8)
plt.scatter(rural_tot_rides,rural_avg_fare,s=5*rural_tot_drivers,color="gold",edgecolors="black", label="rural",alpha=0.8)
plt.scatter(suburban_tot_rides,suburban_avg_fare,s=5*suburban_tot_drivers,color="lightcoral",edgecolors="black",label="suburban",alpha=0.8)

plt.xlabel("Total number of rides (Per City)")
plt.ylabel("Average Fare ($)")
plt.legend(loc="best")
# Move title up with the "y" option
plt.title("Pyber Ride Sharing Data - 2016",y=1.05)

plt.show()
```


![png](output_12_0.png)


# Pie Charts

# Total Fares by City Type


```python
tot_fares = pyber_data.groupby(["type"]).sum()["fare"].rename("Total Fares by City Type")
tot_fares
```




    type
    Rural        4255.09
    Suburban    20335.69
    Urban       40078.34
    Name: Total Fares by City Type, dtype: float64




```python
#Labels for pie chart #2 - Total Rides by City Type
fares_labels= tot_fares.keys()
fares_labels
```




    Index(['Rural', 'Suburban', 'Urban'], dtype='object', name='type')




```python
#Pie chart #1
# % of Total Fares by City Type pie chart
drivers_colors=["gold", "lightskyblue", "lightcoral"]

plt.title("% of Total Fares by City Type")
explode = (0, 0, 0.07)
plt.pie(tot_fares, explode=explode, labels=fares_labels, colors=drivers_colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis("equal")
plt.show()
```


![png](output_17_0.png)


# Total Rides by City Type


```python
tot_ridestype = pyber_data.groupby(["type"]).count()["ride_id"].rename("Total Rides by City Type")
tot_ridestype
```




    type
    Rural        125
    Suburban     657
    Urban       1625
    Name: Total Rides by City Type, dtype: int64




```python
#Labels for pie chart #2 - Total Rides by City Type
rides_labels= tot_ridestype.keys()
rides_labels
```




    Index(['Rural', 'Suburban', 'Urban'], dtype='object', name='type')




```python
#Pie chart #2
# % of Total Rides by City Type pie chart
drivers_colors=["gold", "lightskyblue", "lightcoral"]

plt.title("% of Total Rides by City Type")
explode = [0, 0, 0.07]
plt.pie(tot_ridestype, explode=explode, labels=rides_labels, colors=drivers_colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis("equal")
plt.show()
```


![png](output_21_0.png)


# Total Drivers by City Type


```python
#Amount for pie chart - Drivers by Type
tot_driversbytype = pyber_data.groupby(["type"]).sum()["driver_count"]
tot_driversbytype
```




    type
    Rural         727
    Suburban     9730
    Urban       64501
    Name: driver_count, dtype: int64




```python
#Labels for pie chart - Drivers by Type
drivers_labels= tot_driversbytype.keys()
drivers_labels
```




    Index(['Rural', 'Suburban', 'Urban'], dtype='object', name='type')




```python
#Pie chart #3
# % of Drivers per City Type pie chart
drivers_colors=["gold", "lightskyblue", "lightcoral"]

plt.title("% of Total Drivers by City Type")
explode = (0, 0, 0.07)
plt.pie(tot_driversbytype, explode=explode, labels=drivers_labels, colors=drivers_colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis("equal")
plt.show()
```


![png](output_25_0.png)


#three observable trends based on the data
1.  Urban by far has more rides and therefore more fares.
2.  Rural is small that it might be hard to find drivers.
3.  Suburban is bringing in 31.4% of the fares with only 27% of the rides.  The revenue per ride is good in Suburban.
