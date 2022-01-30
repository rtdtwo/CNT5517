# LAB 3 - Metronome Thing
# Group: RTX2080
# Members: Bhavya Kavdia, Ekleen Kaur, Rishabh Tatiraju

# app.py - The REST Server

from flask import Flask, jsonify, request
from flask_cors import CORS
import bl

# Initialize Flask server
app = Flask(__name__)

# Add CORS to allow cross origin requests
CORS(app)

# API to get all three data points 
# i.e. current, max and min BPM, in one go. 
# Used by the website.
@app.route('/data')
def get_data():
    return jsonify({
        'code': 200,
        'result': bl.get_data()
    })


# API to get the current BPM value
@app.route('/bpm')
def get_bpm():
    return jsonify({
        'code': 200,
        'result': bl.get_current_bpm()
    })


# API to set the current BPM value
@app.route('/bpm', methods=['PUT'])
def set_bpm():
    bpm = request.args.get('bpm')
    if bpm is not None and len(bpm) > 0:
        bpm_int = int(bpm)
        if bpm_int <= 0:
            return jsonify({
                'code': 400,
                'msg': 'BPM has to be more than 0'
            }), 400

        result = bl.set_current_bpm(int(bpm))
        if result:
            return jsonify({
                'code': 200,
                'msg': 'BPM set successfully to {} bpm'.format(bpm),
                'result': bl.get_data()
            })
        else:
            return jsonify({
                'code': 500,
                'msg': 'An error occurred'
            }), 500
    else:
        return jsonify({
            'code': 400,
            'msg': 'No BPM provided'
        }), 400


# API to get the minimum BPM value.
@app.route('/bpm/min')
def get_min_bpm():
    return jsonify({
        'code': 200,
        'result': bl.get_min_bpm()
    })


# API to reset the minimum BPM value
@app.route('/bpm/min', methods=['DELETE'])
def reset_min_bpm():
    result = bl.reset_min_bpm()
    if result:
        return jsonify({
            'code': 200,
            'msg': 'Min BPM reset successfully'
        })
    else:
        return jsonify({
            'code': 500,
            'msg': 'An error occurred'
        }), 500


# API to get the maximum BPM value.
@app.route('/bpm/max')
def get_max_bpm():
    return jsonify({
        'code': 200,
        'result': bl.get_max_bpm()
    })


# API to reset the maximum BPM value.
@app.route('/bpm/max', methods=['DELETE'])
def reset_max_bpm():
    result = bl.reset_max_bpm()
    if result:
        return jsonify({
            'code': 200,
            'msg': 'Max BPM reset successfully'
        })
    else:
        return jsonify({
            'code': 500,
            'msg': 'An error occurred'
        }), 500


# Start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
