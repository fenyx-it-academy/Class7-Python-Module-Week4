class School:
    students =[] 

    def __init__(self, capacity):
        self.capacity = capacity
     
    def add_students(self,std): 
        if len(self.students)<self.capacity:
            self.students.append([std.name,std.age,std.gender])
            print(std.name, " was added")
        else:
            print(f"we cannot add",std.name,"as a new student. sorry, school capacity is full.")
            
class Student(School):

    def __init__(self,name,age, gender):
        self.name=name
        self.age=age
        self.gender=gender

    def __str__(self):  
        return self.name+" "+ str(self.age)+ " " + self.gender 
        
    def print_students():  
        for student in School.students:
            print(student)


school1 = School(3)
 
std1=Student("rama",25,"female")
std2=Student("rami",20,"male")
std3=Student("mazen",30,"male")
std4=Student("hani",10,"male")
 
print(std3)

school1.add_students(std1)
school1.add_students(std2)
school1.add_students(std3)
school1.add_students(std4)
 
Student.print_students() 

print(vars(std1))
print(vars(std2))
print(vars(std3))


 