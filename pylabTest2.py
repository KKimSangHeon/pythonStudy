from pylab import plot, show
from numpy import loadtxt
data = loadtxt("values.txt", float)
x = data[:, 0]
y = data[:, 1]
plot(x,y)
print(x)

print('---')
print(y)

show()
