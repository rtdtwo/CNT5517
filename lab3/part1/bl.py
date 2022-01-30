# LAB 3 - Metronome Thing
# Group: RTX2080
# Members: Bhavya Kavdia, Ekleen Kaur, Rishabh Tatiraju

# bl.py - contains all business logic for the server.

import json


def get_data():
    file = open('db.json', 'r')
    data = json.load(file)
    file.close()

    return {
        'current': data['current'],
        'min': data['min'],
        'max': data['max']
    }


def get_current_bpm():
    with open('db.json', 'r') as f:
        data = json.load(f)
        return data['current']


def set_current_bpm(bpm):
    current_data = get_data()
    current_data['current'] = bpm
    if current_data['min'] > bpm or current_data['min'] == 0:
        current_data['min'] = bpm
    if current_data['max'] < bpm:
        current_data['max'] = bpm

    file = open('db.json', 'w')
    json.dump(current_data, file)
    file.close()

    return True


def get_min_bpm():
    with open('db.json', 'r') as f:
        data = json.load(f)
        return data['min']


def get_max_bpm():
    with open('db.json', 'r') as f:
        data = json.load(f)
        return data['max']


def reset_min_bpm():
    current_data = get_data()
    with open('db.json', 'w') as f:
        current_data['min'] = 0
        json.dump(current_data, f)

    return True


def reset_max_bpm():
    current_data = get_data()
    with open('db.json', 'w') as f:
        current_data['max'] = 0
        json.dump(current_data, f)

    return True
