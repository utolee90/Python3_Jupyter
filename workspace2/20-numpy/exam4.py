import numpy

# numpy 배열을 m x n 행렬(2차원)로 변경
# => numpy 배열을 l x m x n 행렬(3차원)로 변경
# numpy.reshape(m, n)
# => 다른 차원으로 변경 할 때, 변경되는 차원의 행과 열의 갯 수가 일치해야 함
arr1 = numpy.arange(1, 13)
print(arr1)
print(arr1.shape)
print('-' * 30)

arr2 = arr1.reshape(4, 3)
print(arr2)
print(arr2.shape)
print('-' * 30)