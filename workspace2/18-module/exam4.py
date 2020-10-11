from datetime import date

print(date.today())

# 년, 월, 일 설정
d = date(2020, 10, 4)
print(d)
print(d.__str__())

# 일수 계산
day1 = date(2019, 12, 31)
day2 = date.today()
day_num = day2 - day1
print('일수 :', day_num.days)

