from flask import Flask, request
import csv


app = Flask(__name__)

@app.route('/beds')
def beds():
    CSV_PATH = './dataset/usa-hospital-beds.csv'
    output = []
    with open(CSV_PATH) as csvfile:
        reader = csv.DictReader(csvfile)
        output = [item for item in reader]
    return dict(beds=output)