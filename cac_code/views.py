from flask import Flask, render_template, request, jsonify
import pandas as pd
import sys
from cac_code import app

import plotly
import plotly.express as px
import plotly.graph_objs as go

from datetime import datetime, timedelta

def generate_scatter(df):
    plotly_fig = go.Figure(data=go.Scatter(x=df["data"], y=df["totale_positivi"], mode="markers"))
    div = plotly.offline.plot(plotly_fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return div

def generate_line(df, x_col, y_col_s, y_col_e, title):
    if (y_col_e == None):
        print("no end")
        print(df.columns[y_col_s:])
        plotly_fig = px.line(df, x=df.columns[x_col], y=df.columns[y_col_s:], title=title, )
    else:
        print("end")
        print(df.columns[y_col_s:y_col_e])
        plotly_fig = px.line(df, x=df.columns[x_col], y=df.columns[y_col_s:y_col_e], title=title,)
    div = plotly.offline.plot(plotly_fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return div

print('BAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh')
@app.route("/",methods=['GET','POST'])
@app.route("/dashboard",methods=['GET','POST'])
def index():
    # Loads Relevant CSV Files
    battery_data_df = pd.read_csv("cac_code/csv_data/battery_data.csv")
    gen_sol_df = pd.read_csv("cac_code/csv_data/gen_sol.csv")
    # HomeC_df = pd.read_csv("cac_code/csv_data/HomeC.csv").head(10)
    # HomeC_df["time_convert"] = pd.to_datetime(HomeC_df["time"])
    # HomeC_df["time_convert"] = HomeC_df["time_convert"]+pd.Timedelta(days=53*365+13)
    # incremented_use_df = pd.read_csv("cac_code/csv_data/incremented_use.csv")
    use_HO_df = pd.read_csv("cac_code/csv_data/use_HO.csv")

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

    print(main_line_filter_df)
    
    ### Generates line graph with the parameters
    line = generate_line(main_line_filter_df, 0, -3, None, "apple")

    print('indexxx')
    return render_template("index.html", graph = line)

@app.route("/optimization",methods=['GET','POST'])
def optimization():
    print('optimiiizion')
    return render_template("optimization.html")
