from flask import Flask, render_template, request, jsonify
import pandas as pd
import sys
from cac_code import app
print('BAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh')
@app.route("/",methods=['GET','POST'])
def index():
    print('indexxx')
    return render_template("index.html")

@app.route("/optimization",methods=['GET','POST'])
def optimization():
    print('optimiiization')
    return render_template("optimization.html")
