from flask import Flask, render_template, request, jsonify
import pandas as pd
import sys

from stats import total_generated, total_consumed, battery_left,generation_efficiency,hour_avg
from charts import main_line,pie, cons_over_time, corr_heatmap, rec_list

from datetime import datetime, timedelta

from app import app

print('BAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh')
@app.route("/",methods=['GET','POST'])
@app.route("/dashboard",methods=['GET','POST'])
def index():
    print('finished running on '+datetime.now().strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00')
    

    print('indexxx')
    return render_template("index.html", 
                           graph = main_line, pie=pie, tg=total_generated, tc=total_consumed,
                           bl=battery_left, ge=generation_efficiency, ha=hour_avg, heatmap=corr_heatmap     
                           )

@app.route("/optimization",methods=['GET','POST'])
def optimization():

    print('optimiiizion')


    return render_template("optimization.html",pie=pie,rec_list=rec_list,
                            line=cons_over_time)

@app.route("/landing")
def landing():
    print('landing')
    return render_template("landing.html")