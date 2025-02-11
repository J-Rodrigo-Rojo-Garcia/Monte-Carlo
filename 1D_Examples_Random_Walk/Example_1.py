"""
Samples with Random-Walk of Gumbel distribution  
"""

###############################################################################
# Libraries
import numpy as np
import scipy as sp
import Random_Walk_MH as RMH
import matplotlib.pyplot as plt
import Plots as ps
import os

#######################################################################
# Gumbel 1D

# The density is defined as rho(x) = (1/sigma)exp(-u+exp(-u))
# with u = (x-mu)/sigma


# Parameters
mu = 1
sigma = 1

# Log distritribution
Log_dist = True
Log_rho = lambda theta: -(theta-mu)/sigma - np.exp(-(theta-mu)/sigma)

# Density
xk = np.linspace(-1,10,100)
y = np.exp(Log_rho(xk))/sigma

# Properties of the distribution
Dim = 1
Support = np.zeros((Dim,2))
Support[0,0] = -np.inf
Support[0,1] = np.inf

# Params of Random Walk
Sigma2 = 0.1
Gamma = Sigma2*np.ones(Dim)
M = 30000

#Sample
X = RMH.Random_Walk_Metropolis_Hasting(Support,Dim,Log_rho,Gamma,M,Log_dist)

# Filenames
filename = 'Gumbel.txt'

# Save
np.savetxt(filename,X)

# Plots
dist_name = 'Gumbel'
col = 'r'
ps.my_plots(X,xk,y,dist_name,col)