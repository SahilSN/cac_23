from flask import Flask, render_template, request, jsonify
import pandas as pd
import sys


from charts import line,pie

from datetime import datetime, timedelta

from app import app

print('BAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh')
@app.route("/",methods=['GET','POST'])
@app.route("/dashboard",methods=['GET','POST'])
def index():

    

    print('indexxx')
    return render_template("index.html", graph = line,pie=pie)

@app.route("/optimization",methods=['GET','POST'])
def optimization():
    print('optimiiizion')
    return render_template("optimization.html")

@app.route("/landing")
def landing():
    print('landing')
    return render_template("landing.html")