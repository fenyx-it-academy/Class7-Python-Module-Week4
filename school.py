class school:
        capacity=0
        class_dict={}
    
class Student():
    def __init__(self,name,surname,gender='Unknown'):
        self.name=name
        self.surname=surname
        self.gender=gender

    def add_student(self,capacity):      
        self.capacity=school.capacity
        school.capacity+=1
        if school.capacity<4:
            school.class_dict[self.name+self.surname]=[self.name,self.surname,self.gender]
        else:
            print('Sorry class capacity is full')
    def __str__(self) :   
        return(f'Student name:{self.name}\nStudent surname:{self.surname}\nStudent Gender:{self.gender}')

class_a=school()
student_b=Student('Sefa',"sahan",'male')
student_b.add_student(class_a.capacity)
student_b=Student('Omer',"sahan",'male')
student_b.add_student(class_a.capacity)
student_c=Student('Faik',"sahan",'male')
student_c.add_student(class_a.capacity)
student_d=Student('Neyran',"sahan",'Female')
student_d.add_student(class_a.capacity)
print(student_d)
print(student_d.__dict__)
print(class_a.__dict__)
print(class_a.class_dict)

        
            
