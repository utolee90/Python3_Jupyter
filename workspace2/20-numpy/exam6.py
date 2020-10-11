import numpy

# 모든 원소가 0 또는 1인 numpy 배열 생성
# numpy.zeros(갯수), numpy.ones(갯수)
# numpy.zeros((행, 열)), numpy.ones((행, 열)) 튜플로 설정
arr1 = numpy.zeros(10)
print(arr1)
print('-' * 30)

arr1 = numpy.zeros((3, 4))
print(arr1)
print('-' * 30)