def inputNum(n) :
    for x in range(len(n)) :
        n[x] = int(input(str(x+1) + "번째 숫자 입력: "))
    print()  # 한줄 넘김
        
def outputNum(n) :
    print('** 출력 **')
    for x in range(len(n)) :
        print(n[x], end=' ')
    print()  # 한줄 넘김
    
n = [0 for x in range(5)]
inputNum(n)
outputNum(n)
    


