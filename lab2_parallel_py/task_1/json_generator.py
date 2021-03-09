import json

def generate_json(dictionary, filename):
    with open(filename, 'w') as file:
        file.write(json.dumps(dictionary, indent=4))