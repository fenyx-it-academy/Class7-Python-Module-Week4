
# ## 2. Rectangle

# 1. Write a `Rectangle` class, allowing you to build a rectangle with `length` and `width` attributes.
# 2. Create a `perimeter()` method to calculate the perimeter of the rectangle and an `area()` method to calculate the area of ​​the rectangle.
# 3. Create a method `display()` that displays the length, width, perimeter and area of an object created using an instantiation on `Rectangle` class.

class Rectangle:
    def __init__(self, length, width) : 
        self.length=length
        self.width=width
    
    def perimeter(self):
        return (self.length + self.width)*2

    def area(self):    
        return self.length * self.width

    def display(self):
        return f'''
        length : {self.length }
        width : {self.width }
        perimeter :{ self.perimeter()}
        area : {self.area()}
        '''

r1=Rectangle(3,4)
print (r1.display())