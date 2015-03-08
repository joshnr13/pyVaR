import pylab
from pylab import *
import numpy
import matplotlib
import forward_sim as simulator

Nt = 50
Wt = numpy.random.normal(0,1,Nt)

mu = 0.
sigma = 1.0
T = 1.0
P0 = 1e-6

Xm = simulator.milstein(mu,sigma,T,Nt,P0,Wt)
Xe = simulator.euler(mu,sigma,T,Nt,P0,Wt)

figure()
t = numpy.linspace(0.0,T,Nt)
plot(t,Xm,'rs-')
plot(t,Xe,'go-')
show()
