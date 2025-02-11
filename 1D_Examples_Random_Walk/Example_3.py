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
# Logit-normal distribution 1D

# The density is defined as 
# rho(x) = (1/sigma*sqrt(2*pi))[1/(x*(1-x))]exp(-((logit(x)-mu)**2)/(2*(sigma**2))
# 0 < x < 1

# Parameters
mu = 1
sigma = 2

# Auxiliar functions
c = -0.5/(sigma*sigma)
epsi = 0.0001
c2 = 1.0/(sigma*np.sqrt(2.0*np.pi))
logit =  lambda x: np.log(x) - np.log(1.0 - x)

# Log distritribution
Log_dist = True
Log_rho = lambda theta: -np.log(theta) - np.log(1.0 - theta) + c*((logit(theta)-mu)**2)  

# Density
rho = lambda x: (c2/(x*(1-x)))*np.exp(c*((logit(x)-mu)**2))
xk = np.linspace(epsi,1-epsi,100)
y = rho(xk)

# Properties of the distribution
Dim = 1
Support = np.zeros((Dim,2))
Support[0,0] = 0.0 + epsi
Support[0,1] = 1.0 - epsi

# Params of Random Walk
Sigma2 = 0.1
Gamma = Sigma2*np.ones(1)
M = 30000

# Samples 
X = RMH.Random_Walk_Metropolis_Hasting(Support,Dim,Log_rho,Gamma,M,Log_dist)

# Filename
filename = 'Logit_Normal.txt'

# Save
np.savetxt(filename,X)

# Plots
dist_name = 'Logit-Normal'
col = 'g'
ps.my_plots(X,xk,y,dist_name,col)
