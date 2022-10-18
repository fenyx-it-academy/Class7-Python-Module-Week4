# Python program to create Rectangle class
class Rectangle:
    #define constructor with attributes: lenght and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    #create perimeter() method
    def Perimeter(self):
        return 2*(self.length + self.width)


    #create Area() method
    def Area(self):
        return self.length * self.width
    
    #create display() method
    def display(self):
        print('The length of rectangle is :', self.length)
        print("The width of rectangle is: ", self.width)
        print("The perimeter of rectangle is: ", self.Perimeter())
        print("The area of rectangle is: ", self.Area())

my_rectangle = Rectangle(length=int(input('Length: ')), width=int(input('Width: ')))
my_rectangle.display()
