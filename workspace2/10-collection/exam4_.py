a = [1, 2, 3]

print(a)
print('-' * 30)

# 인덱싱 : 데이터 1개 
a[2] = 300
print(a)
print('-' * 30)

a[1] = ['a', 'b', 'c']
print(a)
print('-' * 30)

print(a[1][1])
print('-' * 30)

# 슬라이싱 : 데이터 여러개
a[1:2] = ['x', 'y', 'z']
print(a)
print('-' * 30)

a[1:3] = [10, 20]
print(a)
print('-' * 30)







