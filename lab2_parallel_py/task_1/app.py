from json_generator import generate_json
from students_generator import generate_students

generate_json(generate_students(), 'database.json')
