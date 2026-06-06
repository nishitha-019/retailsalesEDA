from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv("sales_data.csv")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/dataset')
def dataset():
    data = df.to_html(classes="table", index=False)
    return render_template("dataset.html", tables=data)

@app.route('/summary')
def summary():
    summary_data = df.describe().to_html(classes="table")
    return render_template("summary.html", summary=summary_data)

@app.route('/correlation')
def correlation():
    corr = df.corr(numeric_only=True).to_html(classes="table")
    return render_template("correlation.html", corr=corr)

if __name__ == "__main__":
    app.run(debug=True)