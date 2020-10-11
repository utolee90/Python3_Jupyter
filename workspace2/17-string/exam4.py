# 분리와 결합
st1 = 'He likes apples, she likes too'

# 특정 문자를 기준으로 문자열 분리
st2 = st1.split()
print(st1)
print(st2)
print('-' * 30)

st2 = st1.split(',')
print(st1)
print(st2)
print('-' * 30)

st2 = st1.split(' ', 2)
print(st1)
print(st2)
print('-' * 30)

# 라인으로 분리
st3 = '''\
첫 번째 줄
두 번째 줄
세 번째 줄'''
st2 = st3.splitlines()
print(st3)
print(st2)
print('-' * 30)

# 리스트의 문자열을 특정 문자로 결합
st2 = st1.split()
print(st2)

st3 = (':').join(st2)
print(st3)
print('-' * 30)