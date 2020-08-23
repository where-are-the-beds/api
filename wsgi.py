from flask import Flask, request

app = Flask(__name__)

@app.route('/beds')
def beds():
    return dict(beds=[])