"""
Area of a circle with Monte Carlo estimators
"""

###############################################################################
# Libraries
import numpy as np
import matplotlib.pyplot as plt

#######################################################################
# Area of circle with radius r = 1

####################################
# Circle
t = np.linspace(0,2.0*np.pi,100)
x = np.cos(t)
y = np.sin(t)

####################################
# Parameters

# Dimension
Dim = 2

# Size of the sample
M = 10000

####################################
# Plots
def my_plots(Xk,Ik,Jk,l):

    # Plots
    plt.figure(1,figsize = Size)
    plt.plot(Xk[Ik,0],X[Ik,1],'r.')
    plt.plot(Xk[Jk,0],X[Jk,1],'c.')
    plt.plot(x,y,'b')
    plt.xlabel('x',fontsize = 16)
    plt.ylabel('y',fontsize = 16)
    plt.xticks([-1,0,1],fontsize = 16)
    plt.yticks([-1,0,1],fontsize = 16)
    plt.title('Area of circle = '+ str(A),fontsize = 16)
    filename = 'Ex_1_' + str(l) + '.svg'
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.savefig(filename,format = 'svg')
    plt.close()
    
    return


####################################
# Sampling

# Samples
M = np.array([1,10,100,1000,10000])
Size = [9,9]
acum = 1
for k in M:
    # Total sample
    X = np.random.rand(k,Dim)
    X = -1 + 2*X
    # Radius
    r = np.sum(X*X,axis = 1)
    # Nodes inside circle
    I = np.argwhere(r <= 1)
    # Nodes outside circle
    J = np.argwhere(r > 1)
    # Area
    A = (4.0*len(I))/k
    # Plots
    acum += 1
    my_plots(X,I,J,acum)
