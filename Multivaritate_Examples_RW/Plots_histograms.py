"""
Python module implementing the GT functions for the 2D benchmarks
"""

###############################################################################
# Libraries
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.animation import FuncAnimation, PillowWriter, ImageMagickWriter
from moviepy.editor import VideoFileClip
import os

#######################################################################
# Histograms #
def Histograms(X,Dim,Limits,Labels,filename,Size):

    # Plots
    fig, ax = plt.subplots(nrows=Dim, ncols=Dim, figsize = Size)
    N_bins = 100

    # Eras unnecesary axis

    # Bidimensional histograms
    l1 = np.arange(Dim)
    J,I = np.meshgrid(l1,l1)

    for i in range(Dim):
        for j in range(i):
            k = I[i,j]
            l = J[i,j]
            x = X[:,l]
            y = X[:,k]
            ax[i][j].hist2d(x,y,bins=N_bins,cmap = "jet",norm = colors.LogNorm())               
            ax[i][j].set_xlim(left = Limits[l,0],right = Limits[l,1])
            ax[i][j].set_ylim(bottom = Limits[k,0],top = Limits[k,1])
            ax[j][i].axis('off')
            if (j > 0):
                ax[i][j].set_yticks([])
            if (i < Dim-1):
                ax[i][j].set_xticks([])

    # 1D histograms
    for i in range(Dim):
        x = X[:,i]
        ax[i][i].hist(x,bins=N_bins,color = "c",density = True)
        ax[i][i].set_xlim(left = Limits[i,0],right = Limits[i,1])

    # Erase the x-axis
    for i in range(Dim-1):
        ax[i][i].set_xticks([])

    # Axis
    for k in range(Dim):
        ax[Dim-1][k].set_xlabel(Labels[k],fontsize = 12)
        ax[k][0].set_ylabel(Labels[k],fontsize = 12)

    plt.savefig(filename,format = 'svg')
    plt.close()
    return

