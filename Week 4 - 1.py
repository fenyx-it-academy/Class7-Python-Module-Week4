                        ########## School ###########

class School:
    def __init__(self, capacity):
      self.students = []
      self.capacity = capacity

    def add_student(self, *student):
        if self.students == self.capacity:
            print('No more spot for new studnets!')
        else:
            for stdnt in student:
                self.students.append(stdnt)

    def print_students(self):
        for x in self.students:
            print(x.__str__())

class Student(School):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def __str__(self):
        return (f"{self.name} is {self.age} years old and he/she a {self.gender}.")


school = School(2)
student1 = Student('Safo', 27, 'male')
student2 = Student('Reco', 25, 'male')
student3 = Student('Melo', 27, 'female')

school.add_student(student1, student2)
school.print_students()
school.add_student(student3)

print(student1.__dict__)
print(school.__dict__)




