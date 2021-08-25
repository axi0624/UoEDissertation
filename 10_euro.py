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
r=pd.read_csv('switzerland.csv')
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


r1=pd.read_csv('austria.csv')
day1=r1['date']
cases1=r1['smoothed']
rt1=np.zeros(len(day1))
g1=np.zeros(len(day1))
x1=np.arange(len(day1))  
#calculating gamma pdf with Rt
for i in range(len(r)):
       g1[i]=gamma.pdf(i+1,a,scale=1/b)

for i in range(1,len(r1)):
       res1=0
       for j in range(1,i):
            res1=res1+(g1[j-1]*cases1[i-j-1])  
            
       rt1[i-1]=cases1[i-1]/res1
       
rt1[0]=0

#splines to fit the Rt curve
x_new1 = np.linspace(min(x1),max(x1),len(day1)) 
rt_smooth1 = spline(x1, rt1, x_new1)

r2=pd.read_csv('belgium.csv')
day2=r2['date']
cases2=r2['smoothed']
rt2=np.zeros(len(day2))
g2=np.zeros(len(day2))
x2=np.arange(len(day2))  
#calculating gamma pdf with Rt
for i in range(len(r)):
       g2[i]=gamma.pdf(i+1,a,scale=1/b)

for i in range(1,len(r2)):
       res2=0
       for j in range(1,i):
            res2=res2+(g2[j-1]*cases2[i-j-1])  
            
       rt2[i-1]=cases2[i-1]/res2
       
rt2[0]=0

#splines to fit the Rt curve
x_new2 = np.linspace(min(x2),max(x2),len(day2)) 
rt_smooth2 = spline(x2, rt2, x_new2)

   
                                    
r3=pd.read_csv('france.csv')
day3=r3['date']
cases3=r3['smoothed']
rt3=np.zeros(len(day3))
g3=np.zeros(len(day3))
x3=np.arange(len(day3))  
#calculating gamma pdf with Rt
for i in range(len(r)):
       g3[i]=gamma.pdf(i+1,a,scale=1/b)

for i in range(1,len(r3)):
       res3=0
       for j in range(1,i):
            res3=res3+(g3[j-1]*cases3[i-j-1])  
            
       rt3[i-1]=cases3[i-1]/res3
       
rt3[0]=0

#splines to fit the Rt curve
x_new3 = np.linspace(min(x3),max(x3),len(day3)) 
rt_smooth3 = spline(x3, rt3, x_new3)

  
 
r4=pd.read_csv('germany.csv')
day4=r4['date']
cases4=r4['smoothed']
rt4=np.zeros(len(day4))
g4=np.zeros(len(day4))
x4=np.arange(len(day4))  
#calculating gamma pdf with Rt
for i in range(len(r)):
       g4[i]=gamma.pdf(i+1,a,scale=1/b)

for i in range(1,len(r4)):
       res4=0
       for j in range(1,i):
            res4=res4+(g4[j-1]*cases4[i-j-1])  
            
       rt4[i-1]=cases4[i-1]/res4
       
rt4[0]=0

#splines to fit the Rt curve
x_new4 = np.linspace(min(x4),max(x4),len(day4)) 
rt_smooth4 = spline(x4, rt4, x_new4)
   
 


r5=pd.read_csv('greece.csv')
day5=r5['date']
cases5=r5['smoothed']
rt5=np.zeros(len(day5))
g5=np.zeros(len(day5))
x5=np.arange(len(day5))  
#calculating gamma pdf with Rt
for i in range(len(r5)):
       g5[i]=gamma.pdf(i+1,a,scale=1/b)

for i in range(1,len(r5)):
       res5=0
       for j in range(1,i):
            res5=res5+(g5[j-1]*cases5[i-j-1])  
            
       rt5[i-1]=cases5[i-1]/res5
       
rt5[0]=0

#splines to fit the Rt curve
x_new5= np.linspace(min(x5),max(x5),len(day5)) 
rt_smooth5 = spline(x5, rt5, x_new5)


r6=pd.read_csv('italy.csv')
day6=r6['date']
cases6=r6['smoothed']
rt6=np.zeros(len(day6))
g6=np.zeros(len(day6))
x6=np.arange(len(day6))  
#calculating gamma pdf with Rt
for i in range(len(r6)):
       g6[i]=gamma.pdf(i+1,a,scale=1/b)

for i in range(1,len(r6)):
       res6=0
       for j in range(1,i):
            res6=res6+(g6[j-1]*cases6[i-j-1])  
            
       rt6[i-1]=cases6[i-1]/res6
       
rt6[0]=0

#splines to fit the Rt curve
x_new6 = np.linspace(min(x6),max(x6),len(day6)) 
rt_smooth6 = spline(x6, rt6, x_new6)

 
r7=pd.read_csv('netherland.csv')
day7=r7['date']
cases7=r7['smoothed']
rt7=np.zeros(len(day7))
g7=np.zeros(len(day7))
x7=np.arange(len(day7))  
#calculating gamma pdf with Rt
for i in range(len(r7)):
       g7[i]=gamma.pdf(i+1,a,scale=1/b)

for i in range(1,len(r7)):
       res7=0
       for j in range(1,i):
            res7=res7+(g7[j-1]*cases7[i-j-1])  
            
       rt7[i-1]=cases7[i-1]/res7
       
rt7[0]=0

#splines to fit the Rt curve
x_new7 = np.linspace(min(x7),max(x7),len(day7)) 
rt_smooth7 = spline(x7, rt7, x_new7)



r8=pd.read_csv('portugal.csv')
day8=r8['date']
cases8=r8['smoothed']
rt8=np.zeros(len(day8))
g8=np.zeros(len(day8))
x8=np.arange(len(day8))  
#calculating gamma pdf with Rt
for i in range(len(r8)):
       g8[i]=gamma.pdf(i+1,a,scale=1/b)

for i in range(1,len(r8)):
       res8=0
       for j in range(1,i):
            res8=res8+(g8[j-1]*cases8[i-j-1])  
            
       rt8[i-1]=cases8[i-1]/res8
       
rt8[0]=0

#splines to fit the Rt curve
x_new8 = np.linspace(min(x8),max(x8),len(day8)) 
rt_smooth8 = spline(x8, rt8, x_new8)



r9=pd.read_csv('spain.csv')
day9=r9['date']
cases9=r9['smoothed']
rt9=np.zeros(len(day9))
g9=np.zeros(len(day9))
x9=np.arange(len(day9))  
#calculating gamma pdf with Rt
for i in range(len(r9)):
       g9[i]=gamma.pdf(i+1,a,scale=1/b)

for i in range(1,len(r9)):
       res9=0
       for j in range(1,i):
            res9=res9+(g9[j-1]*cases9[i-j-1])  
            
       rt9[i-1]=cases9[i-1]/res9
       
rt9[0]=0

#splines to fit the Rt curve
x_new9 = np.linspace(min(x9),max(x9),len(day9)) 
rt_smooth9 = spline(x9, rt9, x_new9)

   
plt.figure(figsize=(20,10), dpi=80)
plt.figure(1)
ax1 = plt.subplot(431)
plt.plot(x_new,rt_smooth)
ax1.set_title('Switzerland')
plt.tight_layout()
ax2 = plt.subplot(432)
plt.plot(x_new1,rt_smooth1)
ax2.set_title('Austria')
plt.tight_layout()
ax3 = plt.subplot(433)
plt.plot(x_new2,rt_smooth2)
ax3.set_title('Belgium')
plt.tight_layout()
ax4 = plt.subplot(434)
plt.plot(x_new3,rt_smooth3)
ax4.set_title('France')
plt.tight_layout()
ax5 = plt.subplot(435)
plt.plot(x_new4,rt_smooth4)
ax5.set_title('Germany')
plt.tight_layout()
ax6 = plt.subplot(436)
plt.plot(x_new5,rt_smooth5)
ax6.set_title('Greece')
plt.tight_layout()
ax7 = plt.subplot(437)
plt.plot(x_new6,rt_smooth6)
ax7.set_title('Italy')
plt.tight_layout()
ax8 = plt.subplot(438)
plt.plot(x_new7,rt_smooth7)
ax8.set_title('Netherland')
plt.tight_layout()
ax9 = plt.subplot(439)
plt.plot(x_new8,rt_smooth8)
plt.tight_layout()
ax9.set_title('Portugal')
ax10 = plt.subplot(4,3,10)
plt.plot(x_new9,rt_smooth9)
ax10.set_title('Spain')
plt.tight_layout()



