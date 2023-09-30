from flask import Flask, render_template, request, jsonify
import pandas as pd
import sys


from cac_code.charts import line

from datetime import datetime, timedelta

from cac_code import app

print('BAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh')
@app.route("/",methods=['GET','POST'])
@app.route("/dashboard",methods=['GET','POST'])
def index():

    #d={
    #'appliance':['dishwasher','kitchen', 'toilet'],
    #'values':[1,3,4]
    #}
    #df=pd.DataFrame(data=d)
    #pie=generate_pie(df,'test')

    print('indexxx')
    return render_template("index.html", graph = line)#,pie=pie)

@app.route("/optimization",methods=['GET','POST'])
def optimization():
    print('optimiiizion')
    return render_template("optimization.html")

@app.route("/landing")
def landing():
    print('landing')
    return render_template("landing.html")