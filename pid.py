
class PID:

    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.I = 0
        self.values = [0]
        self.lim_max = 10
        self.lim_min = 0

    def setLimits(self, lim_min, lim_max):
        self.lim_max = lim_max
        self.lim_min = lim_min

    def compute(self, err):
        self.I += err
        self.values.append(err)
        if len(self.values) > 100:
            self.I -= self.values[0]
            self.values = self.values[1:]
        ret = self.kp*err + self.kd*(self.values[-1] - self.values[-2]) + self.ki*self.I
        if ret > self.lim_max:
            ret = self.lim_max
        if ret < self.lim_min:
            ret = self.lim_min
        return ret
