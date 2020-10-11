class HelloWorld :
    message = 'Hello'
    
    def setEng(self):
        self.message = 'Hello Python'
        
    def setKor(self):
        self.message = '안녕하세요. 파이썬'
        
    def setKor2(self):
        message = '파이썬 화이팅'
        self.message = '안녕 파이썬'
        HelloWorld.message = 'fighting'    
        
    def sayHello(self):
        print(self.message)
        
hello = HelloWorld()
hello.setEng()
hello.sayHello()
print('-' * 30)

hello.setKor()
hello.sayHello()
print('-' * 30)

hello.setKor2()
hello.sayHello()
print('-' * 30)