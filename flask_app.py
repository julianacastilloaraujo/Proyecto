# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def Home():
    return 'Hola a continuación vas a conocer mas sobre nosotros: Ivan, Cristian, Juliana'

@app.route('/Ivan')
def Ivan():
    return 'Hola, soy Ivan \n Como estudiante me he capacitado mediante los conocimiento que ofrece la carrera y mis estudios autodidactas en los cuales he aprendido'

@app.route('/Cristian')
def Cristian():
    return 'Hola, soy Cristian \n Como estudiante me he capacitado mediante los conocimientos que ofrece la carrera y mis estudios autodidactas en los cuales he aprendido cómo se utilizan las herramientas de diseño para la selección de tecnologías de desarrollo'

@app.route('/Juliana')
def Juliana():
    return 'Hola, soy Juliana \n Como estudiante he abordado temas de vanguardia, como el Análisis de Datos con una Perspectiva Ética en el prestigioso encuentro tecnológico MacaoTech en Honduras.'
