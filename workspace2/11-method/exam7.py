# 매개변수의 갯수가 정해져 있지 않을 때
# => 함수로 전달되는 값이 가변될 때
# args : 데이터가 튜플로 전달됨
def total(*args) :
    tot = 0
    for a in args:
        tot += a
    return tot

print(total(2, 4, 6))
print(total(2, 4, 6, 8, 10))
print(total(2))
print(total())
