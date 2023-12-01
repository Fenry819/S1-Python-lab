class rect:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def display1(self):
        Area=self.length*self.breadth
        print("Area=",Area)
    def display2(self):
        Perimeter=2*(self.length+self.breadth)
        print("Perimeter=",Perimeter)

n=int(input("Choose option: \n1.Area \n2.Perimeter \n"))
l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
val1=rect(l,b)
if(n==1):
    val1.display1()
else:
    val1.display2()