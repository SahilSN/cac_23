from flask import Flask, render_template, request, jsonify
import pandas as pd
import sys
from cac_code import app

from cac_code.charts_class import generate_line

from datetime import datetime, timedelta

print('BAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh')
@app.route("/",methods=['GET','POST'])
@app.route("/dashboard",methods=['GET','POST'])
def index():
    # Loads Relevant CSV Files
    battery_data_df = pd.read_csv("cac_code/csv_data/battery_data.csv")
    gen_sol_df = pd.read_csv("cac_code/csv_data/gen_sol.csv")
    use_HO_df = pd.read_csv("cac_code/csv_data/use_HO.csv")
    future_data_df = pd.read_csv("cac_code/csv_data/future_data.csv")

    # Get relevant timestamps
    dt_now = datetime.now()
    before_12_hr = (dt_now - timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S")
    next_12_hr = (dt_now + timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S")
    now = dt_now.strftime("%Y-%m-%d %H:%M:%S")

    # Creates Main Line Graph
    ### Takes generated solar energy, consumption, and battery level
    main_line_df = gen_sol_df[["time", "gen_Sol"]]
    main_line_df["use_HO"] = use_HO_df["use_HO"]
    main_line_df["battery"] = battery_data_df["battery"].astype("float64")

    ### Filters results to past 12 hours
    mask = (gen_sol_df['time'] >= before_12_hr) & (gen_sol_df['time'] <= now)
    main_line_filter_df = main_line_df.loc[mask]
    
    ### Generates line graph with the parameters
    line = generate_line(main_line_filter_df, 0, 1, None, "Battery")

    print('indexxx')
    return render_template("index.html", graph = line)

@app.route("/optimization",methods=['GET','POST'])
def optimization():
    print('optimiiizion')
    return render_template("optimization.html")
