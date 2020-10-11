# 양수 : '0123456'
# 음수 : '7654321'

st1 = '01234567'
print(st1)
print('-'*20)

# 인덱싱 (indexing) : 문자 1개씩 읽어오기
# => [k] : 특수문자 제외
print(st1[0])
print(st1[1])
print(st1[2])
print(st1[3])
print(st1[4])
print(st1[5])
print(st1[6])
print(st1[7])
print('-'*20)

# 슬라이싱 (slicing) : 문자들을 부분적으로 읽어오기
# => [s:t] -> s 부터 t-1 까지 문자열 추출
# => [s:t:step] -> s 부터 t-1 까지 문자열 추출, step:구간
print(st1[0:8])
print(st1[:7])
print(st1[3:1]) # 못읽어옴
print('-'*20)

print(st1[-6:-4])
print(st1[:-4])
print(st1[-6:])
print('-'*20)

print(st1[::])
print(st1[::1])
print(st1[::2])
print(st1[::3])
print('-'*20)

print(st1[::])
print(st1[::-1])
print(st1[::-2])
print(st1[::-3])
print('-'*20)

# 문자열 인덱싱과 슬라이싱의 주의할 점
# => 문자열 읽기만 되고, 쓰기는 안 됨, 데이터 부분 변경은 안 됨 
print(st1)
print(st1[0])
#st1[0]='x' ERROR
#print(st1[1:3]) = 'xy' ERROR
print('-'*20)

# 문자열 부분변경하기
print(st1)
st2 = st1[0] + 'xy' + st1[3:]
print(st2)
st2 = st1[0:2] + 'xy' + st1[4:]
print(st2)
print('-'*20)

# 멤버쉽 확인하기
# => in 연산자 : 문자열이 포함되어 있는지 검사
# => 결과 : True (있음), False (없음)
print(st1)
print('12' in st1)
print('ab' in st1)
print('-'*20)

# 문자열 길이 확인하기
print(st1)
print(len(st1))









