from flask import Flask, jsonify, request, redirect, url_for, render_template
import numpy as np
from sqlalchemy import create_engine, func
import secrets
import os
import pickle
from sklearn.ensemble import RandomForestClassifier

from flask_sqlalchemy import SQLAlchemy

conn = "postgresql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)
# conn = os.environ.get('DATABASE_URL')
db = create_engine(conn)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)


class pb_dens_1910_2018(db.Model):
    record = db.Column(db.Integer, primary_key=True)
    denid = db.Column(db.Integer)
    spring_year = db.Column(db.Integer)
    data_source = db.Column(db.String(255))
    discovery_method = db.Column(db.String(255))
    latitude = db.Column(db.String(255))
    longitude = db.Column(db.String(255))
    confirmation = db.Column(db.String(255))
    substrate = db.Column(db.String(255))
    position_method = db.Column(db.String(255))
    horizontal_error_m= db.Column(db.String(255))

class pb_1985_2016(db.Model):
    bearid_rsf = db.Column(db.Integer, primary_key=True)
    datetimeutc_rsf = db.Column(db.String(255))
    latitude_rsf = db.Column(db.String(255))
    longitude_rsf = db.Column(db.String(255))
    season = db.Column(db.String(255))
    period = db.Column(db.String(255))
    lc94_rsf = db.Column(db.String(255))
    eainterval_rsf = db.Column(db.String(255))

class pb_2009_2016(db.Model):
    bear_id = db.Column(db.String(255), primary_key=True)
    gmtdate = db.Column(db.String(255))
    gmttime = db.Column(db.String(255))
    long = db.Column(db.String(255))
    lat = db.Column(db.String(255))
    raw_act = db.Column(db.String(255))
    standard_act = db.Column(db.String(255))
    active_den = db.Column(db.String(255))
    habitat = db.Column(db.String(255))

class climate_compile(db.Model):
    year_month = db.Column(db.String(255), primary_key=True)
    land_avg_temp = db.Column(db.String(255))
    land_max_temp = db.Column(db.String(255))
    land_min_temp = db.Column(db.String(255))
    land_ocean_avg_temp = db.Column(db.String(255))
    north_min_temp_anomoly = db.Column(db.String(255))
    north_max_temp_anomoly = db.Column(db.String(255))
    north_mean_temp_anomoly = db.Column(db.String(255))
    global_avg_co2 = db.Column(db.String(255))
    seaice_extent = db.Column(db.String(255))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/machine_learning')
def machine_learning():
    return render_template('machine_learning.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')

@app.route('/result')
def result():
    return render_template('results.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/api/climate')
def climate():
    results = db.session.query().with_entities(climate_compile.year_month,climate_compile.land_avg_temp,climate_compile.land_max_temp,\
    climate_compile.land_min_temp,climate_compile.land_ocean_avg_temp,climate_compile.north_min_temp_anomoly,climate_compile.north_max_temp_anomoly,\
        climate_compile.north_mean_temp_anomoly,climate_compile.global_avg_co2,climate_compile.seaice_extent).limit(10)  
    aggrArray = []

    for year_month,land_avg_temp,land_max_temp,land_min_temp,land_ocean_avg_temp,north_min_temp_anomoly,north_max_temp_anomoly,north_mean_temp_anomoly,global_avg_co2,seaice_extent in results:
        aggrObj = {}
        aggrObj['Year_Month'] = year_month
        aggrObj['Land_Avg_Temp'] = land_avg_temp
        aggrObj['Land_Max_Temp'] = land_max_temp
        aggrObj['Land_Min_Temp'] = land_min_temp
        aggrObj['Land_Ocean_Avg_Temp'] = land_ocean_avg_temp
        aggrObj['North_Min_Temp_Anomoly'] = north_min_temp_anomoly
        aggrObj['North_Max_Temp_Anomoly'] = north_max_temp_anomoly
        aggrObj['North_Mean_Temp_Anomoly'] = north_mean_temp_anomoly
        aggrObj['Global_Avg_Co2'] = global_avg_co2
        aggrObj['SeaIce'] = seaice_extent

        aggrArray.append(aggrObj)

    return {'results': aggrArray} 

@app.route('/api/bears_2009_2016')
def bears_2009_2016():
    results = db.session.query().with_entities(pb_2009_2016.bear_id,pb_2009_2016.gmtdate,pb_2009_2016.gmttime,\
    pb_2009_2016.long,pb_2009_2016.lat,pb_2009_2016.raw_act,pb_2009_2016.standard_act,\
        pb_2009_2016.active_den,pb_2009_2016.habitat).limit(10)  
    aggrArray = []

    for bear_id,gmtdate,gmttime,long,lat,raw_act,standard_act,active_den,habitat in results:
        aggrObj = {}
        aggrObj['BearId'] = bear_id
        aggrObj['GmtDate'] = gmtdate
        aggrObj['GmtTime'] = gmttime
        aggrObj['longitude'] = long
        aggrObj['latitude'] = lat
        aggrObj['Raw_Act'] = raw_act
        aggrObj['Standard_act'] = standard_act
        aggrObj['Active_Den'] = active_den
        aggrObj['Habitat'] = habitat

        aggrArray.append(aggrObj)

    return {'results': aggrArray} 

@app.route('/api/bears_1985_2016')
def bears_1985_2016():
    results = db.session.query().with_entities(pb_1985_2016.bearid_rsf,pb_1985_2016.datetimeutc_rsf,pb_1985_2016.latitude_rsf,\
    pb_1985_2016.longitude_rsf,pb_1985_2016.season,pb_1985_2016.period,pb_1985_2016.lc94_rsf,\
        pb_1985_2016.eainterval_rsf).limit(10)  
    aggrArray = []

    for bearid_rsf,datetimeutc_rsf,latitude_rsf,longitude_rsf,season,period,lc94_rsf,eainterval_rsf in results:
        aggrObj = {}
        aggrObj['BearID_rsf'] = bearid_rsf
        aggrObj['DateTimeUTC_rsf'] = datetimeutc_rsf
        aggrObj['latitude_rsf'] = latitude_rsf
        aggrObj['longitude_rsf'] = longitude_rsf
        aggrObj['season'] = season
        aggrObj['period'] = period
        aggrObj['lc94_rsf'] = lc94_rsf
        aggrObj['eaInterval_rsf'] = eainterval_rsf

        aggrArray.append(aggrObj)

    return {'results': aggrArray}   

@app.route('/api/dens')
def dens():
    results = db.session.query().with_entities(pb_dens_1910_2018.record,pb_dens_1910_2018.denid,pb_dens_1910_2018.spring_year,\
    pb_dens_1910_2018.data_source,pb_dens_1910_2018.discovery_method,pb_dens_1910_2018.latitude,pb_dens_1910_2018.longitude,\
        pb_dens_1910_2018.confirmation,pb_dens_1910_2018.substrate,pb_dens_1910_2018.position_method,pb_dens_1910_2018.horizontal_error_m).limit(10)        
    aggrArray = []

    for record,denid,spring_year,data_source,discovery_method,latitude,longitude,confirmation,substrate,position_method,horizontal_error_m in results:
        aggrObj = {}
        aggrObj['record'] = record
        aggrObj['spring_year'] = spring_year
        aggrObj['data_source'] = data_source
        aggrObj['discovery_method'] = discovery_method
        aggrObj['latitude'] = latitude
        aggrObj['longitude'] = longitude
        aggrObj['confirmation'] = confirmation
        aggrObj['substrate'] = substrate
        aggrObj['position_method'] = position_method
        aggrObj['horizontal_error'] = horizontal_error_m

        aggrArray.append(aggrObj)

    return {'results': aggrArray}

@app.route('/predict', methods=['POST'])
def predict():
    print("AM I WORKING")
    habitat_model = pickle.load(open("machine_learning/models/rf_rsf2.pkl","rb"))
    mobility_model = pickle.load(open("machine_learning/models/knn_mob.pkl","rb"))
    dens_model = pickle.load(open("machine_learning/models/rf_loc.pkl","rb"))

    temp = round(float(request.form['tempRange'])*19+1)
    ocean = round(float(request.form['oceanRange'])*200+300)
    co2 = round(float(request.form['co2Range'])*19+1) 
    ice = round(float(request.form['iceRange'])*19+1)

    
    final_features = [np.array([float(request.form['tempRange']),float(request.form['oceanRange']),float(request.form['co2Range']), float(request.form['iceRange'])])]
    habitat = habitat_model.predict(final_features)
    mobility = mobility_model.predict(final_features)
    dens = dens_model.predict(final_features)

    if int(habitat[0])== 3:
        habitat_output= "Living My Best Life"
    elif int(habitat[0])== 2:
        habitat_output= "Just Maintaining"
    else:
        habitat_output= "The Struggle is Real"

    if str(mobility[0])== "high":
        mobility_output= "Super Mover"
    elif str(mobility[0])== "mid":
        mobility_output= "I Get Around..."
    else:
        mobility_output= "Home Body"


    dens_output = f"Zone {int(dens[0])}"


    return render_template('results.html', habitat_output=habitat_output,mobility_output=mobility_output,dens_output=dens_output, temp=temp, ocean=ocean,co2=co2,ice=ice)


    

if __name__ == "__main__":
    app.run(debug=True)