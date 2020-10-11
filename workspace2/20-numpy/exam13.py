import numpy
data1 = [10, 20, 30, 40 ,50 ,60]

arr1 = numpy.array(data1)
arr2 = numpy.arange(10, 100, 10).reshape(3, 3)

print(arr1)
print(arr2)
print('-' * 30)

# 1차원 인덱싱
print(arr1[2])

# 2차원 인덱싱