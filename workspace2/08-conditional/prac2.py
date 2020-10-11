jumsu1 = int(input("국어 점수 입력해 : "))
jumsu2 = int(input("영어 점수 입력해 : "))

sum1 = jumsu1 + jumsu2
avg1 = sum1 / 2 
if avg1 >= 90 : hak = 'A'
elif avg1 >= 80 : hak = 'B'
elif avg1 >= 70 : hak = 'C'
elif avg1 >= 60 : hak = 'D'
else : hak = 'F'

print('총점 : ', sum1)
print('평균 : ', avg1)
print('학점 : ', hak)