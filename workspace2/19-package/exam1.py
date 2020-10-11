# 패키지 안에 있는 모듈 사용법 1
# import 패키지명.패키지명.모듈
import packages.image.io_file.imgRead
packages.image.io_file.imgRead.pngread()
packages.image.io_file.imgRead.jpgread()
print('-' * 30)

# 패키지 안에 있는 모듈 사용법 2
# import 패키지명.패키지명.모듈명 as 별명
import packages.image.io_file.imgRead as img
img.pngread()
img.jpgread()
print('-' * 30)

# 패키지 안에 있는 모듈 사용법 3
# from 패키지명.패키지명 import 모듈명
from packages.image.io_file import imgRead
imgRead.pngread()
imgRead.jpgread()
print('-' * 30)

# 패키지 안에 있는 모듈 사용법 4
# from 패키지명.패키지명.모듈명 import 변수명 or 함수명 or 클래스명
from packages.image.io_file.imgRead import pngread
from packages.image.io_file.imgRead import jpgread
pngread()
jpgread()
print('-' * 30)

# 패키지 안에 있는 모듈 사용법 5