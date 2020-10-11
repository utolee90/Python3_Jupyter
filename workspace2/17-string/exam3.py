# 편집 및 치환
st1 = '     He likes apples, she likes too     '

# 좌, 우 공백 제거
st2 = st1.strip()
print('---' + st1 + '---')
print('---' + st2 + '---')
print('-' * 30)

# 오른쪽 공백 제거
st2 = st1.rstrip()
print('---' + st1 + '---')
print('---' + st2 + '---')
print('-' * 30)

# 왼쪽 공백 제거
st2 = st1.lstrip()
print('---' + st1 + '---')
print('---' + st2 + '---')
print('-' * 30)

# 문자열 바꾸기
st2 = st1.replace('like', 'love')
print(st1)
print(st2)
print('-' * 30)