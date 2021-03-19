import time

from flask import Flask
app = Flask(__name__)

messages = [
    {
        'name': "Nick",
        'text': "Hello, world",
        'time': "1616140575.879213"
    },
    {
        'name': "Marry",
        'text': "Hello Nick!, How are you?",
        'time': "1616140578.379213"
    },
    {
        'name': "Nick",
        'text': "Hi Marry, I'm fine, what about you?",
        'time': "1616140581.279213"
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
        'server_time': time.time() #unix_time_stamp
    }


@app.route("/get/msgs")
def get_msgs():
    return {
        'msgs': messages
    }

app.run()
