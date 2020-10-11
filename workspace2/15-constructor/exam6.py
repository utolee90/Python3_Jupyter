from random import sample

class Lotto :
    def __init__(self) :
        self.m = 0
        self.buyName = 0
        
    def inputBuyNum(self) :
        self.buyNum = int(input('구매 횟 수를 입력하세요 : '))
        print()     # 한 줄 넘김
        
    def outResult(self) :
        for i in range(6) :
            print('%2s' %self.m[i], end=' ')
            
        print()     # 한 줄 넘김
        
    def selectLotto(self) :
        for i in range(self.buyNum) :
            # 1. 번호 1세트 만들기
            self.m = sample([a for a in range(1, 46)], 6)
            # 2. 번호 1세트 정렬시키기
            self.m.sort()
            self.outResult()
            
lotto = Lotto()         # __init__ 호출 객체 생성
lotto.inputBuyNum()     # 구매 횟 수 입력받아 self.buyNum 에 저장
lotto.selectLotto()     # self.buyNum 만큼 for 문 돌면서 1~46 사이의 숫자 6개 생성
                        # self.m 에 저장