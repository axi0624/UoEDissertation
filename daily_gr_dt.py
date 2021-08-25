import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import spline 
data=pd.read_csv('d1.csv')
d=data['date']
y1=data['sdgr']
y2=data['log']


x=np.arange(504)   
x_new = np.linspace(min(x),max(x),500) 
 
y_1smooth = spline(x, y1, x_new)
y_2smooth = spline(x, y2, x_new)

#plotting
fig=plt.figure(figsize=(15,5))  
plt.xlabel('date')
plt.ylabel('Growth rate of UK')
plt.title('Growth rate of UK')
plt.plot(x_new, y_1smooth,c='g',label='Growth rate') 
plt.grid(axis='y')
plt.legend()  
plt.show() 


fig=plt.figure(figsize=(15,5))  
plt.xlabel('date')
plt.ylabel('Doubling time of UK')
plt.title('Doubling time of UK')
plt.plot(x_new, y_1smooth,c='g',label='Growth rate') 
plt.plot(x_new, y_2smooth,c='g',label='Doubling time') 
plt.grid(axis='y')
plt.legend()  
plt.show()   
           
                         
