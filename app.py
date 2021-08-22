from flask import Flask,render_template,request
from model import Task
import pandas as pd
app=Flask(__name__)
obj=Task('ai4i2020.csv')
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict/',methods=["POST","GET"])
def predict():
    try:
        return render_template('predict.html')
    except Exception as e:
        return e
@app.route('/response/',methods=["POST","GET"])
def result():
    try:
        if request.method=='POST':
            process_temp=float(request.form['process_t'])
            rotational_s=request.form['rotational_s']
            torque=float(request.form['torque'])
            tool_w=request.form['tool_w']
            machine_f=request.form['machine_f']
            twf=request.form['twf']
            hdf=request.form['hdf']
            pwf=request.form['pwf']
            osf=request.form['osf']
            rnf=request.form['rnf']
            data=[[process_temp,rotational_s,torque,tool_w,machine_f,twf,hdf,pwf,osf,rnf]]
            print(data)
            value=obj.predict(data)
            return f"Your predicted value is {value}."
    except Exception as e:
        return e
@app.route('/test_cases/')
def test_case():
    try:
            # if request.methods=='POST':
            #num=request.form['number']
            result=obj.test_case(number=10)
            return render_template('test_case.html', data=result, rangee=range(len(list(result.values())[0])), columns=result.keys())
    except Exception as e:
        return
@app.route('/visualization/')
def visualize():
    try:
        return render_template('visualize.html')
    except Exception as e:
        return e
if __name__=='__main__':
    app.run(debug=True)