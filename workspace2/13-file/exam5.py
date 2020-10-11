students = []       # 학생 각각의 데이터를 묶어서 저장

with open('test.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
print('-' * 30)
    
for line in lines:
    # '\n' 지우기
    line = line.replace('\n','')
    print(line)
print('-' * 30)
    
for line in lines:
    # ',' 로 분리, 분리된 데이터를 리스트로 리턴
    line = line.replace('\n','')
    temp = line.split(',')
    print(temp)
    students.append(temp)
print('-' * 30)

print(students)

# 학생들 성적 출력 & 파일 출력 (result.txt)
f = open('result.txt', 'w')

for student in students:
    name, kor, eng, mat = student # unpacking
    tot = int(kor) + int(eng) + int(mat)
    avg = tot / 3
    result = '이름: {}, 국어: {}, 영어: {}, 수학: {}, 총점: {}, 평균: {:.1f}\n'\
            .format(name, kor, eng, mat, tot, avg)
    print(result, end='')
    f.write(result)

f.close()