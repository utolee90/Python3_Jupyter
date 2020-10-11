# 2차원 리스트
name = ['홍길동', '김철수', '이영희']

# 내포 방법으로 리스트 만들기
score = [[] for j in range(3)]
#score = [[0 for i in range(3)] for j in range(3)]
print(score)

score[0].append(75)
score[0].append(82)
score[0].append(95)

score[1].append(88)
score[1].append(64)
score[1].append(70)

score[2].append(100)
score[2].append(95)
score[2].append(90)

print(score)
print('-' * 30)

# 총점 구하기
tot =[0, 0, 0]
for i in range(3) : 
    tot[i] = sum(score[i])
    print('%s, 총점=%s, 평균=%s' %(name[i], tot[i], tot[i]/len(score[i])))