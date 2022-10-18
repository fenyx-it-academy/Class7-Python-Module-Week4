class School:
        capacity = 1
        dict_of_class = {}


class Student():
    def __init__(self, firstname, lastname, age, gender = 'Unknown'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        
    def add_student(self, capacity):
        self.capacity = School.capacity
        School.capacity += 1
        if School.capacity < 6:
            School.dict_of_class[self.firstname + self.lastname] = [self.firstname, self.lastname, self.age, self.gender]

        else:
            print('Error! Class is full! ')
        
            
    def __str__(self):
        return (f'\nStudent name: {self.firstname} {self.lastname}\nStudent Age: {self.age}\nStudent Gender: {self.gender}')
    
first_class = School()
student1 = Student('Rumi', 'Yakar', 25, 'Female')
student1.add_student(first_class.capacity)
student2 = Student('Said', 'Bostan', 26, 'Male')
student2.add_student(first_class.capacity)
student3 = Student('Sami', 'Yakar', 24, 'Male')
student3.add_student(first_class.capacity)
student4 = Student('Ahmet', 'Yakar', 10, 'Male')
student4.add_student(first_class.capacity)
print(student2)
print(student2.__dict__)
print(first_class.dict_of_class)

