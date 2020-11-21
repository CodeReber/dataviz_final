import pandas as pd
import math
from datetime import datetime as dt
import numpy as np 

df= pd.read_csv("data/polarbears/pB_2009_2016.csv")

df_1=df.drop(columns=["Unnamed: 9","Unnamed: 10","Unnamed: 11"])
df_1['path_id']=""
df_1['distance_to_date']=""
df_1['month'] = pd.DatetimeIndex(df_1['GMTdate']).month

def haversine(lat1,lon1,lat2,lon2):
        
        R=6371000                               # radius of Earth in meters
        phi_1=math.radians(lat1)
        phi_2=math.radians(lat2)

        delta_phi=math.radians(lat2-lat1)
        delta_lambda=math.radians(lon2-lon1)

        a=math.sin(delta_phi/2.0)**2+\
           math.cos(phi_1)*math.cos(phi_2)*\
           math.sin(delta_lambda/2.0)**2
        c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
        
        distance = R*c*0.000621371*5280     #distance in feet from https://nathanrooy.github.io/posts/2016-09-07/haversine-with-python/
        return distance


df_2= df_1

bear ="pb_20132"
lat1= 70.52573552
lon1 = -148.03268880000002
d = 0
i = 1
mon=4
path=1
for index, row in df_2.iterrows():
    print("starting again")
#     months =df_2['month'].unique()
#     mon= months[0]
    if row[0] == bear:
        df_2.loc[index,'path_id'] = path
        path +=1
        if str(row[11]) == str(mon):
            lat2=df_2.loc[index,'lat']
            lon2=df_2.loc[index,'long']
            print(f'index: {index} ,d: {d}, mon: {mon}')
            print(lat1,lon1,lat2,lon2)

            distance = haversine(lat1,lon1,lat2,lon2)
            print(f" have {distance}")
            print(d + distance)
            d = d + distance
            print(f'new distance: {d}')
            df_2.loc[index,'distance_to_date']=d
            lat1=df_2.loc[index,'lat']
            lon1=df_2.loc[index,'long']
            
        if str(row[11]) != str(mon):
            print('second nested if ran')
            mon = row[11]
            d = 0
            lat1=df_2.loc[index,'lat']
            lon1=df_2.loc[index,'long']
            df_2.loc[index,'distance_to_date']=d
            i+=1
    if row[0] != bear:
        print(bear)
        bear = row[0]
        d = 0
        mon= row[11]
        i =1
        print(bear)
        lat1=df_2.loc[index,'lat']
        lon1=df_2.loc[index,'long']
        df_2.loc[index,'distance_to_date']=d
        path = 1
        df_2.loc[index,'path_id'] = path
        path +=1
        print(f'index: {index} ,d: {d}, mon: {mon}')
        
    print(f'index: {index} ,d: {d}, mon: {mon} mon_list: {row[11]}')
    print(bear)
    print(row[0])


df_2.to_csv("haversine_pathids.csv")