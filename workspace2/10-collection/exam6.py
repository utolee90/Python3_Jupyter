# 1차원 리스트
hong = []
hong.append(75)
hong.append(82)
hong.append(95)

kim = []
kim.append(88)
kim.append(64)
kim.append(70)

lee = [100, 95, 90]

tot = [0, 0, 0]

# 총점 구하기

for x in hong :
    tot[0] += x
    
tot[1] = sum(kim)
tot[2] = sum(lee)

print('홍길동 :', tot[0], tot[0]/len(hong))
print('김철수 :', tot[1], tot[1]/len(hong))
print('이영희 :', tot[2], tot[2]/len(hong))