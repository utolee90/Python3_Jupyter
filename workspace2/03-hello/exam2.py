# 정수
print(5)

# 정수
print(5, 1, 2)

# 실수
print(1.5)

# 문자열
print("Hello World")

# boolean
print(False)

# 전부 출력
print(5, 1.2, "Hello World", False)

## 연산하여 출력
# 1. 숫자 + 숫자 = 연산결과
print(5.5+7)

# 2. 문자열 + 문자열 = 결합된 문자열
print("가"+"나")

# 3. 문자열 + 숫자 or boolean = ERROR
'''
print("가" + True)
print("가" + 1.5)
'''

# 4. 문자열 + str(숫자 or boolean) = 결합된 문자열
print("가" + str(True))
print("가" + str(1.5))

## 서식 출력
# 문자열을 출력할 때, 서식문자와 함께 사용하는 것
# 서식문자 : %d, %f, %s, %b
# %d : 정수, %자릿수d
# %f : 실수, %자릿수.소수점자릿수f
# %s : 문자열, %자릿수s
print("정수:%d, 실수:%f, 문자열:%s")
print("정수:%d, 실수:%1.2f, 문자열:%s" %(5, 5.5, "홍길동"))
print("-----------------")

# sep 속성 사용 => 분리문자 설정
print(5, 7, 9)
print(5, 7, 9, sep=',')

# end 속성 사용 => 마지막 문자 설정
print("가\n나")
print("Hello")
print("Python")
print("Hello\nPython")
print("Hello",end=' ')
print("Python")




























