import uuid

name = input("Enter your name: ")
delivery_date = input("Delivery Date: ")

print("Name:", name)
print("Delivery Date:", delivery_date)

class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
    total_students = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_students += 1

    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self. courses_list.append(course)

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")

    def get_student_average(self):
        total_marks = 0
        for course in self.courses_list:
            total_marks += course.course_mark
        return total_marks / len(self.courses_list) if len(self.courses_list) > 0 else 0

    def get_student_details(self):
        return self.__dict__

students = []

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark\n"
                              "6.Exit"))
    except ValueError:
        print("Invalid input. Please enter a valid option.")
        continue

    if selection == 1:
        student_number = input("Enter Student Number: ")
        student_exists = any(student.student_number == student_number for student in students)

        if student_exists:
            print("Student with the given number already exists.")
            continue

        student_name = input("Enter Student Name: ")
        while True:
            try:
                student_age = int(input("Enter Student Age: "))
                break
            except ValueError:
                print("Invalid Age Please enter a valid age")

        new_student = Student(student_name, student_age, student_number)
        students.append(new_student)
        print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number: ")
        student_found = None

        for student in students:
            if student.student_number == student_number:
                student_found = student
                break

        if student_found:
            students.remove(student_found)
            print("Student Deleted Successfully")
        else:
            print("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number: ")
        student_found = None

        for student in students:
            if student.student_number == student_number:
                student_found = student
                break

        if student_found:
            print("Student Details:")
            print(student_found.get_student_details())
            print("Courses:")
            student_found.get_student_courses()
        else:
            print("Student Not Exist")
