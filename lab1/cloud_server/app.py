from flask import Flask, jsonify, request
from flask_cors import CORS
import time
import json
import os

app = Flask(__name__)
CORS(app)

# API endpoint to get data
@app.route('/get_data')
def get_data():
    if os.path.exists('data.json'):
        json_file = open('data.json')
        return jsonify(json.load(json_file)), 200
    return jsonify('No data available'), 200

# API endpoint to update data
@app.route('/set_data', methods=['POST'])
def set_data():
    moisture = request.args['moisture']
    with open('data.json', 'w') as outfile:
        json.dump(
            {
                'moisture': moisture,
                'timestamp': time.time()
            }, 
            outfile
            )

    return jsonify({
        'msg': 'Data added'
    }), 201


# Run the server, 0.0.0.0 signifies that it will have 
# unrestricted access throughout the private network.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
