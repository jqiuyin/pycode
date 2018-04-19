# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 11:27:12 2017

@author: Sherry
"""

from random_walk import RandomWalk
from matplotlib import pyplot as plt

while True:
    walker=RandomWalk()
    walker.fill_walk()
    plt.scatter(walker.x_values,walker.y_values,s=15)
    
    plt.show()
    
    answer=raw_input('Continue to move?(y/n)')
    if answer=='n':
        break