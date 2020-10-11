from matplotlib import pyplot
import numpy

# 한글 설정 : 맑은 고딕
pyplot.rcParams['font.family'] = 'Malgun Gothic'
pyplot.rcParams['axes.unicode_minus'] = False

member_IDs = ['m01','m02','m03','m04']
ex_before = [27, 35, 40, 33]
ex_after = [30, 38, 42, 37]

# 막대 그래프 출력
index = numpy.arange(len(member_IDs))
pyplot.bar(index, ex_before)
pyplot.show()

colors=['r','g','b','c']
pyplot.bar(index, ex_before, color=colors, tick_label=member_IDs)
pyplot.show()

pyplot.bar(index, ex_before, color=colors, tick_label=member_IDs, width=0.4)
pyplot.show()