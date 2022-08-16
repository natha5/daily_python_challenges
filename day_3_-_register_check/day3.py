
def register_check(passed_register):
    students_attending = 0
    for key in passed_register:
        if passed_register[key] == 'yes':
            students_attending += 1
    print(students_attending)
    return students_attending



register = {'Michael': 'yes', 'John': 'no',
               'Peter': 'yes', 'Mary': 'yes'}
register_check(register)