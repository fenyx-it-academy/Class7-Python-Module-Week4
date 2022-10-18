class school:
    students = []
    enrolment = 0
    def __init__(self,capacity):
        self.capacity = capacity

class student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def str (self):
        return f'''
        Name : {self.name}
        Age : {self.age}
        Gender : {self.gender}     
        '''
    def add_student(self, capacity):
        school.enrolment = school.enrolment + 1
        if school.enrolment <= capacity:
            school.students.append(self)
        else:
            print("Sorry class capacity is full")


    def print_student(self):
        for i in school.students:
            print (i.str())
            
student1=student('Ali Sen', 19 ,'m')
student2=student('Ayse Sahin', 18,'f')
student3=student('Hasan Koc', 17, 'f')
class1= school (2)

student1.add_student(class1.capacity)
student2.add_student(class1.capacity)
student3.add_student(class1.capacity)

student1.print_student()
print(student1.__dict__)
print(class1.__dict__)
