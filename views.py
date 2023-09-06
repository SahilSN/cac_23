from flask import Flask, render_template, request, jsonify
import pandas as pd
import sys


print(sys.version)
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
@app.route("/dashboard",methods=['GET','POST'])
def index():
    print('indexxx')
    return render_template("index.html")

@app.route("/optimization",methods=['GET','POST'])
def optimization():
    print('optimiiization')
    return render_template("optimization.html")
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)