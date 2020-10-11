# 클래스에 인스턴스 변수 만들고 사용하기
class Car :
    def drive(self):
        self.speed = 10     # 클래스에 인스턴스 변수 추가 방법 1
                            # 이 방법으로 변수를 추가할 때는
                            # 반드시 이 함수가 호출 되어야 한다.
    
    def output (self):
        print('모델, ', self.Model)
        print('색상, ', self.color)
        
    def output2 (self):
        print('모델, ', self.Model)
        print('색상, ', self.color)
        print('속도, ', self.speed)
        
# 클래스의 사용법
# 객체 생성 : 메모리에 변수와 함수가 만들어져서 사용할 수 있는 상태가 되는 것
myCar = Car()   # myCar : 객체

# 클래스에 인스턴스 변수 추가 방법 2
myCar.Model = 'E-Class'
myCar.color = 'blue'
myCar.output()
print('-' * 30)

myCar.drive()
myCar.output2()