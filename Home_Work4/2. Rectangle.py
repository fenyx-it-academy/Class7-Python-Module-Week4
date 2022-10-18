class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def perimeter(self):
        perimeter = (self.length*2)+(self.width*2)
        return perimeter
    
    def area(self):
        area = (self.length)*(self.width)
        return area
    
    def __str__(self):
        perim = rect.perimeter()
        area = rect.area()
        
        return f'The length is: {self.length}\nThe width is: {self.width}\nThe perimeter is: {perim}\nThe area is: {area}'

rect = Rectangle(8,2)

print(rect)