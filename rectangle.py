class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2*(self.length+self.width)

    def area(self):
        return self.length*self.width

    def display(self):
        print(f'''Rectangle   Length: {self.length},
            Width: {self.width},
            Perimeter: {self.perimeter()}
            Area: {self.area()}''')


rec = Rectangle(12,15)
rec.display()