class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return(self.length*self.breadth)
    def perimeter(self):
        return(2*(self.length+self.breadth))
r1=rectangle(5,3)
r2=rectangle(4,6)
r1.area()
r1.perimeter()
r2.area()
r2.perimeter()

print("area of r1" ,r1.area(),"perimeter of r1",r1.perimeter())
print("area of r2",r2.area(),"perimeter of r2",r2.perimeter())
