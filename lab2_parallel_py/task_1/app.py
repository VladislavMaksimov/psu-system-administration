from json_worker import write_json, read_json
from students_generator import generate_students

write_json(generate_students(), 'database.json')
students = read_json('database.json')