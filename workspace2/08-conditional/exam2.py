num1 = int(input('첫 번째 정수를 입력하세요 : '))
num2 = int(input('두 번째 정수를 입력하세요 : '))

if num1 > num2 :
    num1, num2 = num1, num2

else :
        num1, num2 = num2, num1
    
print('큰 값 : %d, 작은 값 : %d' %(num1, num2))