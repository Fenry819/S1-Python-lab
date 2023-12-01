class student():
    def getdata(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def display(self):
        print("Student name:", self.name)
        print("Roll number:", self.rollno)
        print("Course:", self.course)
class child(student):
    def getdata2(self,mark):
        self.mark=mark
    def display2(self):
        print("Total mark:",self.mark)
rn=int(input("Enter the roll number:"))
nm=input("Enter the name:")
co=input("Enter the course:")
m=int(input("Emter the mark:"))
stud1=child()
stud1.getdata(rn,nm,co)
stud1.getdata2(m)
stud1.display()
stud1.display2()