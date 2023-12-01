#Create a class rectangle with the attributes length and width.Overload less

class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def __lt__(self,other):
        return self.area()<other.area()
    def area(self):
        return self.length*self.width
r1=rectangle(2,3)
r2=rectangle(4,5)
if(r1<r2):
    print("Rectangle 1 is less than Rectangle 2")
else:
    print("Rectangle 2 is less than Rectangle 1")
