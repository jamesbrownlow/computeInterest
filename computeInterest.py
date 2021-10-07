# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 07:06:26 2021

@author: 16617
compute interest rate
These are functions that could be added to your loan class
"""

import numpy as np

# here's the stated problem
PV = 1
pmt = 0.1
n = 12
# compute r


##########   function for exhaustive search ######## 
# given PV, pmt and number of months, n, for a specified r 
# print the difference between specified payment and what
# the payment would be at interest= r (APR)
# This function used for exhaustive search (what r gives min
# difference between the actual pmt and what the payment
# would be for given r) and Newton's method

def f(r, PV, pmt,n):
    r = r/100/12 # monthly rate
    difference = pmt - (PV*r/(1-(1+r)**(-n)))
    return difference


#####  exhaustive search
for r in np.arange(1, 40):
    print(r, f(r, PV, pmt, n))
    
# looks like r = 35: i.e. minimum difference is at r = 35
    

#########   bisection   #############
'''
  r is the interst rate
  given as APR convert to decimal / month
'''

rLow=0
rHigh=100
iterCount = 0

while(1):
    r = (rLow+rHigh)/2
    err = f(r, PV, pmt, n)

    if err > 0:
        rLow = r
    else:
        rHigh = r
    iterCount += 1
    if(abs(rHigh-rLow))< 0.005: break

print('\nbisection')
print('interest = {}%, iterCount={}\n'.format(round(r,2),iterCount))

def fPrime(r, PV, n):
    ''' defivative of the function f (above) with respect
        to r
    '''
    r = r/100/12
    return -(1-(1+r)**(-n))*PV +r*PV*((-n)*(1+r)**(-n-1))/(1-(1+r)**(-n))**2

##########  Newton's method  ###########
# iteration: r[n+1] = r[n] - f(r[n]) / d(f(r))/dr
#  f(r) is the function used in the exhaustive search
  
r = 10  # initial guess at interest rate, APR
iterCount = 0

while(1):
    rnew = r-f(r, PV, pmt,n)/fPrime(r, PV, n)
    if abs(r-rnew) < 1.e-6: break
    r = rnew
    iterCount += 1
    
print("Newton's method")
print('int = {}, iter = {}\n'.format(round(rnew,2), iterCount))
    
