"""
Plots. Banana distribution
"""

###############################################################################
# Libraries
import numpy as np
import scipy as sp
import Plots_histograms as ph
import os

#######################################################################
# Banana shape

# Parameters
Dim = 2

# Chain
filename = 'Ex_1.txt'
Z = np.loadtxt(filename)
M = len(Z)
burnin = 10000
X = Z[burnin:M,:]

# Plot parameters
Labels = [r'$x_1$',r'$x_2$']
filename = 'Ex_1.svg'
Limits = np.zeros((Dim,2))
Limits[:,0] = np.min(X,axis=0)
Limits[:,1] = np.max(X,axis=0)
Size = [9.0,6.0]

# Animation 
ph.Histograms(X,Dim,Limits,Labels,filename,Size)
