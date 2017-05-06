from flask import Flask, render_template, request, redirect
from modelos import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@db_session
def index():
    if request.method == 'POST':
        dni = request.form.get('dni')
        nombre = request.form.get('nombre')
        if dni:
            t = Alumno(doc=dni)
            n = Alumno(name=nombre)

    contexto = {'document': select(t for t in Alumno), 'nombres': select(n for n in Alumno)}
    return render_template('index.html', **contexto)


@app.route('/eliminar/<int:indice>')
@db_session
def eliminar(indice):
    dni = Alumno[indice]
    nombre = Alumno[indice]
    dni.delete()
    nombre.delete()
    return redirect('/')


@app.route('/editar/<int:indice>', methods=['GET', 'POST'])
@db_session
def editar(indice):
    dni = Alumno[indice]
    nombre = Alumno[indice]
    if request.method == 'POST':
        doc = request.form.get('dni')
        name = request.form.get('Nombre')
        if doc:
            dni.doc = doc
            nombre.name = name
            return redirect('/')
    return render_template('editar.html', dni=dni, nombre=dni)

if __name__ == '__main__':
    app.run(debug=True)
