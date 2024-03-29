from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('rf_random_1.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('index1.html')


@app.route('/predict', methods=['POST','GET'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    data9 = request.form['i']
    data10 = request.form['j']
    data11 = request.form['k']
    arr = np.array([[data1, data2 ,data3, data4 , data5, data6, data7, data8, data9, data10, data11]])
    pred = model.predict(arr)
    if pred == 0 :
        return render_template('home1.html',pred="Sorry we can't Approved your loan.")
    else :
        return render_template('home1.html',pred="We can Approved your loan.")


if __name__ == "__main__":
    app.run(debug = True)















