class Rectangle:
    def __init__(self, w, b):
        self.width = w
        self.length = b

    def area(self):
        return self.width * self.length

r = Rectangle(2.2, 1.4)


a = r.area()
print(f"Area is {a}")
