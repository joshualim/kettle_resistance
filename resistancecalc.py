# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 14:30:19 2015

@author: josh
"""
import matplotlib.pyplot as plt
from numpy import *

# set up problem
Vsupply=1
Rwire=30
Relementmin=0; Relementmax=1000; Relementincr=0.1
Relement=arange(Relementmin,Relementmax,Relementincr)

# calc values
I=Vsupply/(Rwire+Relement)
PowerElement=I**2*Relement
PowerWire=I**2*Rwire
PowerTot=PowerElement+PowerWire


# Display graph
plt.plot(Relement,PowerElement,label='Heating Element Power')
plt.plot(Relement,PowerWire,label='Power dissipated in wire')
plt.plot(Relement,PowerTot,label='Total Power')

plt.xlabel('Heating element resistance (Ohms)')
plt.ylabel('Power (W)')
plt.title(( 'V$_{supply}$ = '+str(Vsupply)+' V,  R$_{wire}$ = '+str(Rwire)+' Ohms' ))

plt.legend()


#plt.show()

