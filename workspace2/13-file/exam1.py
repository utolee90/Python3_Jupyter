# 1. 파일 열기
f = open('test.txt', 'w')

# 2. 파일에 data 쓰기
for i in range(1, 11):
    date = str(i) + '번 째 줄입니다.\n'
    f.write(date)

# 3. 파일 닫기
f.close
print('쓰기 완료')