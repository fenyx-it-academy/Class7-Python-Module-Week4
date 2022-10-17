# 1. Write a `Rectangle` class, allowing you to build a rectangle with `length`
# and `width` attributes.

# 2. Create a `perimeter()` method to calculate the perimeter
# of the rectangle and an `area()` method to calculate the area of ​​the rectangle.

# 3. Create a method `display()` that displays the length, width, perimeter and area of an
# object created using an instantiation on `Rectangle` class.

from operator import length_hint


class rectangle():
    
    def __init__(self,width,lenght):
        self.width=width
        self.lenght=lenght
        
    def perimeter(self):
        perimeter=(self.lenght +self.width)*2
        return perimeter
    def area(self):
        area=self.lenght*self.width
        return area
    def display(self):
        x=rectangle.area()
        y=rectangle.perimeter()
        return f'lenght:{self.lenght}, width:{self.width},area:{x},perimeter:{y}'
rectangle=rectangle(3,4)
print(rectangle.display())
