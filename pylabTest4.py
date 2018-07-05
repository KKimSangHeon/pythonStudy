from pylab import plot, show, ylim, xlabel, ylabel
from numpy import linspace,sin

x = linspace (0,10,100 )
y = sin(x)

plot(x,y)
ylim(-100.1)

xlabel("x")
ylabel("y")
show()