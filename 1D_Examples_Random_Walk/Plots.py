"""
Python module implementing the GT functions for the 2D benchmarks
"""

###############################################################################
# Libraries
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import os

#######################################################################
# Plots
def my_plots(X,xk,y,dist_name,col):

    # Length
    M = len(X)

    # Format
    if (len(X.shape) == 1):
        X = np.reshape(X,[M,1])

    # Plots
    X_min = np.min(X)
    X_max = np.max(X)
    J = np.arange(M)

    plt.figure(1)
    plt.xlim([0,M])
    plt.ylim([X_min,X_max])
    plt.xlabel('N')
    plt.ylabel('x')
    plt.title('Trace - ' + dist_name + ' distribution')
    plt.plot(J,X,col)
    plt.savefig('plots/'+ dist_name + '_trace.svg')
    plt.close()

    # Histograms
    filename = 'plots/' + dist_name + '_histogram.svg'
    plt.figure(2)
    plt.xlabel('x')
    plt.plot(xk,y,'k')
    plt.title(dist_name + ' distribution')
    plt.hist(X,bins=100,density=True,color=col)
    plt.legend(['Density','MCMC histogram'])
    plt.savefig(filename)
    plt.close()
    