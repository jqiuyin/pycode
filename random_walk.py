# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 10:30:45 2017

@author: Sherry
"""

from random import choice

class RandomWalk(object):
    def __init__(self,num_points=5000):
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]
        #迈每一步
    def fill_walk(self):
        while len(self.x_values)<=self.num_points:
            x_direction=choice([-1,1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance
            y_direction=choice([-1,1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_direction*y_distance
        #拒绝原地踏步
            if x_step==0 and y_step==0:
                continue
        #计算要落下点的坐标
            x_step=self.x_values[-1]+x_step
            y_step=self.y_values[-1]+y_step
        #把新加入的点作为起点，为下一次迈出步伐做准备
            self.x_values.append(x_step)
            self.y_values.append(y_step)
           
        
        
from matplotlib import pyplot as plt
walker=RandomWalk()
walker.fill_walk()

plt.scatter(walker.x_values,walker.y_values,s=16)

plt.show()
