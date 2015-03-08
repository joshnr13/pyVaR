import numpy as np

def milsteinW(mu,sigma,T,Nt,P0):
    dt = T/Nt
    Wt = np.random.normal(0,1,Nt)
    P  = np.zeros(Nt)
    P[0] = P0
    for i in range(len(P)-1):
        P[i+1] = P[i] + mu*P[i]*dt + P[i]*sigma*Wt[i]*np.sqrt(dt) + 0.5*sigma**2*P[i]*( Wt[i]**2*dt - dt )
    return P
    
def milstein(mu,sigma,T,Nt,P0,Wt):
    dt = T/Nt
    P  = np.zeros(Nt)
    P[0] = P0
    for i in range(len(P)-1):
        P[i+1] = P[i] + mu*P[i]*dt + P[i]*sigma*Wt[i]*np.sqrt(dt) + 0.5*sigma**2*P[i]*( Wt[i]**2*dt - dt )
    return P

def eulerW(mu,sigma,T,Nt,P0):
    dt = T/Nt
    Wt = np.random.normal(0,1,Nt)
    P  = np.zeros(Nt)
    P[0] = P0
    for i in range(len(P)-1):
        P[i+1] = P[i] + mu*P[i]*dt + P[i]*sigma*Wt[i]*np.sqrt(dt)
    return P
    
def euler(mu,sigma,T,Nt,P0,Wt):
    dt = T/Nt
    P  = np.zeros(Nt)
    P[0] = P0
    for i in range(len(P)-1):
        P[i+1] = P[i] + mu*P[i]*dt + P[i]*sigma*Wt[i]*np.sqrt(dt)
    return P
