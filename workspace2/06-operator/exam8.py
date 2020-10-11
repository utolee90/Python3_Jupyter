'''
아이덴티티 연산자
is : 레퍼런스 변수의 주소값이 같은지 검사
    => True : 레퍼런스 값이 같음
       False : 레퍼런스 값이 다름

is not : 레퍼런스 변수의 주소값이 같지 않은지 검사
    => True : 레퍼런스 값이 다름
       False : 레퍼런스 값이 같음

id() : 레퍼런스 값 확인하는 함수
'''

a=1
b=2
c=1
d=a

print(id(a), id(b), id(c), id(d))
print('-' * 30)

print(a is b)
print(a is c)
print(a is d)
print('-' * 30)

print(a is not b)
print(a is not c)
print(a is not d)
print('-' * 30)