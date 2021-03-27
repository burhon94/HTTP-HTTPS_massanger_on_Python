import time
from db import requests

from flask import Flask, request

app = Flask(__name__)
requests.initDB()


@app.route("/")
def main_Page():
    return "<h1>Hello World! from Python by Heroku</h1>"


@app.route("/status")
def status():
    return {
        'status': True,
        'app': "Messenger",
        'server_time': time.time()  # unix_time_stamp
    }


@app.route("/get/msgs", methods=["GET"])
def get_msgs():
    try:
        after = float(request.args['after'])
    except:
        return {
            'code': 400,
            'payload': '',
            'error': 'after not undefined'
        }

    resp = requests.get_msgs(after)
    return resp


@app.route("/send/msg", methods=['POST'])
def send_msg():
    data = request.json
    name = data.get('name')
    text = data.get('text')
    tm = time.time()

    resp = requests.send_msg(name, text, tm)
    return resp


app.run()
