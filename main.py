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
    "nu": 0 # тангаж
}

i = 0

state_d = {
    "x": 0,
    "y": 0,
    "z": 0,
    "gamma": 0,
    "psi": 0,
    "nu": 0
}

collecter1 = []
collecter2 = []
collecter3 = []
collecter4 = []

saver = Saver()

# -- PIDS --
pid_dy = PID(0.7, 1.5, 30000)
pid_dx = PID(0.7, 1.5, 30000)
pid_dz = PID(0.7, 1.5, 30000)
pid_gamma = PID(0.7, 1.5, 30000)
# pid_gamma.setLimits(-1.5, 1.5)
pid_nu = PID(0.7, 1.5, 30000)
# pid_nu.setLimits(-1.5, 1.5)
pid_psi = PID(0.7, 1.5, 30000)

while i < 2000:
    state = getNewState(state, motors)

    U1 = pid_dy.compute(state_d["y"] - state["y"])

    P = sv.getFullP(motors)

    pid_dx.setLimits((-1)*P, P)
    Ux = pid_dx.compute(state_d["x"] - state["x"])
    pid_dz.setLimits((-1)*P, P)
    Uz = pid_dz.compute(state_d["z"] - state["z"])

    # if P != 0:
    #     state_d["nu"] = asin((Uz*cos(state_d["psi"]) + Ux*sin(state_d["psi"])) / P)
    #     state_d["gamma"] = asin((Uz*sin(state_d["psi"]) + Ux*cos(state_d["psi"])) / P)

    U2 = pid_gamma.compute(state_d["gamma"] - state["gamma"])
    U3 = pid_nu.compute(state_d["nu"] - state["nu"])
    U4 = pid_psi.compute(state_d["psi"] - state["psi"])
    
    collecter1.append(U1)
    collecter2.append(U2)
    collecter3.append(U3)
    collecter4.append(U4)

    saver.put(state)

    motors = [U1 + U2 + U4, U1 + U3 - U4, U1 - U2 + U4, U1 - U2 + U4]

    print(U1, U2, U3, U4)

    i += 1


# -- plot -- 
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(saver.getPath("x") , saver.getPath("z"), saver.getPath("y"))
# plt.show()

# plt.plot(saver.getPath("gamma"))
plt.plot(collecter1)
# plt.plot(collecter2)
# plt.plot(collecter3)
# plt.plot(collecter4)
plt.show()