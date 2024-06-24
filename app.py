from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta para manejar solicitudes POST
@app.route('/', methods=['POST'])
def handle_post():
    data = request.get_json()  # Obtener los datos en formato JSON
    if not data:
        return jsonify({'error': 'No data provided'}), 400


    # Procesar los datos recibidos
    response_data = {
        'received': data,
        'message': 'POST request received successfully'
    }
    

    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)