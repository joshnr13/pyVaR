import pylab
from pylab import *
import joblib
from joblib import Parallel, delayed
import numpy
import matplotlib
import forward_sim as simulator

Nt = 100
Nsamples = 5000
mu = 0.0
sigma = 0.05
T = 1.0
P0 = 1e-6

Pf = numpy.zeros(Nsamples)

num_cores = 2

def Xend(i):
    Wt = numpy.random.normal(0.,1.,Nt)
    Xm = simulator.milstein(mu,sigma,T,Nt,P0,Wt)
    return Xm[-1]
    
Pf = Parallel(n_jobs=num_cores)(delayed(Xend)(i) for i in range(Nsamples)) 

res_feq,res_bin = numpy.histogram(Pf,100)

figure()
plot(res_bin[1:len(res_bin)],res_feq,'ok')
show()
