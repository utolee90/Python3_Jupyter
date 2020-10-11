'''
논리 연산자 : 수학의 집합 기호를 명령어로 만들어 놓은 것
            => boolean 연산
<진리표>
x        y           x and y        x or y         not x
true     true        true           true           false  
true     false       false          true           false
false    true        false          true           true 
false    false       false          false          true 
'''

a = 100
b = 200
x = 5
y = 3

r1 = a >= b
r2 = x >= y
print(r1, r2)
print('=' * 30)

result = r1 and r2
print(result)
print('=' * 30)

result = r1 or r2
print(result)
print('=' * 30)

result = not r1
print(result)
print('=' * 30)