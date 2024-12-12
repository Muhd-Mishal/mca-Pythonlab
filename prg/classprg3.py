from operator import truediv

class student:
    tutor="BINDHU MAM"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
        print(__class__.tutor,"is the tutor")
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


first=student("sinu",21)
second=student("shambu",23)
comp=first.compare(second)
if comp:
    print("age is same")
else:
    print ("age is not same")
first.display()
second.display()

