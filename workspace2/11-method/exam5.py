def total(start, end) :
    tot = 0
    for x in range(start, end+1) :
        tot += x
    
    return tot

b = total(1, 10000)
print(b)
print('-' * 30)

a = [x for x in range(1, 10001)]
b = sum(a)
print(b)

