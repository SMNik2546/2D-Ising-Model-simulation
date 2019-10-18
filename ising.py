# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:01:39 2019

@author: Jonathan Frassineti
"""
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt


class Ising():
    "This class simulates the Ising model in 2 dimensions."
    
    def initialstate(self,N):
        "This method generates a random spin configuration for initial condition."
        state = np.random.choice([-1,1],size=(N,N))
        return state
        
    
    def montmove(self,N,config,beta):
        "This method creates a Monte Carlo move using the Metropolis algorithm."
        for i in range(N):
            for j in range(N):
                x = np.random.randint(0,N)
                y = np.random.randint(0,N)
                "State of the (x,y) spin in the lattice."
                z = config[x,y]
                "State of the nearest neighbours spins in the lattice (there are 4)."
                s = config[(x+1)%N,y] + config[x,(y+1)%N] + config[(x-1)%N,y] + config[x,(y-1)%N]
                "Energy change if spin (x,y) is flipped, according to the surrounding spins."         
                cost = 2*s*z
                "If the energy change is negative, accept the move and flip the spin, otherwise accept the move with probability exp(-cost*beta), and flip the spin."
                if cost < 0 :
                    z *= -1
                elif rand() < np.exp(-cost*beta):
                    z *= -1  
                "New state of the spin."    
                config[x,y] = z          
        return config
    
    def energy(self,N,config):
        "This method calculates the energy of a given configuration, given the exchange constant J = 1."
        energy = 0
        for i in range(len(config)):
            for j in range(len(config)):
                zz = config[i,j]
                ss = config[(i+1)%N,j] + config[i,(j+1)%N] + config[(i-1)%N,j] + config[i,(j-1)%N]
                "The change in energy is given by the product of the (x,y) spin and the 4 nearest neighbours spins."
                energy += -ss*zz
        return energy/4
    
    def mag(self,config):
        "This method calculates the magnetization of a given configuratiin of spins."
        magn = np.sum(config)
        return magn  

if __name__ == "main":
    pass  
