from json_worker import read_json

# топ по успеваемости
def get_best_students(count):
    students = read_json('database.json')
    students_sorted_list = []

    for student in students.items():
        average_grade = 0
        subjects = student[1]['subjects']

        for subject in subjects:
            average_grade += subject['grade']
        average_grade /= len(subjects)

        students_sorted_list.append((student[1]['name'], average_grade))
    
    students_sorted_list.sort(key=lambda tup: tup[1], reverse=True)
    return students_sorted_list[0:count]

# топ по пропускам
def get_best_truants(count):
    students = read_json('database.json')
    students_sorted_list = []

    for student in students.items():
        truancies = student[1]['truancies']
        name = student[1]['name']
        students_sorted_list.append((name, truancies))

    students_sorted_list.sort(key=lambda tup: tup[1], reverse=True)
    return students_sorted_list[0:count]

# топ самых сложных предметов
def get_heardest_subjects(count):
    students = read_json('database.json')
    subjects_dict = dict()

    for student in students.items():
        subjects = student[1]['subjects']
        for subject in subjects:
            subject_name = subject['name']
            grade = subject['grade']
            try:
                subjects_dict[subject_name] += grade
            except:
                subjects_dict[subject_name] = grade

    subjects_sorted_list = []
    for subject_name in subjects_dict:
        subjects_sorted_list.append((subject_name, subjects_dict[subject_name]))
    subjects_sorted_list.sort(key=lambda tup: tup[1])
    
    return subjects_sorted_list[0:count]