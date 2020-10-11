class Member:
    def __init__(self, name='none', age=0):
        self.__name = name
        self.__age = age
        
    def output(self):
        print('이름 :', self.__name)
        print('나이 :', self.__age)
        self.__test()
        
    def getName(self):              # getter
        return self.__name
    def setName(self, name):        # setter
        self.__name = name
        
    def getAge(self):
        return self.__age
    def setAge(self, age):
        self.__age = age

    def __test(self):
        print('__test() 함수')
        
mem = Member('홍길동', 25)     # mem.__init__('홍길동', 25)
#print('이름:', mem.__name)   # error, private 멤버
#print('나이:', mem.__age)
mem.output()
print('이름:', mem.getName())   # error, private 멤버
print('나이:', mem.getAge())
print('*' * 30)

mem.setName('고길동')
mem.setAge(40)
mem.output()
#mem.__test()           # private
print('*' * 30)

# 주의 (public 개념의 인스턴스 변수, 변수명이 같지만 서로 다름)
mem.__name = '김철수'
mem.__age = 30
print('이름 :', mem.__name)
print('나이 :', mem.__age)
print('*' * 30)

mem.output()