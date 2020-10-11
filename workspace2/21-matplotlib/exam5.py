from matplotlib import pyplot
import numpy

x = numpy.arange(-4.5, 5, 0.5)
y1 = 2 * x**2
y2 = 5*x + 20
y3 = 4 * x**2 + 10
y4 = 10 * x**2 + 10

# 그래프창 1개에 2x2 행렬 구조로 출력
pyplot.subplot(2, 2, 1)
pyplot.plot(x, y1)

pyplot.subplot(2, 2, 2)
pyplot.plot(x, y2)

pyplot.subplot(2, 2, 3)
pyplot.plot(x, y3)

pyplot.subplot(2, 2, 4)
pyplot.plot(x, y4)
pyplot.show()