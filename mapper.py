import pandas as pd
import geopandas
import matplotlib.pyplot as plt
from folium import Map, Circle, Marker, Popup


def get_beds():
    df = get_df()
    _map = Map(location=[41.8781, -87.6298], tiles='cartodbpositron', zoom_start=10)
    for idx, row in df.iterrows():
        Marker([row['Y'], row['X']], popup=row['HOSPITAL_NAME']).add_to(_map)
    _map.save('templates/all_beds.html')

def get_beds_utilization_rate():
    df = get_df()
    _map = Map(location=[41.8781, -87.6298], tiles='cartodbpositron', zoom_start=10)
    for i in range(0,len(df)):
        Circle(
            location=[df.iloc[i]['Y'], df.iloc[i]['X']],
            radius=10000,
            fill=True,
            color=color(df.iloc[i]['BED_UTILIZATION'])).add_to(_map)
    _map.save('templates/bed_utilization_rate.html')

def color(val):
    if val >= 0.7:
        return 'forestgreen'
    elif val >= 0.4:
        return 'blue'
    else:
        return 'darkred'

def get_df():
    df = pd.read_csv('usa-hospital-beds.csv')
    return df.dropna()
