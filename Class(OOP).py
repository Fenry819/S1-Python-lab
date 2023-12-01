class car:
    def __init__(self,name,prize,color):
        self.name=name
        self.prize=prize
        self.color=color

    def display(self):
        print("Name:",self.name)
        print("Prize:",self.prize)
        print("Color:",self.color)

car1=car("BMW",6000000,"Black")
car2=car("Mercedes-Benz",4500000,"Red")
car1.display()
car2.display()
