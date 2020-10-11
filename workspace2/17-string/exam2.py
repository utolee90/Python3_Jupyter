# 검색 관련
st1 = 'He likes apples, she likes too'

# 문자열에서 특정 문자열의 갯수를 구함
print(st1)
print(st1.count('like'))
print('-' * 30)

# 왼쪽에서 오른쪽으로 문자열 검색, 처음 나타난 위치를 구함
try:
    print(st1)
    print(st1.find('like'))
    prnt('-' * 30)
except:
    print('error message')
    
# 시작되는 단어인 지 검사
    print(st1)
    print(st1.startswith('likes'))
    print(st1.startswith('likes',3))
    print('-' * 30)

# 끝나는 단어인 지 검사
    print(st1)
    print(st1.endswith('likes'))
    print(st1.endswith('likes', 0, 26))
    print('-' * 30)