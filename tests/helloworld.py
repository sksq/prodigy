from flask import Flask, render_template, jsonify
import csv

app = Flask(__name__)
from flask import render_template
@app.route("/")
def hello():
    return render_template('mouseover.html')


def get_data():
    with open('static/data', 'r') as content_file:
        data = content_file.read()
    RESULTS = []
    for line in csv.DictReader(data.splitlines(), skipinitialspace=True):
        RESULTS.append({
            'date': line['date'],
            'close': line['close'],
                    })
    return RESULTS

@app.route("/data")
def data():
    return jsonify(get_data())

if __name__ == "__main__":
    app.run()
