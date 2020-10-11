'''
bool(데이터) : 데이터가 있는지 없는지 검사
    => True : 데이터가 있음
    => False : 데이터가 없음
'''

# 숫자
print(bool(1))
print(bool(0))
print(bool(-1))
print(bool(0.0))
print(bool(1234567.1234567))
print(bool(-1234567.1234567))
print('-' * 30)

# 문자열
print(bool('abcd'))
print(bool(''))
print(bool(' '))
print('-' * 30)

# none
a = None
print(a, type(a))