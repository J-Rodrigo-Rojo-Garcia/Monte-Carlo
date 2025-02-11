"""
Example 2. Rosenbrock function in 3D
"""

###############################################################################
# Libraries
import numpy as np
import scipy as sp
import Random_Walk_MH as RMH
import os

###############################################################################
# Rosenbrock distribution

# The density is defined as 
# rho(x) = C*exp(-[100*(x2 - x1^2)^2 + (1 - x1)^2 + 100*(x3 - x2^2)^2 + (1-x2)^2]/20)
# with C the proportionality constant

# Log distritribution
C1 = -5.0
C2 = -1.0/20.0
Log_dist = True
def Log_rho(theta):
    L_rho = C1*(theta[1]-theta[0]*theta[0])**2
    L_rho += C2*(1.0 - theta[0])**2
    L_rho += C1*(theta[2] - theta[1]*theta[1])**2
    L_rho += C2*(1.0 - theta[1])**2
    return L_rho

# Properties of the distribution
Dim = 3
Support = np.zeros((Dim,2))
#Support[:,0] = -np.Inf
#Support[:,1] = np.Inf
Support[:,0] = np.array([-3.0,-2.0,-2.0])
Support[:,1] = np.array([3.0,8.0,40.0])

# Params of Random Walk
Gamma = np.eye(Dim)
Gamma[0,0] = 0.1
Gamma[1,1] = 0.1
Gamma[2,2] = 0.1
M = 1000000
X0 = np.array([-1,-1,-1])

#Simulations
X = RMH.Random_Walk_Metropolis_Hasting(Support,Dim,Log_rho,Gamma,M,Log_dist,X0)

# Filenames
filename = 'Ex_2.txt'

# Save
np.savetxt(filename,X)