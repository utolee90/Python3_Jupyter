a = [1, 2, 3, 4, 5, 5]
b = (6, 7, 8, 9, 10)
c = {11, 12, 13}

print(a, type(a))
print(b, type(b))
print(c, type(c))
print('-' * 30)

# 리스트를 튜플과 세트로 변환
d1 = tuple(a)
print(d1, type(d1))
print('-' * 30)

e1 = set(a)
print(e1, type(e1))
print('-' * 30)

# 튜플을 리스트와 세트로 변환
d1 = list(b)
print(d1, type(d1))
print('-' * 30)

e1 = set(b)
print(e1, type(e1))
print('-' * 30)

# 세트를 리스트와 튜플로 변환
d1 = list(c)
print(d1, type(d1))
print('-' * 30)

e1 = tuple(c)
print(e1, type(e1))
print('-' * 30)





