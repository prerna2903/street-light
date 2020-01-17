from flask import Flask,render_template,jsonify, request
import pickle
import pandas as pd
import numpy as np
import random
app = Flask(__name__)
@app.route("/")
def index():
  return render_template('index.html')
@app.route("/update_info",methods=['GET','POST'])
def update_info():
  Active = request.form['Active']
  Active1=float(Active)
  Apparent = request.form['Apparent']
  Apparent1=float(Apparent)
  load = request.form['Load']
  load1=float(load)
  data = pickle.load(open('CCSM.pkl','rb'))
  ans = data.predict([[Active1,Apparent1,load1]])
  if ans==0.0:
    return render_template('nonfunctional.html')
  else:
    return render_template('Phase.html')

@app.route("/update",methods=['GET','POST'])
def update():
  r_current = request.form['R_current']
  r_current1=float(r_current)
  r_voltage = request.form['R_voltage']
  r_voltage1=float(r_voltage)

  y_current = request.form['Y_current']
  y_current1=float(y_current)
  y_voltage = request.form['Y_voltage']
  y_voltage1=float(y_voltage)

  b_current = request.form['B_current']
  b_current1=float(b_current)
  b_voltage = request.form['B_voltage']
  b_voltage1=float(b_voltage)

  r = pickle.load(open('rphase.pkl','rb'))
  r_ans = r.predict([[r_current1,r_voltage1]])

  y = pickle.load(open('yphase.pkl','rb'))
  y_ans = y.predict([[y_current1,y_voltage1]])

  b = pickle.load(open('bphase.pkl','rb'))
  b_ans = b.predict([[b_current1,b_voltage1]])
  if r_ans>2.0:
    if y_ans>0.2:
      if b_ans>0.5:
        return render_template('nofault.html')
      else:
        return render_template('bphase.html')
    else:
      if b_ans>0.5:
        return render_template('yphase.html')
      else:
        return render_template('ybphase.html')
  else:
    if y_ans>0.2:
      if b_ans>0.5:
        return render_template('rphase.html')
      else:
        return render_template('rbphase.html')
    else:
      if b_ans>0.5:
        return render_template('ryphase.html')
      else:
        return render_template('fault.html')

@app.route("/rlight")
def rlight():
  l=[]
  list  = [111,222,333]
  n= random.choice(list)
  if n==111:
    df=pd.read_excel(r'C:\Users\lenovo\Desktop\New folder\RPhase_light.xlsx')
  elif n==222:
    df=pd.read_excel(r'C:\Users\lenovo\Desktop\New folder\RPhase_light1.xlsx')
  else:
    df=pd.read_excel(r'C:\Users\lenovo\Desktop\New folder\RPhase_light2.xlsx')
  di={'CONNECTED':1,'DISCONNECTED':0}
  Y=df['Status'].map(di)
  y=np.array(Y)
  for i in range(len(y)):
    if(y[i]==0):
        s=f"lamp {i} is Non working"
        l.append(s)
  return  render_template("rlight.html", len = len(l), l=l)

@app.route("/blight")
def blight():
  l=[]
  list  = [111,222,333]
  n= random.choice(list)
  if n==111:
    df=pd.read_excel(r'C:\Users\lenovo\Desktop\New folder\BPhase_light.xlsx')
  elif n==222:
    df=pd.read_excel(r'C:\Users\lenovo\Desktop\New folder\BPhase_light1.xlsx')
  else:
    df=pd.read_excel(r'C:\Users\lenovo\Desktop\New folder\BPhase_light2.xlsx')
  di={'CONNECTED':1,'DISCONNECTED':0}
  Y=df['Status'].map(di)
  y=np.array(Y)
  for i in range(len(y)):
    if(y[i]==0):
        s=f"lamp {i} is Non working"
        l.append(s)
  return  render_template("blight.html", len = len(l), l=l)

@app.route("/ylight")
def ylight():
  l=[]
  list  = [111,222,333]
  n= random.choice(list)
  if n==111:
    df=pd.read_excel(r'C:\Users\lenovo\Desktop\New folder\YPhase_light.xlsx')
  elif n==222:
    df=pd.read_excel(r'C:\Users\lenovo\Desktop\New folder\YPhase_light1.xlsx')
  else:
    df=pd.read_excel(r'C:\Users\lenovo\Desktop\New folder\YPhase_light2.xlsx')
  di={'CONNECTED':1,'DISCONNECTED':0}
  Y=df['Status'].map(di)
  y=np.array(Y)
  for i in range(len(y)):
    if(y[i]==0):
        s=f"lamp {i} is Non working"
        l.append(s)
  return  render_template("ylight.html", len = len(l), l=l)


	
if __name__ == '__main__':
    app.run(debug=True)