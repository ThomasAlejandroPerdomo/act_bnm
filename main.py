from flask import Flask
import random

app = Flask(__name__)
list = ["El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
         "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
         "Según un estudio de 2019, más del 60 de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
         "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"]



@app.route("/")
def index():
    return f'<h1>bienvenidos a mi pagina web</h1><a href="/datos">ve ideas al azar</a>'\
           '<h2>Lanza una moneda</h2><a href="/mon">¿Cuál caerá?</a>'



@app.route("/datos")
def lista():
    return f'<p>{random.choice(list)}</p>'

@app.route("/moneda")
def moneda():
    return f'<h2>Lanza una moneda</h2><a href="/mon">¿Cuál caerá?</a>'

@app.route("/mon")
def contt():
    res = None
    fet = random.randint(1,2)
    if fet == 1:
        res = 'cara'
    else:
        res = 'cruz'
    return f'<p>{res}</p>'
app.run(debug=True)
