from flask import Flask, render_template, jsonify, request
from pandas_datareader import data
import datetime
import json
from flask_cors import CORS
# from bokeh.plotting import figure, show, output_file
# from bokeh.embed import components
# from bokeh.resources import CDN

app=Flask(__name__)

# FIXME: make below changes only for dev environments
CORS(app)
# cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

@app.route('/')
def home():
    
    # defaults :: these shall not be used
    start = datetime.datetime(2020, 11, 1)
    end = datetime.datetime(2021, 3, 10)
    symbol = "MSFT"

    if(request.args.get('sm') is not None):
        symbol =  request.args.get('sm')
        sdd = request.args.get('sdd')
        smm = request.args.get('smm')
        syr = request.args.get('syr')
        edd = request.args.get('edd')
        emm = request.args.get('emm')
        eyr = request.args.get('eyr')

        start = datetime.datetime(year=int(syr), month=int(smm), day=int(sdd))
        end = datetime.datetime(year=int(eyr), month=int(emm), day=int(edd))
    df = data.DataReader(name=symbol, data_source="yahoo", start=start, end=end)
    df = df[['Open','Close','Low','High','Volume', 'Adj Close']]

    # df.select_dtypes(include='datetime').apply(lambda x: x.strftime("%d-%b-%y"))
    return json.loads(df.to_json(orient="split"))

    # p = figure(x_axis_type='datetime', width=1000, height=300, sizing_mode='scale_both')
    # p.title.text = "Candlestick Chart"
    # p.grid.grid_line_alpha = 0.4
    # hours_12 = 12 * 60 * 60 * 1000

    # def inc_dec(c, o):
    #     if c > o:
    #         value = "Increase"
    #     elif c < o:
    #         value = "Decrease"
    #     else:
    #         value = "Equal"
    #     return value

    # df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
    # df["Middle"] = (df.Open + df.Close) / 2
    # # abs always return a positive value
    # df["Height"] = abs(df.Open - df.Close)

    # # date_increase = df.index[df.Close > df.Open]
    # # date_decrease = df.index[df.Close < df.Open]

    # # Lines
    # p.segment(df.index, df.High, df.index, df.Low, color="black")

    # # Rectangles
    # p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12,
    #        df.Height[df.Status == "Increase"], fill_color="#CCFFFF", line_color="black")

    # p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours_12,
    #        df.Height[df.Status == "Decrease"], fill_color="#FF3333", line_color="black")

    # # Script will be index 0 and div1 will be index 1
    # script1, div1 = components(p)

    # # On our HTML we have to add as well the css and js file of bokeh
    # # use index 0 for both of them
    # cdn_js = CDN.js_files
    # cdn_css = CDN.css_files

    # return render_template("home.html", script1=script1, div1=div1, cdn_css=cdn_css[0], cdn_js=cdn_js[0])

if __name__=="__main__":
    app.run(debug=True)
