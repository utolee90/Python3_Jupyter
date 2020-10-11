import numpy

data1 = [10, 20, 30, 40]
data2 = [100, 200, 300, 400]

# (2행 ,2열) numpy 배열 생성
arr1 = numpy.array(data1).reshape(2,2)
arr2 = numpy.array(data2).reshape(2,2)

print(arr1)
print(arr1.shape)

print(arr2)
print(arr2.shape)
print('_' * 30)

