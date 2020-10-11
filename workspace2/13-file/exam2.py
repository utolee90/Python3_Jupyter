# 파일 읽기 방법 1
f = open('D:/python_bkkwak/workspace/13-file/test.txt','r')
test = f.read()     # 파일을 통째로 읽어옴
print(test)
f.close
print('*' * 30)

# 파일 읽기 방법 2
f = open('test.txt','r')
while True:
    line = f.readline() # 1줄씩 읽어옴
    if not line : break
    print(line, end='') # 끝의 숨겨진 \n 을 없앰
f.close
print('*' * 30)

# 파일 읽기 방법 3
f = open('test.txt','r')
lines = f.readlines()       # 파일을 읽어온 후, 1줄 씩 리스트에 저장
print(lines)

for line in lines:
    print(line, end='')

f.close
print('*' * 30)

# 파일 읽기 방법 4
f = open('test.txt','r')

for line in f:              # f만 사용하면, 내부적으로 f.readlines() 동작을 함
    print(line, end='')

f.close
print('*' * 30)