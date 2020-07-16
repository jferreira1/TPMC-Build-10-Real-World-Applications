from flask import Flask, render_template

app = Flask(__name__)

@app.route('/plot/')
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime(2020,5,28)
    df = data.DataReader(name="AMZN", data_source="yahoo", start=start, end=end)

    def good_bad_day(open, close):
        if open > close:
            value = "Decrease"
        elif open < close:
            value = "Increase"
        else:
            value = "Equal"
        return value

    df["Status"] = [good_bad_day(open, close) for open, close in zip(df.Open, df.Close)]
    df["Middle"] = (df.Open + df.Close)/2
    df["Height"] = abs(df.Open - df.Close)

    p = figure(x_axis_type='datetime', width=1000, height=300, sizing_mode='scale_width')
    p.title.text = "Candlestick Chart"

    hours_12 = 12*60*60*1000
    p.segment(x0=df.index, y0=df.High, x1=df.index, y1=df.Low, line_color="#f4a582", line_width=3)
    p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12, df.Height[df.Status == "Increase"],
     fill_color = "#229954", line_color = "black")
    p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours_12, df.Height[df.Status == "Decrease"],
     fill_color = "#E53935", line_color = "black")

    script1, div1 = components(p)
    cdn_js = CDN.js_files[0]
    return render_template("plot.html", script1=script1, div1=div1, cdn_js=cdn_js)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)