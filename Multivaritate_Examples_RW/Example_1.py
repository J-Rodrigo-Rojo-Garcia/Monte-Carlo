"""
Example 1. Banana distribution 
"""

###############################################################################
# Libraries
import numpy as np
import scipy as sp
import Random_Walk_MH as RMH
import matplotlib.pyplot as plt
import os

#######################################################################
# Banana shaped distribution

# The density is defined as rho(x) = C*exp(-10(x1^2 - x2)^2 - (x2 - 0.25)^4)
# with C the proportionality constant

####################################
# MCMC distribution

# Log distritribution
Log_dist = True
Log_rho = lambda theta: -10*(theta[0]**2 - theta[1])**2 - (theta[1] - 0.25)**4

# Properties of the distribution
Dim = 2
Support = np.zeros((Dim,2))
Support[:,0] = -np.inf
Support[:,1] = np.inf

# Params of Random Walk
Gamma = 0.001*np.eye(Dim)
M = 100000
X0 = np.array([-1.5,-1.5])

#Simulations
X = RMH.Random_Walk_Metropolis_Hasting(Support,Dim,Log_rho,Gamma,M,Log_dist,X0)

# Filenames
filename = 'Ex_1.txt'

# Save
np.savetxt(filename,X)
