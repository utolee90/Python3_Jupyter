class Car:
    # 생성자 => 객체가 생성될 때, 자동으로 호출되는 메소드
    # 목적 => 객체에서 사용할 인스턴스 변수 생성 및 초기화
    def __init__(self, speed=0, color=0, model=0):
        print('생성자 호출')
        self.speed = speed
        self.color = color
        self.model = model
        
    def output(self):
        print('속도 :', self.speed)
        print('색상:', self.color)
        print('모델 :', self.model)
        
# car1.__init__()
car1 = Car()
car1.output()
print('*' * 30)

# car1.__init__(10)
car1 = Car(10)
car1.output()
print('*' * 30)

# car1.__init__(20, 'blue')
car1 = Car(20,'blue')
car1.output()
print('*' * 30)

# car1.__init__(30, 'red', 'E-class')
car1 = Car(30, 'red', 'E-class')
car1.output()
print('*' * 30)