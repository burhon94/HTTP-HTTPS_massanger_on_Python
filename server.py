from flask import Flask
app = Flask(__name__)

massages = [
    {
        'name': "Nick",
        'text': "Hello, world",
        'time': "19/Mar 12:07:25"
    },
    {
        'name': "Marry",
        'text': "Hello Nick!, How are you?",
        'time': "19/Mar 12:07:29"
    },
    {
        'name': "Nick",
        'text': "Hi Marry, I'm fine, what about you?",
        'time': "19/Mar 12:08:07"
    }
]


@app.route("/")
def main_Page():
    return "Hello World! from Flask by python"


app.run()
