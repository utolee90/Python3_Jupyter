jumsu = []

for i in range(5) :
    tmp = int(input(str(i+1) + "번 학생의 점수를 입력 : "))
    jumsu.append(tmp)
    
tot = sum(jumsu)    
avg = tot / len(jumsu)

print(jumsu)
print("총점 : {}, 평균 : {}".format(tot, avg))

