#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy
from main import startSim
from serve import log_func


i = 0
# from utils import printResult

from particleswarm.swarm import Swarm


class Swarm_X2 (Swarm):
    def __init__ (self, 
            swarmsize, 
            minvalues, 
            maxvalues, 
            currentVelocityRatio,
            localVelocityRatio, 
            globalVelocityRatio):
       Swarm.__init__ (self, 
            swarmsize, 
            minvalues, 
            maxvalues, 
            currentVelocityRatio,
            localVelocityRatio, 
            globalVelocityRatio)

    def _finalFunc (self, position):
        global i

        to_state = {
            "x": 1,
            "y": 1,
            "z": 1,
            "gamma": 0,
            "psi": 0,
            "nu": 0
        }

        N = 5000

        _, x_i = log_func(N)
        _, y_i = log_func(N)
        _, z_i = log_func(N)

        state = startSim(N, to_state, position)

        x = numpy.array(state[0].getPath("x"))
        y = numpy.array(state[0].getPath("y"))
        z = numpy.array(state[0].getPath("z"))

        ret = numpy.absolute(numpy.sum(x-x_i)) + numpy.absolute(numpy.sum(y-y_i)) + numpy.absolute(numpy.sum(z-z_i)) 

        print("--> p_N", i)
        i += 1

        # penalty = self._getPenalty (position, 10000.0)
        return ret

iterCount = 300
dimension = 15
swarmsize = 200
minvalues = numpy.array ([0] * dimension)
maxvalues = numpy.array ([100] * dimension)
currentVelocityRatio = 0.1
localVelocityRatio = 1.0
globalVelocityRatio = 5.0

swarm = Swarm_X2 (swarmsize,
        minvalues,
        maxvalues,
        currentVelocityRatio,
        localVelocityRatio,
        globalVelocityRatio
        )

for n in range (iterCount):
    print("--> ", n)
    # print printResult (swarm, n)
    swarm.nextIteration()

print(swarm.globalBestPosition)