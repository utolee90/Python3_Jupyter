a = 'abc2dcba'

# if 삼항 연산식
# => (참일 때 값) if 조건식 else (거짓일 때 값)
print(a, " : 회문" if a==a[::-1] else " : 회문 아님")
print(a[::-1])

'''
if a == a[::-1] :
    print(a, ': 회문')
else:
    print(a, ': 회문아님')
'''

'''
b = 'abcdefg'
print(b)
print(b[2:5])
print(b[:])
print(b[::2])
print(b[::-1])
'''