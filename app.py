from flask import Flask, jsonify, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clean')
def clean():
    return render_template('clean.html')

@app.route('/ml')
def ml():
    return render_template('ml.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/graphs')
def graphs():
    return render_template('graphs.html')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == "__main__":
    app.run(debug=True)