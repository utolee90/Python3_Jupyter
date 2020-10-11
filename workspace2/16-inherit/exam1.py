class CalcParent :
    def plus(self, x, y) :
        return x + y
    
    def minus(self, x, y) :
        return x - y
    
# 상속 : 기존 클래스를 건드리지 않고,
#       어떤 기능을 추가하거나, 수정하기 위함
class CalcChild(CalcParent) :
    def multiply(self, x, y) :
        return x * y
    def divide(self, x, y) :
        return x / y
    def plus(self, x, y) :
        print(super().plus(5,7))
        return x + y + 10
    
calc1 = CalcParent()
print(calc1.plus(5, 7))
print(calc1.minus(5, 7))
print('*' * 30)

calc2 = CalcChild()
print(calc2.plus(5, 7))
print(calc2.minus(5, 7))
print(calc2.multiply(5, 7))
print(calc2.divide(5, 7))
print('*' * 30)