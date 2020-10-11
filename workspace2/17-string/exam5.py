st1 = 'He likes apples, she likes too'

# 가운데 맞춤
st2 = st1.center(50)
print(st1 + '---')
print(st2 + '---')
print('*' * 30)

st2 = st1.center(50, '-')
print(st1 + '---')
print(st2 + '---')
print('*' * 30)

# 오른쪽 맞춤
st2 = st1.rjust(50)
print(st1 + '---')
print(st2 + '---')
print('*' * 30)

# 왼쪽 맞춤
st2 = st1.ljust(50)
print(st1 + '---')
print(st2 + '---')
print('*' * 30)

# 탭문자 (들여쓰기) \t 8자 공백문자로 변환
st3 = '1\t2345\t4467'
st2 = st3.expandtabs()
print(st3)
print(st2)
print('*' * 30)