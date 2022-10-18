class School:

    students = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_student(self, s):
        
        if len(self.students) >= self.capacity :
            print("The capacity is full. You can not register the student.")
        else :
            self.students.append(s)

    def print_students(self):
        for s in self.students:
            print(s)

class Student:
  
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'''Student name: {self.name},
        age: {self.age},
        gender: {self.gender}'''
        
school = School(2)
std1 = Student('Jack','11','M')
std2 = Student('Melissa','10','F')
std3 = Student('Ali','10','M')

school.add_student(std1)
school.add_student(std2)
school.print_students()

school.add_student(std3)

print(school.__dict__)
print(std3.__dict__)
