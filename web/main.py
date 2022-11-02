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
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    else:
        # 모델링 값 결과 == tomato
    return render_template("search.html")

app.run(debug=True)