def add (x=1, y=100):
    tot = 0
    for i in range(x, y+1):
        tot += i
    return tot
    
print(' 1 ~ 100 사이의 합 :', add())
print('30 ~ 100 사이의 합 :', add(30))
print('20 ~ 200 사이의 합 :', add(20, 200))