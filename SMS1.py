class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)

    def display_student_info(self):
        print(f"Student ID: {self.student_id}")
        self.display_info()
        print("Courses Enrolled:")
        for course in self.courses:
            print(f"- {course.course_name}")

class Teacher(Person):
    def __init__(self, name, age, address, employee_id):
        if age < 20:
            raise ValueError("Teacher age must be at least 20.")
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.subjects = []

    def assign_subject(self, course):
        self.subjects.append(course)

    def display_teacher_info(self):
        print(f"Employee ID: {self.employee_id}")
        self.display_info()
        print("Assigned Subjects:")
        for course in self.subjects:
            print(f"- {course.course_name}")

class Course:
    def __init__(self, course_name, course_code, teacher):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = teacher

    def display_course_info(self):
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Teacher: {self.teacher.name}")

def get_teacher_input():
    name = input("Enter teacher's name: ")
    age = int(input("Enter teacher's age: "))
    if age<20:
      print("Invalid input")
      try:
            age = int(input("Enter teacher's age: "))
      except ValueError as e:
        print(e)
    address = input("Enter teacher's address: ")
    employee_id = input("Enter teacher's employee ID: ")
    try:
        teacher = Teacher(name, age, address, employee_id)
    except ValueError as e:
        print(e)
        return None
    num_subjects = int(input("Enter number of subjects to assign: "))
    for _ in range(num_subjects):
        course_name = input("Enter course name: ")
        course_code = input("Enter course code: ")
        course = Course(course_name, course_code, teacher)
        teacher.assign_subject(course)
    return teacher

def get_student_input(available_courses):
    name = input("Enter student's name: ").upper()
    age = int(input("Enter student's age: "))
    address = input("Enter student's address: ")
    student_id = input("Enter student's ID: ")
    student = Student(name, age, address, student_id)
    num_courses = int(input("Enter number of courses to enroll: "))
    for _ in range(num_courses):
        course_name = input("Enter course name: ")
        course = next((course for course in available_courses if course.course_name == course_name), None)
        if course:
            student.enroll_course(course)
        else:
            print("Invalid course name. Try again.")
            try:
                course_name = input("Enter course name: ")
                course = next((course for course in available_courses if course.course_name == course_name), None)
            except ValueError as e:
                print(e)
            return None
    return student

# Collect inputs
teachers = []
students = []
available_courses = []

num_teachers = int(input("Enter number of teachers: "))
for _ in range(num_teachers):
    teacher = get_teacher_input()
    if teacher:
        teachers.append(teacher)
        available_courses.extend(teacher.subjects)

num_students = int(input("Enter number of students: "))
for _ in range(num_students):
    student = get_student_input(available_courses)
    if student:
        students.append(student)

# Display information
print("\nTeacher Information:")
for teacher in teachers:
    teacher.display_teacher_info()
    print()

print("Student Information:")
for student in students:
    student.display_student_info()
    print()

print("Course Information:")
for course in available_courses:
    course.display_course_info()
    print()
