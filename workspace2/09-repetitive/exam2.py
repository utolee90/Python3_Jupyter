a = 0
b = 0

for x in range(1, 101) : # 1~100 까지 정수
    if x%5 == 0 : a+=x
    if x%7 == 0 : b+=x
    
print("a=", a, ", b=", b)
print(a, "-", b, "=", a-b)