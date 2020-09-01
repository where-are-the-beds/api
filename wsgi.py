from flask import Flask, render_template
import csv
import os.path

from s3 import list_bucket, download_file
from mapper import get_beds, get_beds_utilization_rate

app = Flask(__name__)

@app.route('/')
def health():
    return '', 200

@app.route('/test')
def list_beds():
    result = list_bucket()
    return dict(buckets=result)

@app.route('/beds')
def beds():
    CSV_PATH = './usa-hospital-beds.csv'
    if not os.path.exists(CSV_PATH):
        download_file()
    get_beds()
    return render_template('all_beds.html') 

@app.route('/beds-utilization-rate')
def beds_utilization_rate():
    CSV_PATH = './usa-hospital-beds.csv'
    if not os.path.exists(CSV_PATH):
        download_file()
    get_beds_utilization_rate()
    return render_template('bed_utilization_rate.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
