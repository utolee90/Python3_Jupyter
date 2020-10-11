a = ()
print(a)
print('-' * 30)

tup1 = (10, 20, 30, 40, 50)
tup2 = ('c언어', 'Python', 'Java', 'JSP')
tup3 = ('파이썬',)
print(tup1, type(tup1))
print(tup2, type(tup2))
print(tup3, type(tup3))
print('-' * 30)

# indexing
print(tup1[0])
print(tup2[1])
print(tup3[0])
print('-' * 30)

# 데이터 추가, 수정, 삭제 안 됨
# tup1[0] = 100  # ERROR
print(tup1)
print('-' * 30)

#del(tup1[0]) = # ERROR
print(tup1)
print('-' * 30)