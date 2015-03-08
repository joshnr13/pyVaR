import pylab
from pylab import *
import numpy as np
from numpy import *
import matplotlib

init,high,low,close,vol = np.loadtxt(open("table.csv","rb"),delimiter=",",skiprows=1,usecols=(1,2,3,4,5),unpack=True)

t = np.linspace(0,np.size(init),np.size(init))

figure()
plot(t,high,'r.-')
plot(t,close,'ko-')
plot(t,low,'r.-')
show()
