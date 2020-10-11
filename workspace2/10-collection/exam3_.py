str_list = ['국어', '영어', '수학', '사회', '한국사']
print(str_list)

# 슬라이싱
list1 = str_list[1:3]
print(str_list[1:3])
list1 = str_list[:3]
print(str_list[:3])
list1 = str_list[1:]
print(str_list[1:], type(list1))
print('-' * 30)

# 데이터 검사
if '사회' in str_list : print('존재합니다.')
else : print('없습니다.')
print('-' * 30)

# for문 사용
for subject in str_list :
    print(subject)






