from flask import render_template, Flask, request
import jsonify
import requests
import pickle as pkl
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)
model = pkl.load(open("model.pkl", "rb"))


@app.route("/", methods=["GET"])
def HOME():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if request.method == 'POST':
        LandAverageTemperature = float(request.form['LandAverageTemperature'])
        LandMaxTemperature = float(request.form['LandMaxTemperature'])
        LandMinTemperature = int(request.form['LandMinTemperature'])

        prediction = model.predict(
            [[LandAverageTemperature, LandMaxTemperature, LandMinTemperature]])
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text="The Golbal Temperature is {} °C".format(output))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
