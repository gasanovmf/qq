#!/usr/bin/python
# -*- coding: UTF-8 -*-

from swarm_schwefel import Swarm_Schwefel
from utils import printResult

import numpy


if __name__ == "__main__":
    iterCount = 1000

    dimension = 3
    swarmsize = 2000

    minvalues = numpy.array ([-500] * dimension)
    maxvalues = numpy.array ([500] * dimension)

    currentVelocityRatio = 0.5
    localVelocityRatio = 2.0
    globalVelocityRatio = 5.0

    swarm = Swarm_Schwefel (swarmsize, 
            minvalues, 
            maxvalues,
            currentVelocityRatio,
            localVelocityRatio, 
            globalVelocityRatio
            )

    for n in range (iterCount):
        print "Position", swarm[0].position
        print "Velocity", swarm[0].velocity

        print printResult (swarm, n)

        swarm.nextIteration()
