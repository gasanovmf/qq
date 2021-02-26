
class PID():

    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.I = 0
        self.values = [0]
        self.max_ret = 10
        self.min_ret = 0

    def compute(self, err):
        self.I += err
        self.values.append(err)
        if len(self.values) > 100:
            self.I -= self.values[0]
            self.values = self.values[1:]
        ret = self.kp*err + self.kd*(self.values[-1] - self.values[-2]) + self.ki*self.I
        if ret > self.max_ret:
            ret = self.max_ret
        if ret < self.min_ret:
            ret = self.min_ret
        return ret
