class Area :
    def __init__(self, base=0, height=0):
        self.__base = base
        self.__height = height
    
    def setArea(self, base=0, height=0):
        self.__base = base
        self.__height = height
        
    def getBase(self) :
        return self.__base
    def setBase(self, base):
        self.__base = base
        
    def getHeight(self) :
        return self.__height
    def setHeight(self, height):
        self.__height = height
        
    
class Rectangle(Area) :
    def getArea(self):
        # 사각형 넓이 : 밑변 * 높이
        return self.getBase() * self.getHeight() 
    
class Triangle(Area) :
    def getArea(self):
        # 삼각형 넓이 : 밑변 * 높이 / 2
        return self.getBase() * self.getHeight() / 2
    
r = Rectangle()
t = Triangle()

r.setArea(10.5, 20.5)
t.setArea(10.5, 20.5)

print('사각형의 넓이 : ', r.getArea())
print('삼각형의 넓이 : ', t.getArea())