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