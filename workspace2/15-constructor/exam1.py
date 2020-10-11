class Car:
    # 생성자 => 객체가 생성될 때, 자동으로 호출되는 메소드
    # 목적 => 객체에서 사용할 인스턴스 변수 생성 및 초기화
    def __init__(self, speed, color, model):
        print('생성자 호출')
        self.speed = speed
        self.color = color
        self.model = model

    def output(self):
        print('속도 :', self.speed)
        print('색상:', self.color)
        print('모델 :', self.model)
        
car = Car(0, 'blue', 'E-class') # car.__init__(0, 'blue', 'E-class')
car.output()
print('*' * 30)

car.__init__(10, 'red', 'F-class')
car.output()
print('*' * 30)