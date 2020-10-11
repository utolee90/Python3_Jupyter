# 산술 연산자 주의할 점

# 정수끼리 계산 : 정수의 나눗셈은 float 타입
a=6
b=3
result1 = a / b
print(result1, type(result1))
print('-'*20)

# 0으로 나눌경우 무조건 Error But Java는 infinity 출력
a=6.0
b=0.0
result1 = a / b
print(result1, type(result1))
print('-'*20)