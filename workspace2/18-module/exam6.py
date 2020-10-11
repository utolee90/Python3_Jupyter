import calendar

#  달력 출력
print(calendar.calendar(2020))
print('-' * 30)

print(calendar.month(2020, 6))
print('-' * 30)

# 시작 요일과 일수 출력
# (0, 30) : 0 -> 요일수 (0~6, 월~일)
a = calendar.monthrange(2020, 6)
print(a)
print('-' * 30)

# 일주일의 시작요일 출력 및 설정
print(calendar.firstweekday())

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.firstweekday())

print(calendar.month(2020, 6))
print('-' * 30)

# 윤년 확인
c = calendar.isleap(2020)
if c : print('2020년은 윤년')
else : print('2020년은 평년')








