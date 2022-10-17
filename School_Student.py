## 1. School
class school:
    s_lst = []
    s_count = 0
    def __init__(self,capacity):
        self.capacity = capacity
        

class student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def str (self):
        return f"Student name: {self.name}\nStudent age: {self.age}\nStudent gender: {self.gender}"
    
    def add_student(self,capacity):
        school.s_count = school.s_count +1
        print(school.s_count)
        if school.s_count <= capacity:
            school.s_lst.append(self)
        else:
            print("Sorry this student can't be added as the school capacity is full")
        

    def print_student(self):
        for i in school.s_lst:
            print(i.name,i.age,i.gender)


scl = school(3)
stdnt1 = student("Shatha",22,"F")
stdnt2 = student("hata",21,"M")
stdnt3 = student("Ali",29,"M")
stdnt4 = student("Farah",30,"F")
stdnt1.add_student(scl.capacity)
stdnt2.add_student(scl.capacity)
stdnt3.add_student(scl.capacity)
stdnt4.add_student(scl.capacity)
stdnt1.print_student()
print(stdnt1.__dict__)
print(scl.__dict__)