class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def perimeter(self):
        perimeter= 2 * (self.length + self.width)
        return perimeter
    
    def area (self):
        area = self.length * self.width
        return area
    
    def display(self):
        return f'''
        length : {self.length }
        width : {self.width }
        perimeter :{self.perimeter()}
        area : {self.area()}
        '''

r1=Rectangle(3,4)
print (r1.display())