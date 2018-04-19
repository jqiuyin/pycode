import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

def datestr2(s):
	return datetime.strptime(s,"%d-%m-%y").date().weekday()
	



d,c=np.loadtxt('data.csv',delimiter=',',usecols=(1,6),unpack=True)
print('Dates=',dates)
averages=np.zeros(5)
for i in range(5)
	indices=np.where(dates==i)
	prices=np.take(c,indices)
	
returns=np.diff(c)/c[:-1]
print('简单收益率：'+str(returns))