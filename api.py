import csv
from flask import Flask, jsonify, request

##
##   Estructura de lista simple
##

class Nodo:
    def __init__(self, id):
        self.id = id
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar_elemento(self, id):
        nuevo_nodo = Nodo(id)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def retirar_primero(self):
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente

    def retirar_ultimo(self):
        if self.cabeza.siguiente == None:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = None

    def obtener_lista(self):
        lista = []
        actual = self.cabeza
        while actual:
            lista.append(actual.id)
            actual = actual.siguiente
        return lista

app = Flask(__name__)
mi_lista = ListaSimple()


@app.route('/cargar_csv', methods=['GET'])
def cargar_csv():
    with open('estudiante.csv', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)  
        for linea in lector_csv:
            id = linea[0]
            mi_lista.agregar_elemento(id)
    return jsonify(mi_lista.obtener_lista())

@app.route('/agregar_registro', methods=['POST'])
def agregar_registro():
    datos = request.json
    id = datos['id']
    mi_lista.agregar_elemento(id)
    return 'Registro agregado exitosamente'


@app.route('/listar', methods=['GET'])
def listar():
    return jsonify(mi_lista.obtener_lista())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
