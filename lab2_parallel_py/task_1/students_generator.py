from random import randint

subjects = [
    'History',
    'Russian language',
    'English language',
    'Sociology',
    'Algorythms',
    'Iformatics',
    'System administration',
    'Databases',
    'Linear algebra',
    'Mathematical analysis'
]

students = [
    'Damir',
    'Kirill',
    'Irina',
    'Vlad',
    'Nastya',
    'Danil',
    'Misha',
    'Andrey'
]

def generate_truancies():
    return randint(0, 30)

def generate_subjects():
    subjects_list = []
    for subject in subjects:
        subject_dict = {
            'name': subject,
            'grade': randint(2, 5)
        }
        subjects_list.append(subject_dict)
    return subjects_list


def generate_student(student):
    student_dict = {
        'name': student,
        'truancies': generate_truancies(),
        'subjects': generate_subjects()
    }
    return student_dict

def generate_students():
    students_dict = dict()
    for student in students:
        students_dict[id(student)] = generate_student(student)
    return students_dict