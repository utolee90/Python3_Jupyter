dic1 = {'a':1, 'b':2, 'c':'Hello', 'd':'파이썬'}
print(dic1)
print('-' * 30)

print("{} {} {} {}".format(dic1['a'], dic1['b'], dic1['c'], dic1['d']))
print("{a} {b} {c} {d}".format(**dic1)) # 키값을 생략하면 안됌
print("{d} {c} {b} {a}".format(**dic1))
print("{b} {a}".format(**dic1))
print("{d} {c} {b} {a} {d} {d}".format(**dic1))
print('-' * 30)

print("{} {} {} {}".format(*dic1))
print("{} {}".format(*dic1))
print("{0} {1} {2} {3}".format(*dic1))
print("{3} {2} {1} {0}".format(*dic1))
print("{1} {0}".format(*dic1))
print("{3} {2} {1} {0} {3} {2}".format(*dic1))



