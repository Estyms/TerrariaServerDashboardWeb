import dotenv
from flask import Flask, render_template
import requests
import json


#Server IP
SERVER_IP = dotenv.get_key(".env","SERVER_IP")

app = Flask(__name__, static_folder="templates/static", static_url_path="/static")

@app.route("/")
def hello():
    players = json.loads(requests.get("http://"+SERVER_IP+"/players").content)
    world = json.loads(requests.get("http://"+SERVER_IP+"/world").content)
    uptime = json.loads(requests.get("http://"+SERVER_IP+"/uptime").content)
    mods = json.loads(requests.get("http://"+SERVER_IP+"/mods").content)
    print(uptime)

    return render_template("index.html", world=world, players=players, uptime=uptime, mods=mods)

app.run(debug=True)


