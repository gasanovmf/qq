kp = 0.7
kd = 30000
ki = 1.5
I = 0
vs = [0]

max_err = 10
min_err = 0


def PID(err):
    global I, vs

    I += err
    vs.append(err)
    if len(vs) > 100:
        I -= vs[0]
        vs = vs[1:]
    ret = kp*err + kd*(vs[-1] - vs[-2]) + ki*I
    if ret > max_err:
        ret = max_err
    if ret < min_err:
        ret = min_err
    return ret