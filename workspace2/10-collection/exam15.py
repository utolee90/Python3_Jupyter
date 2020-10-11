dic = {101:'사과', 102:'복숭아', 103:'감', 104:'바나나'}
print(dic)
print('-' * 30)

# 키, 데이터, 함께 처리
print(dic.keys())
print(dic.values())
print(dic.items())
print('-' * 30)

# 리스트로 변환
list_keys = list(dic.keys())
list_values = list(dic.values())
list_items = list(dic.items())
print(list_keys, type(list_keys))
print(list_values, type(list_values))
print(list_items, type(list_items))
print('-' * 30)

# 인덱싱
print(list_keys[1])
print(list_values[1])
print(list_items[1])
print(list_items[1][0])
print(list_items[1][1])









