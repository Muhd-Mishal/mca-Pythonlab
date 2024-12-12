class car:
    nowheels="4 wheels"
    def __init__(self,m,c):
        self.milege=m
        self.company=c
    def display(self):
        print(self.milege)
        print(self.company)
        print(__class__.nowheels)

car1=car(4,"pagani")
car2=car(3,"koenigsegg")
car1.display()
car2.display()