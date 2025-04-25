import math
class two_dimensional:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def magnitude(self):
        return (self.x**2+self.y**2)**0.5
    def rotation(self,angle):
        # Convert angle to radians
        theta = math.radians(angle)
        
        # Rotation formulas
        new_x = self.x * math.cos(theta) - self.y * math.sin(theta)
        new_y = self.x * math.sin(theta) + self.y * math.cos(theta)
        return new_x, new_y
    def distance(self,other):
        self.other=other
        distnce=((self.other.x-self.x)**2+(self.other.y-self.y)**2)**0.5
       
        return f"the distance between the two points is :{distnce}"
    def scalar_product(self,other,angle):
        self.other=other
        
        theta=math.radians(angle)
        return self.magnitude()*self.other.magnitude()*math.cos(theta)
    def vector_product(self,x1,y1,angle):
        self.x1=x1
        self.y1=y1
        self.other=two_dimensional(self.x1,self.y1)
        theta=math.radians(angle)
        return self.magnitude()*self.other.magnitude()*math.sin(theta)
class three_dimensional(two_dimensional):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z
    def magnitude(self):
        return (self.x**2+self.y**2+self.z**2)**0.5
    def rotation(self,angle):
        # Convert angle to radians
        theta = math.radians(angle)
        
        # Rotation formulas
        new_x = self.x * math.cos(theta) - self.y * math.sin(theta)
        new_y = self.x * math.sin(theta) + self.y * math.cos(theta)
        return new_x, new_y,self.z
    def distance(self,x1,y1,z1):
        self.x1=x1
        self.y1=y1
        self.z1=z1
        self.other=three_dimensional(self.x1,self.y1,self.z1)
        distnce=((self.x1-self.x)**2+(self.y1-self.y)**2+(self.z1-self.z)**2)**0.5
        return f"the distance between the two points is :{distnce}"        
    def scalar_product(self,other,angle):
        self.other=other
        theta=math.radians(angle)
        return f"The vector product of the given two 3d vector is :{self.magnitude()*self.other.magnitude()*math.cos(theta)}"
    def vector_product(self,other,angle):
        self.other=other
        theta=math.radians(angle)
        return f"The vector product of the given two 3d vector is :{self.magnitude()*self.other.magnitude()*math.sin(theta)}"
    

point3d=three_dimensional(1,2,3)
point3d1=three_dimensional(4,5,6)
print(point3d.distance(4,5,6))
print(point3d.scalar_product(point3d1,90))
print(point3d.vector_product(point3d1,90))
print(point3d.rotation(90))
print(point3d.magnitude())