# 대입 연산자 : =, +=, -=, ...
source = 100

source += 100   #source = source + 100
print('+', source,type(source))

source -= 100   #source = source - 100
print('-', source,type(source))

source *= 100   #source = source * 100
print('*', source,type(source))

source /= 100   #source = source / 100
print('/', source,type(source))

source **= 100   #source = source ** 100
print('**', source,type(source))

source //= 100   #source = source // 100
print('//', source,type(source))

source %= 100   #source = source % 100
print('%', source,type(source))