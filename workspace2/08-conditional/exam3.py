year = int(input('연도를 입력해주세요 : '))

if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0) :
    print('%d년은 윤년입니다.' %year)
else :
    print(str(year) + '년은 평년입니다.')