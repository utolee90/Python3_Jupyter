def sumAndMul(a, b) :
    tot = a + b
    mul = a * b
    return tot, mul   # 여러개 리턴일 경우, 튜플로 리턴됨

result = sumAndMul(5, 7)
print('합 = ', result[0])
print('곱 = ', result[1])

