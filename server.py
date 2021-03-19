import time

from flask import Flask, request

app = Flask(__name__)

messages = [
    {
        'name': "Nick",
        'text': "Hello, world",
        'time': 1616140575.879213
    },
    {
        'name': "Marry",
        'text': "Hello Nick!, How are you?",
        'time': 1616140578.379213
    },
    {
        'name': "Nick",
        'text': "Hi Marry, I'm fine, what about you?",
        'time': 1616140581.279213
    }
]


@app.route("/")
def main_Page():
    return "Hello World! from Flask by python"


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

    msg_filtered = []
    for msg in messages:
        if msg['time'] > after:
            msg_filtered.append(msg)
    return {
        'msgs': msg_filtered
    }


@app.route("/send/msg", methods=['POST'])
def send_msg():
    data = request.json
    name = data.get('name')
    text = data.get('text')

    msg = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    messages.append(msg)

    return {
        'code': 200,
        'payload': msg['time'],
        'error': ''
    }


app.run()
