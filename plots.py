# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:04:25 2019

@author: Jonathan Frassineti
"""

import configuration
import numpy as np
import matplotlib.pyplot as plt

def configurationPlot():
    """This module plots the configuration once 
    passed to it along with time, for a given T.
        
    Parameters:
        f: figure to plot.
        configuration: state of the configuration created by 
        initialstate(N).
        i: time interval.
        N: length of the square lattice (N*N).
        n: number of subplot."""
    config = np.load('./data/time.npy')
    i = [0,1,4,32,100,1000]
    f = plt.figure(figsize=(15, 15), dpi=80)
    X, Y = np.meshgrid(range(configuration.N), range(configuration.M))
    for n in range(len(i)):
        sp =  f.add_subplot(3, 3, n+1)  
        plt.setp(sp.get_yticklabels(), visible=False)
        plt.setp(sp.get_xticklabels(), visible=False)      
        plt.pcolormesh(X, Y, config[n], cmap=plt.cm.RdBu)
        plt.title('Time=%d'%i[n]) 
        plt.axis('tight')    
    f.savefig('./images/timeEvolution.png')
    
def graphPlot():
    """ This method plots the magnetization and the energy of the lattice.
    """
    T = configuration.T.copy()
    energy = np.load('./data/ene.npy')  
    magnetization = np.load('./data/mag.npy')    
    f = plt.figure(figsize=(18, 18)) # plot the calculated values    
    sp = f.add_subplot(2, 2, 1 )
    plt.scatter(T, energy, s=50, marker='o', color='IndianRed')
    plt.xlabel("Temperature (T)", fontsize=20)
    plt.ylabel("Energy ", fontsize=20)        
    plt.axis('tight')
    sp =  f.add_subplot(2, 2, 2 )
    plt.scatter(T, abs(magnetization), s=50, marker='o', color='RoyalBlue')
    plt.xlabel("Temperature (T)", fontsize=20) 
    plt.ylabel("Magnetization ", fontsize=20)   
    plt.axis('tight')
    f.savefig('./images/energy_magnetization.png')

configurationPlot()
graphPlot()