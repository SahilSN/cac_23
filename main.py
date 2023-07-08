from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    r='test'
    df = pd.read_csv("HomeC.csv", low_memory=False)
    print(df.head(3))
    return render_template("index.html",r=df.head(3))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)