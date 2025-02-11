"""
Python module implementing the GT functions for the 2D benchmarks
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
# Weibull 1D

# The density is defined as rho(x) = (k/L)[(x/L)^{k-1}]exp(-[x/L]^k)
# x>= 0

# Parameters
k = 1.1
L = 1.1

# Auxiliar constants
c1 = k-1
c2 = np.log(L)

# Log distritribution
Log_dist = True
Log_rho = lambda theta: c1*(np.log(theta) - c2) - (theta/L)**k  

# Density
rho = lambda x:(k/L)*((x/L)**(k-1))*np.exp(-(x/L)**k)
xk = np.linspace(0,10,100)
y = rho(xk)

# Properties of the distribution
Dim = 1
Support = np.zeros((Dim,2))
Support[0,0] = 0.0
Support[0,1] = np.inf

# Params of Random Walk
Sigma2 = 0.8
Gamma = Sigma2*np.ones(Dim)
M = 30000

# Sample
X = RMH.Random_Walk_Metropolis_Hasting(Support,Dim,Log_rho,Gamma,M,Log_dist)

# Filename
filename = 'chains/Weibull.txt'

# Save
np.savetxt(filename,X)

# Plots
dist_name = 'Weibull'
col = 'c'
ps.my_plots(X,xk,y,dist_name,col)
