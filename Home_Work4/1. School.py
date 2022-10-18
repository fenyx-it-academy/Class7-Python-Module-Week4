list_est = list()

class School:
    def __init__(self, capacity):
        self.capacity = capacity
        
    def capacityFull(self):
        full = self.__capacity = len(list_est)
        if full > 0:
            return full
        
        
class Student: 
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def addStudent(self):
        print('*** Register Student***\n')
        na = (input("Please put the name: ").upper())
        ag = (input("Please put the age: "))
        ge = (input("Please put gender: ").upper())
        est = Student(na, ag, ge)    
        list_est.append(est)
        print("Succes ! \n")



    def Display(self):
        
        return (f'''
    STUDENT DETAILS
    ------------------
    Name  : {self.name}
    Age   : {self.age}
    Gender: {self.gender}
        ''')
        
def menu():
    
    play= True
    est = Student('',0,'')
    
    while play:
         
        print('\n*** Menu ***')
        print('1. Add Student')
        print('2. Display Student')
        print("3. Exit")
        try:
            option = int(input("\nPlease choose you option: "))
        except:
            print("\n   ( ¬_¬)   Wrong choice...   (¬_¬)  ")
            continue
        print()
        
        if option == 1:

            capt = School(0)
            capt.capacityFull()
            
            if capt.capacityFull() ==3:
                 print('Sorry, capacity is full ! You can not be add more students ')

            else:
                est.addStudent()
         
        elif option ==2:
            
            est_report = f'''
            {'='*40}
            {'STUDENT REPORT'.center(40)}
            {'='*40}''' 
            
            for estl in list_est:
                est_report += estl.Display()
        
            print(est_report)
            print()
            
        elif option ==3:
            exit()

        else:
            print('Wrong option')
menu()