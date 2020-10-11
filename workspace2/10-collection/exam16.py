a = {1, 2, 3}
b = {1, 2, 3, 3, 3}

print(a)
print(b)
print('-' * 30)

print(len(a))
print(len(b))
print('-' * 30)

# 데이터 추가
a.add(4)
print(a)
print('-' * 30)

# 인덱싱
#print(a[0])   #error, index가 없기 때문에
print('-' * 30)

# 데이터 추출
print('pop :', a.pop())
print(a)
print('-' * 30)

# for
for x in a :
    print(x)

print(a)
print('-' * 30)

# 데이터 유무 확인
print(2 in a)
print(2 not in a)

print(sorted(a))

# 
a.remove(2)
print(a)
print('-' * 30)







