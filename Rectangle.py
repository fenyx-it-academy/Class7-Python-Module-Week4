## 2. Rectangle

class rectangle:
    def __init__(self,lng,wd):
        self.lng = lng
        self.wd = wd
    
    def perimeter(self):
        return 2*(self.lng+self.wd)
    
    def area (self):
        return (self.lng*self.wd)

    def display(self):
        print(f"Rectangle dimentions are {self.lng}, {self.wd}. Perimeter is {rectangle.perimeter(self)}. Area is {rectangle.area(self)}")



rect = rectangle(5,10)
rect.perimeter()
rect.area()
rect.display()
