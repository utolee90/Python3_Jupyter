class calc:
    @staticmethod
    def plus1(x, y):
        print('static method')
        return x+y
    
    def plus2(self, x, y):
        print('instance method')
        return x+y
    
    def f(self, x, y):
        result1 = plus3(x, y)      # 일반 메소드 (클래스 밖에)
        print(result1)
        result2 = self.plus2(x, y) # 인스턴스 메소드 (클래스 안에 ex > self.)
        print(result2)
        result3 = calc.plus1(x, y) # 스태틱 메소드 (클래스 안에 ex > 클래스.)
        print(result3)
    
def plus3(x, y):
    print('일반 함수')
    return x+y

print(calc.plus1(5, 7))
print('-' * 30)

cc = calc()
print(cc.plus2(2, 8))
print('-' * 30)

print(plus3(7, 9))
print('-' * 30)

cc.f(5, 7)
print('-' * 30)