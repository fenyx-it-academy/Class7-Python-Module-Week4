class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def perimeter(self):
        self.perimeter=self.length*2+self.width*2
    def area(self):
        self.area=self.length*self.width
    def display(self):
        print (f'Rectangle lenght:{self.length}\nRectangle width:{self.width}\nRectangle perimeter:{self.perimeter}\nRectangle area:{self.area}\n')
        
a=Rectangle(3,4)
a.perimeter()
a.area()
print(a.display())

