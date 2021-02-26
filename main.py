import serve as sv
import params
from quad import getNewState
from pid import PID

from math import sin, cos, acos, asin
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

w1 = 3
w2 = 1.9475

W = [w1, w1, w1, w1]

x = []
y = []
z = []
gamma = []
psi = []
nu = []

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
    "y": 1,
    "z": 0,
    "gamma": 0,
    "psi": 0,
    "nu": 0
}

ws = []

pid_dy = PID(0.7, 1.5, 30000)

pid_dx = PID(0.7, 1.5, 30000)
pid_dx.setLimits(0, 1.5)

pid_dz = PID(0.7, 1.5, 30000)
pid_dz.setLimits(0, 1.5)

while i < 2000:
    state = getNewState(state, W)

    Uy = pid_dy.compute(state_d["y"] - state["y"])
    Ux = pid_dx.compute(state_d["x"] - state["x"])
    Uz = pid_dz.compute(state_d["z"] - state["z"])
    
    P = sv.getFullP(W)

    if P != 0:
        state_d["gamma"] = asin((Uz*cos(state_d["psi"]) + Ux*sin(state_d["psi"])) / P)
        state_d["nu"] = acos((Uz*sin(state_d["psi"]) - Ux*cos(state_d["psi"])) / P)

    W = [Uy, Uy, Uy, Uy]

    # -- save --
    ws.append(Uy)
    z.append(state["z"])
    y.append(state["y"])
    x.append(state["x"])
    gamma.append(state["gamma"])
    psi.append(state["psi"])
    nu.append(state["nu"])

    i += 1

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, z, y)

plt.show()

plt.plot(y)
plt.plot(ws)
# plt.plot(np.array(gamma))
# plt.plot(np.array(psi))
# plt.plot(np.array(nu))

plt.show()