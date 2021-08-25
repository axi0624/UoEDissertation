import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gamma
from scipy.interpolate import spline  
#gamma distribution shape and scale params
exp=4.8
var=3*3
a=exp*exp/var
b=exp/var
r=pd.read_csv('d1.csv')
day=r['date']
cases=r['standard']
rt=np.zeros(504)
g=np.zeros(504)
x=np.arange(504)  
#calculating gamma pdf with Rt
for i in range(len(r)):
       g[i]=gamma.pdf(i+1,a,scale=1/b)

for i in range(1,len(r)):
       res=0
       for j in range(1,i):
            res=res+(g[j-1]*cases[i-j-1])  
            
       rt[i-1]=cases[i-1]/res
       
rt[0]=0

rt1 = pd.DataFrame(rt)

writer = pd.ExcelWriter('d2.xlsx')
rt1.to_excel(writer)		

writer.save()
writer.close()

#splines to fit the Rt curve
x_new = np.linspace(min(x),max(x),500) 
rt_smooth = spline(x, rt, x_new)

fig=plt.figure(figsize=(15,5))  

plt.xlabel('days')
plt.ylabel('Rt')

plt.title('Rt')
plt.ylim(ymax=4)
plt.plot(x_new,rt_smooth,c='b') 
plt.grid(axis='y')

plt.title('Reproduction number of UK')
plt.legend() 
plt.show()      
 
 

