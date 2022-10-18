## 2. Rectangle

# 1. Write a `Rectangle` class, allowing you to build a rectangle with `length` and `width` attributes.
# 2. Create a `perimeter()` method to calculate the perimeter of the rectangle and an `area()` method to calculate the area of ​​the rectangle.
# 3. Create a method `display()` that displays the length, width, perimeter and area of an object created using an instantiation on `Rectangle` class.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return 2*(self.length + self.width)

    def Area(self):
        return self.length * self.width
    
    def display(self):
        print('The length of rectangle is :', self.length)
        print("The width of rectangle is: ", self.width)
        print("The perimeter of rectangle is: ", self.Perimeter())
        print("The area of rectangle is: ", self.Area())

my_rectangle = Rectangle(length=int(input('Length: ')), width=int(input('Width: ')))
my_rectangle.display()
