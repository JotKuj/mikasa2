from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello(name=None):
     return render_template('base.html', name=name)

@app.route('/ropa')
def ropa(name=None):
     return render_template('posesiones/ropa.html', name=name)

@app.route('/ropa/registra')
def ropa(name=None):
     return render_template('posesiones/ropa.html', name=name)