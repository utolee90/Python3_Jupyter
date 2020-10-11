# 리스트 내포
result = [0 for a in range(5)]
print(result)
print('-' * 30)

result = [num*3 for num in range(1, 5) if num%2 == 0]
print(result)
print('-' * 30)

# enumerate : 리스트의 위치 값과 데이터를 묶어서 관리
list1 = ['foo', 'bar', 'baz']
for i, v in enumerate(list1) :
    print(i, v)
print('-' * 30) 

# zip(리스트, 리스트) : 리스트를 동일한 위치 값끼리 묶어서 관리하는 함수
list2 = ['one', 'two', 'three']
for a, b in zip(list1, list2):
    print(a, b)
