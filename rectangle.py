class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    
    def perimeter(self):
        return 2*(self.lenght + self.width)

    def area(self):
        return self.lenght*self.width

    def display(self):
        print(f"""
        Lenght:    {self.lenght}
        Width:     {self.width}
        Perimeter: {self.perimeter()}
        Area:      {self.area()}   
        
                
        """)

Rectangle1 = Rectangle(15,5)
Rectangle1.display()

    