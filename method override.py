class Methodoverride1:
    def display(self):
        print("method invoked from from the base class")
class Methodoverride2(Methodoverride1):
    def display(self):
        print("method invoked from derived class")
ob=Methodoverride2()
ob.display()