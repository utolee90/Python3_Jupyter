import numpy

data1 = [10, 20, 30, 40]
data2 = [100, 200, 300, 400]

# numpy 배열 생성
arr1 = numpy.array(data1)
arr2 = numpy.array(data2)

print(arr1)
print(arr2)
print('-' * 30)

# 사칙 연산
arr_add = arr1 + arr2
print(arr_add)

list_add = data1 + data2
print(list_add)

arr_add = arr1 + 3
print(arr_add)

# list_add = data1 + 3 
