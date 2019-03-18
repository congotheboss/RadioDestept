import time
import random
import json
import os
import signal
import subprocess

from thing import PiThing

from flask import *



playproc = ""
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html') #prima pagina


@app.route("/radio")
def radio():
    return render_template('radio.html')  # pagina radio

@app.route("/radio_player")
def radio_player():
    return render_template('radio_player.html')  # pagina radio player
@app.route("/camera")
def camera():
    return render_template('camera.html') #pagina camera
# @app.route("/radio")
# def radio():
#     return render_template("index.html")

# @app.route("/test")
# def test():
#     return render_template('index.html')
    
# @app.route("/kent")
# def kent():
#     return render_template('select.html')




#Comenzi Pentru sistem :

@app.route("/play")
def play():
    station = request.args.get('station') #COMMAND INJECTION!!!!!!!!!
    print("Playing Station")
    os.system("mpc clear")
    os.system("mpc add {}".format(station)) #COMMAND INJECTION!!!!!!!!!
    os.system("mpc play")
    return "Done"

@app.route("/stop")
def stop():
    os.system("mpc stop")
    os.system("mpc clear")
    return "Done"
    
@app.route("/volume")
def volume():
    vol = request.args.get('volume')
    os.system("mpc volume {}".format(vol))
    return "Done"


# Server-sent event endpoint that streams the thing state every second.


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
