from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import model


app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':    
        Wheelbase = request.form.get('Wheelbase')
        Car_Length = request.form.get('Car_Length')
        carWidth = request.form.get('carWidth')
        Crubweight = request.form.get('Crubweight')
        fueltype = request.form.get('fueltype')
        enginesize = request.form.get('enginesize')
        Boreratio = request.form.get('Boreratio')
        Horsepower = request.form.get('Horsepower')
        mpg = request.form.get('mpg')
        enginetype = request.form.get('enginetype')
        Fueltype = request.form.get('fueltype')
        CarBody = request.form.get('CarBody')
        aspiration = request.form.get('aspiration')
        cylinderNumber = request.form.get('cylinderNumber')
        DriveWheel = request.form.get('DriveWheel')
        Crubweight = request.form.get('Crubweight')
        arr=[[Wheelbase,Car_Length,carWidth,Crubweight,enginesize,Boreratio,Horsepower,mpg,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        if enginetype=='dohcv':
            arr[0][8]=1
        if enginetype=='L':
            arr[0][9]=1
        if enginetype=='ohc':
            arr[0][10]=1
        if enginetype=='ohcf':
            arr[0][11]=1
        if enginetype=='ohcv':
            arr[0][12]=1
        if enginetype=='rotor':
            arr[0][13]=1 
        if fueltype=='gas':
            arr[0][14]=1
            arr[0][15]=1
        if CarBody=='hardtop':
            arr[0][16]=1
        if CarBody=='hatchback':
            arr[0][17]=1
        if CarBody=='sedan':
            arr[0][18]=1
        if CarBody=='wagon':
            arr[0][19]=1
        if aspiration=='turbo':
            arr[0][20]=1
        if cylinderNumber=='five':
            arr[0][21]=1
        if cylinderNumber=='four':
            arr[0][22]=1
        if cylinderNumber=='six':
            arr[0][23]=1
        if cylinderNumber=='three':
            arr[0][24]=1  
        if cylinderNumber=='twelve':
            arr[0][25]=1
        if cylinderNumber=='two':
            arr[0][26]=1 
        if DriveWheel=='fwd':
            arr[0][27]=1  
        if DriveWheel=='rwd':
            arr[0][28]=1 
          
        
        result=model.lr.predict([arr])
        return render_template("renameindex.html",result=res)

    return render_template("renameindex.html")




# @app.route('/predict',methods=['POST','GET'])

# def predict():
#     int_features=[int(x) for x in request.form.values()]
#     final=[np.array(int_features)]
#     print(int_features)
#     print(final)
#     prediction=model.predict_proba(final)

#     if output>str(0.5):
#         return render_template('index.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output),bhai="kuch karna hain iska ab?")
#     else:
#         return render_template('index.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")


if __name__ == '__main__':
    app.run(debug=True)
