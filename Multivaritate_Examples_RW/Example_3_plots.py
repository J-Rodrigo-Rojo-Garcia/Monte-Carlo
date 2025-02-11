"""
Plots. Rosenbrock 4D
"""

###############################################################################
# Libraries
import numpy as np
import scipy as sp
import Plots_histograms as ph
import matplotlib.pyplot as plt
import os

#######################################################################
# Bread and peace

##################################
# Histograms

# Parameters
Dim = 4

# Chain
filename = 'Ex_3.txt'
Z = np.loadtxt(filename)
M = len(Z)
burnin = 10000
X = Z[burnin:M,:]

# Plot parameters
Labels = [r'$x_1$',r'$x_2$',r'$x_3$',r'$x_4$']
Limits = np.zeros((Dim,2))
#Limits[:,0] = np.array([-5.0,-2.0,-10.0])
#Limits[:,1] = np.array([5.0,15.0,200.0])
Limits[:,0] = np.array([-10.0,-5.0,-10.0,-5.0])
Limits[:,1] = np.array([10.0,50.0,10.0,50.0])

Size = [14.0,9.0]

# Histograms 
filename = 'Ex_3.svg'
ph.Histograms(X,Dim,Limits,Labels,filename,Size)
