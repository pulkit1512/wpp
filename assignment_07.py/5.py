class shape:
    def __init__(self):
        pass

    def area(self):
        pass
    
    def perimeter(self):
        pass

   
class circle(shape):
    def __init__(self,  radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius 

class rectange(shape):
    def __init__(self,length,breath):
        super().__init__()
        self.length=length
        self.breath=breath
    def area(self):
        return self.length*self.breath
    def perimeter(self):
        return 2*(self.length+self.breath)            
circle1=circle(5)
print(circle1.area())
print(circle1.perimeter())
rectange1=rectange(5,6)
print(rectange1.area())
print(rectange1.perimeter())    