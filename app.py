from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('xb_model.pkl', 'rb'))

<<<<<<< HEAD

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=["GET"])
def getForm():
    return render_template("predict.html")


=======
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

>>>>>>> 889aac468263d589ce4e29b64360d624d3cf5173
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Carat = float(request.form['Carat'])
<<<<<<< HEAD
        Cut = int(request.form['Cut'])
        Color = int(request.form['Color'])
        Clarity = int(request.form['Clarity'])
        Depth = float(request.form['Depth'])
        Table = float(request.form['Table'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        z = float(request.form['z'])

        prediction = model.predict(pd.DataFrame({'carat': [Carat], 'cut': [Cut], 'color': [Color],
                                                 'clarity': [Clarity], 'depth': [Depth],
                                                 'table': [Table], 'x': [x],
                                                 'y': [y], 'z': [z]}))

        if prediction < 0:
            return render_template('result.html', prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('result.html', prediction_text="{:.3f}".format(prediction[0]))
    else:
        return render_template('index.html')


if __name__ == "__main__":
=======
        Cut=int(request.form['Cut'])
        Color=int(request.form['Color'])
        Clarity=int(request.form['Clarity'])
        Depth=float(request.form['Depth'])
        Table=float(request.form['Table'])
        x=float(request.form['x'])
        y=float(request.form['y'])
        z=float(request.form['z'])

        prediction=model.predict(pd.DataFrame({'carat':[Carat], 'cut':[Cut], 'color':[Color],
                      'clarity':[Clarity], 'depth':[Depth],
                      'table':[Table], 'x':[x],
                      'y':[y], 'z':[z]}))

        if prediction<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="Price {}".format(prediction))
    else:
        return render_template('index.html')

if __name__=="__main__":
>>>>>>> 889aac468263d589ce4e29b64360d624d3cf5173
    app.run(debug=True)
