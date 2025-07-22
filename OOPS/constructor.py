class rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y =y

    def area(self):
        print("Area of Rectangle:",self.x*self.y)

    def perimeter(self):
        print("Perimeter:",2*(self.x+self.y))



x = 10
y = 20
c = rectangle(x,y)
c.area()
c.perimeter()

