x = 0
y = 0

for x in range(2,10):
    for y in range(1,10):
        print("%d*%d=%2d " %(x, y, x*y), end='')
    print()
print('-' * 30)

for y in range(1,10):
    for x in range(2,10):
        print("%d*%d=%2d " %(x, y, x*y), end='')
    print()
print('-' * 30)