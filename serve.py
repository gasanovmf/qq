import params

def getP(w):
    return params.ci*w**2

def getFullP(wAll):
    sum = 0
    for w in wAll:
        sum += getP(w)
    return sum

