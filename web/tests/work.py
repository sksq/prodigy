from flask import Flask, render_template, jsonify, request
import csv
import json
import datetime
app = Flask(__name__)
from flask import render_template
@app.route("/")
def hello():
    return render_template('graphmult.html')

@app.route("/gp")
def gp():
    return render_template('graph.html')
@app.route("/bt")
def bt():
    return render_template('beautigraph.html')

@app.route("/bt1")
def bt1():
    return render_template('beautigraph1.html')

@app.route('/showText')
def showText():
    dt=request.args.get('stringData')
    return jsonify(dt.split(' -- '))


def mapfunct(x):
    x.timestamp=datetime.datetime.strptime(x.timestamp,"%Y-%m-%d %H:%M:%S")
    return x
def get_data():
    with open('static/data2', 'r') as content_file:
        data = content_file.read()
    data = json.loads(data)
    for key1, value1 in data.items():
        for key2,value2 in value1.items():
            map(mapfunct, value2)

    for key1, value1 in data.items():
        for key2,value2 in value1.items():
            value2.sort(key=lambda x: x["timestamp"])

    return data

    # RESULTS = []
    # for line in csv.DictReader(data.splitlines(), skipinitialspace=True):
    #     RESULTS.append({
    #         'date': line['date'],
    #         'close': line['close'],
    #                 })
    # return RESULTS

@app.route("/data")
def data():
    grpby=request.args.get('grpby')
    print(grpby)
    return jsonify(get_data())

if __name__ == "__main__":
    app.run()
