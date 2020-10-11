class CalcParent1 :
    def plus(self, x, y) :
        return x + y
    
    def minus(self, x, y) :
        return x - y
    
class CalcParent2 :
    def plus(self, x, y) :
        return x + y + 100
    
    def minus2(self, x, y) :
        return x - y - 100
    
# 부모 클래스들 중에 똑같은 메소드가 존재 할 경우,
# 첫 번째로 상속받은 클래스의 메소드가 우선적으로 적용 됨
class CalcChild(CalcParent1, CalcParent2) :
    def multiply(self, x, y) :
        return x * y
    def divide(self, x, y) :
        print(super().plus(5, 7))
        return x / y

    
calc = CalcChild()
print(calc.plus(5,7))
print(calc.minus(5,7))
#print(calc.plus2(5,7))
print(calc.minus2(5,7))
print(calc.divide(5,7))