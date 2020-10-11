# 모듈 사용법 1
# import 폴더명.모듈명
import modules.my_module2
modules.my_module2.my_func2()
print('-' * 30)

# 모듈 사용법 2
# import 폴더명.모듈명 as 별명
import modules.my_module2 as my
my.my_func2()
print('-' * 30)

# 모듈 사용법 3
# from 폴더명.모듈명 import 변수, 함수, 클래스
from modules.my_module2 import my_func2
my_func2()
print('-' * 30)

# 모듈 사용법 4
# from 폴더명.모듈명 import 변수, 함수, 클래스 as 별명
from modules.my_module2 import my_func2 as func2
func2()
print('-' * 30)









