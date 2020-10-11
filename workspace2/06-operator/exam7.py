'''
소속 연산자
=> 문자열, 리스트, 튜플 등에서 사용

in : 어떤 데이터가 특정 데이터안에 존재하는지 검사
=> 결과값은 True : 존재함, False : 존재하지 않음

not in : 어떤 데이터가 특정 데이터안에 존재하지 않는지 검사
=> 결과값은 True : 존재하지 않음, False : 존재함
'''

st1 = 'abcedfg'
print('st1 =', st1)
result = 'fg' in st1
print(result)

result = 'xy' in st1
print(result)

result = 'fg' not in st1
print(result)

result = 'xy' not in st1
print(result)