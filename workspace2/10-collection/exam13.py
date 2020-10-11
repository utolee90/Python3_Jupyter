dic1 = {'a':1, 'b':2, 'c':'Hello', 'd':'파이썬'}
print(dic1)
print('-' * 30)

# 키 값 유무
print('c' in dic1)
print('c' not in dic1)
print('-' * 30)

# 키 값만 확인
print(dic1.keys())
print('-' * 30)

# value(데이터)만 확인
print(dic1.values())
print('-' * 30)

# 키 값과 value(데이터)  모두 확인
print(dic1.items())
print('-' * 30)

print('Hello' in dic1.values())
print('-' * 30)

# 개별 데이터 확인
print(dic1['c'])
print(dic1.get('c'))
print('-' * 30)

# print(dic1['f'])      # Error, Key 없음
print(dic1.get('f'))
print('-' * 30)

# for문 사용
for key in dic1.keys() : 
    print(key, end=' ')
print()    
k = dic1.keys()
# print(k[0])           # Error, 인덱싱을 사용못함
k_list = list(dic1.keys())
print(k_list[0])
print('-' * 30)

for values in dic1.values() : 
    print(values, end=' ')
print()
print('-' * 30)

for key, val in dic1.items() :
    print(key, val, end=', ')
print('-' * 30)
    
# 정렬
for key in sorted(dic1.keys()) : 
    print(key, dic1[key], end=', ')
print('-' * 30)    
    
for key in sorted(dic1.keys(), reverse=True) : 
    print(key, dic1[key], end=', ')