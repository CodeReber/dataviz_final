from flask import Flask, jsonify, request, redirect, url_for, render_template
import numpy as np
import pickle
from sqlalchemy import create_engine, func
import secrets

from flask_sqlalchemy import SQLAlchemy

conn = "postgresql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)
db = create_engine(conn)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)
model = pickle.load(open('model.pkl', 'rb'))

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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cleaning')
def cleaning():
    return render_template('cleaning.html')

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
    return render_template('result.html')

@app.route('/api/dens')
def dens():
    results = db.session.query().with_entities(pb_dens_1910_2018.record,pb_dens_1910_2018.denid,pb_dens_1910_2018.spring_year,\
    pb_dens_1910_2018.data_source,pb_dens_1910_2018.discovery_method,pb_dens_1910_2018.latitude,pb_dens_1910_2018.longitude,\
        pb_dens_1910_2018.confirmation,pb_dens_1910_2018.substrate,pb_dens_1910_2018.position_method,pb_dens_1910_2018.horizontal_error_m)        
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

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features) #this is connected to model.pkl

    output = round(prediction[0], 2)

    return render_template('results.html', prediction_text='CO2 Emission of the vehicle is :{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)