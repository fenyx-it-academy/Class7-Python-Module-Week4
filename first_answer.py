import sys


class School:
    students = []

    def __init__(self, capacity: int):
        self.capacity = capacity


class Student(School):
    num_of_students = 0

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Student.num_of_students += 1

    def __str__(self):
        return f''''
        studen name = {self.name} 
        age = {self.age}
        gender = {self.gender}
        '''

    def add_student(self, capacity):
        if Student.num_of_students <= capacity:
            School.students.append(self)
        else:
            print("OOps!, it is full capacity")

    def print_students(self):
        for i in School.students:
            print(Student.__str__(self))


cap = School(2)
student1 = Student("Mike", 20, "M")
student2 = Student("Jack", 22, "M")

student1.add_student(cap.capacity)
student2.add_student(cap.capacity)
print(cap.students)

student3 = Student("Rose", 21, "F")
student3.add_student(cap.capacity)
print(cap.students)
