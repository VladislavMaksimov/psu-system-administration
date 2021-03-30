import json

def write_json(dictionary, filename):
    with open(filename, 'w') as file:
        file.write(json.dumps(dictionary, indent=4))

def read_json(filename):
    try:
        with open(filename, 'r') as file:
            students = json.load(file)
            return students
    except Exception as e:
        print(e)