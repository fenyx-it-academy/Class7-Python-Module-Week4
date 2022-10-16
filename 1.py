## 1. School

# 1. Create a `School` class with instance attribute `capacity`.
# 2. Add `students` as the class attribute. This will be a list and keep track of the students in the school.
# 3. Create a `Student` class with attributes: `name`, `age`, `gender`
# 4. Add `__str__` method to this class to print the objects.
# 6. Add `add_student` method to the class. If capacity is full print error message else add the student.
# 7. Add `print_students` method to print the all existing students. Loop through the students list and print each student object.
# 8. Create a `School` object and threee students, add first 2 students to school. Print students and afterwards try to add the third student.
# 9. Use `__dict__` method to see attributes

class School:

    def __init__(self,capacity):
        self.students=[]
        self.capacity=capacity

    def add_student (self,*student)  :
        if len(self.students) >= self.capacity :
            print ('Capacity is full!')
        else: 
            for s in student : #ability to add multiple students at once 
                self.students.append (s)


    def  print_students (self):
        for s in self.students : 
            print (s.__str__())


class Student:
    def __init__(self , name , age , gender):
        self.name=name
        self.age=age
        self.gender=gender


    def __str__(self):
        return f'''
        {self.name }
        {self.age }
        {self.gender}
         '''

student1=Student('Henry s',19,'m')
student2=Student('J s',18,'f')
student3=Student('Mary x',17,'f')
school1=School (2)


#adding first two students :
school1.add_student(student1,student2)
school1.print_students()
#adding last student, but capacity is full!
school1.add_student(student3)
 

print (student1.__dict__)
print (school1.__dict__)