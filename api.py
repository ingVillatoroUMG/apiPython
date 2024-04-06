from flask import Flask, request, jsonify

app = Flask(__name__)

class Student:
    def __init__(self, nombre, carnet):
        self.nombre = nombre
        self.carnet = carnet
        self.siguiente = None

class ListaEstudiantes:
    def __init__(self):
        self.cabeza = None

    def add_student(self, nombre, carnet):
        new_student = Student(nombre, carnet)
        if not self.cabeza:
            self.cabeza = new_student
        else:
            current = self.cabeza
            while current.siguiente:
                current = current.siguiente
            current.siguiente = new_student

    def list_estudiantes(self):
        estudiantes = []
        current = self.cabeza
        while current:
            estudiantes.append({'nombre': current.nombre, 'carnet': current.carnet})
            current = current.siguiente
        return estudiantes

    def delete_student(self, carnet):
        if not self.cabeza:
            return False

        if self.cabeza.carnet == carnet:
            self.cabeza = self.cabeza.siguiente
            return True

        current = self.cabeza
        while current.siguiente:
            if current.siguiente.carnet == carnet:
                current.siguiente = current.siguiente.siguiente
                return True
            current = current.siguiente

        return False

student_list = ListaEstudiantes()

@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.json
    nombre = data.get('nombre')
    carnet = data.get('carnet')
    if not nombre or not carnet:
        return jsonify({'error': 'Nombre y Carnet Rquerido'}), 400
    student_list.add_student(nombre, carnet)
    return jsonify({'message': 'Estudiante registrado correctamente'}), 201

@app.route('/list_estudiantes', methods=['GET'])
def list_estudiantes():
    estudiantes = student_list.list_estudiantes()
    return jsonify({'estudiantes': estudiantes}), 200

@app.route('/delete_student', methods=['DELETE'])
def delete_student():
    carnet = request.args.get('carnet')
    if not carnet:
        return jsonify({'error': 'carnet is required'}), 400
    if student_list.delete_student(carnet):
        return jsonify({'message': 'Student deleted successfully'}), 200
    else:
        return jsonify({'error': 'Student not found'}), 404

@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({'respuesta':'done'}),200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)

