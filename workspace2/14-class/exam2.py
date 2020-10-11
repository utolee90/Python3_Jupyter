class Car :
    speed = 5             # 클래스 안에서, 멤버함수 밖에 위치한 변수 (클래스 변수)
    
    def drive(self):
        self.speed = 10   # 클래스 안에서, 멤버함수 안에 위치한 변수 (인스턴스 변수)
        
        
    def output(self):
        print ('Car.speed :', Car.speed)
        print ('self.speed :', self.speed)
        
print(Car.speed)
print('-' * 30)

myCar = Car()
myCar.output()
print('-' * 30)

myCar.drive()
myCar.output()
print('-' * 30)

print(myCar.speed)
print(Car.speed)
myCar.speed = 100
Car.speed = 200
print('-' * 30)

print(myCar.speed)
print(Car.speed)
print('-' * 30)