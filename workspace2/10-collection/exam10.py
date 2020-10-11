tup1 = (10, 20, 30, 40, 50, 30)
tup2 = ('c언어', 'Python', 'Java', 'JSP', '파이썬')

print(tup1)
print(tup2)
print('-' * 30)

tup3 = tup1 + tup2
tup4 = tup1 * 3
print(tup3)
print(tup4)
print('-' * 30)

print(30 in tup1)
print(30 not in tup1)
print('-' * 30)

print(tup1.index(30))
print(tup1.index(30, 4))
p = tup1.index(30)
print(tup1.index(30, p+1))
print('-' * 30)

print(tup1.count(20))
print(tup1.count(30))
print('-' * 30)

# 파이썬 내장함수 사용
print(len(tup1))
print(max(tup1))
print(max(tup2))
print(min(tup1))
print(max(tup2))
print('-' * 30)

print(sorted(tup1))
print(sorted(tup1, reverse=True))