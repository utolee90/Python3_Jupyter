# 모듈 (~.py 파일)안의 클래스 사용
# => 모듈을 현재파일에 포함시켜야 함 => import

# import 방법 1
# import 파일명
import calcurator
#import exam5

myCalc1 = calcurator.Calc()
print(myCalc1.plus(5,7))
print(myCalc1.minus(5,7))
print('-' * 30)

#myCalc2 = exam5.calc()
#print(myCalc2.plus1(5,7))
#print(myCalc2.plus2(5,7))
#print('-' * 30)

# import 방법 2
# => from 파일명 import 클래스명
# => from 파일명 import 메소드명

from calcurator import Calc
myCalc = Calc()
print(myCalc1.plus(5,7))
print(myCalc1.minus(5,7))
print('-' * 30)
