class Car :
    def __init__(self, speed=0, color=0, model=0):
        self.speed = speed
        self.color = color
        self.model = model

    # 용도 : 모든 인스턴스 변수값을 문자열로 리턴
    def __str__(self) :
        return '속도: %s, 색상: %s, 모델: %s'\
            %(self.speed, self.color, self.model)
        
    def dirve(self, speed) :
        self.speed = speed

    def output(self):
        print('속도 :', self.speed)
        print('색상:', self.color)
        print('모델 :', self.model)
        
car = Car(0, 'blue', 'E-class') # car.__init__(0, 'blue', 'E-class')
car.output()
print('*' * 30)

print(car) # car.__str__()