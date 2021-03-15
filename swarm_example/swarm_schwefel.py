#!/usr/bin/python
# -*- coding: UTF-8 -*-

from particleswarm.swarm import Swarm

import numpy


class Swarm_Schwefel (Swarm):
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
        function = sum (-position * numpy.sin (numpy.sqrt (numpy.abs (position) ) ) )
        penalty = self._getPenalty (position, 10000.0)
        return function + penalty
