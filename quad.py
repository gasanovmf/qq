from params import *
import numpy as np
from serve import getFullP, getP
from math import cos, sin, tan

def getNewState(state, W):
    w1 = W[0] + W[2] - W[1] - W[3]
    w2 = W[1] + W[3] - W[0] - W[2]

    Mmx = Im*state["wz"]*w1
    Mmz = Im*state["wx"]*w2
    Mpx = Ip*state["wz"]*w1
    Mpz = Ip*state["wx"]*w2

    Mqx = (getP(W[2]) - getP(W[0]))*l
    Mqz = (getP(W[1]) - getP(W[3]))*l
    Mqy = getP(W[1]) + getP(W[3]) - getP(W[0]) - getP(W[2])

    MRx = Mqx + Mmx + Mpx
    MRy = Mqy
    MRz = Mqz + Mmz + Mpz

    P = getFullP(W)
    A = {}
    A["ax"] =  P*((-1)*cos(state["gamma"])*cos(state["psi"])*sin(state["nu"]) - sin(state["gamma"])*sin(state["psi"]))/m
    A["ay"] = (P*cos(state["gamma"])*cos(state["nu"]) - m*g)/m
    A["az"] =  P*((-1)*cos(state["gamma"])*sin(state["psi"])*sin(state["nu"]) - sin(state["gamma"])*cos(state["psi"]))/m
    A["wx_dot"] = Iyzx*state["wy"]*state["wz"] + MRx/Ix
    A["wy_dot"] = Izxy*state["wx"]*state["wz"] + MRy/Iy
    A["wz_dot"] = Ixyz*state["wx"]*state["wy"] + MRz/Iz
    A["gamma_dot"] = state["wx"]*cos(state["nu"]) - state["wy"]*sin(state["nu"])
    A["psi_dot"] = (state["wx"]*sin(state["nu"] - state["wy"]*cos(state["nu"]))) / cos(state["gamma"])
    A["nu_dot"] = state["wz"] + cos(state["nu"])*tan(state["gamma"])*state["wx"] + cos(state["nu"])*tan(state["gamma"])*state["wy"]

    return integrator(state, A)

def integrator(state, A):
    ret = {}

    ret["vx"] = state["vx"] +  A["ax"]*dt
    ret["x"] = state["x"] + ret["vx"]*dt

    ret["vy"] = state["vy"] +  A["ay"]*dt
    ret["y"] = state["y"] + ret["vy"]*dt

    ret["vz"] = state["vz"] +  A["az"]*dt
    ret["z"] = state["z"] + ret["vz"]*dt

    ret["wx"] = state["wx"] +  A["wx_dot"]*dt
    ret["wy"] = state["wy"] +  A["wy_dot"]*dt
    ret["wz"] = state["wz"] +  A["wz_dot"]*dt

    ret["gamma"] = state["gamma"] +  A["gamma_dot"]*dt
    ret["psi"] = state["psi"] +  A["psi_dot"]*dt
    ret["nu"] = state["nu"] +  A["nu_dot"]*dt

    return ret


