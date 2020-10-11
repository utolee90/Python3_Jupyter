import numpy

# 난수 numpy 배열 생성
f1 = numpy.random.rand() # 0 <= 난수 < 1 사이의 실수 1개 생성
print(f1)
print('-' * 30)

f2 = numpy.random.rand(2, 3) # 0 <= 난수 < 1 사이의 실수 2행, 3열 생성
print(f2)
print('-' * 30)

d1 = numpy.random.randint(1, 10)
print(d1)
print('-' * 30)