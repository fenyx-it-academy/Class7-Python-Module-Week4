# 1. Create a `School` class with instance attribute `capacity`.
# 2. Add `students` as the class attribute. This will be a list and keep track of the students in the school.
# 3. Create a `Student` class with attributes: `name`, `age`, `gender`
# 4. Add `__str__` method to this class to print the objects.
# 6. Add `add_student` method to the class. If capacity is full print error message else add the student.

# 7. Add `print_students` method to print the all existing students. Loop through the students list and
# print each student object.

# 8. Create a `School` object and threee students, add first 2 students to school.
# Print students and afterwards try to add the third student.

# 9. Use `__dict__` method to see attributes
# s=[]
# while len(s)<=4:
#     x=str(input('inter'))
#     s.append(x)
# print(s)

# class school():
#     students=[]
#     def __init__(self,capacity):
#         self.capacity=capacity 
#     def add_student(self):
        
#         while len(capacity.students)<= self.capacity:
#             student_name=(input('enter student name'))
#             capacity.students.append(student_name)
#             return capacity.students
#         else:
#             print('error')
            
       
# capacity=school(3) 
# print(capacity.add_student())   

def s():
    l=[]
    while len(l)<=2:
        d=input('enter n')
        l.append(d)
        print(l,end='')
    else:
        print('error')
s()

            
        
    
# class student():
#     def __init__(self,name,age,gender) :
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def __str__(self) :
#         "name is % s, " "age is % s"  "gender is % s" % (self.a, self.b)
        
#     def add_student(self):
        
