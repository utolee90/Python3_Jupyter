# 람다 함수 1
fun1 = lambda x=1, y=2, z=3 : x + 2*y + 5*z 
print(fun1())
print('-' * 30)

# 람다 함수 2
print((lambda x=1, y=2, z=3 : x + 2*y + 5*z)(3,4,5))