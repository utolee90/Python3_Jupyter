from matplotlib import pyplot
import numpy

city = ['서울','인천','대전','대구','울산','부산','광주']
lat = [37.56, 37.45, 36.35, 33.87, 35.53, 35.18, 35.16] # 위도
lng = [126.97, 126.70, 127.38, 128.60, 129.31, 129.07, 126.85] # 경도
pop_den = [16154, 2751, 2839, 2790, 1099, 4454, 2995] # 인구밀도

# 한글 설정 : 맑은 고딕
pyplot.rcParams['font.family'] = 'Malgun Gothic'
pyplot.rcParams['axes.unicode_minus'] = False

# 산점도 그래프 출력
# 색상지정
colors = ['r','g','b','c','m','k','y']
size = numpy.array(pop_den) * 0.2
pyplot.scatter(lng, lat, s=size, c=colors)