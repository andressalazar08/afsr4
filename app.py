
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from pulp import*

app = Flask(__name__)

@app.route('/')
def opt():
    modelo=LpProblem("modelobase",LpMaximize)
    #Crear variables de decisión
    x1=LpVariable("X1",0,None,LpContinuous)
    x2=LpVariable("X2",0,None,LpContinuous)
    x3=LpVariable("X3",0,None,LpContinuous)
    #Crear función objetivo
    modelo+=1000*x1+1050*x2+1320*x3
    #Restricciones
    modelo+=x1+2*x2+3*x3<=10
    modelo+=x2+2*x3<=10
    modelo+=3*x1+5*x3<=7
    #Ejecutar el solver
    modelo.solve()
    x1resultado=round(value(x1),2)
    x2resultado=round(value(x2),2)

    return render_template('ejercicio.html',x1resultado=x1resultado,x2resultado=x2resultado)
