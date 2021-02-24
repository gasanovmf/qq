import serve as sv
import params
from quad import getNewState
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
    "gamma": 0,
    "psi": 0,
    "nu": 0
}

i = 0

while i < 2000:
    state = getNewState(state, W)
    z.append(state["z"])
    y.append(state["y"])
    x.append(state["x"])
    if y[-1] > 1:
        W = [w2, w2, w2, w2]

    gamma.append(state["gamma"])
    psi.append(state["psi"])
    nu.append(state["nu"])

    i += 1

# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(x, z, y)

# plt.show()

plt.plot(y)
# plt.plot(np.array(gamma))
# plt.plot(np.array(psi))
# plt.plot(np.array(nu))

plt.show()