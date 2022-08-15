# Spatial harvested_population model 
# van Nes, Egbert H., and Marten Scheffer. "Implications of spatial heterogeneity for catastrophic regime shifts in ecosystems." Ecology 86.7 (2005): 1797-1807..
import numpy as np
import matplotlib.pyplot as plt
import tqdm


def f(x,c):
    K = 10
    return x*(1 - x/K) - c *(x**2)/(1 + x**2) 

def ddx(X,dx):
    return dx*(np.roll(X,1,axis=0) + np.roll(X,1,axis=1) + np.roll(X,-1,axis=0) + np.roll(X,-1,axis=1) - 4* X)

def get_data(n = 20,sigma = 0.01):
    dt = 0.1
    dx = 0.01
    T = 1000
    times = np.arange(0,T,dt)

    x = np.zeros((times.shape[0],n,n))
    omega = sigma * np.random.randn(times.shape[0],n,n)

    p_min = 1
    p_max = 2.8
    c = p_min + (p_max - p_min) * times/T
    x0 = 8.0*np.ones((n,n))
    for k in range((times.shape[0]-1)//10):
        x0 = x0 + dt *(f(x0,c[0]) + ddx(x[k],dx))
        x0[x0<0]=0


    x[0] = x0
    print('Generate time-series data of a harvested_population model')
    for k in tqdm.tqdm(range(times.shape[0]-1)):
        x[k+1] = x[k] + dt *(f(x[k],c[k]) + ddx(x[k],dx))+ np.sqrt(dt)*omega[k]
        x[k+1,x[k+1]<0]=0

    y = np.zeros(times.shape[0])
    y[c>2.604] = 1
    return times,x.reshape(-1,n*n),y