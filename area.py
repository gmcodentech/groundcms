class Rectangle:
    def __init__(self,w,l):
        self.width = w
        self.length = l
    
    def area(self):
        return self.width * self.length

r = Rectangle(2.2,1.4)
a = r.area()
print(f"Area is {a}");