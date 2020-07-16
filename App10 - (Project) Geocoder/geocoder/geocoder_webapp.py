from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename
from geocoder_coordinates import csv_coordinates
from geocoder_plot import create_map
import pandas as pd

ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.secret_key = b'\xa8\xe3\x04\x95\xf9)\xe1)\xf3GcG\x99\xd9\x9cB'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/sucess/", methods=["POST"])
def sucess():
    if request.method == "POST":
        if request.form['action'] == 'Submit':

            file = request.files['file_name']
            if file.filename == '':
                return render_template("index.html", text=r'style="color:crimson"')
            
            if not allowed_file(file.filename):
                return render_template("index.html", text2="Selecione um arquivo CSV", text=r'style="color:crimson"')

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save('./geocoder/address.csv')
                df = csv_coordinates('./geocoder/address.csv')
                return render_template("result.html", df=df)
                #return send_file('address_updated.csv', as_attachment=True, attachment_filename='address_updated.csv')
                pass

        elif request.form['action'] == 'Download_Sample':
            return send_file('addresses_sample.csv', as_attachment=True, attachment_filename='addresses.csv')

        elif request.form['action'] == 'Map':
            return redirect(url_for('map'))

        elif request.form['action'] == 'Download_Updated':
            return send_file('addresses_updated.csv', as_attachment=True, attachment_filename='addresses.csv')

    pass

@app.route('/map')
def map():
    if request.method == "POST" or request.method != "POST":
        create_map()
        return render_template('plot.html')



if __name__ == "__main__":
    app.run(debug=True)

    