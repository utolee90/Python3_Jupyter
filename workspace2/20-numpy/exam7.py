import numpy

# 단위 행렬로 numpy 배열 생성
# 단위 행렬 : n x n 정사각형 행렬에서 주 대각선이 모두 1이고 나머지는 모두 0 인 행렬
# numpy.eye(숫자)
arr1 = numpy.eye(10)
print(arr1)