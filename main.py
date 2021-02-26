import serve as sv
import params
from quad import getNewState
from pid import PID
from save import Saver

from math import sin, cos, acos, asin
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

motors = [0, 0, 0, 0]

state = {
    "vx": 0,
    "vy": 0,
    "vz": 0,
    "x": 0,
    "y": 0,
    "z": 0,
    "wx": 0,
    "wy": 0,
    "wz": 0,
    "gamma": 0, # крен
    "psi": 0, # рыскание
    "nu": 1.5 # тангаж
}

i = 0

state_d = {
    "x": 0,
    "y": 1,
    "z": 0,
    "gamma": 0,
    "psi": 0,
    "nu": 0
}

collecter1 = []

saver = Saver()

pid_dy = PID(0.7, 1.5, 30000)
pid_dx = PID(0.7, 1.5, 30000)
pid_dz = PID(0.7, 1.5, 30000)

while i < 2000:
    state = getNewState(state, motors)

    Uy = pid_dy.compute(state_d["y"] - state["y"])

    P = sv.getFullP(motors)

    pid_dx.setLimits(0, P)
    Ux = pid_dx.compute(state_d["x"] - state["x"])
    pid_dz.setLimits(0, P)
    Uz = pid_dz.compute(state_d["z"] - state["z"])

    if P != 0:
        state_d["gamma"] = asin((Uz*cos(state_d["psi"]) + Ux*sin(state_d["psi"])) / P)
        state_d["nu"] = asin((Uz*sin(state_d["psi"]) + Ux*cos(state_d["psi"])) / P)
    
    collecter1.append(state_d["nu"])

    saver.put(state)

    motors = [Uy, Uy, Uy, Uy]

    i += 1


# -- plot -- 
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(saver.getPath("x") , saver.getPath("z"), saver.getPath("y"))
# plt.show()

# plt.plot(saver.getPath("y"))
plt.plot(collecter1)
plt.show()