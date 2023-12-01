class parent:
    def f(self):
        print("The f method in parent class")
class child(parent):
    def f(self):
        print("The f method in child class")
obj1=child()
obj1.f()