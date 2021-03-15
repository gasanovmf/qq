import params
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def getP(w):
    return params.ci*w**2

def getFullP(wAll):
    sum = 0
    for w in wAll:
        sum += getP(w)
    return sum


"""
Leszek Cedro - 
Optimizing PID controller gains to model the performance of
a quadcopter
"""

def getW(U):
    b = params.b
    d = params.d
    l = params.l
    A = [[b, b, b, b],
        [(-1)*b*l, 0, b*l, 0],
        [0, (-1)*b*l, 0, b*l],
        [d, (-1)*d, d, (-1)*d]]
    B = U
    x = LA.solve(A, B)
    return x    


def log_func(n):
    K = 1
    r = 0.01
    P = 1
    a = 500
    x = np.linspace(0, n, n) 
    y = K*P*np.exp(r*(x - a))/(K + P*(np.exp(r*(x - a)) + 1))
    return [x, y]

if __name__ == "__main__":
    x, y = log_func(5000)
    plt.plot(x, y) 
    plt.show()