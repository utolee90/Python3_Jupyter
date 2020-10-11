dic1 = {'a':1, 'b':2, 'c':'Hello', 'd':'파이썬'}
print(dic1)
print('-' * 30)

# 인덱싱 : dic1[키 값]
print(dic1['a'])
print(dic1['c'])
#print(dic1[0])
print('-' * 30)

# 데이터 추가
dic1['홍길동'] = '010-1234-5678'
print(dic1)
print(dic1['홍길동'])
print('-' * 30)

# 데이터 삭제
del(dic1['b'])
print(dic1)
print('-' * 30)

dic1.clear()
print(dic1)
print('-' * 30)