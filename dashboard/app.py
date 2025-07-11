# Flask dashboard to display data
from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)
@app.route('/')
def index():
    df = pd.read_csv('data_log.csv', names=['Time','Temp','Hum','Gas'])
    return render_template('index.html', tables=[df.tail().to_html(classes='data')])
if __name__ == '__main__':
    app.run(debug=True)