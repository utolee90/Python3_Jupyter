# + 연산자
# 정수 + 실수 = 실수
# 문자열 + 문자열 = 문자열
# 정수, 실수, bool 문자열로 변경 => str() 함수 사용
#
# 문자열 => 정수 : int() 함수 사용
# 문자열 => 실수 : float() 함수 사용

str1 = '123'
str2 = '5.567'
num1 = int(str1)
num2 = float(str2)
print('-'*20)

print(str1)
print(str2)
print(num1)
print(num2)
print('-'*20)

print(type(str1))
print(type(str2))
print(type(num1))
print(type(num2))
print('-'*20)

# *  연산자
# 숫자 * 숫자 = 숫자
# 문자열 * 문자열 => ERROR
# 문자열 * 숫자 => 문자열을 숫자만큼 반복된 문자열 생성

print(num1*num1)
print('ab' * 5)
print(5 * 'ab')
print('-'*20)