from flask import Flask, render_template, request
import pickle
import joblib
import numpy as np
app = Flask(__name__)

model = pickle.load(open("placement.pkl", 'rb'))
ct = joblib.load('placement.pkl')


@app.route('/')
def hello():
    return render_template("Index.html")

@app.route('/index1')
def hello1():
    return render_template("Index1.html")

@app.route('/guest', methods=["POST"])
def guest():
    sen1 = request.form["sen1"]
    sen2 = request.form["sen2"]
    sen3 = request.form["sen3"]
    sen4 = request.form["sen4"]
    sen5 = request.form["sen5"]
    sen6 = request.form["sen6"]

    # Your code for processing the user inputs goes here

@app.route('/y_predict', methods=["POST"])
def y_predict():
    x_test = [[(yo) for yo in request.form.values()]]
    x_test = np.array(x_test).astype(float)

    prediction = model.predict(x_test)

    prediction = prediction[0]

    return render_template("secondpage.html", y=prediction)

if __name__== "__main__":
    app.run(debug=True)


























# from flask import Flask, render_template, request
# import pickle
# import joblib

# app = Flask(__name__)

# model = pickle.load(open("placement.pkl", 'rb'))
# ct = joblib.load('placement.pkl')


# @app.route('/')
# def hello():
#     return render_template("index.html")

# @app.route('/guest', methods=["POST"])
# def guest():
#     sen1 = request.form["sen1"]
#     sen2 = request.form["sen2"]
#     sen3 = request.form["sen3"]
#     sen4 = request.form["sen4"]
#     sen5 = request.form["sen5"]
#     sen6 = request.form["sen6"]

#     # Process the user inputs
#     # For example, you can convert the user inputs to numerical values
#     # and scale them using a pre-trained scaler object like ct

#     # Convert the user inputs to a list of numerical values
#     x = [float(sen1), float(sen2), float(sen3), float(sen4), float(sen5), float(sen6)]

#     # Scale the numerical values using the pre-trained scaler object ct
#     x_scaled = ct.transform([x])

#     # Pass the processed user inputs to the model for prediction
#     prediction = model.predict(x_scaled)

#     # Convert the prediction to a string for display
#     prediction = str(prediction[0])

#     # Return the prediction to the user
#     return render_template("secondpage.html", y=prediction)


# if __name__ == "__main__":
#     app.run(debug=True)
