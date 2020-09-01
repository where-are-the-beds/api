import pandas as pd
import geopandas
import matplotlib.pyplot as plt
import folium
from folium import Circle, Marker


def get_beds():
    df = pd.read_csv('usa-hospital-beds.csv')

    m_1 = folium.Map(location=[36.778259, -119.417931], tiles='cartodbpositron', zoom_start=10)

    m_2 = folium.Map(location=[36.778259, -119.417931], tiles='cartodbpositron', zoom_start=10)

    df = df.dropna()

    # Marker -- Find all available beds
    for idx, row in df.iterrows():
        Marker([row['Y'], row['X']], popup=row['HOSPITAL_NAME']).add_to(m_1)

    m_1.save('templates/all_beds.html')
