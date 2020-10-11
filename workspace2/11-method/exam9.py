def calc_area(radius) :
    global area                 # 전역 변수
    area = 3.14 * radius**2     # 원의 넓이

area = 0
calc_area(5)
print('원의 넓이 :', area)