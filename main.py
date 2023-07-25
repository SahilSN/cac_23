from flask import Flask, render_template, request, jsonify
import pandas as pd
import sys
print(sys.version)
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    r='test'
    df = pd.read_csv("csv_data/HomeC.csv", low_memory=False)
    print(df.head(3))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True,threaded=True)