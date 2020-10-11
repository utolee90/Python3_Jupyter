tup1 = (1, 2, 3, 4, 5)
print(tup1)
print('-' * 30)

# 서식 문자로 사용
print('%d %d' %(tup1[0], tup1[3]))
print('%s %d' %(tup1[0], tup1[3]))
print('-' * 30)

# format() 함수 사용
print("{} {}".format(tup1[0], tup1[3]))
print("{0} {0} {1}".format(tup1[0], tup1[3]))
print("{1} {0}".format(tup1[0], tup1[3]))
print('-' * 30)

# unpacking
