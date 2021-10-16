#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np
def rule1(Q,a,da):
    dQ = Q*(da/a)
    return dQ

Q = 2
a=4
da = 0.01
errtotal=rule1(Q,a,da)
print ("Rule 1 numbers check")
print (errtotal)


# In[39]:


import numpy as np
def rule2 (Q,m,a,da):
    dQ = Q*m*(da/a)
    return dQ
Q=2
m=3
a=4
da=.03
errtotal=rule2(Q,m,a,da)
print ("Rule 2 numbers check")
print (errtotal)


# In[40]:


import numpy as np
def rule3(da,db):
    dQ = np.sqrt(da**2 + db**2)
    return dQ

d1 = 1.2
d2 = 1.3
errd1 = 0.01
errd2 = 0.01
errtotal = rule3(errd1,errd2)
print ("Rule 3 numbers check")
print (errtotal)


# In[41]:


import numpy as np
def rule4(Q,m,da,a,n,db,b):
    dQ = Q*np.sqrt((m*((da/a)**2))+(n*((db/b)**2)))
    return dQ
Q=4
m=2
da=0.01
a=3
n=0.5
db=0.003
b=7
errtotal=rule4(Q,m,da,a,n,db,b)
print ("Rule 4 numbers check")
print (errtotal)


# In[43]:


import numpy as np
def rule3 (da,db,dc):
    dX = np.sqrt(da**2 + db**2 + dc**2)
    return dX
da=0.0005
db=0.0005
dc=0.0005
errtotal=rule3(da,db,dc)
print ("Error in X using rule 3")
print (errtotal)


# In[45]:


import numpy as np
def rule4(v,m,dX,X,n,dy,y):
    dv=v*np.sqrt((m*(dX/X))**2+(n*(dy/y))**2)
    return dv
v=2.089
m=1
dX=0.000866
X=0.939
n=0.5
dy=0.0005
y=0.990
errtotal=rule4(v,m,dX,X,n,dy,y)
print ("Rule 4 reporting of error in velocity initial using dX calculated from rule 3.")
print (errtotal)


# In[37]:


print ("The error calculated using rule 3 and 4 has returned a much lower error value than the method used last week in the report. The error calculated with this method was only ~0.002 while the method last week returned a value of 0.011. likely because the error in X is different having used rule 3 this time to calculate it")


# In[25]:


import numpy as np
x=np.array([1.2,1.3,1.4,0.9,0.95,1.05])
x_avg=np.average(x)
x_std=np.std(x)
print("x_avg:",x_avg)
print("x_std:",x_std)
print("The average value of x is",x_avg, "and the standard deviation of x is",x_std)


# In[32]:


print ("1) generic form of rule 3")
print ("2) initial velocity error equation from above"),
print ("3) error in x equation used last week in the lab to calculate initial velocity error")


# 1) $\delta Q = \sqrt{(\delta A)^2 + (\delta B)^2}$

# 2) $\delta v = \sqrt{((\delta X)/X)^2 + ((\delta y) * 0.5)/y)^2}$

# 3) $\delta X = \sigma/\sqrt{N}$
