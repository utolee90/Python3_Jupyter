'''
print(range(0, 5, 1))   # 0, 1, 2, 3, 4
print(range(0, 5))      # 0, 1, 2, 3, 4
print(range(5))         # 0, 1, 2, 3, 4
# print(range(0, 5, 0,1)) # 증감 값 실수 사용불가

print(range(0, 5, 2))   # 0, 2, 4
'''

a= ""
for x in range(5) :
    a += str(x) + " "
    print(a)
print('-' * 30)

a= ""
for x in range(0,5,1) :
    a += str(x) + " "
    print(a)