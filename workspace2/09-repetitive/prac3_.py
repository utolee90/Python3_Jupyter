while True:
    dan = int(input('몇 단을 출력할 지 입력하시오: '))
    for a in range(1, 10) :  # 1~9
        print('%d * %d = %d' %(dan, a, dan*a))
    
    choose = input("선택하시오(y: 계속) : ")
    
    if(choose=='y' or choose=='Y') : continue
    else :
        print('종료합니다.')
        break

