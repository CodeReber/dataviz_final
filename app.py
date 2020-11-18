from flask import Flask, jsonify, request, redirect, url_for, render_template
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('results.html', prediction_text='CO2 Emission of the vehicle is :{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)