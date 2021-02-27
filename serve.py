import params

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