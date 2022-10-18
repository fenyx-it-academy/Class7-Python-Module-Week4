class FenyxSchool:
   
    def __init__(self, capacity):
        self.capacity = capacity
        self.students = []

    def add_student(self, std):
        if len(self.students) >= self.capacity:
            print("There is no place because of capacity of school is full!")
        else:
            self.students.append(std)
    
    def print_students(self):
        for std in self.students:
            print(std)         



class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"""
        Student Name:   {self.name}
        Student Age:    {self.age}
        Student Gender: {self.gender}        
        
        """


FenyxSchool = FenyxSchool(2)
student1 = Student("Ahmet", "18", "Boy")
student2 = Student("Suat", "19", "Boy")
student3 = Student("Rana", "18", "Girl")

FenyxSchool.add_student(student1)
FenyxSchool.add_student(student2)
FenyxSchool.print_students()
FenyxSchool.add_student(student3)

print(FenyxSchool.__dict__)







