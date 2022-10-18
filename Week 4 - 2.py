                #####################  Rectangle  ########################


class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def perimeter(self):
        return 2*(self.lenght + self.width)

    def area(self):
        return(self.lenght * self.width)

    def display(self):
        return(f'{self.lenght} {self.width} {self.perimeter()} {self.area()}')
    
result = Rectangle(8, 9)
print(result.display())
