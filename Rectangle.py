class Rectangle:

    def __init__(self,width,length):
        self.width=width
        self.length=length

    def perimeter(self):
        return 2*(self.length+self.width)

    def area(self):
        return  self.length*self.width
    
    def display(self):
        print("Width is:", self.width, "\nLength is:", self.length, "\nArea is:",self.area(), "\nPerimeter is:", self.perimeter())

rec1=Rectangle(3,4)
rec1.display()