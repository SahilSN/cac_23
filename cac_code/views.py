from flask import Flask, render_template, request, jsonify
import pandas as pd
import sys

#from stats import total_generated, total_consumed, battery_left,generation_efficiency,hour_avg
from stats import est_energy_savings,est_co2e_savings,est_car_miles,est_plane_miles,est_trees
from charts import compare_bar
#from charts import main_line,pie,pie_statement_list, optimization_line, corr_heatmap
from datetime import datetime, timedelta

from app import app

print('BAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh')
@app.route("/",methods=['GET','POST'])
@app.route("/dashboard",methods=['GET','POST'])
def index():

    

    print('indexxx')
    return render_template("index.html")
    # return render_template("index.html", 
    #                        graph = main_line, pie=pie, tg=total_generated, tc=total_consumed,
    #                        bl=battery_left, ge=generation_efficiency, ha=hour_avg, heatmap=corr_heatmap     
    #                        )

@app.route("/optimization",methods=['GET','POST'])
def optimization():

    print('optimiiizion')
    return render_template("optimization.html")
    # return render_template("optimization.html",pie=pie,pie_list=pie_statement_list,
    #                         line=optimization_line)

@app.route("/landing")
def landing():
    print('landing')
    return render_template("landing.html")

@app.route("/stats")
def stats():
    est_energy_savings,est_co2e_savings,est_car_miles,est_plane_miles,est_trees
    print("STATS COMPARISON")
    return render_template("comparison.html",compare_bar=compare_bar, est_energy_savings=est_energy_savings,
                           est_co2e_savings=est_co2e_savings,est_car_miles=est_car_miles,est_plane_miles=est_plane_miles,
                           est_trees=est_trees)