"""
Area of a circle with Monte Carlo estimators
"""

###############################################################################
# Libraries
import numpy as np
import matplotlib.pyplot as plt
import os

#######################################################################
# Area of circle with radius r = 1

####################################
# Constants
Pi = np.pi
C1 = np.sqrt(2*Pi)

####################################
# Samples
M = np.arange(1,6)
M = 10**M
N = len(M)

####################################
# Functions
f1 = lambda x: np.cos(x)
f2 = lambda x: np.sin(x)
f3 = lambda x: x**x
f4 = lambda x: x**(-x)
f5 = lambda x: -np.log(x)
f6 = lambda x: 0.5*x/(1.0-np.exp(-x))

####################################
# Integrals
I0 = np.ones(N)
I1 = C1*np.exp(-0.5)*I0
I2 = 0*I0
I3 = 0.7834305107*I0
I4 = 1.291285997*I0
I5 = 0.57721566490153286060*I0
I6 = 1.202056903159594*I0

####################################
# Gaussian
J1 = np.zeros(N)
J2 = np.zeros(N)
for k in range(N):
    X = np.random.randn(M[k])
    J1[k] = C1*np.mean(f1(X))
    J2[k] = C1*np.mean(f2(X))

####################################
# Uniform
J3 = np.zeros(N)
J4 = np.zeros(N)
for k in range(N):
    X = np.random.rand(M[k])
    J3[k] = np.mean(f3(X))
    J4[k] = np.mean(f4(X))

####################################
# Gamma
J5 = np.zeros(N)
J6 = np.zeros(N)
for k in range(N):
    X = np.random.gamma(shape = 1, scale = 1, size=M[k])
    J5[k] = np.mean(f5(X))
    X = np.random.gamma(shape = 2, scale = 1, size=M[k])
    J6[k] = np.mean(f6(X))

####################################
# Errors
E1 = np.abs(J1-I1)
E2 = np.abs(J2-I2)
E3 = np.abs(J3-I3)
E4 = np.abs(J4-I4)
E5 = np.abs(J5-I5)
E6 = np.abs(J6-I6)

####################################
# Plot structure
def Plots(Ik,Jk,Title,filename):
    plt.figure(1)
    plt.semilogx(M,Jk,'k-')
    plt.semilogx(M,Ik,'r-')
    plt.xlabel('M',fontsize = 16)
    plt.ylabel('I',fontsize = 16)
    plt.title(Title)
    plt.legend(['Monte Carlo','True value'],loc = "best")
    plt.savefig(filename,format = 'svg')
    plt.close()
    return

####################################
# Plots
Plots(I1,J1,r'$I_{1} \approx 1.5203469$','I1.svg')
Plots(I2,J2,r'$I_{2} = 0$','I2.svg')
Plots(I3,J3,r'$I_{3} \approx 0.7834305107$','I3.svg')
Plots(I4,J4,r'$I_{4} \approx 1.291285997$','I4.svg')
Plots(I5,J5,r'$I_{5} \approx 0.5772156649$','I5.svg')
Plots(I6,J6,r'$I_{6} \approx 1.2020569031$','I6.svg')
