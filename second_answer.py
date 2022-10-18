class Rectangle:

    def __init__ (self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.width

    def display(self):
        return f''''
        Length = {self.length}
        Width = {self.width}
        Perimeter = {self.perimeter()}
        area = {self.area()}
        '''


r = Rectangle(5,6)
print(r.display())
