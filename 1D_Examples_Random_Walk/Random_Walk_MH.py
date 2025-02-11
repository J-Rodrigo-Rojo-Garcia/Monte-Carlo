"""
Python module implementing for Random-Walk Metropolis Hasting algorithm
"""

###############################################################################
# Libraries
import numpy as np
import scipy.linalg as spl

###############################################################################
# Random-Walk-Metropolis-Hasting interface
def Random_Walk_Metropolis_Hasting(Support,Dim,Rho,Gamma,M,Log_dist):

    # Initial point
    X0 = Initial_Point(Support,Dim)

    # Tolerance in support
    K0 = 10

    # Cholesky decomposition
    if (Dim == 1):
        Gamma_1_2 = np.sqrt(Gamma)
    else:
        Gamma_1_2 = spl.chol(Gamma)       

    # Log condition
    if(Log_dist == True):
        Alpha = lambda a,b: min(0,b-a)
        U = lambda c: np.log(np.random.rand())
    else:
        Alpha = lambda a,b: min(1,b/a)
        U = lambda c: np.random.rand()
    
    # Sample with Random Walk
    X = Random_Walk(Support,Dim,Rho,Gamma_1_2,M,X0,K0,Alpha,U)
    
    return X

    
### Random-Walk without logarithm ###
def Random_Walk(Support,Dim,Rho,Gamma_1_2,M,X0,K0,Kernel,Uk):

    # Allocate memory
    X = np.zeros((M,Dim))

    # Initial point
    X[0,:] = X0

    # Empieza RWMH
    for k in range(M-1):

        # Evaluation
        rho_1 = Rho(X[k,:])
        # Support test
        K = 1; Supp = 1
#        while(Supp == 1 and K < K0):
#            # Realization of the normal (step size)
#            w = Gamma_1_2@np.random.randn(Dim)
#            # Step
#            Y = X[k,:] + Supp*w
#            # Calculate support
#            Supp = Support_Acceptance(Support,Dim,Y)
#            # Update
#            K += 1

        # Realization of the normal (step size)
        w = Gamma_1_2@np.random.randn(Dim)
        # Step
        Y = X[k,:] + Supp*w
        # Calculate support
        Supp = Support_Acceptance(Support,Dim,Y)
        Y = X[k,:] + Supp*w
        # New evaluaton
        rho_2 = Rho(Y)
        # Kernel
        Alpha = Kernel(rho_1,rho_2)
        # Uniform realization
        u = Uk(0) 
        if (u < Alpha):
            X[k+1,:] = np.copy(Y)
        else:
            X[k+1,:] = np.copy(X[k,:])
    return X


###############################################################################
# Extra functions 

### Function for calculate the initial point ###
def Initial_Point(Support,Dim):

    # Allocate
    X0 = np.zeros(Dim)
    a = -np.inf
    b = np.inf

    # Limits
    for k in range(Dim):
        if(Support[k,0] > a and Support[k,1] < b):
            X0[k] = Support[k,0] + (Support[k,1] - Support[k,0])*np.random.rand()
        elif(Support[k,0] > a and Support[k,1] == b):
            X0[k] = Support[k,0] + np.random.rand()
        elif(Support[k,0] == a and Support[k,1] < b):
            X0[k] = Support[k,1] - np.random.rand()
        else:
            X0[k] = np.random.rand()
    
    return X0

### Function for calculate support ###
def Support_Acceptance(Support,Dim,x):

    # Support
    supp = 1

    # Limits
    for k in range(Dim):
        if(Support[k,0] <= x[k] and x[k] <= Support[k,1]):
            supp *= 1
        else:
            supp *= 0

    return supp