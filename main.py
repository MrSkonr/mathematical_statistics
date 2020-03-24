import numpy as np
import pandas as pn
from scipy.stats import expon
import seaborn as sb
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import math as m

n=2
theta=1
res = 0.01
counter_1=0
counter_2=0
    
#2.4
while n<600:
    X = np.random.uniform(0,theta,(n,1000))
    Random_Xes = pn.DataFrame(X)
    i=0
    while i < n:
        Random_Xes.rename(index={i:'X_'+ str(i+1)}, inplace=True)
        i = i+1
    X_1 = list()
    X_2 = list()
    i=0
    while i<1000:
        X_1.append(((n+1)/n)*(Random_Xes[i].max()))
        X_2.append(2*(Random_Xes[i].sum()/n))
        X_1[i]=abs(X_1[i]-theta)
        X_2[i]=abs(X_2[i]-theta)
        if X_1[i]<res:
            counter_1=counter_1+1
        if X_2[i]<res:
            counter_2=counter_2+1
        i=i+1
    print('n = ',n,counter_1,counter_2)
    counter_1=0
    counter_2=0
    n=n*2

#2.5
n = 4
k = 1
while n<600:
    X = np.random.uniform(0,theta,(n,1000))
    Random_Xes = pn.DataFrame(X)
    i=0
    while i < n:
        Random_Xes.rename(index={i:'X_'+ str(i+1)}, inplace=True)
        i = i+1
    X_1 = list()
    i=0
    while i<1000:
        X_1.append(m.sqrt(n)*(2*Random_Xes[i].sum()/n-theta))
        i=i+1
    Random_Numbers = pn.DataFrame(data={"X_1": X_1})
    sb.distplot(Random_Numbers["X_1"])
    i=0
    X_1 = list()
    while i<1000:
        X_1.append( m.sqrt(n)*(2*((Random_Xes[i].sort_values()).iloc[k+1:n-k]).sum()/(n-2*k)-theta) )
        i=i+1  
    Random_Numbers = pn.DataFrame(data={"X_1": X_1})
    sb.distplot(Random_Numbers["X_1"])
    n=n*2
    k=k*2
    plt.figure(figsize=(12, 10))

plt.show()