def grade(avg) :
    if avg>=90 : return 'A'
    elif avg>=80 : return 'B'
    elif avg>=70 : return 'C'
    elif avg>=60 : return 'D'
    else : return 'F'

def input_jumsu() :
    kor = int(input('국어 점수 입력 : '))
    eng = int(input('영어 점수 입력 : '))
    return kor, eng   # 데이터가 여러개인 경우, 튜플로 리턴

def calc(kor, eng) :
    tot = kor + eng
    avg = tot / 2
    return avg

def output(avg) :
    print(grade(avg), '학점입니다.')
    
# 입력 : 변수에 데이터 저장하기
kor, eng = input_jumsu()   # 튜플의 unpacking
# 연산 : 변수에 저장된 데이터 가공하기
avg = calc(kor, eng)
# 출력 : 결과값 확인
output(avg)







