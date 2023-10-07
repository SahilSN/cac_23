from flask import Flask, render_template, request, jsonify
import pandas as pd
import sys

from stats import total_generated, total_consumed, battery_left,generation_efficiency,hour_avg
from charts import main_line,pie,pie_statement_list, optimization_line

from datetime import datetime, timedelta

from app import app

print('BAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh')
@app.route("/",methods=['GET','POST'])
@app.route("/dashboard",methods=['GET','POST'])
def index():

    

    print('indexxx')
    return render_template("index.html", 
                           graph = main_line, pie=pie, tg=total_generated, tc=total_consumed,
                           bl=battery_left, ge=generation_efficiency, ha=hour_avg       
                           )

@app.route("/optimization",methods=['GET','POST'])
def optimization():

    print('optimiiizion')


    return render_template("optimization.html",pie=pie,pie_list=pie_statement_list,
                            line=optimization_line)

@app.route("/landing")
def landing():
    print('landing')
    return render_template("landing.html")