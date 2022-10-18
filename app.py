from flask import Flask, render_template, redirect, request
import json
import requests


app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    pronto = {}
    pronto['clienteID'] = 9999
    pronto['lista_produtos'] = [{},{}]
    with open('dados.txt','w') as arq:
        arq.write(json.dumps(pronto))
    return ''

@app.route("/index", methods=["POST", "GET"])
def index():
    if request.method == 'GET':
        if request.form['OKA']:
            return redirect('/venda')
    return render_template("index.html")

@app.route('/converter')
def converter():
    valor = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
    valor = float(valor.json()['USDBRL']['high'])
    return str(valor)

#pip install requests
@app.route("/venda", methods=["POST", "GET"])
def venda():
    return render_template("venda.html")