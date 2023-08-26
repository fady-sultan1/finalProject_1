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
