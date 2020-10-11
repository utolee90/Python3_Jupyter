f = open('test.txt', 'a')
for i in range(11, 16):
    date = str(i) + '번 째 줄입니다.\n'
    f.write(date)
f.close

f = open('test.txt', 'r')
print(f.read())
f.close