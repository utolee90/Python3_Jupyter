class Character :
    name = 0        # 클래스 변수
    age = 0         # 클래스 변수
    
d = Character()
d.name = '둘리'     # 인스턴스 변수
d.age = 19          # 인스턴스 변수
print(d.name, ',', d.age)
print(Character.name, ',', Character.age)
print('-' * 30)

h = Character()
h.name = '희동'
h.age = 3
print(h.name, ',', h.age)
print(Character.name, ',', Character.age)
print('-' * 30)

Character.name = '길동'
Character.age = 40
print(d.name, ',', d.age)
print(h.name, ',', h.age)
print(Character.name, ',', Character.age)
print('-' * 30)
