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
#         while True:
#             if len(capacity_obj.students)<=self.capacity:
#                 student_name=input('enter student name')
#                 capacity_obj.students.append(student_name)
#                 print(capacity_obj.students)
        
#             else:
#                 if len(capacity_obj.students)>self.capacity:
#                   print('error;beyoned the capacity')
#                   break
#     def print_student(self):
#         ad_st=capacity_obj.add_student()
#         for student in capacity_obj.students: 
#             print(student,end=', ')
# capacity_obj=school(3)
# capacity_obj.add_student()
# print(capacity_obj.print_student())
            
class student():
    def __init__(self,name,age,gender) :
        self.name=name
        self.age=age
        self.gender=gender
    def __str__(self) :
        return f'{self.name},{self.age},{self.gender}'
        #"name is % s, " "age is % s"  "gender is % s" % (self.name, self.age,self.gender)
    
        
student_obj=student('name','age','gender')
print(student_obj)