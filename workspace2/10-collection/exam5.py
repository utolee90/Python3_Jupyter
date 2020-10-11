str_list = ['국어', '영어', '수학', '사회', '한국사']
print(str_list)
print('-' * 30)

# 항목변경
str_list[3] = '과학'
print(str_list)
print('-' * 30)

# 항목추가 - 제일 뒷 자리
str_list.append('세계사')
print(str_list)
print('-' * 30)

# 항목추가 - 중간 자리
str_list.insert(2, '일본어')
print(str_list)
print('-' * 30)

# 정렬 (원본데이터는 변경되지 않음)
# 오름차순
str_list_sort = sorted(str_list) 
print(str_list)
print(str_list_sort)
print('-' * 30)

# 내림차순
str_list_sort = sorted(str_list, reverse=True)
print(str_list)
print(str_list_sort)
print('-' * 30)

# 정렬 (원본데이터 변경)
# 오름차순
str_list.sort()
print(str_list)
print('-' * 30)

# 내림차순
str_list.sort(reverse=True)
print(str_list)
print('-' * 30)

# 삭제 방법 1 : 위치
del(str_list[4])    # 인덱싱
print(str_list)
print('-' * 30)

del(str_list[0:2])  # 슬라이싱
print(str_list)
print('-' * 30)

# 삭제 방법 2
if '영어' in str_list : str_list.remove('영어') # 특정 데이터
print(str_list)
print('-' * 30)

str.clear()                                     # 전체 데이터



























