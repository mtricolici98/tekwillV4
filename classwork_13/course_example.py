courses = {
    1: 'Python Basics',
    2: 'Functional',
    3: 'Object Oriented'
}


def get_course_info_by_id(course_id: int):
    print(courses.get(course_id))  # 10 linii de cod


get_course_info_by_id(1)
get_course_info_by_id(1)

student_list = ['Marius', 'Ion', 'Vasile']


def show_sorted_student_list(students):
    # sorted_students = sorted(students) Ver 1
    sorted_students = students.copy()  # Ver 2
    sorted_students.sort()
    print(sorted_students)


show_sorted_student_list(student_list)
print(student_list)

results_history = []
c = 0


def sum(a, b):
    c = a + b
    results_history.append(c)
    print(results_history)
    return c


def print_result():
    print(sum(1, 2))
    print(sum(2, 2))
    print(sum(3, 2))
    print(c)


print_result()
