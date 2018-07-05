from __future__ import division
from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid
import numpy

data = numpy.loadtxt("sunspot.txt", float)

def movingaverage(interval, window_size):
    window = numpy.ones(int(window_size))/float(window_size)
    return numpy.convolve(interval, window, 'same')

x = data[:,0];y = data[:,1]

plot(x,y,"k.")
y_av = movingaverage(y, 10)
plot(x, y_av,"r")
xlim(0,1000)
xlabel("Month since Jan 1749")
ylabel("No. of Nun spots")
grid(True)
show()