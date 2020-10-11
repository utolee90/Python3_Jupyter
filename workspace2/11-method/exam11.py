# 일반 함수
def square1(x):
    return x**2

def test():
    print('test')
    return  # 기본적으로 return을 사용해야 하지만,
            # return 값이 없으면 생략 가능하다.   

print(square1(5))
a = test()  # 함수에 return 이 없어도 기본 return 동작

print(a)
print('-' * 30)

# 람다 함수 1
# lambda 매개변수 : 리턴 값
square2 = lambda x : x**2
print (square2(5))

test2 = lambda : print('test')
a = test2()
print(a)
print('-' * 30)

# 람다 함수 2
print((lambda y : y**2)(5))
(lambda : print('test'))()