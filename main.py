import serve as sv
import params
from quad import getNewState
from pid import PID
from physics import world_physics

from save import Saver
import logger as lgg

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
    "y": 10,
    "z": 1,
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

kp_x = 0.4
Tx = 30000
pid_dx = PID(kp_x, 2*kp_x/Tx, kp_x*Tx/2.5)

kp_z = 0.4
Tz = 30000
pid_dz = PID(kp_z, 2*kp_z/Tz, kp_z*Tz/2.5)

kp_gamma = 3
Tgamma = 7000
pid_gamma = PID(kp_gamma, 0.1*kp_gamma/Tgamma, kp_gamma*Tgamma/4)

pid_gamma.setLimits(-1, 1)

kp_nu = 3
Tnu = 7000
pid_nu = PID(kp_nu, 0.1*kp_nu/Tnu, kp_nu*Tnu/4)
pid_nu.setLimits(-1, 1)

pid_psi = PID(0.7, 1.5, 30000)

while i < 10000:
    state = world_physics(getNewState(state, motors))

    U1 = round(pid_dy.compute(state_d["y"] - state["y"]), 2)

    P = sv.getFullP(motors)

    pid_dx.setLimits((-1)*P, P)
    Ux = (-1)*pid_dx.compute(state_d["x"] - state["x"])
    pid_dz.setLimits((-1)*P, P)
    Uz = pid_dz.compute(state_d["z"] - state["z"])

    if P != 0:
        state_d["gamma"] = np.clip(asin((Uz*cos(state_d["psi"]) + Ux*sin(state_d["psi"])) / P), -1, 1)
        state_d["nu"] = np.clip(asin((Uz*sin(state_d["psi"]) + Ux*cos(state_d["psi"])) / P), -1, 1)

    K = 0.5

    U2 = round(pid_gamma.compute(state_d["gamma"] - state["gamma"]), 2)*U1*0.5
    U3 = round(pid_nu.compute(state_d["nu"] - state["nu"]), 2)*U1*0.5
    U4 = round(pid_psi.compute(state_d["psi"] - state["psi"]), 2)*U1*0.5
    
    saver.put(state)

    motors = [round(U1 - U2 + U4, 2), round(U1 + U3 - U4, 2), round(U1 + U2 + U4, 2), round(U1 - U3 - U4, 2)]

    collecter1.append(U2)
    collecter2.append(Ux)
    collecter3.append(U3)
    collecter4.append(U4)


    lgg._print("N____________________________", i)
    lgg._print(motors)
    lgg._print(state)
    lgg._print(state_d)
    lgg._print(U1, U2, U3, U4)
    lgg._print(Ux, Uz)
    # input()
    

    i += 1


# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(saver.getPath("x") , saver.getPath("z"), saver.getPath("y"))
# plt.show()

# plt.plot(saver.getPath("x"), saver.getPath("z"))
# plt.plot(saver.getPath("y"))
plt.plot(saver.getPath("gamma"))
plt.plot(saver.getPath("z"))
# plt.plot(collecter1)
# plt.plot(collecter2)
# plt.plot(collecter3)
# plt.plot(collecter4)
plt.show()