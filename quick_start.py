from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/hello/plau/')
def plau():
    return 'plau'

@app.route('/plau/')
def ktchuplei():
    return 'ktchuplei'

@app.route('/multiplicacao/<int:numero1>&<int:numero2>')
def mult(numero1, numero2):
    result = numero1 * numero2
    return f'A multiplicaçao de {numero1} com {numero2} é {result}'

from flask import render_template

@app.route('/hello/<name>')
def hellow(name=None):
    return render_template('hello.html', name=name)