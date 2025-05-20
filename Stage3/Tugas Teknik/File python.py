from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def data():
    if request.is_json:
        data = request.get_json()
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        response = {"message": "Data received", "temperature": temperature, "humidity": humidity}
        return jsonify(response), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
