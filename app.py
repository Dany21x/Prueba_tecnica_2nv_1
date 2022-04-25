from flask import Flask, render_template, url_for, jsonify
from werkzeug.utils import redirect
from requests import get

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Hola mundo desde Flask!'

@app.route('/mostrarPokemon/', methods=['GET','POST'])
def mostrar_nombre():
    pokemons = ['spearow', 'fearow', 'ekans', 'arbok', 'pikachu', 'raichu', 'sandshrew', 'sandslash', 'nidorina']
    return render_template('mostrar.html', pokemons=pokemons)

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('inicio'))

@app.route('/api/habilidad/<nombre>')
def mostrar_habilidad(nombre):
    print(nombre)
    habilidades = get('https://pokeapi.co/api/v2/pokemon/'+nombre).json()
    print("long habilid",len(habilidades['abilities']))
    lista_habilidades = ''
    for i in range(0,len(habilidades['abilities'])):
        lista_habilidades= habilidades['abilities'][i]['ability']['name']+ ', ' + lista_habilidades
    return "La lista de habilidades de "+nombre+ " es " + lista_habilidades
    #return habilidades['abilities']flask[0]['ability']['name']