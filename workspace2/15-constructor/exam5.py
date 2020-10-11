# 모듈 선언
#import 모듈명         # 모둘명.변수, 모듈명.함수, 모듈명.클래스

#from 모듈명
from random import random, randint, randrange, sample

# 0<= 실수 <1 사이의 실수 난수 1개 생성
print(random())    
print(randint(0,9))
print(randrange(5,10,2))
print('*' * 30)

# 임의의 문자 생성
# => ASCII 코드 사용 : a~z 97~122, A-Z 65~90
print(chr(randint(65, 90)))
print(chr(randint(97, 122)))
print('*' * 30)

# 리스트에서 임의의값 선택 출력하기
list1 = [1,2,3,4,5,6]
list2 = [a for a in range(1, 15)]
print(list1)
print(list2)
print(sample(list1,4))  # list1 의 임의의 숫자 4개 출력
print(sample(list2,1))  # list2 의 임의의 숫자 1개 출력