from pylab import plot, show,ylim, xlabel, ylabel
from numpy import linspace, sin, cos
x = linspace(0,10,100)
y1 = sin(x)
y2 = cos(x)
plot(x,y1,"k-")
plot(x,y2,"k--")

ylim(-5,1.1)
xlabel("x axis")
ylabel("y = sin x")
show()

