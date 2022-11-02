from crypt import methods
from re import S
from flask import Flask, render_template, request, redirect, send_file
import sqlite3
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/search')
def search():
    sun = request.args.get("sun")
    temp = request.args.get("temperature")
    humid = request.args.get("humidity")
    carbon = request.args.get("CO2")
    land_moist = request.args.get("land_moist")
    if sun == None:
        return redirect("/")
    elif temp == None:
        return redirect("/")
    elif humid == None:
        return redirect("/")
    elif carbon == None:
        return redirect("/")
    elif land_moist == None:
        return redirect("/")
    else:
        
    return render_template("search.html")

app.run(debug=True)