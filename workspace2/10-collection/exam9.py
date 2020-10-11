tup1 = (10, 20, (30, 40, 50))
tup2 = ('c언어', 'Python', 'Java', 'JSP')

# 인덱싱
print(tup1[0])
print(tup2[2][1])
print(tup2[1])
print('-' * 30)

# 슬라이싱
print(tup2[1:3])
print(tup2[:3])
print(tup2[1:])
print(tup2[::2])
print(tup2[::-1])