import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gamma
from scipy.interpolate import spline 
from scipy.interpolate import interp1d 
#gamma distribution shape and scale params
exp=3.3
var=3.9*3.9
a=exp*exp/var
b=exp/var
r=pd.read_csv('france.csv')
day=r['date']
cases=r['smoothed']
rt=np.zeros(len(day))
g=np.zeros(len(day))
x=np.arange(len(day))  
#calculating gamma pdf with Rt
for i in range(len(r)):
       g[i]=gamma.pdf(i+1,a,scale=1/b)

for i in range(1,len(r)):
       res=0
       for j in range(1,i):
            res=res+(g[j-1]*cases[i-j-1])  
            
       rt[i-1]=cases[i-1]/res
       
rt[0]=0

#splines to fit the Rt curve
x_new = np.linspace(min(x),max(x),len(day)) 
rt_smooth = spline(x, rt, x_new)

fig=plt.figure(figsize=(15,5))  
plt.xlabel('date')
plt.ylabel('Rt')
plt.grid(axis='y')
plt.title('Rt of france')

plt.plot(x_new,rt_smooth,c='b') 
plt.legend() 
plt.show()      
 
 


           
                         
